# 📂 File Organizer Script

This Python script tidies up a specified directory by grouping files into subfolders named after their extensions (for example, `.txt`, `.jpg`, `.pdf`). It processes only files (ignoring existing folders), creates any needed extension folders, moves files accordingly, and logs every action.

---

## 🔄 How It Works

1. Scan the **target folder** for files (skip subdirectories).  
2. For each file:  
   - Determine its extension (e.g., `.txt`)  
   - Create a folder named after that extension if it doesn’t exist  
   - If a file with the same name already exists in the destination, prompt the user before overwriting  
   - Move the file into its extension folder  
   - Record the action in `log.txt` (one directory above the target folder)

---

## 🗂 Workflow Diagram

```bash
[ Target Folder ]
       │
       ▼
  Scan for files
       │
       ▼
[Extension Folders] ←─ Create if missing
       │
       ▼
Prompt on name conflicts
       │
       ▼
   Move files
       │
       ▼
  Append to log.txt
```

---

## ✨ Features

- Automatic categorization of files by extension

- User confirmation to prevent accidental overwrites

- Detailed timestamped logging of all operations

- Ignores directories, processes files only

---

## 📦 Requirements

- Python 3.x

- No external libraries (uses built-in `os`, `shutil`, and `datetime`)

---

## 🚀 How to Run

1. Place your files in the target folder you want to organize.

2. Ensure a writable log.txt exists one level above that folder (it will be created automatically if missing).

3. Run the script:

```bash
python file_organizer.py
```

4. Follow any overwrite prompts, then verify that files have been moved into their new extension-named subfolders.

---

## 👤 Author

SirLuciferZ 📅 2025-09-01
