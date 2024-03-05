import random
import sqlite3
import Readfile # Import functions from read_data.py

def main():
  # Connect to the database
  conn = sqlite3.connect("databasefile1.db")

  # Welcome message and instructions
  print("Welcome to the Quiz Bowl!")
  print("Test your knowledge across various categories!")
