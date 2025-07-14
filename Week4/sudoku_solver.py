import numpy as np
import tkinter as tk
from tkinter import simpledialog, messagebox

root = tk.Tk()
root.withdraw()

# Ask for grid size (square matrix)
size = simpledialog.askinteger("Grid Size", "Enter square matrix size (e.g., 9):", minvalue=2, maxvalue=25)
root.deiconify()
root.title(f"{size}×{size} Solver")
entries = []

# Create grid
for i in range(size): # type: ignore
    row = []
    for j in range(size): # type: ignore
        e = tk.Entry(root, width=2, font=('Arial', 16), justify='center')
        e.grid(row=i, column=j, padx=2, pady=2)
        row.append(e)
    entries.append(row)

# Extract board from GUI
def get_board():
    board = np.zeros((size, size), dtype=int) # type: ignore
    for i in range(size): # type: ignore
        for j in range(size): # type: ignore
            val = entries[i][j].get()
            board[i, j] = int(val) if val.isdigit() else 0
    return board

# Find next empty cell
def find_empty(grid):
    result = np.where(grid == 0)
    return (result[0][0], result[1][0]) if result[0].size else None

# Validity check
def is_valid(grid, row, col, num):
    if num in grid[row, :] or num in grid[:, col]:
        return False
    sub_size = int(size**0.5) # type: ignore
    if sub_size**2 != size:
        return True
    sub_row, sub_col = sub_size * (row // sub_size), sub_size * (col // sub_size)
    if num in grid[sub_row:sub_row+sub_size, sub_col:sub_col+sub_size]:
        return False
    return True

# Recursive solver
def solve(grid):
    empty = find_empty(grid)
    if not empty:
        return True
    row, col = empty
    for num in range(1, size + 1): # type: ignore
        if is_valid(grid, row, col, num):
            grid[row, col] = num
            if solve(grid):
                return True
            grid[row, col] = 0
    return False

# Solve button callback
def solve_gui():
    board = get_board()
    if solve(board):
        for i in range(size): # type: ignore
            for j in range(size): # type: ignore
                entries[i][j].delete(0, tk.END)
                entries[i][j].insert(0, str(board[i, j]))
    else:
        messagebox.showerror("Error", "No solution found!")

# Clear button callback
def clear_grid():
    for i in range(size): # type: ignore
        for j in range(size): # type: ignore
            entries[i][j].delete(0, tk.END)

# Buttons
tk.Button(root, text="Solve", command=solve_gui).grid(row=size, column=size // 3, pady=10) # type: ignore
tk.Button(root, text="Clear", command=clear_grid).grid(row=size, column=2 * size // 3, pady=10) # type: ignore
root.mainloop()