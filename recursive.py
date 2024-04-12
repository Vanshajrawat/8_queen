# N Queen Problem
# Recursive solution

import tkinter as tk

import time

numQueens = 8  # number of queens we are solving for !!!!!!

currentSolution = [0 for x in range(numQueens)]  # will hold current testing data
solutions = set()  # found solutions


def isSafe(testRow, testCol):
    # no need to check for row 0
    if testRow == 0:
        return True

    for row in range(0, testRow):

        # check vertical
        if testCol == currentSolution[row]:
            return False

        # diagonal
        if abs(testRow - row) == abs(testCol - currentSolution[row]):
            return False

    # no attack found
    return True

def placeQueen(row):
    global currentSolution, solutions, numQueens

    for col in range(numQueens):
        if not isSafe(row, col):
            continue
        else:
            currentSolution[row] = col
            if row == (numQueens - 1):
                #  last row
                #solutions.append(currentSolution.copy())
                solutions.add(tuple(currentSolution))
                print( f"Solution number {len( solutions )}: {currentSolution}" )
            else:
                placeQueen(row + 1)



def draw_solution(solution):
    # Clear the board
    for i in range(numQueens):
        for j in range(numQueens):
            board_labels[i][j].config(text='', bg='white')

    # Draw the solution
    for row in range(numQueens):
        col = solution[row]
        board_labels[row][col].config(text='Q', bg='lightblue')


def on_next_solution():
    global current_solution_index

    solutions_list = list(solutions)

    if current_solution_index < len(solutions_list):
        draw_solution(solutions_list[current_solution_index])
        current_solution_index += 1
    else:
        current_solution_index = 0


# Initialize the main application window
root = tk.Tk()
root.title("8 Queens Problem")

# Create a 2D array of labels to represent the chess board
board_labels = [[None] * numQueens for _ in range(numQueens)]
for row in range(numQueens):
    for col in range(numQueens):
        label = tk.Label(root, width=3, height=1, text='', font=('Arial', 24), borderwidth=1, relief='solid')
        label.grid(row=row, column=col, padx=5, pady=5)
        board_labels[row][col] = label

# Solve the problem and store solutions
placeQueen(0)
current_solution_index = 0

# Create a button to cycle through the solutions
next_solution_button = tk.Button(root, text="Next Solution", command=on_next_solution)
next_solution_button.grid(row=numQueens, column=0, columnspan=numQueens, pady=10)

# Start the main event loop
root.mainloop()
