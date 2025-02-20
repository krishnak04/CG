import matplotlib.pyplot as plt

# Define a 10x10 grid using lists (no NumPy)
grid = [
    [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],
    [1, 1, 0, 0, 1, 2, 2, 2, 2, 2],
    [1, 1, 0, 0, 1, 1, 1, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 2, 2, 2],
    [3, 3, 3, 1, 1, 1, 1, 2, 2, 2],
    [3, 3, 3, 3, 3, 1, 1, 1, 2, 2],
    [3, 3, 3, 3, 3, 1, 1, 1, 1, 2],
    [3, 3, 3, 3, 3, 1, 1, 1, 1, 1],
    [3, 3, 3, 3, 3, 1, 1, 1, 1, 1],
]

# Get the grid size
rows, cols = len(grid), len(grid[0])

# Recursive Flood Fill function
def flood_fill(x, y, target_color, fill_color):
    # Base case: check boundaries
    if x < 0 or x >= rows or y < 0 or y >= cols:
        return
    # Stop if the color is not the target color or already filled
    if grid[x][y] != target_color or grid[x][y] == fill_color:
        return
    
    # Fill the current cell
    grid[x][y] = fill_color
    
    # Recursively fill neighboring cells (4-way connectivity)
    flood_fill(x + 1, y, target_color, fill_color)
    flood_fill(x - 1, y, target_color, fill_color)
    flood_fill(x, y + 1, target_color, fill_color)
    flood_fill(x, y - 1, target_color, fill_color)

# Function to update plot on mouse click
def on_click(event):
    if event.xdata is None or event.ydata is None:
        return  # Ignore clicks outside the grid
    
    x, y = int(event.ydata), int(event.xdata)  # Convert click coordinates to grid index
    target_color = grid[x][y]  # Get the color of the clicked cell
    fill_color = 9  # Choose a new fill color (should not be in the grid initially)

    # Apply flood fill only if the cell is not already filled
    if target_color != fill_color:
        flood_fill(x, y, target_color, fill_color)
        redraw_grid()

# Function to redraw the grid
def redraw_grid():
    plt.clf()
    plt.imshow(grid, cmap="tab10", origin="upper")
    plt.grid(visible=True, color="black")
    plt.xticks(range(cols))
    plt.yticks(range(rows))
    plt.title("Click on the grid to apply Flood Fill")
    plt.draw()

# Initialize plot
plt.figure(figsize=(6, 6))
redraw_grid()
plt.gcf().canvas.mpl_connect("button_press_event", on_click)
plt.show()
