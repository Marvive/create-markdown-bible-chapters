# Markdown Bible Structure Generator

A simple Python script that generates a complete hierarchical folder structure of the Bible in Markdown format, perfect for note-taking applications like Obsidian, Logseq, or any markdown-based PKM system.

## What This Script Does

- Creates a complete Bible folder structure organized by:
  - Testament (Old Testament, New Testament)
  - Categories (Torah, Historical Books, Wisdom Literature, etc.)
  - Books (Genesis, Exodus, etc.)
  - Individual chapter files for each book

- Generates markdown files for:
  - 66 books of the Bible
  - 1,189 total chapter files
  - Folder notes for each testament, category, and book

- Includes proper hierarchical organization with:
  - The 39 books of the Old Testament 
  - The 27 books of the New Testament
  - All organized by their traditional categories

## How to Use

### Download the Script

1. Download the `create_bible_structure.py` script from this repository
2. Save it to the location where you want to create your Bible folder structure

### Run the Script

1. Open your terminal/command prompt
2. Navigate to the folder where you saved the script
3. Run the script with Python:

```
python create_bible_structure.py
```

4. The script will generate a "Bible" folder in the same directory where the script is located
5. Once complete, you'll see a confirmation message showing the number of books, chapters, and folder notes created
6. You can then drag the created "Bible" folder to your desired location (like your Obsidian vault or notes directory)

## Structure Overview

```
Bible/
├── Old Testament/
│   ├── Torah/
│   │   ├── Genesis/
│   │   │   ├── Genesis.md (folder note)
│   │   │   ├── Genesis 1.md
│   │   │   ├── Genesis 2.md
│   │   │   └── ...
│   │   ├── Exodus/
│   │   └── ...
│   ├── Historical Books/
│   ├── Wisdom Literature/
│   ├── Major Prophets/
│   └── Minor Prophets/
└── New Testament/
    ├── Gospels/
    ├── Acts/
    ├── Pauline Epistles/
    ├── Pastoral Epistles/
    ├── General Epistles/
    └── Apocalyptic/
```

## Future Updates

Planned enhancements for future versions:

- Option to enable/disable the creation of folder notes
- Toggle for creating subcategory folders (like Torah, Gospels, etc.)
- Option to include/exclude Testament level folders
- Support for various Bible translations or additional religious texts
- Customizable templates for chapter and book notes

## Requirements

- Python 3.x

## License

This project is open source and available for personal use.

---

Made with ❤️ for markdown enthusiasts and Bible scholars 