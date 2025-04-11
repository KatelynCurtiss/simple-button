
# Katelyn Curtiss
# April 10 2025
# Simple Button

import pygame
import sys
from config import *
  
def init_game():
    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    pygame.display.set_caption(TITLE)
    return screen

def handle_events(button):
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            return False
        if events.type == pygame.MOUSEBUTTONDOWN:
            if button.collidepoint(events.pos):
                pygame.quit()
                sys.exit()
        if events.type == pygame.KEYDOWN:
            return False
        return True
    
def main():
    font = pygame.font.SysFont('Georgia', 40, bold=True)
    surf = font.render('Quit', True, GREEN)

button_length = 200
button_width = 60 
button_x = 300
button_y = 125
button = pygame.Rect(button_x,button_y,button_length,button_width)

surf_rect = surf.get_rect()
surf_rect.center = button.center

mouse_x, mouse_y = pygame.mouse.get_pos()  

if button.collidepoint(mouse_x, mouse_y):
     button_color = (180, 180, 180)
else:
     button_color = (110, 110, 110)
        
     pygame.draw.rect(screen, button_color, button)

     screen.blit(surf, surf_rect) # surf is the text for the button, and surf_rect is the surface (area on the screen) where the button text will be drawn

     pygame.display.flip()

     clock.tick(FPS)

pygame.quit()

    sys.exit()

if __name__ == "__main__":
    main()

  


