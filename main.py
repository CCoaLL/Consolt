# README.md 봐

from classes import edulite, Answers
import os, random, requests
import Settings

db = edulite.edulite("users")  # Edulite 클래스 : 데이터베이스 관리
db.sql("CREATE TABLE IF NOT EXISTS user (id TEXT, pw TEXT, money INTEGER)")
db.disconnect()

mdb = edulite.edulite("memos")  # 메모 데이터베이스
mdb.sql("CREATE TABLE IF NOT EXISTS memo (text TEXT, id TEXT)")

logged_in = False  # 로그인 상태
logged_id = None  # 아이디
logged_pw = None  # 비밀번호

aws = Answers.Answers(['abc'])
aws.ans("firsttime")  # '도움말' 이라고 치세요 출력
print("\n\n")

while True:
    cmd = str(input(">>> "))  # 명령어
    cmd = cmd.lower()

    tokens = cmd.split()  # 토큰

    answers = Answers.Answers(tokens)  # Answers 클래스 : 여러개의 답변 기능

    ne = True  # 에러가 났는지 안 났는지 확인

    try:
        if tokens[0] == "...":
            pass
    except IndexError:
        ne = False

    if ne == False:
        continue

    if tokens[0] == "설정" or tokens[0] == "setting":  # 설정 명령
        if tokens[1] == "데이터베이스" or tokens[1] == 'database':  # 데이터베이스 설정
            if tokens[2] == "생성" or tokens[2] == 'create':
                db = edulite.edulite("users")
                db.sql("CREATE TABLE user (id TEXT, pw TEXT, money INTEGER)")
                db.disconnect()
            elif tokens[2] == "삭제" or tokens[2] == 'delete':
                os.remove("DB/users.db")
    elif tokens[0] == "가입" or tokens[0] == "join":
        noerror = True  # [아이디] [비번] 썼는지 안 썼는지 체크
        try:
            if tokens[1] == "" or tokens[2] == "":
                pass
        except IndexError:
            noerror = False

        if noerror == False:
            answers.ans('joinerror')
            continue
        else:
            db = edulite.edulite("users")
            db.c.execute("INSERT INTO user VALUES(?, ?, ?)",
                         (tokens[1], tokens[2], 1000))  # 1000은 기본 지급 돈
            db.conn.commit()  # 저장
            db.disconnect()  # db 연결 끊기 (매우 중요!)
            answers.ans('joinsuccess')  # TODO: ✔ 초록색으로 변경
            answers.ans('joinid')
            answers.ans('joinpw')
            logged_in = True
            logged_id = tokens[1]
            logged_pw = tokens[2]
            continue
    elif tokens[0] == "로그인" or tokens[0] == "login":
        noerror = True  # 알지?
        try:
            if tokens[1] == "" or tokens[2] == "":
                pass
        except IndexError:
            noerror = False

        if noerror == False:
            answers.ans('loginerror')
            continue
        else:
            if logged_in == True:
                answers.ans('loggedinalready')
                continue

            db = edulite.edulite("users")  # 유저 db 불러오기
            db.c.execute("SELECT * FROM user WHERE id=?",
                         (tokens[1], ))  # 해당 아이디가 있는 유저 검색
            account = db.c.fetchone()  # 계정 정보

            if type(account) == type(None):  # 아이디로 유저를 찾지 못함
                answers.ans('nouser')
            else:  # 찾음
                if tokens[2] == account[1]:  # tokens[2]는 입력한 비번
                    # account[1]은 계정의 실제 비번
                    answers.ans('loginsuccess')
                    logged_in = True
                    logged_id = tokens[1]
                    logged_pw = tokens[2]

            continue
    elif tokens[0] == "내정보" or tokens[0] == "myaccount":
        if logged_in == False:
            answers.ans("notloggedin")
            continue

        db = edulite.edulite("users")  # 유저 db 불러오기
        db.c.execute("SELECT * FROM user WHERE id=?", (logged_id, ))
        # 로그인된 아이디로 계정 검색
        account = db.c.fetchone()

        if Settings.lang == 'ko':  # 한국어
            print("아이디: " + account[0])
            print("비밀번호: " + account[1])
            print("보유 자산: " + str(account[2]))
        elif Settings.lang == 'en':  # 영어
            print("id: " + account[0])
            print("pw: " + account[1])
            print("money" + str(account[2]))
    elif tokens[0] == "로그아웃" or tokens[0] == 'logout':
        if logged_in == False:
            answers.ans("alreadyloggedout")
        else:
            logged_id = None
            logged_pw = None
            logged_in = False  # 로그아웃
    elif tokens[0] == "도움말" or tokens[0] == "help":
        answers.ans("help")  # classes/Answers.py 꼭 확인

        continue
    elif tokens[0] == "주사위" or tokens[0] == "dice":
        if logged_in == False:
            print("로그인이 필요한 기능입니다.")
            print("로그인 [아이디] [비밀번호] 로 로그인 해주시기 바랍니다.")
            continue

        db = edulite.edulite("users")  # 유저 계정

        db.c.execute("SELECT * FROM user WHERE id=?", (logged_id, ))
        account = db.c.fetchone()

        noerror = True
        ne = True

        try:
            m = tokens[1]  # m은 건 돈
        except IndexError:
            noerror = False
            ne = False
            m = 0  # 0이 기본값임.

        if ne != False:
            if (int(account[2]) < int(tokens[1])):
                print("건 돈이 보유 돈 보다 작습니다...")
                db.disconnect()
                continue

        me = random.randrange(1, 7)
        op = random.randrange(1, 7)

        m = int(m)

        if me > op:  #win
            print("\033[92m이기셨습니다!\033[0m")
            if m == 0:
                winmoney = 100  # 건 돈이 0 (기본값)일때 100 코인만
            else:
                winmoney = m * random.randrange(3, 6)  # 건 돈의 3~5배 만큼

            db.c.execute("UPDATE user SET money=? WHERE id=?",
                         (int(winmoney) + int(account[2]), logged_id))
            db.conn.commit()
            db.disconnect()
            print(f"보상: \033[92m+{winmoney}\033[0m 코인")
            continue
        else:  #lose

            print("\033[31m지셨습니다...\033[0m")

            if m == 0:
                losemoney = 50
            else:
                losemoney = m

            db.c.execute("UPDATE user SET money=? WHERE id=?",
                         (int(account[2]) - int(losemoney), logged_id))
            print(f"손해: \033[31m-{losemoney}\033[0m 코인")
            db.conn.commit()
            db.disconnect()
            continue
    elif tokens[0] == "가위바위보" or tokens[0] == "rockscissorpaper":
        if logged_in == False:
            print("로그인이 필요한 기능입니다.")
            print("로그인 [아이디] [비밀번호] 로 로그인 해주시기 바랍니다.")
            continue

        db = edulite.edulite("users")

        db.c.execute("SELECT * FROM user WHERE id=?", (logged_id, ))
        account = db.c.fetchone()

        noerror = True
        ne = True

        try:
            m = tokens[1]  # m은 추가할 돈
        except IndexError:
            noerror = False
            ne = False
            m = 0  # 0이 기본값임.

        if ne != False:
            if (int(account[2]) < int(tokens[1])):  #
                print("건 돈이 보유 돈 보다 작습니다...")
                db.disconnect()
                continue

        m = int(m)

        me = random.choice(['rock, scissor', 'paper'])
        MrPuter = random.choice(['rock', 'scissor', 'paper'])

        if (me == 'rock' and MrPuter == 'scissor') or (
                me == 'scissor'
                and MrPuter == 'paper') or (me == 'paper'
                                            and MrPuter == 'rock'):
            print("\033[92m이기셨습니다!\033[0m")
            if m == 0:
                winmoney = 10 * random.randrange(2, 11)
            else:
                winmoney = m * random.randrange(2, 11)

            db.c.execute("UPDATE user SET money=? WHERE id=?",
                         (int(winmoney) + int(account[2]), logged_id))
            db.conn.commit()
            db.disconnect()
            print(f"보상: \033[92m+{winmoney}\033[0m 코인")
            continue
        elif not ((me == 'rock' and MrPuter == 'scissor') or
                  (me == 'scissor' and MrPuter == 'paper') or
                  (me == 'paper' and MrPuter == 'rock')):
            print("\033[31m지셨습니다...\033[0m")
            if m == 0:
                losemoney = 10 * random.randrange(2, 6)
            else:
                losemoney = m * random.randrange(2, 6)

            db.c.execute("UPDATE user SET money=? WHERE id=?",
                         (int(account[2]) - int(losemoney), logged_id))
            print(f"손해: \033[31m-{losemoney}\033[0m 코인")
            db.conn.commit()
            db.disconnect()
            continue
        else:
            print("\033[33m비겼습니다.\033[0m")
            continue
    elif tokens[0] == "종료" or tokens[0] == "quit":
        print(
            "made by \033[90mCCoaLL\033[37m#7517\033[0m and \033[90mighe\033[37m#7999"
        )
        print("프로그램을 종료합니다.")
        break
    elif tokens[0] == "한강" or tokens[0] == "hanriver":
        requestData = requests.get('https://api.hangang.msub.kr/')
        print(str(requestData.json()['temp']) + "도 입니다.")
    elif tokens[0] == '언어' or tokens[0] == 'language':
        Settings.ChangeLang()
        continue
    elif tokens[0] == '메모' or tokens[0] == 'memo':
        # 크크루삥뽕 빵삥뽕 빠뽕삥크롱 핑크퐁

        if logged_in == False:
            print("로그인이 필요한 기능입니다.")
            print("로그인 [아이디] [비밀번호] 로 로그인 해주시기 바랍니다.")
            continue

        mdb = edulite.edulite('memos')
        mdb.c.execute("SELECT * FROM memo WHERE id=?", (logged_id,))

        memo = mdb.c.fetchall()

        ne = True
        
        try:
            print(memo[int(tokens[1])-1][0])
        except:
            ne = False

        if ne == False:
            for i in memo:
                print(i[0])

        mdb.disconnect()
                
        continue

    elif tokens[0] == '개발도구' and tokens[1] == '메모작성':
        if logged_in == False:
            print("로그인이 필요한 기능입니다.")
            print("로그인 [아이디] [비밀번호] 로 로그인 해주시기 바랍니다.")
            continue

        contents = tokens[2] 

        contents = contents.replace("$space", " ").replace("$newline", "\n")
        
        mdb = edulite.edulite('memos')

        mdb.c.execute("INSERT INTO memo VALUES(?, ?)",
                     (contents, logged_id))
        mdb.conn.commit()
        mdb.disconnect()

    elif tokens[0] == '메모작성' or tokens[0] == 'write':
        if logged_in == False:
            print("로그인이 필요한 기능입니다.")
            print("로그인 [아이디] [비밀번호] 로 로그인 해주시기 바랍니다.")
            continue            

        contents = tokens[1] 

        contents = contents.replace("$space", " ").replace("$newline", "\n")
        
        mdb = edulite.edulite('memos')

        mdb.c.execute("INSERT INTO memo VALUES(?, ?)",
                     (contents, logged_id))
        mdb.conn.commit()
        mdb.disconnect()
    else:
        answers.ans('what?')
