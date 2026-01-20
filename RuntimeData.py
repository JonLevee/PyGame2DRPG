import pygame

class RuntimeData:
    """Class for storing runtime data."""
    def __init__(self):
        self.user_name = ""
        self.screen = NotImplemented

# create global instance
GLOBAL_runtime_data = RuntimeData()
