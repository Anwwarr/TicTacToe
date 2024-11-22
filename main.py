import time
#Time library is used to make the game smoother

print("Here is the game board, Type the slot you want to insert your symbol to:")
print('INSERT "D" TO STOP PLAYING')

last = "O"
board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
board2 = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

def reset():
    boardp = [
        ["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"]
    ]

    return boardp

def find(slot):
    board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    for i in range(3):
        for j in range(3):
            if board[i][j] == slot:
                lista = [i, j]
                return lista

def draw(lista, lista2):
    print(f"BOARD:      SLOTS:")
    time.sleep(0.2)
    for i in range(3):
        print("|", end="")
        for j in range(3):
            print(lista2[i][j], end="|")
        print("    ", end="|")
        for j in range(3):
            print(lista[i][j], end="|")
        time.sleep(0.2)
        print()



draw(board, board2)
symbol = -1

def win(lista):
    for i in range(3):

        if (lista[i][0] == lista[i][1]) and (lista[i][1] == lista[i][2]) and (lista[i][0] == "X" or lista[i][0] == "O"):
            return True
        elif (lista[0][i] == lista[1][i]) and (lista[1][i] == lista[2][i]) and (
                lista[2][i] == "X" or lista[2][i] == "O"):
            return True
        elif (lista[0][0] == lista[1][1]) and (lista[1][1] == lista[2][2]) and (
                lista[2][2] == "X" or lista[2][2] == "O"):
            return True
        elif (lista[0][2] == lista[1][1]) and (lista[1][1] == lista[2][0]) and (
                lista[2][0] == "X" or lista[2][0] == "O"):
            return True
    return False

def ai(boar):
    boardt = []
    boardt2 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    for row in boar:
        boardt.append(row)

    for i in range(3):
        for j in range(3):
            if boardt[i][j] == "-":
                boardt[i][j] = "O"
                if win(boardt):
                    return boardt2[i][j]
                else:
                    boardt[i][j] = "-"

    for i in range(3):
        for j in range(3):
            if boardt[i][j] == "-":
                boardt[i][j] = "X"
                if win(boardt):
                    return boardt2[i][j]
                else:
                    boardt[i][j] = "-"

    if boar[1][1] == "-":
        return int(5)
    elif boar[0][0] == "-":
        return 1
    elif boar[0][2] == "-":
        return 3
    elif boar[2][0] == "-":
        return 7
    elif boar[2][2] == "-":
        return 9
    elif boar[0][1] == "-":
        return 2
    elif boar[1][0] == "-":
        return 4
    elif boar[1][2] == "-":
        return 6
    elif boar[2][1] == "-":
        return 8
    else:
        return 0


last = "O"

while True:

    if last == "O":
        print()
        print("Your Turn:")
        time.sleep(0.5)
        slot = input("slot: ")
        print()
        time.sleep(0.5)
        if slot == "D":
            print("Thanks for playing!")
            break

        try:
            slot = int(slot)
            while slot > 9 or slot < 1:
                print("Not Valid Slot!")
                slot = int(input("slot: "))
                if slot == "D":
                    print("Thanks for playing!")
                    exit()

            lista = find(slot)
            x = lista[0]
            y = lista[1]

            if board2[x][y] != "-":
                print("Slot already taken! Choose another slot.")
                continue

            if board2[x][y] == "-":
                board2[x][y] = "X"
                last = "X"

        except ValueError:
            print("Not Valid Slot!")
            pass

    elif any("-" in row for row in board2):
        print()
        time.sleep(1)
        print("AI's turn:")
        time.sleep(1)
        slot = int(ai(board2))
        lista = find(slot)
        x = lista[0]
        y = lista[1]
        board2[x][y] = "O"
        symbol *= -1
        last = "O"

    elif not any("-" in row for row in board2):
        print()
        time.sleep(0.5)
        print()
        print("TIE")
        print()
        time.sleep(0.5)
        print("Restarting the game...")
        time.sleep(0.5)
        board2 = reset()

    else:
        print()
        time.sleep(0.5)
        print()
        print("TIE")
        print()
        time.sleep(0.5)
        print("Restarting the game...")
        time.sleep(0.5)
        board2 = reset()

    if win(board2):
        print()
        draw(board, board2)
        print()
        print(f"{last} wins!")
        time.sleep(0.5)
        print("Restarting the game...")
        print()
        time.sleep(0.5)
        board2 = reset()

    draw(board, board2)

print("Made with no algoritms, no libraries (except time), no AI. Just vanilla")
print("python with simple text based board and search method for AI's turn.")
