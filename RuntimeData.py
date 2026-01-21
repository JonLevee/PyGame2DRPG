import pygame
import GameMenus

class RuntimeData:
    """Class for storing runtime data."""
    def __init__(self):
        self.user_name = ""
        self.menu = NotImplemented

    def set_menu(self, menu):
        self.menu = menu


# create global instance
GLOBAL_runtime_data = RuntimeData()
