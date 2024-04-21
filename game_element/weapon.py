import pygame
import animation
from .entity import Entity
from .data import DATA

class Weapon(Entity):
    def __init__(self, name, position):
        """
        ['axe', 'bow', 'holy_sword', 'ice_sword', 'purple_staff']
        """
        weapon_infor = DATA.get_weapon_info(name)
        super().__init__(animation.WeaponAnimation(weapon_infor['name'], position, weapon_infor['frame_speed']))
        self.dame = weapon_infor['dame']
        self.range = weapon_infor['range']
        self.speed_attack = weapon_infor['speed_attack']

    def update(self, current_time):
        self.anim.update(current_time)

    def render(self, screen):
        self.anim.render(screen)


