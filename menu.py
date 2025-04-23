from ciph_hill import *
from ciph_recur_hill import *
def menu():
    cipher =str(input("Выберите шифр, котрым хотите воспользоваться:\n 1 - Шифр Хилла\n 2 - Рекуррентный шифр Хилла\n Ваш выбор: "))
    action = str(input("Выберите, что хотите сделать:\n 1 - Зашифровать\n 2 - Расшифровать\n Ваш выбор: "))
    if cipher == '1' and action == '1':
        ciph_hill_encode()

    if cipher == '1' and action == '2':
        ciph_hill_decode()

    if cipher == '2' and action == '1':
        rec_hill_encode()

    if cipher == '2' and action =='2':
        rec_hill_decode()