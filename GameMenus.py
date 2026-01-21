import pygame
import pygame_menu
from pygame_menu import themes

EVENT_UPDATE_LOADING = pygame.USEREVENT + 0

class GameMenus:
    """Class for storing menu data."""
    def __init__(self):
        self.set_menu(self)

    def set_menu(self):
        screen = pygame.display.get_surface()
        self.mainmenu = pygame_menu.Menu('Welcome', width=screen.get_width(), height=screen.get_height(), theme=themes.THEME_SOLARIZED)
        self.mainmenu.add.text_input('Name: ', default='username')
        self.mainmenu.add.button('Play', self.start_the_game)
        self.mainmenu.add.button('Levels', self.level_menu)
        self.mainmenu.add.button('Quit', pygame_menu.events.EXIT)
        
        self.level = pygame_menu.Menu('Select a Difficulty', 600, 400, theme=themes.THEME_BLUE)
        self.level.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=self.set_difficulty)
        
        self.loading = pygame_menu.Menu('Loading the Game...', 600, 400, theme=themes.THEME_DARK)
        self.loading.add.progress_bar("Progress", progressbar_id = "1", default=0, width = 200, )
        
        self.arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size = (10, 15))

    def resized(self):
        screen = pygame.display.get_surface()
        self.mainmenu.resize(width=screen.get_width(), height=screen.get_height())

    def set_difficulty(self, value, difficulty):
        print(value)
        print(difficulty)
    
    def start_the_game(self):
        self.mainmenu._open(self.loading)
        pygame.time.set_timer(EVENT_UPDATE_LOADING, 30)
    
    def level_menu(self):
        self.mainmenu._open(self.level)
        