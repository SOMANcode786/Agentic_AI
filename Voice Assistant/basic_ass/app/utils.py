import shutil
from pathlib import Path

UPLOAD_DIR = Path("uploads")

async def save_upload_file(upload_file):
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
    file_path = UPLOAD_DIR / upload_file.filename
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)
    return str(file_path)
