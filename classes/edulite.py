import sqlite3

class edulite:
  def __init__(self):
    self.conn = sqlite3.connect("DB/users.db")
    self.c = self.conn.cursor()

  def sql(self, query, rt=False, allorone="all"):
    self.c.execute(query)

    if rt:
      if allorone=="all":
        return self.c.fetchall()
      else:
        return self.c.fetchone()
    else:
      self.conn.commit()

  def disconnect(self):
    self.conn.close()