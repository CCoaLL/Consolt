from msvcrt import getch
import getpass, sys

def input_password(prompt='비밀번호 : '):
    if sys.stdin is not sys.__stdin__:
        pwd = getpass.getpass(prompt)
        return pwd
    else:
        pwd = ""        
        sys.stdout.write(prompt)
        sys.stdout.flush()        
        while True:
            key = ord(getch())
            if key == 13:
                sys.stdout.write('\n')
                break
            if key == 8:
                if len(pwd) > 0:
                    sys.stdout.write('\b' + ' ' + '\b')                
                    sys.stdout.flush()
                    pwd = pwd[:-1]                    
            else:
                char = chr(key)
                sys.stdout.write('*')
                sys.stdout.flush()                
                pwd = pwd + char
        return pwd


a = input_password()

print(a)