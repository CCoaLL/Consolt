import random
import Settings

class Answers:
    def __init__(self, tokens):
        self.tokens = tokens
        
    def ans(self, question):
        tokens = self.tokens
        if question == "what?":
            if Settings.lang == 'ko':
                print(random.choice(["잘 알아듣지 못했습니다... `도움말` 이라고 쳐서 명령어들을 확인하세요.", "없는 명령어입니다. `도움말` 이라고 쳐서 명령어들을 확인하세요.", "명령어를 잘못 치신 것 같습니다. 아니라면 `도움말` 이라고 쳐서 명령어들을 확인하세요.", "죄송하지만 알아듣지 못했습니다. `도움말` 이라고 쳐서 명령어들을 확인하세요."]))
            elif Settings.lang == 'en':
                print(random.choice(["I didn't get that. Can you say it again? Type `help` to check the commands.", "I missed what you said. What was that? Type `help` to check the commands.", "Sorry, could you say that again? Type `help` to check the commands.", "Sorry, can you say that again? Type `help` to check the commands.", "Can you say that again? Type `help` to check the commands.", "Sorry, I didn't get that. Can you rephrase? Type `help` to check the commands.", "Sorry, what was that? Type `help` to check the commands.", "One more time? Type `help` to check the commands.", "Say that one more time? Type `help` to check the commands.", "I didn't get that. Can you repeat? Type `help` to check the commands."]))
        elif question == "firsttime":
            if Settings.lang == 'ko':
                print(random.choice(["안녕하세요? 처음이시라면 `도움말` 이라고 쳐보세요.", "처음 사용해보신다면 `도움말` 이라고 쳐보세요." "오늘이 첫 시간이라면 `도움말` 이라고 쳐보세요.", "재미있는 챗봇의 기능을 보시려면 `도움말` 이라고 쳐보세요."]))
            elif Settings.lang == 'en':
                print("If you are using it the first time, type `help`")
        elif question == 'joinerror':
            if Settings.lang == 'ko':
                print("❗  형식: `가입 [아이디] [비밀번호]`")
            elif Settings.lang == 'en':
                print("❗  Form: `join [id] [pw]`")

        elif question == 'loginerror':
            if Settings.lang == 'ko':
                print('❗  형식: `로그인 [아이디] [비밀번호]`')
            elif Settings.lang == 'en':
                print('❗  form: `login [id] [pw]`')
        elif question == 'joinsuccess':
            if Settings.lang == 'ko':
                print('✔  가입 완료') 
            elif Settings.lang == 'en':
                print('✔  join success')
        elif question == 'joinid':
            if Settings.lang == 'ko':
                print(f'가입된 아이디: {tokens[1]}')
            elif Settings.lang == 'en':
                print(f'your id: {tokens[1]}')
        elif question == 'joinpw':
            if Settings.lang == 'ko':
                print("가입된 비밀번호: " + tokens[2])
            elif Settings.lang == 'en':
                print("your pw: " + tokens[2])
        elif question == 'loggedinalready':
            if Settings.lang == 'ko':
                print("이미 로그인이 되어있습니다.")
            elif Settings.lang == 'en':
                print("you are logged in already")
        elif question == 'nouser':
            if Settings.lang == 'ko':
                print("존재하지 않는 유저입니다.")
            elif Settings.lang == 'en':
                print("user doesn't exist")
        elif question == 'loginsuccess':
            if Settings.lang == 'ko':
                print("로그인에 성공하였습니다!")
            elif Settings.lang == 'en':
                print("login success")
        elif question == 'notloggedin':
            if Settings.lang == 'ko':
                print("로그인이 되어있지 않습니다")
            elif Settings.lang == 'en':
                print("login, first")
        elif question == 'alreadyloggedout':
            if Settings.lang == 'ko':
                print("이미 로그아웃 상태입니다")
            elif Settings.lang == 'en':
                print("you are already logged out")
        elif question == 'help':
            if Settings.lang == 'ko':
                print("\033[95m---------- 도움말 ----------\033[0m")
                print("\n")
                print("[] = 필수   |   () = 선택적")
                print("\n")
                print("\033[33m 계정 관련 명령어들\033[96m")
                print(
            "  \033[0m■ \033[96m가입 \033[31m[아이디] [비밀번호]" + "\033[0m" +
            "   :   \033[31m[아이디]\033[0m와 \033[31m[비밀번호]\033[0m로 계정을 생성하고 로그인합니다."
        )
                print("  \033[0m■ \033[96m로그인 \033[31m[아이디] [비밀번호]" + "\033[0m" +
              "   :   \033[31m[아이디]\033[0m와 \033[31m[비밀번호]\033[0m로 로그인합니다.")
                print("  \033[0m■ \033[96m내정보" +
              "\033[0m   :   로그인된 유저의 정보(아이디, 비밀번호, 보유자산)을 보여줍니다.")
                print("  \033[0m■ \033[96m로그아웃\033[0m   :   현재 계정에서 로그아웃합니다.")
                print("")
                print("\033[33m 게임 관련 명령어들")
                print("")
                print("  \033[0m■ \033[96m주사위 \033[31m[걸 돈]" +
              "\033[0m   :   이기면 건 돈의 3~5배가 되는 보상을, 지면 건 돈을 모두 잃어버립니다.")
                print(
            "  \033[0m■ \033[96m가위바위보 \033[31m[가위/바위/보] [걸 돈]" +
            "\033[0m   :   이기면 건 돈의 2~10배가 되는 보상을, 지면 건 돈의 2~5배가 되는 돈을 잃습니다.")
                print("")
                print("\033[33m 설정 관련 명령어들")
                print("")
                print("  \033[0m■ \033[96m설정 \033[31m데이터베이스 [생성/삭제]" +
              "\033[0m   :   관리용 명령어입니다. 특별한 경우가 아니면 이용하지 말하주세요.")
                print("  \033[0m■ \033[96m종료" + "\033[0m   :   프로그램을 종료합니다.")
                print("")
                print("\033[33m 편의 관련 명령어들")
                print("")
                print("  \033[0m■ \033[96m한강" + "\033[0m   :   한강 온도를 알려줍니다.")
                print("  \033[0m■ \033[96m언어" + "\033[0m   :   언어를 한국어에서 영어로, 영어에서 한국어로 바꿉니다.")

                print("\n\033[95m----------        ----------\033[0m")
            elif Settings.lang == 'en':
                print("\033[95m---------- Help ----------\033[0m")
                print("\n")
                print("[] = essential   |   () = optional")
                print("\n")
                print("\033[33m account commands\033[96m")
                print(
            "  \033[0m■ \033[96mjoin \033[31m[id] [pw]" + "\033[0m" +
            "   :   make an account with \033[31m[id]\033[0mand \033[31m[pw]\033[0m."
        )
                print("  \033[0m■ \033[96mlogin \033[31m[id] [pw]" + "\033[0m" +
              "   :   login with \033[31m[id]\033[0mand \033[31m[pw]\033[0m.")
                print("  \033[0m■ \033[96mmyaccount" +
              "\033[0m   :   shows id, pw, and money")
                print("  \033[0m■ \033[96mlogout\033[0m   :   logout to an account")
                print("")
                print("\033[33m game commands")
                print("")
                print("  \033[0m■ \033[96mdice \033[31m[money to gamble]" +
              "\033[0m   :   if you win, you'll get [money to gamble] × 3~5. However, if you lose, you will lost [money to gamble]")
                print(
            "  \033[0m■ \033[96mrockscissorpaper \033[31m[rock/scissor/paper] [money to gamble]" +
            "\033[0m   :   win -> [money to gamble] × 2~10\nlose -> - [money to gamble] × 2~5")
                print("")
                print("\033[33m setting command")
                print("")
                print("  \033[0m■ \033[96msetting \033[31mdatabase [create/delete]" +
              "\033[0m   :   do not use this command.")
                print("  \033[0m■ \033[96mquit" + "\033[0m   :   quit program")
                print("")
                print("\033[33m convenience command")
                print("")
                print("  \033[0m■ \033[96mhanriver" + "\033[0m   :   sends han river's temperature")
                print("  \033[0m■ \033[96mlanguage" + "\033[0m   :   turn language (ko -> en, en -> kp)")

                print("\n\033[95m----------        ----------\033[0m")