"""
Library Management System
A simple command-line application to manage a collection of books.

Author: Mal.ALH
"""

import json
import os
from dataclasses import dataclass, asdict
from typing import List, Optional

DATA_FILE = "library_data.json"


@dataclass
class Book:
    """Represents a single book in the library."""
    title: str
    author: str
    year: int

    def __str__(self) -> str:
        return f"Title: {self.title} | Author: {self.author} | Year: {self.year}"


class Library:
    """Manages a collection of Book objects with add/view/search/delete operations."""

    def __init__(self, data_file: str = DATA_FILE) -> None:
        self.data_file = data_file
        self.books: List[Book] = self._load_books()

    # ---------- Persistence ----------
    def _load_books(self) -> List[Book]:
        """Load books from the JSON data file if it exists."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r", encoding="utf-8") as f:
                    raw = json.load(f)
                return [Book(**item) for item in raw]
            except (json.JSONDecodeError, TypeError):
                print("⚠️  Warning: data file was corrupted, starting with an empty library.")
                return []
        # Default starter book, same as the original script
        return [Book(title="Python", author="Ahmed", year=2024)]

    def _save_books(self) -> None:
        """Persist the current book list to disk."""
        with open(self.data_file, "w", encoding="utf-8") as f:
            json.dump([asdict(b) for b in self.books], f, ensure_ascii=False, indent=2)

    # ---------- Core operations ----------
    def add_book(self, title: str, author: str, year: int) -> None:
        self.books.append(Book(title=title, author=author, year=year))
        self._save_books()

    def view_books(self) -> List[Book]:
        return self.books

    def search_book(self, title: str) -> List[Book]:
        return [b for b in self.books if b.title.lower() == title.lower()]

    def delete_book(self, title: str) -> bool:
        original_len = len(self.books)
        self.books = [b for b in self.books if b.title.lower() != title.lower()]
        deleted = len(self.books) < original_len
        if deleted:
            self._save_books()
        return deleted

    def count_books(self) -> int:
        return len(self.books)


# ---------- Input helpers ----------
def read_non_empty_string(prompt: str) -> str:
    """Keep asking until the user provides a non-empty string."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("⚠️  This field cannot be empty. Please try again.")


def read_year(prompt: str) -> int:
    """Keep asking until the user provides a valid integer year."""
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print("⚠️  Please enter a valid number for the year.")


# ---------- Menu / UI ----------
MENU_TEXT = """
===== Library System =====
1. Add Book
2. View Books
3. Search Book
4. Delete Book
5. Count Books
6. Exit
"""


def print_books(books: List[Book]) -> None:
    if not books:
        print("No books available.")
        return
    for index, book in enumerate(books, start=1):
        print(f"{index}. {book}")


def main() -> None:
    library = Library()

    while True:
        print(MENU_TEXT)
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            print("\n--- Add Book ---")
            title = read_non_empty_string("Enter book title: ")
            author = read_non_empty_string("Enter book author: ")
            year = read_year("Enter book year: ")
            library.add_book(title, author, year)
            print(f"✅ Book '{title}' added successfully.")

        elif choice == "2":
            print("\n--- View Books ---")
            print_books(library.view_books())

        elif choice == "3":
            print("\n--- Search Book ---")
            title = read_non_empty_string("Enter book title to search: ")
            results = library.search_book(title)
            if results:
                for book in results:
                    print(book)
            else:
                print("❌ Book not found.")

        elif choice == "4":
            print("\n--- Delete Book ---")
            title = read_non_empty_string("Enter book title to delete: ")
            if library.delete_book(title):
                print(f"✅ Book '{title}' deleted successfully.")
            else:
                print("❌ Book not found.")

        elif choice == "5":
            print(f"\n📚 Total books in the library: {library.count_books()}")

        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("⚠️  Invalid option, please choose a number between 1 and 6.")


if __name__ == "__main__":
    main()
