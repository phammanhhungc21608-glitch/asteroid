import pygame
import sys
from constants import *
from logger import log_state,log_event
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot


def main():
    pygame.init()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable,)
    Asteroid.containers = (asteroids, updatable, drawable)
    clock = pygame.time.Clock()
    dt = 0 

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    while True:
        log_state()
        screen.fill("black")
        for i in drawable:
            i.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for i in asteroids:
            if i.collides_with(player):
                print("Game Over!")
                log_event("player_hit")
                sys.exit()
            for shot in shots:
                if i.collides_with(shot):
                    log_event("asteroid_shot")
                    i.split()
                    shot.kill()
        pygame.display.flip()
        dt = (clock.tick(60))/1000
        


if __name__ == "__main__":
    main()
