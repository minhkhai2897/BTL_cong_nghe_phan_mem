import pygame
import animation
from .entity import Entity
from .data import DATA

class Item(Entity):
    def __init__(self, name, position):
        """
        flask_big_red, flask_big_yellow"""
        item_infor = DATA.get_item_info(name)
        super().__init__(animation.ItemAnimation(item_infor['name'], position, item_infor['frame_speed']))
    
    def update(self, current_time):
        self.anim.update(current_time)
    
    def render(self, screen):
        self.anim.render(screen)