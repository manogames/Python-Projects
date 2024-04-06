from assets import ASCII_ASSETS
import os
import time
import random
#Simple function to clean all terminal and detects your OS
def clear_console():
    match os.name:
        case "nt":
            os.system('clear')
        case _ :
            os.system('clear')
#SECTION WHEN "TURNING DICE" AND GIVES A RESULT
def turning_and_result(predict:int):
    clear_console()
    print(ASCII_ASSETS["Menu_Image"])
    print("\n\nTurning...")
    result = random.randint(1,6)
    time.sleep(2)
    clear_console()
    print(ASCII_ASSETS[result])
    print(result)
    print("\nRESULT!!!")
    if result == predict:
        print('\n\nYOU WON!!!')
    else:
        print('\n\nYOU LOST... :(')
    print("\n\n  ⚠  Redirecting to menu...")
    time.sleep(4)
    menu()
#SECTION WHEN CLIENT CHOISE A NUMBER
def Game_Step1():
    clear_console()
    print(ASCII_ASSETS["ready?"])
    try:
        input_number = int(input('Choise a number from 1 to 6\n\n> '))
        turning_and_result(input_number)
    except ValueError:
        clear_console()
        print("  ⚠  That's not a number... redirecting to menu")
        time.sleep(3)
        menu()

#MENU SECTION
def menu():
    clear_console()
    print(ASCII_ASSETS["TextMenu"])
    print(ASCII_ASSETS["Menu_Image"])
    input_menu = input('\nPress Enter to play or type "exit" to leave the game\n\n> ')
    match input_menu:
        case "exit":
            exit()
        case '' :
            Game_Step1()

    

if __name__ == '__main__':
    menu()