import pygame


clock = pygame.time.Clock()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Crossing Game"
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)


class Game:
    
    TICK_RATE = 60

    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        self.game_screen = pygame.display.set_mode((width, height))
        self.game_screen.fill(WHITE_COLOR)
        pygame.display.set_caption(title)

    def run_game_loop(self):
        is_game_over = False
        direction = 0
        player_character = PlayerCharacter("player.png", 375, 700, 50, 50)
        enemy_0 = EnemyCharacter('enemy.png', 20, 400, 50, 50)

        # Game Loop
        while not is_game_over:
            # Gets all event occuring at a time
            for event in pygame.event.get():
                # if quit type event then exit loop
                if event.type == pygame.QUIT:
                    is_game_over = True
                    
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        direction = 1
                    elif event.key == pygame.K_DOWN:
                        direction = -1
                        
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        direction = 0

                print(event)

            self.game_screen.fill(WHITE_COLOR)
            player_character.move(direction)
            player_character.draw(self.game_screen)
            enemy_0.move(self.width)
            enemy_0.draw(self.game_screen)
            
       
            # Update all graphics         
            pygame.display.update()
            clock.tick(self.TICK_RATE)


class GameObject:
    
    def __init__(self, image_path, x, y, width, height):
        object_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(object_image, (width, height))

        self.x_pos = x
        self.y_pos = y

        self.width = width
        self.height = height
        
    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))



class PlayerCharacter(GameObject):

    SPEED = 10
    
    def __init__ (self,image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    def move(self, direction, max_height):
        if direction > 0:
            self.y_pos -= self.SPEED
        elif direction < 0:
            self.y_pos += self.SPEED

        if self.y_pos >= max_height - 20:
            self.y_pos = nax_hegiht - 20

class EnemyCharacter(GameObject):

    SPEED = 15

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    def move(self, max_width):
        if self.x_pos <= 20:
            self.SPEED = abs(self.SPEED)
        elif self.x_pos >= max_width - 50:
            self.SPEED = -abs(self.SPEED) 
        self.x_pos += self.SPEED 
        

        
pygame.init()

new_game = Game(SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop()

player_image = pygame.image.load("player.png")
player_image = pygame.transform.scale(player_image, (50,50))

 # Quit pygame
pygame.quit()
quit()


#pygame.draw.rect(game_screen, BLACK_COLOR, [350, 350, 100, 100])
#pygame.draw.circle(game_screen, BLACK_COLOR, (400, 300), 50)
#game_screen.blit(player_image, (375, 375))

