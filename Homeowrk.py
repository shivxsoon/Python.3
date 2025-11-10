import pygame

# Initialize Pygame
pygame.init()

# Create window
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Basic Shapes")

# Define colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)

# Fill background
window.fill(WHITE)

# Rectangle
pygame.draw.rect(window, RED, (50, 50, 100, 60))

# Solid Circle
pygame.draw.circle(window, GREEN, (300, 100), 40)

# Outlined Circle
pygame.draw.circle(window, BLUE, (400, 100), 40, 4)

# Line
pygame.draw.line(window, BLACK, (50, 150), (450, 150), 5)

# Polygon (triangle)
pygame.draw.polygon(window, PURPLE, [(250, 300), (200, 400), (300, 400)])

# Update display
pygame.display.update()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
