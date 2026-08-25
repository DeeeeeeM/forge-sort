from pathlib import Path
from shutil import move
from organizer.file_extensions import FILE_TYPE_EXTENSIONS
        

def organize_files(folder_files, input_directory : Path):
    for file in folder_files:
        file_ext = file.suffix.lower()
        matched = False
        
        for category, values in FILE_TYPE_EXTENSIONS.items():
            if file_ext in values:
                output_dir = input_directory / category
                output_dir.mkdir(parents=True, exist_ok=True)                
                
                if (output_dir / file.name).exists(): continue
                
                move(file, output_dir)
                matched = True
                break   
            
        if matched == False:
            output_dir = input_directory / "Other Files"
            output_dir.mkdir(parents=True, exist_ok=True)
            move(file, output_dir)