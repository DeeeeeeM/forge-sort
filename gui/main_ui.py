from __future__ import annotations

import sys
from pathlib import Path

from PySide6.QtCore import QFile, QSettings, QUrl
from PySide6.QtGui import QAction, QDesktopServices
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import (
    QApplication, QCheckBox, QDialog, QFileDialog, QLabel, QLineEdit, QMessageBox,
    QPushButton, QProgressBar, QTextEdit,
)

PROJECT_ROOT = Path(__file__).resolve().parents[1]
REPOSITORY_URL = "https://github.com/DeeeeeeM/forge-sort"
ISSUES_URL = f"{REPOSITORY_URL}/issues"
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from modules.helper import check_duplicate, organize_files, scan_files


class ForgeSortWindow:

    def __init__(self) -> None:
        ui_path = Path(__file__).with_name("forge_sort_dark.ui")
        ui_file = QFile(str(ui_path))
        if not ui_file.open(QFile.ReadOnly):
            raise RuntimeError(f"Cannot open UI file: {ui_path}")
        self.window = QUiLoader().load(ui_file)
        ui_file.close()
        if self.window is None:
            raise RuntimeError("Qt could not load forge_sort_dark.ui")

        self.path_input = self._child(QLineEdit, "pathInput")
        self.browse_button = self._child(QPushButton, "browseButton")
        self.organize_button = self._child(QPushButton, "organizeButton")
        self.duplicates_button = self._child(QPushButton, "duplicatesButton")
        self.result_label = self._child(QLabel, "resultLabel")
        self.activity_log = self._child(QTextEdit, "activityLog")
        self.activity_title = self._child(QLabel, "sectionTitle_2")
        self.progress_bar = self._child(QProgressBar, "progressBar")
        # Keep preferences beside the GUI so they work consistently whether the
        # app is run from source or launched outside an installed package.
        self.settings = QSettings(
            str(Path(__file__).with_name(".forgesort-settings.ini")),
            QSettings.IniFormat,
        )
        self.set_progress(0, "Ready")

        self.browse_button.clicked.connect(self.choose_folder)
        self.organize_button.clicked.connect(self.organize_folder)
        self.duplicates_button.clicked.connect(self.find_duplicates)
        self.path_input.returnPressed.connect(self.inspect_folder)
        self._action("actionPreferences").triggered.connect(self.show_preferences)
        self._action("actionAbout").triggered.connect(self.show_about)
        self._action("actionReportBugs").triggered.connect(self.report_bugs)
        self._action("actionCheckUpdates").triggered.connect(self.check_for_updates)
        self.apply_preferences()

    def _child(self, widget_type, name):
        widget = self.window.findChild(widget_type, name)
        if widget is None:
            raise RuntimeError(f"Required widget '{name}' is missing from the UI file")
        return widget

    def _action(self, name: str) -> QAction:
        action = self.window.findChild(QAction, name)
        if action is None:
            raise RuntimeError(f"Required action '{name}' is missing from the UI file")
        return action

    def apply_preferences(self) -> None:
        show_activity = self.settings.value("show_activity", True, type=bool)
        self.activity_title.setVisible(show_activity)
        self.activity_log.setVisible(show_activity)
        # Activity needs room for both its title and the result panel.  Resize
        # deliberately so hiding it produces a compact window rather than
        # stretching the header and folder controls.
        target_height = 660 if show_activity else 480
        self.window.resize(self.window.width(), target_height)

    def set_progress(self, value: int, message: str) -> None:
        self.progress_bar.setValue(value)
        self.window.statusBar().showMessage(message)

    def strict_mode_enabled(self) -> bool:
        return self.settings.value("strict_mode", True, type=bool)

    def is_allowed_folder(self, folder: Path) -> bool:
        if not self.strict_mode_enabled():
            return True
        resolved_folder = folder.resolve()
        profile = Path.home().resolve()
        # Drive roots remain selectable so users can navigate a different drive.
        if resolved_folder == Path(resolved_folder.anchor):
            return True
        return resolved_folder.is_relative_to(profile)

    def choose_folder(self) -> None:
        folder = QFileDialog.getExistingDirectory(self.window, "Choose a folder to sort")
        if folder:
            selected = Path(folder)
            if not self.is_allowed_folder(selected):
                QMessageBox.warning(
                    self.window,
                    "Strict mode is enabled",
                    f"Choose a folder inside your user profile:\n{Path.home()}\n\n"
                    "You can turn off strict mode in File > Preferences.",
                )
                return
            self.path_input.setText(folder)
            self.inspect_folder()

    def selected_folder(self) -> Path | None:
        raw_path = self.path_input.text().strip()
        folder = Path(raw_path).expanduser()
        if not raw_path or not folder.is_dir():
            self.result_label.setText("Choose a valid folder to continue")
            self.activity_log.setPlainText("No valid folder is selected.")
            return None
        if not self.is_allowed_folder(folder):
            self.result_label.setText("This folder is blocked by strict mode")
            self.activity_log.setPlainText(
                "Strict mode only permits folders in your user profile. "
                "Change this in File > Preferences."
            )
            return None
        return folder

    def show_preferences(self) -> None:
        dialog = self._load_dialog("preferences.ui")
        show_activity = self._dialog_child(dialog, QCheckBox, "showActivityCheck")
        strict_mode = self._dialog_child(dialog, QCheckBox, "strictModeCheck")
        save_button = self._dialog_child(dialog, QPushButton, "saveButton")
        cancel_button = self._dialog_child(dialog, QPushButton, "cancelButton")
        show_activity.setChecked(self.settings.value("show_activity", True, type=bool))
        strict_mode.setChecked(self.strict_mode_enabled())
        save_button.clicked.connect(
            lambda: self._save_preferences(dialog, show_activity.isChecked(), strict_mode.isChecked())
        )
        cancel_button.clicked.connect(dialog.reject)
        dialog.exec()

    def _save_preferences(self, dialog: QDialog, show_activity: bool, strict_mode: bool) -> None:
        self.settings.setValue("show_activity", show_activity)
        self.settings.setValue("strict_mode", strict_mode)
        self.apply_preferences()
        dialog.accept()

    def _load_dialog(self, filename: str) -> QDialog:
        ui_file = QFile(str(Path(__file__).with_name(filename)))
        if not ui_file.open(QFile.ReadOnly):
            raise RuntimeError(f"Cannot open UI file: {filename}")
        dialog = QUiLoader().load(ui_file, self.window)
        ui_file.close()
        if not isinstance(dialog, QDialog):
            raise RuntimeError(f"{filename} did not load a dialog")
        return dialog

    @staticmethod
    def _dialog_child(dialog: QDialog, widget_type, name):
        widget = dialog.findChild(widget_type, name)
        if widget is None:
            raise RuntimeError(f"Required widget '{name}' is missing from the dialog")
        return widget

    def show_about(self) -> None:
        QMessageBox.about(
            self.window,
            "About ForgeSort",
            "<h2>ForgeSort</h2>"
            "<p>A focused file-management utility for organizing top-level files into "
            "category folders and reviewing duplicate files safely.</p>"
            "<p><b>Created by:</b> Heidel Medina</p>"
            f"<p><a href='{REPOSITORY_URL}'>Project repository</a></p>",
        )

    def check_for_updates(self) -> None:
        QDesktopServices.openUrl(QUrl(REPOSITORY_URL))

    def report_bugs(self) -> None:
        QDesktopServices.openUrl(QUrl(ISSUES_URL))

    def inspect_folder(self) -> None:
        folder = self.selected_folder()
        if folder is None:
            return
        count = len(scan_files(folder))
        self.set_progress(100, f"Ready: {count} top-level files")
        self.result_label.setText(f"Ready to scan {count} top-level file{'s' if count != 1 else ''}")
        self.activity_log.setPlainText(
            f"Folder: {folder}\n\nForgeSort only scans files directly inside this folder."
        )

    def organize_folder(self) -> None:
        folder = self.selected_folder()
        if folder is None:
            return
        files = scan_files(folder)
        self.set_progress(15, "Preparing files for organization…")
        if not files:
            self.result_label.setText("Nothing to organize")
            self.activity_log.setPlainText("No top-level files were found in the selected folder.")
            return
        reply = QMessageBox.question(
            self.window, "Organize files?",
            f"Move {len(files)} top-level files into category folders inside:\n{folder}",
            QMessageBox.Yes | QMessageBox.Cancel, QMessageBox.Cancel,
        )
        if reply != QMessageBox.Yes:
            self.set_progress(0, "Organization cancelled")
            return
        organize_files(files, folder)
        self.set_progress(100, f"Organized {len(files)} files")
        self.result_label.setText(f"Organized {len(files)} files")
        self.activity_log.setPlainText(
            f"Completed\n\nMoved {len(files)} top-level files into their extension categories."
        )

    def find_duplicates(self) -> None:
        folder = self.selected_folder()
        if folder is None:
            return
        files = scan_files(folder)
        self.set_progress(15, "Checking files for duplicates…")
        duplicate_groups = check_duplicate(files)
        duplicate_count = sum(len(group) for group in duplicate_groups)
        self.set_progress(100, f"Duplicate check complete: {duplicate_count} found")
        self.result_label.setText(
            f"Found {duplicate_count} duplicate file{'s' if duplicate_count != 1 else ''}"
        )
        if not duplicate_groups:
            self.activity_log.setPlainText(
                f"Scanned {len(files)} top-level files.\n\nNo duplicate files were found."
            )
            return
        groups = []
        for index, group in enumerate(duplicate_groups, start=1):
            names = "\n".join(f"  • {file.name}" for file in group)
            groups.append(f"Duplicate group {index}\n{names}")
        self.activity_log.setPlainText(
            f"Scanned {len(files)} top-level files.\n\n" + "\n\n".join(groups)
        )


def main() -> int:
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    forge_sort = ForgeSortWindow()
    forge_sort.window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
