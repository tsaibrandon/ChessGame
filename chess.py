import pygame

# initializing pygame
pygame.init()

# constants
WIDTH = 800
HEIGHT = 800
ROWS = 8
COLS = 8
SQUARE_SIZE = WIDTH // COLS

# creating the display
display = pygame.display.set_mode((WIDTH, HEIGHT))

# opening the display
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# creating the squares
while 0 < WIDTH < 800 and 0 < HEIGHT < 800:
    pygame.draw.rect(display, (128, 128, 128), (0, 0, 100, 100))
    WIDTH - 100
    HEIGHT - 100




# make the pieces
# make the pieces move 
