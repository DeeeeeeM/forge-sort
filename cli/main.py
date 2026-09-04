import argparse
from pathlib import Path
from rich.panel import Panel
from rich.console import Console
from modules.helper import organize_files
from modules.helper import scan_files
from modules.helper import check_duplicate

# CLI ARG PARSER
parser = argparse.ArgumentParser(
    prog="forgesort",
    usage="forgesort [command] [options] <folder>",
    description="ForgeSort is a file management utility for organizing files, bulk renaming, and duplicate detection.",
    epilog="Examples: \nforgesort organize Downloads\nforgesort rename Photos\nforgesort duplicates Documents",
    formatter_class=argparse.RawDescriptionHelpFormatter
)

parser.add_argument("-o", "--organize", help="organizes files inside a specified folder", type=Path)
parser.add_argument("-ch", "--checkdup", help="Check any duplicate files inside a specified folder", type=Path)
args = parser.parse_args()

# RICH CONSOLE
console = Console()

if args.organize:
    folder_files = scan_files(args.organize)
    with console.status("Organizing..."):
        organize_files(folder_files, args.organize)
    config = (
        f"Input: {args.organize}\n"
        f"Mode: File Organizer\n"
        f"[green]Status: {len(folder_files)} files processed[/green]"
    )
    console.print(
        Panel.fit(
            config,
            title="Scan Configuration",
            border_style="cyan"
        )
    )

elif args.checkdup:
    folder_files = scan_files(args.checkdup)
    with console.status("Checking..."):
        duplicate_files = check_duplicate(folder_files)
        num_duplicate = sum(len(group) for group in duplicate_files)
    config = (
        f"Input: {args.checkdup}\n"
        f"Mode: Check Duplicate Files\n"
        f"[green]Status: {len(folder_files)} files processed[/green]\n"
        f"[yellow]Number of duplicate files: {num_duplicate}[/yellow]"
    )
    console.print(
        Panel.fit(
            config,
            title="Checking Report",
            border_style="cyan"
        )
    )
    
    config_files = "\n\n".join(
        f"File Group {index}\n"
        + "\n".join(file.name for file in group)
        for index, group in enumerate(duplicate_files, start=1)
    )
    
    console.print(
        Panel.fit(
            config_files,
            title="File Duplicates",
            border_style="cyan"
        )
    )
    
    
        
    
    