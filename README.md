# Quartely-Assessment-2


How to Start the quiz bowl:
1. Too start the Quiz the only file that you should have too run is Appfile.py



How to play:
1. When you run Appfile.py, the application will display a list of available categories based on your database tables.
2. Select the category you want to be quizzed on by entering the corresponding number (1, 2, 3, 4, 5,).
3. The application will present 10 question one by one. Enter your answer.
4. You will receive immediate feedback after entering each answer (green for correct, red for incorrect).
5. After all questions are answered, you'll see your final score.



datebasefile1.db:
1. stores all 5 categories in it along with there questions and answers


Createfile.py:
1. Connects to an SQLite database (or creates it).
2. Defines categories (Business Statistics, etc.).
3. Creates tables for each category with columns for question, answer, and unique identifier.
4. Inserts sample questions using a dictionary.
5. Saves changes and closes the connection.


Readfile.py
1. Get Category Lists: Retrieves all tables (categories) from the database.
2. Get Questions by Category: Fetches all question-answer pairs from a specific category table.



Appfile.py:
- This file lets you play a quiz bowl game and explore categories in the database.

Key Functionalities:
1. Connects to the database.
2. Displays available categories.
3. Guides you through a quiz based on your chosen category.
4. Provides feedback and tracks your score.


