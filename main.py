import string
import random
import time
import os
import sys
import argparse
import hashlib

import pizza_encrypt
import cryptography


SYMBOLS = string.ascii_uppercase + string.ascii_lowercase + string.digits

class Passwordella:

    def design_line():
        ''' Function to display line of = in terminal '''
        print('=' * 25,'\n')

    def start():
        ''' Function for launch program, and for I/O connection with user '''
        print('''
╔═╗────╔═╗╔═╗───────────╔╗─────────────
║╬║╔═╗─║═╣║═╣╔╦╦╗╔═╗╔╦╗╔╝║╔═╗╔╗─╔╗─╔═╗─
║╔╝║╬╚╗╠═║╠═║║║║║║╬║║╔╝║╬║║╩╣║╚╗║╚╗║╬╚╗
╚╝─╚══╝╚═╝╚═╝╚══╝╚═╝╚╝─╚═╝╚═╝╚═╝╚═╝╚══╝
Hello, it\'s Passwordella(Program for generate passwords)\n
https://github.com/RenatYakublevich/Passwordella
version 1.3 - created by Renat Yakublevich
        ''')
        answer_users = input('What do you want to produce\n 1 - Generate random password from random symbols and random length\n 2 - Generate a random password from random characters and a certain length\n 3 - Generate a lot of number of passwords \n 4 - Generate password with MD5 \n 5 - Generate a password with specific encryption \n 6 - Use our encryption - Pizza Encrypt\n - - - - - - - - - - - - - - - - - - - -\n 7 - All encrypt on you PC\n 8 - Caesar Cipher ')
        Passwordella.design_line()

        try:
            if answer_users.find('1') != -1:
                print(Passwordella.generate_random_password())

            elif answer_users.find('2') != -1:
                length = int(input('Write length for password '))
                print(Passwordella.generate_random_password(length))

            elif answer_users.find('3') != -1:
                Passwordella.generate_many_random_password()
            elif answer_users.find('4') != -1:
                Passwordella.generate_password_with_encrypt()

            elif answer_users.find('5') != -1:
                specific_encrypt = input('Write name of encryption ')
                Passwordella.generate_password_with_encrypt(specific_encrypt)

            elif answer_users.find('6') != -1:
                question = input(' 1 - Code \n 2 - Decode ')
                string = input('Write your string for Code ')
                if question == '1':
                    print(pizza_encrypt.pizza_encrypt(list(string)))
                elif question == '2':
                    print(pizza_encrypt.pizza_decrypt(list(string)))
                else:
                    print('Write only num!')
                    time.sleep(1.2)
                    Passwordella.start()
                    return

            elif answer_users.find('7') != -1:
                Passwordella.all_encrypt()

            elif answer_users.find('8') != -1:
                input_string = input('Enter the original string ')
                input_rot = input('Enter ther ROT ')

                print(cryptography.encode_caesar(input_string,int(input_rot)))






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

    def generate_password_with_encrypt(encrypt='md5'):
        ''' Function for generate pasword with encrypion '''
        try:
            source_string = input('Enter a keyword for encryption(for example, the site where you want to register) ')
            length = input('Write length for you password(write pass to save the required password length)')

            hash_object = hashlib.new(encrypt)
            hash_object.update(b'{source_string}')

            if length == 'pass':
                print(hash_object.hexdigest())
                return
            print(hash_object.hexdigest()[0:int(length)])
        except ValueError:
            print('There is no such encryption!')

    def all_encrypt():
        ''' Function for return all encryption on PC '''
        for el in hashlib.algorithms_available:
            print(el)

#Работа с аргументами командной строки
parser = argparse.ArgumentParser()
parser.add_argument("--length")
args = parser.parse_args()
length = args.length
if length:
    print(Passwordella.generate_random_password(int(length)))
    exit()

if __name__ == "__main__":
    Passwordella.start()
