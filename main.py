import pygame
import sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	pygame.init()
	fps = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (updatable, drawable, shots)

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	field = AsteroidField()

	while True:
		log_state()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill("black")
		for drawing in drawable:
			drawing.draw(screen)
		pygame.display.flip()
		fps.tick(60)
		dt = fps.tick(60) / 1000
		updatable.update(dt)
		for asteroid in asteroids:
			if asteroid.collides_with(player):
				log_event("player_hit")
				print("Game Over!")
				sys.exit()
			for shot in shots:
				if asteroid.collides_with(shot):
					log_event("asteroid_shot")
					shot.kill()
					asteroid.split()

if __name__ == "__main__":
    main()