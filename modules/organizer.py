from pathlib import Path
from organizer.file_extensions import FILE_TYPE_EXTENSIONS
from shutil import copy2

def organize_files(folder_files, input_directory : Path):
    
    for file in folder_files:
        
        file_ext = file.suffix.lower()
        matched = False
        
        for category, values in FILE_TYPE_EXTENSIONS.items():
            if file_ext in values:
                output_dir = input_directory / category
                output_dir.mkdir(parents=True, exist_ok=True)
                copy2(file, output_dir)
                matched = True
                break
                
        if matched == False:
            output_dir = input_directory / "Other Files"
            output_dir.mkdir(parents=True, exist_ok=True)
            copy2(file, output_dir)
            
            
            
            
        
# RECEIVE file
# GET extension
# NORMALIZE extension to lowercase
# FOR each category
#     CHECK whether extension belongs to category
#     IF found
#           RETURN category
#           How can we check if category folder already exist?
#           create folder / move file to folder if exists
#           
# RETURN Misc