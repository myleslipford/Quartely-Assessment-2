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

# Insert questions for each category
sample_questions = {
     'Business Statistics': [
        ('What statistical measure represents the average of a set of values and is commonly used in business to assess central tendency?', 'mean'),
        ('In business statistics, what term describes the measure of the spread of data points around the mean?', 'Standard Deviation'),
        ('What type of statistical analysis examines the relationship between two or more variables, often used in forecasting and optimization in business decision-making?', "Regression Analysis"),
        ("In hypothesis testing, what is the term for the probability of rejecting a true null hypothesis?", "Type Error"),
        ("Which statistical distribution is commonly used to model the distribution of asset prices in finance and is characterized by a bell-shaped curve?", "normal Distribution"),
        ("What statistical tool is employed in quality control to monitor and maintain consistent processes by identifying and addressing variations?", "conttol chart"),
        ("In business, what term describes the systematic collection and interpretation of numerical data, often used for market research and performance analysis?", "Data Analytics"),
        ("What method in statistics involves drawing conclusions about a population based on a subset of data, often used in market research and opinion polling?", "Inferential Statistics"),
        ("Which probability distribution is used to model the number of successes in a fixed number of independent Bernoulli trials and is often applied to scenarios like product defects?", "Binomial Distribution"),
        ("What technique involves analyzing historical data to identify patterns and trends over time, commonly used in business for forecasting and strategic planning?", "Time Series Analysis"),
        
    ],

}