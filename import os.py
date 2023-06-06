import os
import msvcrt
import time

scrnWidth = 80  # Setting screen width for border, can be changed and program will automatically adjust everything else
scrnHeight = 20  # Setting screen height for border, can be changed and program will automatically adjust everything else
gameWidth = 63  # Setting game screen width, can be changed and program will automatically adjust everything else
boardWidth = 17  # Setting scoreboard width, can be changed and program will automatically adjust everything else
leftGapScrn = 6  # space of gap on the left side of the border
ship = [[' ', '^', ' '], ['/', ' ', '\\'], ['-', '-', '-']]  # Storing ship in a list
alienRow = [0, 0]  # Container to store Row/Y-axis of 2 aliens
alienCol = [0, 0]  # Container to store column/X-axis of 2 aliens
alienLifeCheck = [False, False]  # Flag check for checking number of on-screen aliens alive
shipXpos = boardWidth + leftGapScrn + (gameWidth // 2)  # Setting ship position with respect to the border and game screen defined
bullets = [[0, 0, 0, 0] for _ in range(20)]  # Containers for bullet path
bulletMaxRow = [0] * 20  # Max range of bullet path
bulletIndex = 0  # Index of bullet for column/X axis of bullet
points = 0  # In-game Points (1-50)
stage = 1  # In-game stage (5 total)
lifecount = 3

def moveCursor(col, row):
    # Function for repositioning cursor
    os.system("cls" if os.name == "nt" else "clear")
    print("\033[%d;%dH" % (row + 1, col + 1), end='')

def printShip(number):
    # Function to print the ship stored in the list
    for i in range(3):
        print("\t|\t\t|", end='')
        for _ in range(30 + number):
            print(" ", end='')
        print("\033[33m", end='')
        for k in range(3):
            print(ship[i][k], end='')
        print("\033[0m", end='')
        for _ in range(30 - number):
            print(" ", end='')
        print("|")
        print()

    print("\t|\t\t|\t\t\t\t\t\t\t\t|")

def printBorder(number, scr, l):
    # Function to Print the border with respect to the values given above
    print("\t", end='')
    for _ in range(scrnWidth):
        print("_", end='')
    print()

    for _ in range(scrnHeight):
        print("\t|\t\t|\t\t\t\t\t\t\t\t|")

    printShip(number)  # Calling the function to print ship

    print("\t", end='')
    for _ in range(scrnWidth):
        print("_", end='')
    print()

# Main game loop
while True:
    moveCursor(0, 0)
    printBorder(points, stage, lifecount)
    if msvcrt.kbhit():
        key = msvcrt.getch()
        if key == b'q':
            break
    time.sleep(0.1)
