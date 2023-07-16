from settings import Settings
import game_functions as gf
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
        gf.check_events()
                
        #Make the most recently drawn screen visible
        gf.update_screen(ai_settings, screen, ship)
        
run_game()