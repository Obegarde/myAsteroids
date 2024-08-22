import pygame
from circleshape import CircleShape
from constants import *
import random
class Asteroid(CircleShape):
    def __init__(self,x,y, radius):
        super().__init__(x,y,radius)
        self.position = pygame.Vector2(x,y)
        self.rotation = 0
        self.angles_distances = self.generate_pre_polygons()
        
    
    def generate_pre_polygons(self):
        out_array = []
        #Generate a random number between 5 and 9
        num_sides = random.randint(5,9)
        #Generate random angles for each vertex keeping them sorted so the shape closes properly
        angles = sorted([random.uniform(0,360)for _ in range(num_sides)])
        for angle in angles: 
            out_array.append([angle,self.radius * random.uniform(0.8,1.2)])
        return out_array


    def polygon(self,):
        
        #Calculate the points in the polygon
        points = []
        for list in self.angles_distances:
            #Rotate the direction vector to get the angle for each vertex
            vertex_angle = pygame.Vector2(0,-1).rotate(self.rotation + list[0])

            #Calculate the vertex position
            vertex_position = self.position + vertex_angle * list[1]
            points.append(vertex_position)
    
        return points


    def draw(self, screen):
        pygame.draw.polygon(screen, 'white',self.polygon(),2)

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
