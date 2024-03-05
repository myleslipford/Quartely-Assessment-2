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

