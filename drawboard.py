import random

arr = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

initPosX = 10
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
    print("\t===============")
    print("\t  Tic Tac Toe  ")
    print("\t===============")
    print(f"\033[12;0H Move cursor and mark \"X\" ")
    print(f"\033[13;0H Click Esc to Quit ")


def setdefaultpos():
    move(posX, posY)


def drawboard():
    print(f"\033[4;0H  ")
    for row in [[" "] * 3] * 3:
        col_num = 1
        print("\t", end="")
        for col in row:
            col_num += 1
            if col_num <= 3:
                print("   ", end="|")
            else:
                print("   ")
        print("\t", end="")
        print(12 * "-")


def move(x: int, y: int):
    x = int((posX - initPosX) / stepX)
    y = int((posY - initPosY) / stepY)
    try:
        if not bool(arr[x][y].strip()):
            print(f"\033[{posY};{posX}H_")
    except:
        None


def clear_step():
    x = int((posX - initPosX) / stepX)
    y = int((posY - initPosY) / stepY)
    try:
        if not bool(arr[x][y].strip()):
            print(f"\033[{posY};{posX}H ")
            return True
        return False
    except:
        return False


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
    clear_step()
    global posY
    posY -= stepY
    if posY < minY:
        posY = minY
    move(posX, posY)


def goDown():
    clear_step()
    global posY
    posY += stepY
    if posY > maxY:
        posY = maxY
    move(posX, posY)


def goLeft():
    clear_step()
    global posX
    posX -= stepX
    if posX < minX:
        posX = minX
    move(posX, posY)


def goRight():
    clear_step()
    global posX
    posX += stepX
    if posX > maxX:
        posX = maxX
    move(posX, posY)


def print_debug():
    x = int((posX - initPosX) / stepX)
    y = int((posY - initPosY) / stepY)
    # print(f"\033[12;0H X = {posX}, Y = {posY}")
    # print(f"\033[13;0H initX = {initPosX}, Y = {initPosY}")
    # print(f"\033[14;0H stepX = {stepX}, Y = {stepY}")
    # print(f"\033[15;0H X = {x}, Y = {y}, is blank : {bool(arr[x][y].strip())}\t\t")
    # print(f"\033[16;0H arr = {arr}\t\t")


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
                # check vertically
                if arr[cell[0]][cell[0]].strip() == mark \
                        and arr[cell[1]][cell[1]].strip() == mark \
                        and not bool(arr[cell[2]][cell[2]].strip()):
                    computer_mark(cell[2], cell[2])
                    return True

    for row in range(len(arr)):
        for col in range(len(arr[row])):
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
