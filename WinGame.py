
global GLOBAL_runtime_data

from time import sleep
import pygame
import pygame_menu
from pygame_menu import themes
import RuntimeData



(numpass,numfail) = pygame.init()
if (numpass <= 0 or numfail > 0):
    pygame.quit()
    exit()

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




# Form screen with 400x400 size
# with not resizable
displays = pygame.display.get_num_displays()
screen = pygame.display.set_mode((400, 400), pygame.RESIZABLE, display=displays-1)
RuntimeData.GLOBAL_runtime_data.screen = screen

# set title
pygame.display.set_caption('Not resizable')

# run window
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            continue

        if event.type == pygame.MOUSEMOTION:
            continue
        print(f"event: {pygame.event.event_name(event.type)}")

# quit pygame after closing window
pygame.quit()

print("Hello world!")
