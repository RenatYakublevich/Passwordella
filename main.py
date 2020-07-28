import string
import random
import time
import os
import sys
import argparse


SYMBOLS = string.ascii_uppercase + string.ascii_lowercase + string.digits

class Passwordella:

    def design_line():
        ''' Function to display line of = in terminal '''
        print('=' * 25,'\n')

    def start():
        ''' Function for launch program, and for I/O connection with user '''
        Passwordella.design_line()
        print('Hello, it\'s Passwordella(Program for generate passwords)\n')
        answer_users = input('What do you want to produce\n 1 - Generate random password from random symbols and random length\n 2 - Generate a random password from random characters and a certain length\n 3 - Generate a lot of number of passwords ')
        Passwordella.design_line()

        try:
            if answer_users == '1':
                print(Passwordella.generate_random_password())

            elif answer_users == '2':
                length = int(input('Write length for password '))
                print(Passwordella.generate_random_password(length))

            elif answer_users == '3':
                Passwordella.generate_many_random_password()

            elif answer_users == 'cls' or answer_users == 'clear()' or answer_users == 'clear':
                sys.exit()
            else:
                print('I dont understand u!')
                time.sleep(1.5)
                os.system('cls||clear')

                Passwordella.start()
        except ValueError:
            print('Error!\nWrite only numbers in length!')
            time.sleep(2)
            os.system('cls||clear')

            Passwordella.start()

        except Exception as e:
            print('ooops...\n{e}'.format(e=e))
            time.sleep(2)
            os.system('cls||clear')

    def generate_random_password(length = 8):
        ''' Function for generation password '''
        final_password = ''
        for el in range(length):
            final_password += random.choice(SYMBOLS)

        return 'Your password - ' + final_password

    def generate_many_random_password(length = 8):
        ''' Function for generation a lot of password '''
        count_password_for_generation = int(input('Write the number of passwords '))

        all_passwords = []
        for element in range(count_password_for_generation):
            final_password = ''
            for el in range(length):
                final_password += random.choice(SYMBOLS)
            all_passwords.append(final_password)

        for el in all_passwords:
            print('Your password - {0}'.format(el))
        question_about_save = input('Want to write all passwords to a txt file?( Y / N ) ')
        if question_about_save == 'Y':
            for el in all_passwords:
                with open('psw.txt','a') as txt:
                    txt.write(el + '\n')
            print('Success!')
        elif question_about_save == 'N':
            sys.exit()
        else:
            print('Repeat pls\nYou can only answer Y or N')
            time.sleep(1.5)
            os.system('cls||clear')
            Passwordella.generate_many_random_password()

#Работа с аргументами командной строки
parser = argparse.ArgumentParser()
parser.add_argument("--length")
args = parser.parse_args()
length = args.length
if str(length) in string.digits:
    print(Passwordella.generate_random_password(int(length)))
    exit()

if __name__ == "__main__":
    Passwordella.start()
