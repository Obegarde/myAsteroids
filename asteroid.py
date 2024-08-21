import pygame
from circleshape import CircleShape
from constants import *
import random
class Asteroid(CircleShape):
    def __init__(self,x,y, radius):
        super().__init__(x,y,radius)
        self.position = pygame.Vector2(x,y)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
        
        if self.position.x < 0 - self.radius:
            self.position.x = SCREEN_WIDTH
        elif self.position.x > SCREEN_WIDTH + self.radius:
            self.position.x = 0
        elif self.position.y < 0 - self.radius:
            self.position.y = SCREEN_HEIGHT
        elif self.position.y > SCREEN_HEIGHT + self.radius:
            self.position.y = 0

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(10,60) 
            new_velocity_one = self.velocity.rotate(random_angle)
            new_velocity_two = self.velocity.rotate(-random_angle)
            asteroid_one = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            asteroid_one.velocity = new_velocity_one * 1.2 
            asteroid_two = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            asteroid_two.velocity = new_velocity_two * 1.2
