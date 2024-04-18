import pygame
from abc import ABC
import animation

class Entity(ABC):
    def __init__(self, anim : animation.Animation):
        self.anim = anim

    def get_name(self) -> str:
        return self.anim.get_name()

    def get_width(self) -> int:
        return self.anim.get_width()
    
    def get_height(self) -> int:
        return self.anim.get_height()
    
    def get_rect(self) -> pygame.Rect:
        return self.anim.get_rect()
    
    def check_collision(self, other: 'Entity') -> bool:
        return self.anim.check_collision(other.anim)
    
    def update(self, current_time):
        pass

    def render(self, screen):
        pass

    def set_position(self, position : tuple[float, float]):
        self.anim.set_position(position)

    def get_position(self):
        return self.anim.get_position()
    
    def get_center(self):
        return self.anim.get_center()
    
    def set_center(self, center):
        self.anim.set_center(center)
