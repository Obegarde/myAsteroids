import pygame
from constants import *
from player import Player 
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys
def main():
    #Initialize pygame
    pygame.init()
    #Initialize a display object set to our chosen width and height in constants
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #Initialze a Clock to be used to manage the game loop
    game_clock = pygame.time.Clock()
    #Delta time, initialized will be used to ensure the game runs at the same pace
    dt = 0
    


    #Variable to hold the current score
    score = 0
    #Initialze a font object
    font = pygame.font.Font('freesansbold.ttf', 32)
    #Create a text surface object for the text to be rendered on
    score_text = font.render(str(score), False, 'white','black')
    #create a rect object for the text surface object
    scoreRect = score_text.get_rect()
    #set the center of the rect object
    scoreRect.center = (SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 8 )


    #create a group for the asteroids
    asteroids = pygame.sprite.Group()
    #Group the updateable code so it is easier to call
    updatable = pygame.sprite.Group()
    #Group the code that needs to be drawn to the screen
    drawable = pygame.sprite.Group()
    #Create a group for shots fired
    shots = pygame.sprite.Group()
    #Add instances of Shot to shots,updatable and drawable
    Shot.containers = (shots, updatable, drawable)
    #Add player to drawable and updatable 
    Player.containers = (updatable, drawable)
    #Add asteroid to the asteroids group along with updatable and drawable
    Asteroid.containers = (asteroids, updatable, drawable)
    #Add the AsteroidField class to the updatable group
    AsteroidField.containers = (updatable)
    
    #Iniates a asteroidfield object
    asteroidfield = AsteroidField()

    #Iniates the a Player object, placed in the middle of the screen
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT /2,PLAYER_RADIUS)
    #Our game loop keeps rerunning to make the game happen
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #fills the screen with a color black in this case
        screen.fill('#000000')


        #Iterate through the updateable group and update all members
        for member in updatable: 
            member.update(dt)

        #Iterate through asteroids and check for collisions with the player
        for asteroid in asteroids:
            if asteroid.collision_check(player):
                print("Game Over!")
                print("You scored " + str(score) + " points")
                sys.exit()
            #Iterate through shots and check if the collide with any asteroid
            for shot in shots:
                if asteroid.collision_check(shot):
                    asteroid.split()
                    shot.kill()
                    score += 1
            
        #iterate through drawable group and draw all members
        for member in drawable:
            member.draw(screen)
        


        #Update the scoretext object
        score_text = font.render(str(score), False, 'white','black')
        #Write the scoretext and scorerect to the screen display object
        screen.blit(score_text, scoreRect)
        
        #Update the display
        pygame.display.flip()
        #Limit the framerate to 60 fps
        dt = game_clock.tick(60) / 1000
 







if __name__ == "__main__":
    main()
