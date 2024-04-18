import pygame
import animation
from .entity import Entity

class Item(Entity):
    def __init__(self, name, position):
        """
        ['chest_empty_open_anim', 'chest_full_open_anim', 'chest_mimic_open_anim']

        ['flask_big_red', 'flask_big_blue', 'flask_big_green', 'flask_big_yellow', 'flask_red', 'flask_blue', 'flask_green', 'flask_yellow']
 
        ['skull', 'crate', 'coin_anim']

        ['ui_heart_full', 'ui_heart_half', 'ui_heart_empty']"""
        super().__init__(animation.ItemAnimation(name, position))
    
    def update(self, current_time):
        self.anim.update(current_time)
    
    def render(self, screen):
        self.anim.render(screen)