from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional
from pathlib import Path
from modules.helper import scan_files, check_duplicate

app = FastAPI(title="ForgeSort API")

class HealthCheck(BaseModel):
    status: str
    
class PathRequest(BaseModel):
    folder_path: Path

def path_validator(folder_path: Path):
    if not folder_path.exists():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Invalid path!")
    if not folder_path.is_dir():
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="Path is not a directory!")        

@app.get("/health")
def health_check():
    return{"status": "healthy"} 

@app.post("/duplicate")
def duplicates(request: PathRequest):
    path_validator(request.folder_path)
    items = scan_files(request.folder_path)
    duplicate_files = check_duplicate(items)
    num_duplicate = sum(len(group) for group in duplicate_files)
    file_path_duplicates = []
    for group in duplicate_files:
        file_list = []
        for item in group:
            file_list.append(str(item))
        file_path_duplicates.append(file_list)
    
    return {
        "duplicate_quantity": num_duplicate,
        "duplicate_list": file_path_duplicates
    }