import argparse
from pathlib import Path
from modules.organizer import organize_files
from rich.panel import Panel
from rich.console import Console

parser = argparse.ArgumentParser(
    prog="forgesort",
    usage="forgesort [command] [options] <folder>",
    description="ForgeSort is a file management utility for organizing files, bulk renaming, and duplicate detection.",
    epilog="Examples: \nforgesort organize Downloads\nforgesort rename Photos\nforgesort duplicates Documents",
    formatter_class=argparse.RawDescriptionHelpFormatter
)
parser.add_argument("-o", "--organize", required=True, help="organizes files inside a specified folder", type=Path)
args = parser.parse_args()

folder_files = [i for i in args.organize.iterdir() if i.is_file()]

console = Console()

import time

with console.status("Scanning files..."):
    time.sleep(5)
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