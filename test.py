import pygame
import random
import time


sucess, fails = pygame.init()
print("sucesses {} fails {}".format(sucess, fails))
pygame.font.init()
font = pygame.font.SysFont("Arial", 50)

WIDTH, HEIGHT = 1400, 750

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Space Shooter || yossef ")

# Load images player
YELLOW_SPACE_SHIP = pygame.transform.scale(
    pygame.image.load("assets/pixel_ship_yellow.png"), (65, 65))
YELLOW_SPACE_LASER = pygame.transform.scale(
    pygame.image.load("assets/pixel_laser_yellow.png"), (50, 60))

# load image enemy
RED_SHIP = pygame.transform.scale(pygame.image.load(
    "assets/pixel_ship_red_small.png"), (50, 50))
GREEN_SHIP = pygame.transform.scale(pygame.image.load(
    "assets/pixel_ship_green_small.png"), (50, 50))


# for bullets
lasers = []


class YellowShip:
    def __init__(self, x, y, step, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.step = step
        self.shooting = False

    def draw(self, window):
        window.blit(YELLOW_SPACE_SHIP, (self.x, self.y))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.step
        if keys[pygame.K_RIGHT] and self.x + 64 < WIDTH:
            self.x += self.step

    def shoot(self):
        if self.shooting:
            # if len(lasers) < 5:
            lasers.append(
                Laser(self.x + 6, self.y - 20, YELLOW_SPACE_LASER, 10))


yellow_ship = YellowShip(300, 650, 16)


class Laser:
    def __init__(self, x, y, img, step) -> None:
        self.x = x
        self.y = y
        self.img = img
        self.step = step

    def draw(self):
        WIN.blit(self.img, (self.x, self.y))

    def move(self):
        self.y -= self.step


def draw_window():
    BG = pygame.transform.scale(pygame.image.load(
        "assets/background-black.png"), (WIDTH, HEIGHT))
    WIN.blit(BG, (0, 0))
    for bullet in lasers:
        bullet.draw()
    yellow_ship.draw(WIN)
    pygame.display.update()


def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        # shoot
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    yellow_ship.shooting = True
                    yellow_ship.shoot()
        for bullet in lasers:
            bullet.move()
            if bullet.y < 0:
                lasers.remove(bullet)
        yellow_ship.move()
        draw_window()


if __name__ == "__main__":
    main()
