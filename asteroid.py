import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if ASTEROID_MIN_RADIUS >= self.radius:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        a1 = self.velocity.rotate(angle)
        a2 = self.velocity.rotate(-angle)
        new_r = self.radius - ASTEROID_MIN_RADIUS
        new1 = Asteroid(self.position.x, self.position.y, new_r)
        new2 = Asteroid(self.position.x, self.position.y, new_r)
        new1.velocity = a1 * 1.2
        new2.velocity = a2 * 1.2