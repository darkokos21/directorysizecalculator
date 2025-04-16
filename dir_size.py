import os
from pathlib import Path

def get_dir_size(directory):
    """Calculate total size of files in directory in bytes."""
    path = Path(directory)
    if not path.exists():
        print(f"Directory {directory} does not exist.")
        return 0
    
    total_size = 0
    for file_path in path.rglob("*"):
        if file_path.is_file():
            total_size += file_path.stat().st_size
    return total_size

if __name__ == "__main__":
    size = get_dir_size("./files")
    print(f"Total size: {size} bytes")