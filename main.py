from pynput import keyboard
import sys
import os
clear = lambda: os.system('cls')


def returnFalse():
    
    return False
    

def press(action):
    if action == "z":
        print("je suis un Z")
    elif action == "s":
        print("je suis un S")
    elif action == "a":
        print("vous desirez faire une action")
        moove = input("quell action voulez vous effectuer ? ")
        print(moove)
    elif action == "w":
        moove = input("que veux tu faire ")
        if moove == "stop":
            print("je m'arrete")
            global end
            end = "ko"

def on_press(key):
    try:
        press(key.char)
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def initListener():
    # with keyboard.Listener(
    #         on_press=on_press,
    #     on_release=on_release) as listener:
    #     listener.join()
    listener = keyboard.Listener(
    on_press=on_press)
    listener.start()

global end
end = "ok"
osef = 0
initListener()
while end == "ok":
    osef += 1