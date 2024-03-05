import sqlite3

# Connect to the SQLite database (or create it if not exists)
conn = sqlite3.connect('databasefile1.db')
cursor = conn.cursor()

# Create tables for different categories
categories = [
    'Business Statistics',
    'Business Database mgmt Science',
    'General Biology II',
    'Mgmt organization Behavior',
    'Business Applications'
]

# Create tables for each category
for category in categories:
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {category.replace(" ", "_")} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            answer TEXT
        );
    ''')