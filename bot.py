from webbot import Browser
from random import randint
from time import sleep
from pyautogui import press
web = Browser()
web.go_to("www.instagram.com")


def genRandomDetails():
    email = 'kranepwp%d@yahoo.com' % randint(1,100000)
    #email = '0728599%d%d%d' % (randint(0,10),randint(0,10),randint(0,10))
    name = '' #5 letter name 2 times
    for i in range(2):
        for i in range(6):
            letter = randint(97,120)
            name +=chr(letter)
        name+= ' '
    
    #check empty spaces
    if name[-1] == ' ':
        name = name[:-1]

    #nickname is same as the name but without white spaces
    nickname = ''
    for l in name:
        if l != ' ':
            nickname+=l
    
    #password is same as the nickname + a random 2 digits
    password = ''
    for l in nickname:
        password+=l
    for i in range(1):
        password+=str(randint(1,100))
    #log it
    with open("emailNameNickNamePassword.txt",'a') as f:
        f.write('Email: '+str(email)+'\t\t'+'Name: '+str(name)+'\t\t'+'Nickname: '+str(nickname)+'\t\t'+'Password: '+str(password)+'\n')
        f.close()

    return email,name,nickname,password
        
def enterDet():
    rnd = genRandomDetails()
    sleep(2)
    web.type(rnd[0],into='Email')
    sleep(0.5)
    web.type(rnd[1],into='Full Name')
    sleep(0.5)
    press('tab')
    web.type(rnd[2])
    sleep(0.5)
    web.type(rnd[3],into='Password')
    sleep(1)

def register():
    web.click('Next')
    sleep(0.7)
    web.click('18')
    web.click('Next')
    #next after the error
    sleep(1.5)
    web.click('Next')
    #make sure
    web.click('Next')

def follow():
    sleep(0.5)
    url = 'https://www.instagram.com/mararara84/'
    web.go_to(url)
    sleep(2)
    web.click("Follow")

#work
genRandomDetails()
enterDet()
register()
follow()

'''
gets to register,
enter reg details,
press next,
asks if you are 18 or older as a radio button check,
press next,
press next,
account created

test acc : kranepwp kranenr1 #banned by legal terms

it works sometimes then after a while it gets banned. 
You can make 1 account per ip seems like
'''