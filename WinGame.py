
global GLOBAL_runtime_data

from time import sleep
import pygame

import GameMenus
import RuntimeData

(numpass,numfail) = pygame.init()
if (numpass <= 0 or numfail > 0):
    pygame.quit()
    exit()

# Form resizable screen on last display
display_index = pygame.display.get_num_displays()-1
screen = pygame.display.set_mode((400, 400), pygame.RESIZABLE, display=display_index)

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
pygame.display.set_caption('resizable')

# run window
running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == GameMenus.EVENT_UPDATE_LOADING:
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
