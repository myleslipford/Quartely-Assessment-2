import sqlite3

def get_table_names(conn):
  """Retrieves a list of all table names from the database.

  Args:
      conn: A database connection object.

  Returns:
      A list of table names.
  """
  c = conn.cursor()
  c.execute("SELECT name FROM sqlite_master WHERE type='table'")
  table_names = [row[0] for row in c.fetchall()]
  return table_names

def get_all_data(conn, table_name):
  """Retrieves all data (questions and answers) from a specific table.

  Args:
      conn: A database connection object.
      table_name: The name of the table to retrieve data from.

  Returns:
      A list of dictionaries, where each dictionary contains a question and answer.
  """
  c = conn.cursor()
  c.execute(f"SELECT * FROM {table_name}")
  data = c.fetchall()
  return [{'question_text': row[1], 'answer_text': row[2]} for row in data]
