import pygame
import random
import math

# initialisation de Pygame
pygame.init()

# définition des couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# définition de la taille de l'écran
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

# définition des paramètres des créatures
CREATURE_SIZE = 4
INITIAL_CREATURE_COUNT = 100
CREATURE_SPEED = 1

# création de l'écran
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Civilisation 2")

# création d'une classe pour les créatures
class Creature:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = random.uniform(0, 2 * math.pi)

    def move(self):
        self.x += math.cos(self.direction) * CREATURE_SPEED
        self.y += math.sin(self.direction) * CREATURE_SPEED

        # méthode pour empêcher les créatures de sortir de l'écran
        if self.x < 0:
            self.x = SCREEN_WIDTH
        elif self.x > SCREEN_WIDTH:
            self.x = 0
        if self.y < 0:
            self.y = SCREEN_HEIGHT
        elif self.y > SCREEN_HEIGHT:
            self.y = 0

    def draw(self):
        pygame.draw.circle(screen, RED, (int(self.x), int(self.y)), CREATURE_SIZE)

    def eat(self, other_creature):
        if self == other_creature:
            return
        distance = math.sqrt((self.x - other_creature.x) ** 2 + (self.y - other_creature.y) ** 2)
        if distance < CREATURE_SIZE:
            creatures.remove(other_creature)
            statistics["disappeared"] += 1
            statistics["surviving"] -= 1

# création de la liste des créatures
creatures = []
for i in range(INITIAL_CREATURE_COUNT):
    x = random.uniform(0, SCREEN_WIDTH)
    y = random.uniform(0, SCREEN_HEIGHT)
    creature = Creature(x, y)
    creatures.append(creature)

# initialisation des statistiques
statistics = {
    "initial": INITIAL_CREATURE_COUNT,
    "surviving": len(creatures),
    "disappeared": 0
}

# création de la police pour les statistiques
font = pygame.font.SysFont(None, 30)

# boucle principale du jeu
running = True
while running:
    # gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # mise à jour des créatures
    for creature in creatures:
        creature.move()
        for other_creature in creatures:
            creature.eat(other_creature)

    # dessin des créatures
    screen.fill(BLACK)
    for creature in creatures:
        creature.draw()

    if (statistics["surviving"] <= 1):
        running = False
        print("\033[91m____FIN DE LA SIMULATION____")

    # affichage des statistiques
    text = f"Population initiale: {statistics['initial']} Survivants: {statistics['surviving']} Morts: {statistics['disappeared']}"
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.topright = (SCREEN_WIDTH, 0)
    screen.blit(text_surface, text_rect)

    pygame.display.flip()

# arrêt de Pygame
pygame.quit()




