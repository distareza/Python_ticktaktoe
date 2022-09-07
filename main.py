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

def checkWinner():
    print(f"\033[16;0H")
    if drawboard.winner == "X":
        print("\tEnd Game - You Win")
    elif drawboard.winner == "O":
        print("\tEnd Game - You Loose")
    else:
        print("\tEnd Game - Draw")
    keyboard.press(Key.esc)

def on_release(key):
    try :
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

        # ignore any key press before enter
        if key == Key.enter:
            return

        if key == Key.esc:
            # Stop listener
            return False

        if key.char == 'x':
            if drawboard.mark():
                if drawboard.checkifWin():
                    checkWinner()
                    return False

                if not drawboard.computer_move():
                    return False

                if drawboard.checkifWin():
                    checkWinner()
                    return False

    except Exception as e:
        print(f"\033[16;0H exception = {e}")

# Collect events until released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

keyboard.press(Key.esc)
print(f"\033[17;0H ")
