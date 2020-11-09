import os
import datetime
import string
import json
import random

def setup():
    os.system('clear')
    print('Hii!!!... I am your digital assistant!.. I am there to help you whenever you want...')
    print('Before getting started, I would like to know you more, so that I can do my best in assisting you...')
    choice = input('Would you like to set me up? : ')
    if'yes' in choice or 'yeah' in choice or 'yep' in choice or 'sure' in choice or 'yup' in choice or 'okay' in choice or 'y' in choice or 'Y' in choice or 'sure' in choice:
        print('Okay, so lets get started....')
        os.system('clear')
        print('*********PLEASE ENTER YOUR INFORMATION*********')
        print('please enter your name: ',end='')
        uname=string.capwords(input())
        print('Okay... Now I have sufficient information about you. Now its time to customize me.')
        os.system('clear')
        print('Thats it! I am all set and ready to asist you.')
        flag = '1'
        info={"uname":uname, "flag":flag}
        data=json.dumps(info)
        with open('user_info.json','w') as f:
            f.write(data)
            f.close()
    else:
        print('No worries, you can set me up later on...')


def greet():
    morning=['Good Morning','Hii','Hello','Hey']
    afternoon=['Good Afternoon','Hii','Hello','Hey']
    evening=['Good Evening','Hii','Hello','Hey']
    night=['Hii','Hello','Hey']
    hour=int(datetime.datetime.now().hour)
    if hour>=4 and hour<12:
        print(random.choice(morning) + usr_name)
    
    elif hour>=12 and hour<=5:
        print(random.choice(afternoon) + usr_name)
   
    elif hour>=6 and hour<9:
        print(random.choice(evening) + usr_name)
    
    else:
        print(random.choice(night) + usr_name)


while(True):
    data=json.load(open('user_info.json'))
    usr_name=(data["uname"])
    flag=((data["voice"]))
    if flag=='0':
        setup()
    else:
        os.system('clear')
        print('---------')
        print('MAIN MENU')
        print('---------')
        print('')
        greet()
        print('\n1. Hadoop Management')
        print('2. HTTPD / Apache Web Server Management')
        print('3. Docker Management')
        print('4. Amazon Web Server Management')
        print('5. Partition Management')
        choice = input('\nEnter your choice: ')
        if choice == '1':
            input('Press any key to open Hadoop Management Menu.')
            path_file = (os.path.abspath("hadoop.py"))
            os.system('python3 hadoop.py -p ' + path_file)

        elif choice == '2':
            input('Press any key to open Web Server Management Menu.')
            path_file = (os.path.abspath("httpd.py"))
            os.system('python3 httpd.py -p ' + path_file)

        elif choice == '3':
            input('Press any key to open Docker Management Menu.')
            path_file = (os.path.abspath("docker.py"))
            os.system('python3 docker.py -p ' + path_file)

        elif choice == '4':
            input('Press any key to open AWS Management Menu.')
            path_file = (os.path.abspath("awscli.py"))
            os.system('python3 awscli.py -p ' + path_file)

        elif  choice == '5':
            path_file = (os.path.abspath("staticpart.py"))
            os.system('python3 staticpart.py -p ' + path_file)

        else:
            print('Oops! INVALID CHOICE. Please Try Again!')