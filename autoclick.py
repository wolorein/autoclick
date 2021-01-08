from pynput.keyboard import Key, Listener
from pynput.mouse import Button, Controller
from time import sleep
from sys import exit
from threading import Thread

def click_func():
    global isCrafting
    global timeToStop

    while True:
        if timeToStop:
            return
        if isCrafting:
            mouse.press(Button.left)
            sleep(1)
            mouse.release(Button.left)

def key_listen_func(key):
    global isCrafting
    global timeToStop

    if key == Key.esc:
        timeToStop = True
        sleep(1)
        exit(0)
    if key == Key.f6:
        isCrafting = not isCrafting

timeToStop = False
isCrafting = False
mouse = Controller()
x = Thread(target=click_func)
l = Listener(on_release=key_listen_func)

x.start()
l.start()
x.join()
l.join()
