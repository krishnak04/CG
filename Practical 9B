import matplotlib.pyplot as plt

# Define a 10x10 grid with boundaries (1 represents boundary, other numbers are fillable areas)
grid = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 2, 2, 2, 1],
    [1, 0, 0, 0, 0, 1, 2, 2, 2, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 2, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 2, 1],
    [1, 3, 3, 3, 0, 1, 1, 1, 2, 1],
    [1, 3, 3, 3, 3, 1, 1, 1, 2, 1],
    [1, 3, 3, 3, 3, 1, 1, 1, 1, 1],
    [1, 3, 3, 3, 3, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# Get the grid size
rows, cols = len(grid), len(grid[0])

# Recursive Boundary Fill function
def boundary_fill(x, y, boundary_color, fill_color):
    # Base case: check boundaries
    if x < 0 or x >= rows or y < 0 or y >= cols:
        return
    # Stop if we hit the boundary color or already filled
    if grid[x][y] == boundary_color or grid[x][y] == fill_color:
        return
    
    # Fill the current cell
    grid[x][y] = fill_color
    
    # Recursively fill neighboring cells (4-way connectivity)
    boundary_fill(x + 1, y, boundary_color, fill_color)
    boundary_fill(x - 1, y, boundary_color, fill_color)
    boundary_fill(x, y + 1, boundary_color, fill_color)
    boundary_fill(x, y - 1, boundary_color, fill_color)

# Function to update plot on mouse click
def on_click(event):
    if event.xdata is None or event.ydata is None:
        return  # Ignore clicks outside the grid
    
    x, y = int(event.ydata), int(event.xdata)  # Convert click coordinates to grid index
    boundary_color = 1 # The defined boundary color
    fill_color = 9  # Choose a new fill color

    # Apply boundary fill if clicked inside a fillable area
    if grid[x][y] != boundary_color and grid[x][y] != fill_color:
        boundary_fill(x, y, boundary_color, fill_color)
        redraw_grid()

# Function to redraw the grid
def redraw_grid():
    plt.clf()
    plt.imshow(grid, cmap="tab10", origin="upper")
    plt.grid(visible=True, color="black")
    plt.xticks(range(cols))
    plt.yticks(range(rows))
    plt.title("Click inside an enclosed area to apply Boundary Fill")
    plt.draw()

# Initialize plot
plt.figure(figsize=(6, 6))
redraw_grid()
plt.gcf().canvas.mpl_connect("button_press_event", on_click)
plt.show()
