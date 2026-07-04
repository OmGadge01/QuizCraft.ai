from pathlib import Path

# ai-service/
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# storage/
STORAGE_DIR = BASE_DIR / "storage"

# storage/Notes/
NOTES_DIR = STORAGE_DIR / "Notes"