from pathlib import Path

changed_files = (Path('.') / "changed_files.txt").read_text()

print(changed_files)
