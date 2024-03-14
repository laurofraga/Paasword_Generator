import PySimpleGUI as sg
import string
import random

layout = [
    [sg.Text("E-mail/Usuário", size=(10, 1)),
     sg.Input(key="usuario", size=(10, 1))],
    [sg.Text("Quantidade de dígitos"), sg.Combo(values=list(range(30)), key="total_chars", 
                                                default_value=1, size=(3, 1))],
    [sg.Output(size=(40, 5))],
    [sg.Button("Gerar senha")]
]

window = sg.Window("Password Generator", layout)

def password_generator(len=8, options=None):
    asccii_options = string.ascii_letters
    number_options = string.digits
    punctuation_options = string.punctuation
    options = asccii_options + number_options + punctuation_options
    
    password_user = ""
    for i in range(len):
        character = random.choice(options)
        password_user += character
    return password_user

while True:
    event, value = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == "Gerar senha":
        user_choice = int(value["total_chars"])
        new_password = password_generator(user_choice)
        print(new_password)
