from random import randint
import random

alphabet = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','.', '_','!','#','$','%']

class PasswordGen():

    def __innit__(self, alphabet, lettersL, symbolsL):
       
        self.alphabet = alphabet
        self.lettersL = lettersL
        self.symbolsL = symbolsL
    
    def letters(alphabet):

        lettersL = []
        while len(lettersL) < randint(5,25):
            x = randint(11,61)
            lettersL.append(alphabet[x])
        return lettersL
    
    def numbers(alphabet):

        numbersL = []
        while len(numbersL) < randint(5,25):
            x = randint(0,10)
            numbersL.append(alphabet[x])
        return numbersL

    def symbols(alphabet):

        symbolsL = []
        while len(symbolsL) < randint(5,25):
            x = randint(62,67)
            symbolsL.append(alphabet[x])
        return symbolsL

   
    lettersL = letters(alphabet)
    numbersL = numbers(alphabet)
    symbolsL = symbols(alphabet)
    randoml = []
    password = []
    while len(randoml) < randint(12,(len(lettersL) + len(numbersL) + len(symbolsL))):
        randoml.append(random.choice(lettersL))
        randoml.append(random.choice(numbersL))
        randoml.append(random.choice(symbolsL))

    while len(password) < randint(randint(12,15),randint(20,30)):
        password.append(random.choice(randoml))
    
    print('Your generated password is:',''.join(password))


PasswordGen()
