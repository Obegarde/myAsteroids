import pygame
from circleshape import CircleShape
from constants import *
class Player(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        self.position = pygame.Vector2(x,y)
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        right = pygame.Vector2(0,1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a,b,c]
    
    def draw(self,screen):
        pygame.draw.polygon(screen,'white',self.triangle(),2)


    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        # Call rotate with negative delta time so pressing A rotates you counter clockwise
        if keys[pygame.K_a]:
            self.rotate(-dt)
        #Call rotate with delta time to rotate clockwise
        if keys[pygame.K_d]:
            self.rotate(dt)
        #call move with positive delta time to move forward
        if keys[pygame.K_w]:
            self.move(dt)
        #call move with negative dt to move backwards
        if keys[pygame.K_s]:
            self.move(-dt)

    def move(self,dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt 

