import sqlite3
from unittest import result
class Schema:
    def __init__(self):
          self.conn=sqlite3.connect('todo.db')
          self.conn.execute("PRAGMA journal_mode=WAL")
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

class ToDoModel:
    TABLENAME = "Todo"
    def __init__(self):
        self.conn=sqlite3.connect('todo.db')
        self.conn.execute("PRAGMA journal_mode=WAL")
    def create(self,text,description):
        query = f'insert into {self.TABLENAME} '\
                f'(Title, Description) '\
                f'values("{text}", "{description}")'
        result=self.conn.execute(query)
        return result.lastrowid
    def delete(self,todo_id):
        query = f'delete from {self.TABLENAME} where id={todo_id}'
        result=self.conn.execute(query)
        return result.rowcount
    def update(self,todo_id,text,description):
        query = f'update {self.TABLENAME} set Title="{text}", Description="{description}" where id={todo_id}'
        result=self.conn.execute(query)
        return result.rowcount
    def get_all(self):
        query = f'SELECT * FROM {self.TABLENAME}'
        result = self.conn.execute(query)
        return [dict(zip([key[0] for key in result.description], row)) for row in result.fetchall()]
    
