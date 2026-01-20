import pygame
import GameMenus

class RuntimeData:
    """Class for storing runtime data."""
    def __init__(self, screen):
        self.user_name = ""
        self.screen = screen
        self.Menus = GameMenus.GameMenus()

(numpass,numfail) = pygame.init()
if (numpass <= 0 or numfail > 0):
    pygame.quit()
    exit()

# Form screen with 400x400 size
# with not resizable
displays = pygame.display.get_num_displays()
screen = pygame.display.set_mode((400, 400), pygame.RESIZABLE, display=displays-1)

# create global instance
GLOBAL_runtime_data = RuntimeData(screen)
