import argparse
from pathlib import Path
from modules.helper import organize_files
from modules.helper import scan_files
from rich.panel import Panel
from rich.console import Console


# CLI ARG PARSER
parser = argparse.ArgumentParser(
    prog="forgesort",
    usage="forgesort [command] [options] <folder>",
    description="ForgeSort is a file management utility for organizing files, bulk renaming, and duplicate detection.",
    epilog="Examples: \nforgesort organize Downloads\nforgesort rename Photos\nforgesort duplicates Documents",
    formatter_class=argparse.RawDescriptionHelpFormatter
)
parser.add_argument("-o", "--organize", required=True, help="organizes files inside a specified folder", type=Path)
args = parser.parse_args()

folder_files = scan_files(args.organize)

# RICH CONSOLE
console = Console()

with console.status("Organizing files..."):
    organize_files(folder_files, args.organize)

config = (
    f"Input: {args.organize}\n"
    f"Mode: Organizer\n"
    f"[green]Status: {len(folder_files)} files processed[/green]"
)
    
console.print(
    Panel.fit(
        config,
        title="Scan Configuration",
        border_style="cyan"
    )
)