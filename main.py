import os
from pynput.keyboard import Key, Listener, Controller
import drawboard
import time

keyboard = Controller()

time.sleep(1)
os.system("cls") # for windows
#os.system("clear") for linux
print("")
drawboard.print_banner()
drawboard.drawboard()
drawboard.setdefaultpos()

def on_press(key):
    None

def on_release(key):
    try :
        if drawboard.checkifWin():
            print(f"\033[16;0H End Game\t\t")
            keyboard.press(Key.esc)
            return False

        if key == Key.up:
            drawboard.goUp()
            drawboard.print_debug()
            return
        if key == Key.down:
            drawboard.goDown()
            drawboard.print_debug()
            return
        if key == Key.right:
            drawboard.goRight()
            drawboard.print_debug()
            return
        if key == Key.left:
            drawboard.goLeft()
            drawboard.print_debug()
            return

        if key == Key.esc:
            # Stop listener
            return False

        if key.char == 'x':
            drawboard.mark()
            if drawboard.checkifWin():
                print(f"\033[16;0H End Game\t\t")
                keyboard.press(Key.esc)
                return False

        if not drawboard.computer_move():
            return False

        if drawboard.checkifWin():
            print(f"\033[16;0H End Game\t\t")
            keyboard.press(Key.esc)
            return False

    except Exception as e:
        print(f"\033[16;0H exception = {e}")

# Collect events until released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
