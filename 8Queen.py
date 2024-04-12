import tkinter as tk
from tkinter import PhotoImage


numQueens = 8  # Number of queens we are solving for

currentSolution = [0 for _ in range(numQueens)]  # Current testing data
solutions = set()  # Found solutions


def isSafe(testRow, testCol):
    """Check if a queen can be placed on the testRow and testCol without conflict."""
    if testRow == 0:
        return True

    for row in range(testRow):
        # Check vertical line
        if currentSolution[row] == testCol:
            return False

        # Check diagonals
        if abs(testRow - row) == abs(testCol - currentSolution[row]):
            return False

    return True


def placeQueen(row):
    """Place queens on the board using recursion."""
    for col in range(numQueens):
        if not isSafe(row, col):
            continue

        currentSolution[row] = col

        if row == numQueens - 1:
            # Last row, add solution to set
            solutions.add(tuple(currentSolution))
        else:
            # Recurse to the next row
            placeQueen(row + 1)


def draw_solution(solution):
    """Draw the chessboard with the given solution."""
    for row in range(numQueens):
        col = solution[row]
        for c in range(numQueens):
            color = 'black' if (row + c) % 2 == 0 else 'white'
            board_labels[row][c].config(bg=color, image='', text='')


    queen_symbol = "\u265B"  # Unicode for black chess queen (♛)
    for row in range(numQueens):
        col = solution[row]
        board_labels[row][col].config(text=queen_symbol, bg='lightblue')


def on_next_solution():
    """Display the next solution on the chessboard."""
    global current_solution_index

    solutions_list = list(solutions)

    if current_solution_index < len(solutions_list):
        draw_solution(solutions_list[current_solution_index])
        current_solution_index += 1
    else:
        # Reset to the first solution if reached the end
        current_solution_index = 0
        draw_solution(solutions_list[current_solution_index])
        current_solution_index += 1


# Initialize the main application window
root = tk.Tk()
root.title("8 Queens Problem")


# Set the window to take up the full screen
root.attributes("-fullscreen", True)

# Create a 2D array of labels to represent the chessboard
board_labels = [[None] * numQueens for _ in range(numQueens)]
for row in range(numQueens):
    for col in range(numQueens):
        # Alternate colors for the chessboard (black and white)
        color = 'black' if (row + col) % 2 == 0 else 'white'
        label = tk.Label(root, width=4, height=2, text='', font=('Arial', 24), borderwidth=1, relief='solid', bg=color)
        label.grid(row=row, column=col, sticky='nsew')  # Use sticky to fill the grid cell
        board_labels[row][col] = label

# Solve the problem and store solutions
placeQueen(0)
current_solution_index = 0

# Create a button to cycle through the solutions
next_solution_button = tk.Button(root, text="Next Solution", command=on_next_solution)
next_solution_button.grid(row=numQueens, column=0, columnspan=numQueens, pady=10, sticky='ew')

# Start the main event loop
root.mainloop()
