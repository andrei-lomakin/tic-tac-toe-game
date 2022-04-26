# This game is implemented by means of the Python standard library
from tkinter import *
import random

root = Tk()
root.title('Tic-tac-toe')
# Game state variable
game_run = True
# List for storing cell values
cells = []
# A variable for identifying a "drawn game" situation
cross_count = 0
# The constant below sets the size of the playing field
FIELD_SIZE = 4
''' The "drawn" level (when the number of crosses specified in the variable below is reached and there is no victory for anyone, a "drawn" is declared)'''
drawn_level = int(FIELD_SIZE ** 2 / 2) + 1

FIELD_SIZE = int(FIELD_SIZE)


# Function to start a new game
def new_game():
    for row in range(FIELD_SIZE):
        for col in range(FIELD_SIZE):
            cells[row][col]['text'] = ' '
            cells[row][col]['background'] = 'lavender'
    global game_run
    game_run = True
    global cross_count
    cross_count = 0


# Function-handler of clicks on game fields
def click(row, col):
    if game_run and cells[row][col]['text'] == ' ':
        cells[row][col]['text'] = 'X'
        global cross_count
        cross_count += 1
        check_win('X')
        if game_run and cross_count < drawn_level:
            computer_move()
            check_win('O')


# The function of checking whether someone's victory has come
def check_win(val):
    # Checking the horizontals
    for row in range(FIELD_SIZE):
        if all(cells[row][col]['text'] == val for col in range(FIELD_SIZE)):
            for col in range(FIELD_SIZE):
                cells[row][col]['background'] = 'green'
            global game_run
            game_run = False
        # Checking verticals
        elif all(cells[col][row]['text'] == val for col in range(FIELD_SIZE)):
            for col in range(FIELD_SIZE):
                cells[col][row]['background'] = 'green'
            game_run = False
    # Checking the first diagonal
    if all(cells[row][row]['text'] == val for row in range(FIELD_SIZE)):
        for row in range(FIELD_SIZE):
            cells[row][row]['background'] = 'green'
        game_run = False
    # Checking the second diagonal
    if all(cells[row][col]['text'] == val for row, col in zip(range(FIELD_SIZE), range(-1, -(FIELD_SIZE + 1), -1))):
        for row, col in zip(range(FIELD_SIZE), range(-1, -(FIELD_SIZE + 1), -1)):
            cells[row][col]['background'] = 'green'
            game_run = False


# The function of checking the possibility of winning (the bot tries not to let the person win)
def can_win(line, val):
    res = False
    empty = [u for u in line if u['text'] == ' ']
    other = [o for o in line if o['text'] == val]
    for l in line:
        if l['text'] == ' ' and len(empty) == 1 and len(other) == (FIELD_SIZE - 1):
            l['text'] = 'O'
            res = True
    return res


# Computer moves function
def computer_move():
    temp_list = []
    # Checking horizontal rows
    for row in range(FIELD_SIZE):
        for col in range(FIELD_SIZE):
            temp_list.append(cells[row][col])
        if can_win(temp_list, 'X'):
            return
        if can_win(temp_list, 'O'):
            return
        temp_list.clear()

    # Checking vertical rows
    for row in range(FIELD_SIZE):
        for col in range(FIELD_SIZE):
            temp_list.append(cells[col][row])
        if can_win(temp_list, 'X'):
            return
        if can_win(temp_list, 'O'):
            return
        temp_list.clear()

    # Checking the first diagonal
    for row in range(FIELD_SIZE):
        temp_list.append(cells[row][row])
    if can_win(temp_list, 'X'):
        return
    if can_win(temp_list, 'O'):
        return
    temp_list.clear()

    # Checking the second diagonal
    for row, col in zip(range(FIELD_SIZE), range(-1, -(FIELD_SIZE + 1), -1)):
        temp_list.append(cells[row][col])
    if can_win(temp_list, 'X'):
        return
    if can_win(temp_list, 'O'):
        return
    temp_list.clear()

    while True:
        row = random.randint(0, (FIELD_SIZE - 1))
        col = random.randint(0, (FIELD_SIZE - 1))
        if cells[row][col]['text'] == ' ':
            cells[row][col]['text'] = 'O'
            break


# Graphical interface of the game
for row in range(FIELD_SIZE):
    line = []
    for col in range(FIELD_SIZE):
        button = Button(root, text=' ', width=4, height=2,
                        font=('Verdana', 20, 'bold'),
                        background='lavender',
                        command=lambda row=row, col=col: click(row, col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    cells.append(line)

new_button = Button(root, text='Play', background='green', fg='#FFF', command=new_game)
new_button.grid(row=10, column=1, sticky='nsew')
root.mainloop()
