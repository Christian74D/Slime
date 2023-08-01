import pygame
import random

# Initialize Pygame
pygame.init()

# Set the dimensions of the simulation window
width, height = 200, 200

# Create the simulation window
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Slime Mold Growth")

# Set the size of each cell
cell_size = 5

# Calculate the number of cells in the x and y directions
num_cells_x = width // cell_size
num_cells_y = height // cell_size

# Create the grid to store the state of each cell
grid = [[0] * num_cells_y for _ in range(num_cells_x)]

# Set the initial state of a few random cells as food
for _ in range(100):
    x = random.randint(0, num_cells_x - 1)
    y = random.randint(0, num_cells_y - 1)
    grid[x][y] = 1

# Define the colors for the slime mold, food, and empty cells
color_slime_mold = (255, 0, 0)
color_food = (0, 255, 0)
color_empty = (0, 0, 0)

# Define the movement directions for the slime mold
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

# Define the initial position and size of the slime mold
slime_mold_x = num_cells_x // 2
slime_mold_y = num_cells_y // 2
slime_mold_size = 1

# Main game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the grid
    grid = [[0] * num_cells_y for _ in range(num_cells_x)]

    # Update the position of the slime mold
    dx, dy = random.choice(directions)
    slime_mold_x = (slime_mold_x + dx) % num_cells_x
    slime_mold_y = (slime_mold_y + dy) % num_cells_y

    # Check if the slime mold has found food
    if grid[slime_mold_x][slime_mold_y] == 1:
        # Increase the size of the slime mold
        slime_mold_size += 1
        # Remove the food from the grid
        grid[slime_mold_x][slime_mold_y] = 0

    # Place the slime mold on the grid
    grid[slime_mold_x][slime_mold_y] = slime_mold_size

    # Draw the grid on the screen
    window.fill(color_empty)
    for x in range(num_cells_x):
        for y in range(num_cells_y):
            if grid[x][y] == 1:
                rect = pygame.Rect(x * cell_size, y *
                                   cell_size, cell_size, cell_size)
                pygame.draw.rect(window, color_food, rect)
            elif grid[x][y] > 1:
                rect = pygame.Rect(x * cell_size, y *
                                   cell_size, cell_size, cell_size)
                pygame.draw.rect(window, color_slime_mold, rect)

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
