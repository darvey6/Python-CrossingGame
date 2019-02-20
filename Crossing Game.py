import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
TICK_RATE = 60

game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game_screen.fill(WHITE_COLOR)

# Game Loop
clock = pygame.time.Clock()
is_game_over = False


while not is_game_over:

    # Gets all event occuring at a time
    for event in pygame.event.get():
        # if quit type event then exit loop
        if event.type == pygame.QUIT:
            is_game_over = True
            
    # Update all graphics         
    pygame.display.update()
    clock.tick(TICK_RATE)


# Quit pygame
pygame.quit()
quit()
