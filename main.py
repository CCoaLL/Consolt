from classes import edulite
import os, random

logged_in = False
logged_id = None
logged_pw = None

print("처음 사용해보신다면 `도움말` 이라고 쳐보세요.")
print("\n\n")

db = edulite.edulite()
db.sql("CREATE TABLE IF NOT EXISTS user (id TEXT, pw TEXT, money INTEGER)")
db.disconnect()

while True:
  cmd = str(input(">>> "))
  tokens = cmd.split()

  ne = True

  try:
    if tokens[0] == "...":
      pass
  except IndexError:
    ne = False

  if ne == False:
    continue

  if tokens[0] == "설정": #설정 명령
    if tokens[1] == "데이터베이스": #데이터베이스 설정
      if tokens[2] == "생성":
        db = edulite.edulite()
        db.sql("CREATE TABLE user (id TEXT, pw TEXT, money INTEGER)")
        db.disconnect()
      elif tokens[2] == "삭제":
        os.remove("DB/users.db")
  elif tokens[0] == "가입":
    noerror = True
    try:
      if tokens[1] == "" or tokens[2] == "":
        pass
    except IndexError:
      noerror = False

      
    if noerror == False:
      print("❗  형식: `가입 [아이디] [비밀번호]`")
      continue
    else:
      db = edulite.edulite()
      db.c.execute("INSERT INTO user VALUES(?, ?, ?)", (tokens[1], tokens[2], 1000))
      db.conn.commit()
      db.disconnect()
      print("✔  가입 완료")
      print("가입된 아이디: " + tokens[1])
      print("가입된 비밀번호: " + tokens[2])
      logged_in = True
      logged_id = tokens[1]
      logged_pw = tokens[2]
      continue
  elif tokens[0] == "로그인":
    noerror = True
    try:
      if tokens[1] == "" or tokens[2] == "":
        pass
    except IndexError:
      noerror = False

      
    if noerror == False:
      print("❗  형식: `로그인 [아이디] [비밀번호]`")
      continue
    else:
      db = edulite.edulite()
      db.c.execute("SELECT * FROM user WHERE id=?", (tokens[1],))
      account = db.c.fetchone()

      if type(account) == type(None):
        print("존재하지 않는 유저입니다.")
      else:
        if tokens[2] == account[1]:
          print("로그인에 성공하였습니다!")
          logged_in = True
          logged_id = tokens[1]
          logged_pw = tokens[2]

      continue
  elif tokens[0] == "내정보":
    if logged_in == False:
      print("로그인이 되어있지 않습니다")
      continue
      
    db = edulite.edulite()
    db.c.execute("SELECT * FROM user WHERE id=?", (logged_id,))
    account = db.c.fetchone()

    print("아이디: "+account[0])
    print("비밀번호: "+account[1])
    print("보유 자산: "+str(account[2]))
  elif tokens[0] == "로그아웃":
    if logged_in == False:
      print("이미 로그아웃 상태입니다.")  
    else:
      logged_id = None
      logged_pw = None
      logged_in = False
  elif tokens[0] == "도움말":
    print("\033[95m---------- 도움말 ----------\033[0m")
    print("\n")
    print("[] = 필수   |   () = 선택적")
    print("\n")
    print("\033[33m 계정 관련 명령어들\033[96m")    
    print("  \033[0m■ \033[96m가입 \033[31m[아이디] [비밀번호]"+"\033[0m"+"   :   \033[31m[아이디]\033[0m와 \033[31m[비밀번호]\033[0m로 계정을 생성하고 로그인합니다.")
    print("  \033[0m■ \033[96m로그인 \033[31m[아이디] [비밀번호]"+"\033[0m"+"   :   \033[31m[아이디]\033[0m와 \033[31m[비밀번호]\033[0m로 로그인합니다.")
    print("  \033[0m■ \033[96m내정보"+"\033[0m   :   로그인된 유저의 정보(아이디, 비밀번호, 보유자산)을 보여줍니다.")
    print("  \033[0m■ \033[96m로그아웃\033[0m   :   현재 계정에서 로그아웃합니다.")    
    print("")
    print("\033[33m 게임 관련 명령어들")
    print("")    
    print("  \033[0m■ \033[96m주사위 \033[31m(걸 돈)"+"\033[0m   :   이기면 건 돈의 3~5배가 되는 보상을, 지면 건 돈을 모두 잃어버립니다.")
    print("")
    print("\033[33m 기타 명령어들\033[96m")
    print("  \033[0m■ \033[96m종료\033[0m   :   프로그램을 종료합니다.")    
    

    print("\n\033[95m----------        ----------\033[0m")

    continue
  elif tokens[0] == "주사위":
    if logged_in == False:
      print("로그인이 필요한 기능입니다.")
      print("로그인 [아이디] [비밀번호] 로 로그인 해주시기 바랍니다.")
      continue

    
    noerror = True

    try:
      m = tokens[1]
    except IndexError:
      noerror = False
      m = -7 #  -7이 기본값임.

    me = random.randrange(1, 7)
    op = random.randrange(1, 7)

    db = edulite.edulite()

    db.c.execute("SELECT * FROM user WHERE id=?", (logged_id,))
    account = db.c.fetchone()

    m = int(m)    

    if me > op: #win
      print("\033[92m이기셨습니다!\033[0m")
      if m == -7:
        winmoney = 100
      else:
        winmoney = m*random.randrange(3, 6)

      db.c.execute("UPDATE user SET money=? WHERE id=?", (int(winmoney)+int(account[2]), logged_id))
      db.conn.commit()
      db.disconnect()
      print(f"보상: \033[92m+{winmoney}\033[0m 코인")
      continue
    else: #lose
      
      print("\033[31m지셨습니다...\033[0m")

      if m==-7:
        losemoney = 50
      else:
        losemoney = m

      db.c.execute("UPDATE user SET money=? WHERE id=?", (int(account[2])-int(losemoney), logged_id))
      print(f"손해: \033[31m-{losemoney}\033[0m 코인")
      db.conn.commit()
      db.disconnect()
      continue
  elif tokens[0] == "종료":
    print("프로그램을 종료합니다")
    break
  else:
    print("없는 명령어입니다. `도움말` 이라고 쳐서 명령어들을 확인하세요.")