import pygame
import random

# Initialize Pygame
pygame.init()

# Set up screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 200
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the ground
ground_height = 50
ground = pygame.Rect(0, SCREEN_HEIGHT - ground_height, SCREEN_WIDTH, ground_height)

# Set up the dinosaur
dino_width = 44
dino_height = 47
dino = pygame.Rect(50, SCREEN_HEIGHT - ground_height - dino_height, dino_width, dino_height)
dino_image = pygame.image.load('dino.png')

# Set up the cactus
cactus_width = 20
cactus_height = 40
cactus_image = pygame.image.load('cactus.png')

# Set up the score
score = 0
font = pygame.font.SysFont(None, 24)

# Set up the game loop
clock = pygame.time.Clock()
game_over = False

while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dino_jump = True

    # Update the game
    cactus_speed = 5
    dino_jump_speed = 10
    cactus_chance = 0.01
    dino_jump_gravity = 1

    # Move the cactus
    cactus_move = cactus_speed
    cactus_list = []
    for cactus in cactus_list:
        cactus.move_ip(-cactus_move, 0)

    # Create new cactus
    if random.random() < cactus_chance:
        new_cactus = pygame.Rect(SCREEN_WIDTH, SCREEN_HEIGHT - ground_height - cactus_height, cactus_width, cactus_height)
        cactus_list.append(new_cactus)

    # Move the dinosaur
    if dino_jump:
        dino.move_ip(0, -dino_jump_speed)
        dino_jump_speed -= dino_jump_gravity
        if dino.bottom >= SCREEN_HEIGHT - ground_height:
            dino.bottom = SCREEN_HEIGHT - ground_height
            dino_jump = False
            dino_jump_speed = 10
    else:
        dino.move_ip(0, 5)

    # Check for collision
    for cactus in cactus_list:
        if dino.colliderect(cactus):
            game_over = True

    # Draw the screen
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, ground)
    screen.blit(dino_image, dino)
    for cactus in cactus_list:
        screen.blit(cactus_image, cactus)
    score += 1
    score_text = font.render(f'Score: {score}', True, BLACK)
    screen.blit(score_text, (10, 10))
    pygame.display.update()

    # Set the game speed
    clock.tick(60)

# Quit Pygame
pygame.quit()