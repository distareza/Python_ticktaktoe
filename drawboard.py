import random

arr = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

initPosX = 12
initPosY = 5

posX = initPosX
posY = initPosY
stepY = 2
stepX = 4

minY = posY
maxY = posY + 2 * stepY

minX = posX
maxX = posX + 2 * stepX

winner = None


def print_banner():
    print(f"\033[0;0H ")
    print("\t ===============")
    print("\t   Tic Tac Toe  ")
    print("\t ===============")
    print(f"\033[12;0H Move cursor and mark \"X\" ")
    print(f"\033[13;0H Click Esc to Quit ")


def setDefaultPos():
    global posX, posY
    posX = initPosX
    posY = initPosY
    print(f"\033[{posY};{posX}H_")


def drawboard():
    print(f"\033[{initPosY+0};{initPosX-1}H {arr[0][0]} | {arr[0][1]} | {arr[0][2]}")
    print(f"\033[{initPosY+1};{initPosX-2}H { 12 * '-'}")
    print(f"\033[{initPosY+2};{initPosX-1}H {arr[1][0]} | {arr[1][1]} | {arr[1][2]}")
    print(f"\033[{initPosY+3};{initPosX-2}H { 12 * '-'}")
    print(f"\033[{initPosY+4};{initPosX-1}H {arr[2][0]} | {arr[2][1]} | {arr[2][2]}")
    print(f"\033[{initPosY+5};{initPosX-2}H { 12 * '-'}")

def go(direction):
    global posX, posY
    currPosX = posX
    currPosY = posY
    x = int((posX - initPosX) / stepX)
    y = int((posY - initPosY) / stepY)
    currX = x
    currY = y

    try:

        while x >= 0 and x < len(arr) and y >= 0 and y < len(arr[0]):
            if direction == "up":
                y -= 1
            elif direction == "down":
                y += 1
            elif direction == "right":
                x += 1
            elif direction == "left":
                x -= 1

            if x >= 0 and x < len(arr) and y >= 0 and y < len(arr[0]):
                print_debug()
                if not bool(arr[x][y].strip()):
                    if not bool(arr[currX][currY].strip()):
                        print(f"\033[{currPosY};{currPosX}H ")
                    posX = initPosX + x * stepX
                    posY = initPosY + y * stepY
                    print(f"\033[{posY};{posX}H_")
                    print_debug()
                    return

        # set any where empty slot is available
        gotoemptyslot()

    except Exception as ex:
        print(f"\033[17;0H arr = {ex}\t\t")


def mark():
    x = int((posX - initPosX) / stepX)
    y = int((posY - initPosY) / stepY)
    if not bool(arr[x][y].strip()):
        arr[x][y] = 'X'
        print(f"\033[{posY};{posX}HX")
        return True
    else:
        return False


def goUp():
    go("up")


def goDown():
    go("down")


def goLeft():
    go("left")


def goRight():
    go("right")


def print_debug():
    x = int((posX - initPosX) / stepX)
    y = int((posY - initPosY) / stepY)
    # print(f"\033[4;30H posX = {posX}, posY = {posY}")
    # print(f"\033[5;30H initX = {initPosX}, initY = {initPosY}")
    # print(f"\033[6;30H stepX = {stepX}, stepY = {stepY}")
    # print(f"\033[7;30H x = {x}, y = {y}, is blank : {bool(arr[x][y].strip())}\t\t")
    # print(f"\033[8;30H arr = {arr}\t\t")


def checkifWin():
    global winner
    winner = None
    for mark in 'X', 'O':
        for i in range(3):
            if arr[i][0] == mark and arr[i][0] == arr[i][1] and arr[i][1] == arr[i][2]:
                winner = mark
                return True
            if arr[0][i] == mark and arr[0][i] == arr[1][i] and arr[1][i] == arr[2][i]:
                winner = mark
                return True

        if arr[0][0] == mark and arr[0][0] == arr[1][1] and arr[1][1] == arr[2][2]:
            winner = mark
            return True

        if arr[2][0] == mark and arr[2][0] == arr[1][1] and arr[1][1] == arr[0][2]:
            winner = mark
            return True

    return False


def computer_move():
    list_move = []
    # check user move
    for mark in ("O", "X"):
        for x in range(3):
            list_cell = [(0, 1, 2), (1, 2, 0), (2, 0, 1)]
            for cell in list_cell:
                # check horizontally
                if arr[x][cell[0]].strip() == mark \
                        and arr[x][cell[1]].strip() == mark \
                        and not bool(arr[x][cell[2]].strip()):
                    computer_mark(x, cell[2])
                    return True
                # check vertically
                if arr[cell[0]][x].strip() == mark \
                        and arr[cell[1]][x].strip() == mark \
                        and not bool(arr[cell[2]][x].strip()):
                    computer_mark(cell[2], x)
                    return True

        # check diagonally
        for mark_sign in [(' ', mark, mark), (mark, ' ', mark), (mark, mark, ' ')]:
            if arr[0][0].strip() == mark_sign[0].strip() \
                    and arr[1][1].strip() == mark_sign[1].strip() \
                    and arr[2][2].strip() == mark_sign[2].strip():
                for i in range(3):
                    if not bool(mark_sign[i].strip()):
                        computer_mark( i, i)
                        return True
            if arr[2][0].strip() == mark_sign[0].strip() \
                    and arr[1][1].strip() == mark_sign[1].strip() \
                    and arr[0][2].strip() == mark_sign[2].strip():
                if not bool(mark_sign[0].strip()):
                    computer_mark(2, 0)
                    return True
                if not bool(mark_sign[1].strip()):
                    computer_mark(1, 1)
                    return True
                if not bool(mark_sign[2].strip()):
                    computer_mark(0, 2)
                    return True

    print(f"\033[17;0HRandom move")
    arr_row = [0, 1, 2]
    random.shuffle(arr_row)
    arr_col = [0, 1, 2]
    random.shuffle(arr_col)
    for row in arr_row:
        for col in arr_col:
            if not bool(arr[row][col].strip()):
                list_move.append((row, col))
    if len(list_move) > 0:
        com_move = random.choice(list_move)
        computer_mark(com_move[0], com_move[1])
        return True
    else:
        print(f"\033[15;0H No other move\t\t")
        return False


def computer_mark(com_x, com_y):
    arr[com_x][com_y] = 'O'
    comPosX = initPosX + com_x * stepX
    comPosY = initPosY + com_y * stepY
    print(f"\033[{comPosY};{comPosX}HO")
    gotoemptyslot()

# set any where empty slot is available
def gotoemptyslot():
    global posX, posY
    arr_row = [0, 1, 2]
    random.shuffle(arr_row)
    arr_col = [0, 1, 2]
    random.shuffle(arr_col)
    for x in arr_row:
        for y in arr_col:
            if not bool(arr[x][y].strip()):
                posX = initPosX + x * stepX
                posY = initPosY + y * stepY
                print(f"\033[{posY};{posX}H_")
                return
