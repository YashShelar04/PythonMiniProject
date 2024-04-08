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
score = 0

# Game loop
game_over = False
running = True
while running:
    if not game_over:
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
            score += 1  # Increase score when a new pipe is generated

        # Move pipes to the left
        for pipe in pipes:
            pipe['x'] -= 3

        # Remove off-screen pipes
        pipes = [pipe for pipe in pipes if pipe['x'] > -PIPE_WIDTH]

        # Check for collisions
        for pipe in pipes:
            if bird_x < pipe['x'] + PIPE_WIDTH and bird_x + BIRD_SIZE > pipe['x'] and (bird_y < pipe['height'] or bird_y + BIRD_SIZE > pipe['height'] + 150):
                game_over = True

        # Check if bird is out of bounds
        if bird_y < 0 or bird_y > HEIGHT - BIRD_SIZE:
            game_over = True

        # Clear the screen
        screen.fill(BACKGROUND_COLOR)

        # Draw pipes
        for pipe in pipes:
            pygame.draw.rect(screen, PIPE_COLOR, (pipe['x'], 0, PIPE_WIDTH, pipe['height']))
            pygame.draw.rect(screen, PIPE_COLOR, (pipe['x'], pipe['height'] + 150, PIPE_WIDTH, HEIGHT - pipe['height'] - 150))

        # Draw bird
        pygame.draw.rect(screen, BIRD_COLOR, (bird_x, bird_y, BIRD_SIZE, BIRD_SIZE))

        # Draw score
        font = pygame.font.Font(None, 36)
        text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(text, (10, 10))

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        pygame.time.Clock().tick(60)
    else:
        # Display game over screen
        screen.fill(BACKGROUND_COLOR)
        font = pygame.font.Font(None, 48)
        text = font.render("Game Over", True, (255, 255, 255))
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 + text.get_height()))
        pygame.display.flip()

        # Wait for a key press to restart the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_y = HEIGHT // 2
                    bird_dy = 0
                    pipes = []
                    score = 0
                    game_over = False

# Quit Pygame
pygame.quit()
