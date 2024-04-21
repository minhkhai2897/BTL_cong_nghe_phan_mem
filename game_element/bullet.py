import pygame
import animation
import math
from .entity import Entity
from .data import DATA

class Bullet(Entity):
    def __init__(self, name, position, speed : float = 4, angle : float = 0):
        """
        ['arrow', 'axe', 'fireball', 'ice_pick']
        """
        self.__speed = speed
        self.__angle = angle * math.pi / 180
        bullet_infor = DATA.get_bullet_info(name)
        super().__init__(animation.BulletAnimation(bullet_infor['name'], position, bullet_infor['frame_speed']))
    
    def update(self, current_time):
        self.move()
        self.anim.update(current_time)
    
    def render(self, screen):
        self.anim.render(screen)

    def move(self):
        dx = self.__speed * math.cos(self.__angle)
        dy = self.__speed * math.sin(self.__angle) * -1
        self.anim.move(dx, dy)

    def set_angle(self, angle : float):
        self.__angle = angle * math.pi / 180
    
    def set_speed(self, speed : float):
        self.__speed = speed