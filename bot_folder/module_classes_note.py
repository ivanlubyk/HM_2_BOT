from collections import UserDict
from string import ascii_letters
from datetime import datetime, timedelta
import os
import locale
locale.setlocale(locale.LC_ALL, "")
import json
import time

class Record:
    def __init__(self):
        self.notes = self.load_notes()

    def save_notes(self):
        with open("notes.json", "w") as f:
            json.dump(self.notes, f)
        print("Saved {} notes".format(len(self.notes)))

    def load_notes(self):
        if not os.path.exists("notes.json"):
            with open("notes.json", "w") as f:
                json.dump([], f)
        with open("notes.json", "r") as f:
            notes = json.load(f)
        count_notes = len(notes)
        print("Loaded {} notes".format(count_notes))
        return notes

    def load_notes_from_file(self, file_path):
        with open(file_path, "r") as f:
            notes = json.load(f)
        self.notes = notes
        self.save_notes()
        print("Loaded {} notes from file".format(len(notes)))

    def add_note(self):
        title = input("Enter a title: ")
        text = input("Enter the text: ")
        tags = input("Enter tags (comma-separated): ").split(",")
        while not tags or all(not tag.strip() for tag in tags):
            print("Error: At least one tag must be provided.")
            tags = input("Enter tags (comma-separated): ").split(",")
        new_note = {"title": title, "text": text, "tags": [tag.strip() for tag in tags]}
        self.notes.append(new_note)
        self.save_notes()
        print("Note added successfully.")

    def search_notes_by_tags(self, tags):
        result_notes = []
        for note in self.notes:
            if set(tags).issubset(set(note["tags"])):
                result_notes.append(note)
        self.print_notes(result_notes)
        print("{} note(s) found.".format(len(result_notes)))

    def sort_notes_by_tags(self):
        sorted_notes = sorted(self.notes, key=lambda x: x["tags"])
        self.print_notes(sorted_notes)

    def print_notes(self, notes):
        print("-" * 66)
        print("| {:^20s} | {:^20s} | {:^20s} |".format("Title", "Text", "Tags"))
        print("-" * 66)
        for note in notes:
            print("| {:20s} | {:20s} | {:20s} |".format(note["title"], note["text"], ", ".join(note["tags"])))
            print("-" * 66)
        
    def edit_note(self, title):
        for note in self.notes:
            if note["title"] == title:
                new_title = input("Enter a new title: ")
                new_text = input("Enter new text: ")
                new_tags = input("Enter tags (comma-separated): ")
                while not new_tags or all(not tag.strip() for tag in new_tags.split(",")):
                    print("Error: At least one tag must be provided.")
                    new_tags = input("Enter tags (comma-separated): ")
                new_tags = [tag.strip() for tag in new_tags.split(",")]
                note["title"] = new_title
                note["text"] = new_text
                note["tags"] = new_tags
                print("The note has been edited successfully")
                self.save_notes()
                return
        print("No note with this title was found.")

    def delete_note(self, title):
        for note in self.notes:
            if note["title"] == title:
                self.notes.remove(note)
                print("Note deleted successfully.")
                self.save_notes()
                return
        print("No note with this title was found.")