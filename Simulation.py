import pygame
import random

# Définir les constantes de la simulation
WINDOW_SIZE = (1000, 700)
CREATURE_SIZE = 1
NUM_CREATURES = 30
FOOD_SIZE = 5
NUM_FOOD = 50

# Définir la classe Creature
class Creature:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = 1
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.size = CREATURE_SIZE

    def move(self):
        self.x += random.randint(-self.speed, self.speed)
        self.y += random.randint(-self.speed, self.speed)

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.size)

    def eat(self, food_list):
        for food in food_list:
            if abs(self.x - food.x) < (self.size + FOOD_SIZE)/2 and abs(self.y - food.y) < (self.size + FOOD_SIZE)/2:
                self.size += 1
                food_list.remove(food)

# Définir la classe Food
class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (0, 255, 0)
        self.size = FOOD_SIZE

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.size, self.size))

# Initialiser pygame
pygame.init()

# Créer la fenêtre de simulation
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Simulation de créatures 3")

# Créer les créatures
creatures = []
for i in range(NUM_CREATURES):
    x = random.randint(0, WINDOW_SIZE[0])
    y = random.randint(0, WINDOW_SIZE[1])
    speed = random.randint(1, 5)
    creature = Creature(x, y, speed)
    creatures.append(creature)

# Créer les carrés de nourriture
food_list = []
for i in range(NUM_FOOD):
    x = random.randint(0, WINDOW_SIZE[0])
    y = random.randint(0, WINDOW_SIZE[1])
    food = Food(x, y)
    food_list.append(food)

# Boucle principale de la simulation
running = True
while running:
    # Gérer les événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Déplacer les créatures et les dessiner
    for creature in creatures:
        creature.move()
        creature.draw(window)
        creature.eat(food_list)

    # Dessiner les carrés de nourriture
    for food in food_list:
        food.draw(window)

    # Mettre à jour l'affichage
    pygame.display.update()

# Quitter pygame
pygame.quit()
