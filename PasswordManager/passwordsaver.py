from passwordgenerator import PasswordGen
from passwordgenerator import password

PasswordGen()

def fileSave():

    f2 = open('numberOfPasswords.txt', 'r')
    p = f2.read()
    p = int(p)
    f2.close()
    answer = input('Would you like to save this password? Y/N...: ')

    if answer.upper() == 'Y':
        p+=1
        f = open('passwords.txt', 'a')
        f.write(f'\nPassword {p}: {password}')
        f.close()
        f2 = open('numberOfPasswords.txt', 'a')
        f2.truncate(0)
        f2.write(str(p))
        f2.close()
    else:
        f = open('passwords.txt', 'r')
        print(f.read())


fileSave()
