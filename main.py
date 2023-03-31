import pynput
import os

keyboard = pynput.keyboard
keyboardCon = keyboard.Controller
mouse = pynput.mouse
mouseCon = mouse.Controller

def ReadKeyboard(key):
    global activeListener

    print('\nYou Entered {0}'.format( key))
 
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    
def StartKeyboardListener():
    # Collect all event until released
    with keyboard.Listener(on_press = ReadKeyboard) as listener:  
        listener.join()
        MainMenu()

def MainMenu():
    os.system('clear')
    while True:
        try:
            print("Choose option:\n1. Keyboard\n2. Mouse\n3. Exit")
            choice = input("Selection: ")
        except:
            print("Please enter a valid value.\n")
            continue
        if choice != None:
            break
    if choice == "1":
        print("Starting Keyboard Listener...")
        StartKeyboardListener()
    elif choice == "2":
        return(None)
    elif choice == "3":
        print("Quitting...")
        exit()

MainMenu()