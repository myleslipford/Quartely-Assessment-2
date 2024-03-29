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
  categories = Readfile.get_table_names(conn)
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

# Retrieve questions and answers for the chosen category
  category_data = Readfile.get_all_data(conn, selected_category)

  # Start the quiz loop
  score = 0
  num_questions = len(category_data)
  for i, question in enumerate(category_data):
    print(f"\nQuestion {i+1} out of {num_questions}:")
    print(question['question_text'])
    answer = input("Your answer: ")
    if answer.lower() == question['answer_text'].lower():
      print("\033[38;2;0;250;0mCorrect!")
      print("\033[38;2;250;250;250m")
      score += 1
    else:
      print(f"\033[38;2;250;0;0mIncorrect. The answer is: {question['answer_text']}")
      print("\033[38;2;250;250;250m")

  # Display final score
  print(f"\nYour final score: {score} out of {num_questions}")

  # Close the database connection
  conn.close()

if __name__ == "__main__":
  main()