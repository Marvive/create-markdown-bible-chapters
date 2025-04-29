#!/usr/bin/env python3

import os
import shutil

# First, remove the existing Bible directory
if os.path.exists("Bible"):
    shutil.rmtree("Bible")

# Dictionary of Bible books and their chapter counts, organized by categories
bible_structure = {
    "Old Testament": {
        "Torah": {
            "Genesis": 50,
            "Exodus": 40,
            "Leviticus": 27,
            "Numbers": 36,
            "Deuteronomy": 34
        },
        "Historical Books": {
            "Joshua": 24,
            "Judges": 21,
            "Ruth": 4,
            "1 Samuel": 31,
            "2 Samuel": 24,
            "1 Kings": 22,
            "2 Kings": 25,
            "1 Chronicles": 29,
            "2 Chronicles": 36,
            "Ezra": 10,
            "Nehemiah": 13,
            "Esther": 10
        },
        "Wisdom Literature": {
            "Job": 42,
            "Psalms": 150,
            "Proverbs": 31,
            "Ecclesiastes": 12,
            "Song of Solomon": 8
        },
        "Major Prophets": {
            "Isaiah": 66,
            "Jeremiah": 52,
            "Lamentations": 5,
            "Ezekiel": 48,
            "Daniel": 12
        },
        "Minor Prophets": {
            "Hosea": 14,
            "Joel": 3,
            "Amos": 9,
            "Obadiah": 1,
            "Jonah": 4,
            "Micah": 7,
            "Nahum": 3,
            "Habakkuk": 3,
            "Zephaniah": 3,
            "Haggai": 2,
            "Zechariah": 14,
            "Malachi": 4
        }
    },
    "New Testament": {
        "Gospels": {
            "Matthew": 28,
            "Mark": 16,
            "Luke": 24,
            "John": 21
        },
        "Acts": {
            "Acts": 28
        },
        "Pauline Epistles": {
            "Romans": 16,
            "1 Corinthians": 16,
            "2 Corinthians": 13,
            "Galatians": 6,
            "Ephesians": 6,
            "Philippians": 4,
            "Colossians": 4,
            "1 Thessalonians": 5,
            "2 Thessalonians": 3
        },
        "Pastoral Epistles": {
            "1 Timothy": 6,
            "2 Timothy": 4,
            "Titus": 3,
            "Philemon": 1
        },
        "General Epistles": {
            "Hebrews": 13,
            "James": 5,
            "1 Peter": 5,
            "2 Peter": 3,
            "1 John": 5,
            "2 John": 1,
            "3 John": 1,
            "Jude": 1
        },
        "Apocalyptic": {
            "Revelation": 22
        }
    }
}

# Base directory
base_dir = "Bible"

# Create folders and files
total_books = 0
total_chapters = 0

for testament, categories in bible_structure.items():
    testament_dir = os.path.join(base_dir, testament)
    os.makedirs(testament_dir, exist_ok=True)
    
    for category, books in categories.items():
        category_dir = os.path.join(testament_dir, category)
        os.makedirs(category_dir, exist_ok=True)
        
        for book, chapters in books.items():
            total_books += 1
            book_dir = os.path.join(category_dir, book)
            os.makedirs(book_dir, exist_ok=True)
            
            # Create chapter files
            for chapter in range(1, chapters + 1):
                total_chapters += 1
                chapter_file = os.path.join(book_dir, f"{book} {chapter}.md")
                with open(chapter_file, "w") as f:
                    f.write(f"# {book} Chapter {chapter}\n\n")
                    
print(f"Created Bible structure with {total_books} books and {total_chapters} chapters.") 