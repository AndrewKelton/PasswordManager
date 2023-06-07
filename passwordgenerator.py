from random import randint
import random

alphabet = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','.', '_','!','#','$','%']
password = []

class PasswordGen(object):

    def __innit__(self, alphabet, lettersL, numbersL, symbolsL):
       
        self.alphabet = alphabet
        self.lettersL = lettersL
        self.numbersL = numbersL
        self.symbolsL = symbolsL
    
    def letters(alphabet):

        lettersL = []
        while len(lettersL) < randint(5,25):
            x = randint(10,61)
            lettersL.append(alphabet[x])
        return lettersL
    
    def numbers(alphabet):

        numbersL = []
        while len(numbersL) < randint(5,25):
            x = randint(0,9)
            numbersL.append(alphabet[x])
        return numbersL

    def symbols(alphabet):

        symbolsL = []
        while len(symbolsL) < randint(5,25):
            x = randint(62,67)
            symbolsL.append(alphabet[x])
        return symbolsL

    x = randint(randint(20,30),randint(30,40))
    lettersL = letters(alphabet)
    numbersL = numbers(alphabet)
    symbolsL = symbols(alphabet)
    randoml = []

    while len(password) < x:
        lettersL = letters(alphabet)
        numbersL = numbers(alphabet)
        symbolsL = symbols(alphabet)
        randoml.append((random.choice(lettersL)))
        randoml.append((random.choice(numbersL)))
        randoml.append((random.choice(symbolsL)))
        if len(randoml) > 10000: password.append(random.choice(randoml)) 
        
    
    print('Your generated password is:', ''.join(password))
    
