
global GLOBAL_runtime_data

from time import sleep
import pygame
import pygame_menu
from pygame_menu import themes

import GameMenus
import RuntimeData

def run():
    init()
    while True:
        processInput()
        update()
        render()

def init():
    print("done")
    

def processInput():
    print("done")

def update():
    print("done")

def render():
    print("done")



# set title
pygame.display.set_caption('Not resizable')

# run window
running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == RuntimeData.GLOBAL_runtime_data.Menus.update_loading:
            progress = RuntimeData.GLOBAL_runtime_data.Menus.loading.get_widget("1")
            progress.set_value(progress.get_value() + 1)
            if progress.get_value() == 100:
                pygame.time.set_timer(RuntimeData.GLOBAL_runtime_data.Menus.update_loading, 0)

        if event.type == pygame.QUIT:
            running = False
            continue

    if RuntimeData.GLOBAL_runtime_data.Menus.mainmenu.is_enabled():
        RuntimeData.GLOBAL_runtime_data.Menus.mainmenu.update(events)
        RuntimeData.GLOBAL_runtime_data.Menus.mainmenu.draw(RuntimeData.GLOBAL_runtime_data.screen)
        if (RuntimeData.GLOBAL_runtime_data.Menus.mainmenu.get_current().get_selected_widget()):
            RuntimeData.GLOBAL_runtime_data.Menus.arrow.draw(
                RuntimeData.GLOBAL_runtime_data.screen, 
                RuntimeData.GLOBAL_runtime_data.Menus.mainmenu.get_current().get_selected_widget())
    
        pygame.display.update()

        if event.type == pygame.MOUSEMOTION:
            continue
        print(f"event: {pygame.event.event_name(event.type)}")

# quit pygame after closing window
pygame.quit()

print("Hello world!")
