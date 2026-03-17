import sqlite3
class Schema:
    def __init__(self):
          self.conn=sqlite3.connect('todo.db')
          self.create_user_table()
          self.create_todo_table()

    def create_todo_table(self):
      query = """
      CREATE TABLE IF NOT EXISTS "Todo" (
        id INTEGER PRIMARY KEY,
        Title TEXT,
        Description TEXT,
        _is_done BOOLEAN,
        _is_deleted BOOLEAN,
        CreatedOn Date DEFAULT CURRENT_DATE,
        DueDate Date,
        UserId INTEGER, FOREIGN KEY(UserId) REFERENCES User(id)
        );
        """
      self.conn.execute(query)

    def create_user_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "User"(
        id INTEGER PRIMARY KEY,
        Name TEXT,
        Email TEXT,
        Username TEXT,
        Password TEXT);
        """
        self.conn.execute(query)

    if __name__=='__main__':
        Schema()
        app.run(debug=True)
