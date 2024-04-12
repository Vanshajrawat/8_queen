import tkinter as tk

# Number of queens
numQueens = 8

# Current solution being tested
currentSolution = [0 for _ in range(numQueens)]

# Found solutions
solutions = set()

def isSafe(testRow, testCol):
    if testRow == 0:
        return True

    for row in range(testRow):
        if testCol == currentSolution[row]:
            return False
        
        if abs(testRow - row) == abs(testCol - currentSolution[row]):
            return False
    
    return True

def placeQueen(row):
    global currentSolution, solutions, numQueens
    
    for col in range(numQueens):
        if not isSafe(row, col):
            continue
        
        currentSolution[row] = col
        
        if row == numQueens - 1:
            solutions.add(tuple(currentSolution))
        else:
            placeQueen(row + 1)

def draw_solution(solution):
    # Clear the board
    for i in range(numQueens):
        for j in range(numQueens):
            board_labels[i][j].config(text='', bg='white')

    # Draw the solution
    queen_symbol = "\u265B"  # Unicode for black chess queen (♛)
    for row in range(numQueens):
        col = solution[row]
        board_labels[row][col].config(text=queen_symbol, bg='lightblue')

    # Display current solution number
    solution_number_label.config(text=f"Solution {current_solution_index + 1}")

def on_next_solution(event=None):
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

# Center the window on the screen
root.geometry("400x400")  # Set an initial size
root.update_idletasks()  # Required to get window dimensions
window_width = root.winfo_width()
window_height = root.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
root.geometry(f"+{x}+{y}")

# Create a 2D array of labels to represent the chess board
board_labels = [[None] * numQueens for _ in range(numQueens)]
for row in range(numQueens):
    for col in range(numQueens):
        label = tk.Label(root, width=3, height=1, text='', font=('Arial', 24), borderwidth=1, relief='solid')
        label.grid(row=row, column=col, padx=1, pady=1)  # Use small padding to avoid gaps
        board_labels[row][col] = label

# Solve the problem and store solutions
placeQueen(0)
current_solution_index = 0

# Create a label to display the current solution number
solution_number_label = tk.Label(root, text=f"Solution {current_solution_index + 1}", font=('Arial', 12))
solution_number_label.grid(row=numQueens + 1, column=0, columnspan=numQueens, pady=10)

# Bind the space key to change to the next solution
root.bind("<space>", on_next_solution)

# Set a protocol to handle the window close event
root.protocol("WM_DELETE_WINDOW", root.destroy)

# Start the main event loop
root.mainloop()
