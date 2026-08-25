from pathlib import Path

input_directory = Path("C:/Users/Heidel/Downloads")

#SCAN FILES
folder_files = [i for i in input_directory.iterdir() if i.is_file()]
file_extension = input_directory.suffix