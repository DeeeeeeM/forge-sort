import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxlayout, QHBoxlayout, QPushButton, QLineEdit, QTextEdit, QComboBox
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Hello!")
        
        container = QWidget()
        self.setCentralWidget(container)

        layout = QVBoxlayout(container)

        label = QLabel('Label')
        label.setAlignment(Qt.AlignCenter)

        button = QPushButton('Click Me')

        line_edit = QLineEdit()
        text_edit = QTextEdit()

        combobox = QComboBox()
        combobox.addItems(['One', 'Two', 'Three' ])

        layout.addWidget(label)
        layout.addWidget(button)
        layout.addWidget(line_edit)
        layout.addWidget(text_edit)
        layout.addWidget(combobox)
        
        
        
        
app = QApplication()

window = MainWindow()
window.show()

app.exec()