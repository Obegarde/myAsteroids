import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot
class Player(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        self.position = pygame.Vector2(x,y)
        self.rotation = 0
        self.shooting_cooldown = 0
        self.lives = 3
        self.current_speed = 0
        self.acceleration = 5
        self.max_speed = 1000

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
        self.move(dt)
        # Call rotate with negative delta time so pressing A rotates you counter clockwise
        if keys[pygame.K_a]:
            self.rotate(-dt)
        #Call rotate with delta time to rotate clockwise
        if keys[pygame.K_d]:
            self.rotate(dt)
        #call move with positive delta time to move forward
        if keys[pygame.K_w]:
            self.current_speed += self.acceleration
        #call move with negative dt to move backwards
        if keys[pygame.K_s]:
            self.current_speed -= self.acceleration
        if keys[pygame.K_SPACE]:
            self.shoot()
        
        self.shooting_cooldown -= dt

     
    def move(self,dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * self.current_speed * dt
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.position.x < 0:
            self.position.x = SCREEN_WIDTH
        elif self.position.x > SCREEN_WIDTH:
            self.position.x = 0
        elif self.position.y < 0:
            self.position.y = SCREEN_HEIGHT
        elif self.position.y > SCREEN_HEIGHT:
            self.position.y = 0

    
    def shoot(self):
        if self.shooting_cooldown <= 0:
            shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOT_SPEED
            self.shooting_cooldown = PLAYER_SHOOT_COOLDOWN
    
    def take_damage(self):
        self.lives -= 1
        if self.lives < 1:
            return "dead"
        else:
            return "alive"




