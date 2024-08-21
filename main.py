import pygame
from constants import *
from player import *
def main():
    #Initialize pygame
    pygame.init()
    #Initialize a display object set to our chosen width and height in constants
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #Initialze a Clock to be used to manage the game loop
    game_clock = pygame.time.Clock()
    #Delta time, initialized will be used to ensure the game runs at the same pace
    dt = 0
    #Iniates the a Player object, placed in the middle of the screen
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT /2,PLAYER_RADIUS)

    #Our game loop keeps rerunning to make the game happen
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #fills the screen with a color black in this case
        screen.fill('#000000')
        #draw the player to the screen
        player.draw(screen)
        #Update the display
        pygame.display.flip()
        #Limit the framerate to 60 fps
        dt = game_clock.tick(60) / 1000
 







if __name__ == "__main__":
    main()
