import random
import string

def password_generator(len = 8):
    asccii_options = string.ascii_letters
    number_options = string.digits
    punctuation_options = string.punctuation
    options = asccii_options + number_options + punctuation_options
    
    password_user = ""
    for i in range(0, len):
        character = random.choice(options)
        password_user = password_user + character
    return print("Senha gerada : /n" + password_user)

user_choice = input("Quantos digitos você deseja utilizar? ")
if user_choice.isdigit():
    user_choice = int(user_choice)
else:
    print("Entrada invalida. ")
    quit()
    
    
password_generator(len=user_choice)