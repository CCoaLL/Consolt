import sqlite3

class edulite:
  def __init__(self, db): # db = 데이터베이스 이름 ex) DB/users.db, DB/memos.db
    self.conn = sqlite3.connect("DB/"+db+".db")
    self.c = self.conn.cursor()

  def sql(self, query, rt=False, allorone="all"): # rt, allorone은 무시하셈
    self.c.execute(query) # 실행

    if rt: # 여기부터
      if allorone=="all":
        return self.c.fetchall()
      else:
        return self.c.fetchone()
    else:
      self.conn.commit() # 여기까지 무시

  def disconnect(self):
    self.conn.close() # 필수