import pygame
import random

# Initialize Pygame
pygame.init()
# Constants
WIDTH, HEIGHT = 600, 400
PIPE_WIDTH = 50
PIPE_HEIGHT = random.randint(50, 300)
PIPE_COLOR = (0, 255, 0)
BIRD_SIZE = 20
BIRD_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (0, 0, 0)
GRAVITY = 0.25
JUMP = -5

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy Bird')

# Game variables
bird_x = 50
bird_y = HEIGHT // 2
bird_dy = 0
pipes = []

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_dy = JUMP

    # Update bird position
    bird_dy += GRAVITY
    bird_y += bird_dy

    # Generate new pipes
    if len(pipes) == 0 or pipes[-1]['x'] < WIDTH - 200:
        pipe_height = random.randint(50, 300)
        pipes.append({'x': WIDTH, 'height': pipe_height})

    # Move pipes to the left
    for pipe in pipes:
        pipe['x'] -= 3

    # Remove off-screen pipes
    pipes = [pipe for pipe in pipes if pipe['x'] > -PIPE_WIDTH]

    # Check for collisions
    for pipe in pipes:
        if bird_x < pipe['x'] + PIPE_WIDTH and bird_x + BIRD_SIZE > pipe['x'] and (bird_y < pipe['height'] or bird_y + BIRD_SIZE > pipe['height'] + 150):
            running = False

    # Check if bird is out of bounds
    if bird_y < 0 or bird_y > HEIGHT - BIRD_SIZE:
        running = False

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Draw pipes
    for pipe in pipes:
        pygame.draw.rect(screen, PIPE_COLOR, (pipe['x'], 0, PIPE_WIDTH, pipe['height']))
        pygame.draw.rect(screen, PIPE_COLOR, (pipe['x'], pipe['height'] + 150, PIPE_WIDTH, HEIGHT - pipe['height'] - 150))

    # Draw bird
    pygame.draw.rect(screen, BIRD_COLOR, (bird_x, bird_y, BIRD_SIZE, BIRD_SIZE))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
