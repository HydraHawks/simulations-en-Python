import pygame
import random

# constantes
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
BG_COLOR = (50, 50, 50)
SNAKE_COLOR = (102, 205, 170)
SNAKE_SPEED = 0.5
SNAKE_LENGTH = 10

# initialisation de pygame
pygame.init()

# création de la fenêtre
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simulation de Serpents 1")

# classe de serpent
class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
        self.length = SNAKE_LENGTH

    def move(self):
        if self.direction == "UP":
            self.y -= SNAKE_SPEED
        elif self.direction == "DOWN":
            self.y += SNAKE_SPEED
        elif self.direction == "LEFT":
            self.x -= SNAKE_SPEED
        elif self.direction == "RIGHT":
            self.x += SNAKE_SPEED

        if self.x < 0:
            self.x = SCREEN_WIDTH
        elif self.x > SCREEN_WIDTH:
            self.x = 0
        if self.y < 0:
            self.y = SCREEN_HEIGHT
        elif self.y > SCREEN_HEIGHT:
            self.y = 0

        # changer de direction aléatoirement
        if random.randint(1, 100) == 1:
            self.direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])

    def draw(self):
        pygame.draw.rect(screen, SNAKE_COLOR, (self.x, self.y, self.length, self.length))

# liste de serpents
snakes = []
for i in range(50):
    x = random.randint(0, SCREEN_WIDTH - SNAKE_LENGTH)
    y = random.randint(0, SCREEN_HEIGHT - SNAKE_LENGTH)
    snakes.append(Snake(x, y))

# boucle principale du jeu
running = True
while running:

    # gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # effacement de l'écran
    screen.fill(BG_COLOR)

    # mise à jour et dessin des serpents
    for snake in snakes:
        snake.move()
        snake.draw()

    # mise à jour de l'affichage
    pygame.display.flip()

pygame.quit()