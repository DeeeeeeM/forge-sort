from pathlib import Path
from shutil import move
from modules.file_extensions import FILE_TYPE_EXTENSIONS
import hashlib  
     
      
def scan_files(file_path):
    return [i for i in file_path.iterdir() if i.is_file()]

def calculate_hash(file_path):
    with open(file_path, "rb") as file:
        digest = hashlib.file_digest(file, "sha256")
        return digest.hexdigest()

def organize_files(folder_files : list, input_directory : Path):
            
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
                break   
        
        if matched == False:
            output_dir = input_directory / "Other Files"
            output_dir.mkdir(parents=True, exist_ok=True)
            move(item, output_dir)


def check_duplicate(folder_files : list):
    
    grouped_items = {}
    duplicate_items = []
    
    for item in folder_files:
        item_stat = item.stat().st_size
        grouped_items.setdefault(item_stat, []).append(item)
    
    for size, value_items in grouped_items.items():
        if len(value_items) > 1:
            
            hashed_group = {}
            
            for candidate_file in value_items:
               file_hash = calculate_hash(candidate_file)
               hashed_group.setdefault(file_hash, []).append(candidate_file)
               
            for hash_key, duplicate_groups in hashed_group.items():
                if len(duplicate_groups) > 1:
                    duplicate_items.append(duplicate_groups)
    
    return duplicate_items          
