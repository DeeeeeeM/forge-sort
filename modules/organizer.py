from pathlib import Path
from shutil import move
from modules.file_extensions import FILE_TYPE_EXTENSIONS
from rich.progress import Progress
        

def organize_files(folder_files : list, input_directory : Path):
    
    total_files = len(folder_files)
    
    with Progress() as progress:
        task = progress.add_task("Organizing files...", total=total_files)
    
        for item in folder_files:
            file_ext = item.suffix.lower()
            matched = False
            
            for category, values in FILE_TYPE_EXTENSIONS.items():
                if file_ext in values:
                    output_dir = input_directory / category
                    output_dir.mkdir(parents=True, exist_ok=True)            
                    if (output_dir / item.name).exists(): 
                        continue
                    move(item, output_dir)
                    matched = True
                    progress.update(task, advance=1)
                    break   
            
            if matched == False:
                output_dir = input_directory / "Other Files"
                output_dir.mkdir(parents=True, exist_ok=True)
                move(item, output_dir)
                progress.update(task, advance=1)