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

    'Business Database mgmt Science': [
        ('Purpose of RDBMS?', 'organization'),
        ('SQL Full Form?', "Structured Query Language"),
        ('Combining Data Sources?', "Integration"),
        ("Decision Trees in", "Modeling"),
        ("Purpose of Normalization?", "Efficiency"),
        ("OLAP vs. OLTP?", "analysis"),
        ("Linear Programming in?", "Optimization"),
        ("Primary Key ensures", "uniqueness"),
        ("Database Index Purpose", "Retrieval"),
        ("Data Warehouse vs. Database?", "Analytical"),
        
    ],

    'General Biology II': [
        ('What is the process by which cells engulf large particles, such as food or other cells, by wrapping their cell membrane around them?', 'Phagocytosis'),
        ("In genetics, what term describes the alteration of an organism's genetic material, often resulting in new traits or characteristics?", "Mutation"),
        ("What is the name of the process by which a cell duplicates its DNA and then divides into two identical daughter cells?", "Cell Division"),
        ("Which organelle is responsible for the synthesis of lipids, detoxification of drugs and poisons, and storage of calcium ions in eukaryotic cells?", "Smooth Endoplasmic Reticulum "),
        ("What term describes the tendency of organisms to maintain internal stability in response to environmental changes?", "Homeostasis"),
        ("In cellular respiration, what is the final electron acceptor in the electron transport chain?", "Oxygen"),
        ("What is the name of the process by which cells convert light energy into chemical energy, producing glucose in plants?", "Photosynthesis"),
        ("Which molecule is often called the building blocks of life and consists of a sugar, a phosphate group, and a nitrogenous base?", "Nucleotide"),
        ("What is the term for the phase of the cell cycle during which the cell is actively growing, carrying out its normal functions, and preparing for cell division?", "Interphase"),
        ("In ecology, what is the term for the community of organisms and their physical environment interacting as an ecological unit?", "Ecosystem"),
        
    ],
    'Mgmt organization Behavior': [
        ('What psychological theory suggests that individuals are motivated by internal factors such as autonomy, mastery, and purpose in the workplace?', 'Self-Determination Theory'),
        ('In organizational behavior, what term describes the process through which individuals acquire the knowledge, skills, and attitudes necessary to be effective members of an organization?', "Onboarding"),
        ('What leadership style involves a leader who sets clear expectations, makes decisions independently, and expects subordinates to follow instructions without much input?', "Autocratic Leadership"),
        ("According to Frederick Herzberg's Two-Factor Theory, what are the two categories of factors that influence job satisfaction and dissatisfaction?", "Hygiene and motivators"),
        ("What term in organizational behavior refers to the psychological discomfort a person feels when their attitudes or beliefs are inconsistent with their behavior?", "Cognitive Dissonance"),
        ("In the context of teams, what term describes a group phenomenon where members prioritize agreement and consensus over critical evaluation of information?", "Groupthink"),
        ("What organizational change model proposes that change occurs through a series of stages: unfreezing, changing, and refreezing?", " Lewin's Change Mode"),
        ("What concept in organizational behavior refers to the degree to which individuals believe they control their own fate and can influence their work environment?", "Locus of Control"),
        (" Who introduced the concept of the psychological contract in the context of employment, emphasizing the mutual expectations between employees and organizations?", "Denise Rousseau"),
        ("What communication model, introduced by Wilbur Schramm, involves the sender encoding a message, the message being transmitted through a channel, and the receiver decoding the message?", "Schramm's Model of Communication"),
        
    ],

    'Business Applications': [
        ('What does "HTML" stand for?', 'HyperText Markup Language'),
        ('Which programming language is often used for creating dynamic web pages in business applications?', "JavaScript"),
        ("What does API stand for in software development?", "Application Programming Interface"),
        ("Which design pattern separates the presentation layer, business logic, and data access in an application?", "MVC"),
        ("What type of database is commonly used for business applications and uses tables to store data?", "Relational"),
        ("In version control, what does VCS stand for?", "Version Control System"),
        ("What does UX stand for in mobile app development?", "User Experience"),
        ("Which programming language is known for its platform independence and is widely used in enterprise-level business applications?", "Java"),
        ("In software development, what does DevOps aim to integrate?", "agile"),
        ("In software development, what does DevOps aim to integrate?", "Development and Operations"),
        
    ],

}