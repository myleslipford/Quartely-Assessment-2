import random
import sqlite3
import Readfile # Import functions from read_data.py

def main():
  # Connect to the database
  conn = sqlite3.connect("databasefile1.db")

  # Welcome message and instructions
  print("Welcome to the Quiz Bowl!")
  print("Test your knowledge across various categories!")

 # Get a list of available categories
  categories = ReadFileone.get_table_names(conn)
  print("\nAvailable Categories:")
  for i, category in enumerate(categories):
    print(f"{i+1}. {category}")
    
# User chooses a category
  while True:
    try:
      choice = int(input("\nChoose a category (by number): "))
      if 1 <= choice <= len(categories):
        selected_category = categories[choice - 1]
        break
      else:
        print("Invalid choice. Please enter a number between 1 and", len(categories))
    except ValueError:
      print("Invalid input. Please enter a number.")
