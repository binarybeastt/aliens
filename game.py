import sys
from settings import Settings
from ship import Ship
import pygame

def run_game():
    #Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((
        ai_settings.screen_width, ai_settings.screen_height
    ))
    pygame.display.set_caption('Alien Invasion')
    bg_color = (230, 230, 230)
    
    #Make a ship
    ship = Ship(screen)
    
    #Start the main game loop
    while True:
        
        #Watch for game and keyboard events
        for event in pygame.event.get():
            screen.fill(ai_settings.bg_color)
            ship.blitme()
            if event.type == pygame.QUIT:
                sys.exit()
                
        #Make the most recently drawn screen visible
        pygame.display.flip()
        
run_game()