# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from player import *
from asteroid import *
from asteroidfield import *
from constants import *

def main():
    pygame.init()
    track_time = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable,)
    Shot.containers = (shots, updateable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for draws in drawable:
            draws.draw(screen)
        for updates in updateable:
            updates.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player):
                sys.exit("Game Over!")
            for bullet in shots:
                if asteroid.collision(bullet):
                    asteroid.split()
                    bullet.kill()
        pygame.display.flip()
        dt = track_time.tick(60) / 1000
    #print("Starting Asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()