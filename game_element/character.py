import pygame
import animation
from game_element.weapon import Weapon
from .entity import Entity

class Character(Entity):
    def __init__(self, name, position, max_hp):
        """
        ['knight_m', 'knight_f', 'wizzard_m', 'wizzard_f', 'lizard_m', 'lizard_f', 'elf_m', 'elf_f']

        ['big_demon', 'ogre', 'big_zombie', 'chort', 'wogol', 'necromancer', 'orc_shaman', 'orc_warrior', 'masked_orc', 'ice_zombie', 'zombie',
        """
        super().__init__(animation.CharacterAnimation(name, position))
        self.__max_hp = max_hp
        self.__hp = max_hp
        
        self.__dame = 1
        self.__range = 100
        self.__speed_attack = 1
        self.__direction = "left"

    def change_direction(self, direction):
        if (direction in ["left", "right", "up", "down"]):
            self.__direction = direction

    def get_direction(self):
        return self.__direction

    def get_current_hp(self):
        return self.__hp
    
    def get_max_hp(self):
        return self.__max_hp
    
    def set_hp(self, hp):
        pass


    def update(self, current_time):
        self.anim.update(current_time)

    def render(self, screen):
        self.anim.render(screen, self.__hp, self.__max_hp)

    def move(self, dx, dy):
        self.anim.move(dx, dy)

    def add_weapon(self, weapon : Weapon):
        self.__get_buff_weapon(weapon)
        self.anim.add_weapon(weapon.anim)

    def __get_buff_weapon(self, weapon : Weapon):
        self.__range += weapon.range
        self.__dame += weapon.dame
        self.__speed_attack += weapon.speed_attack
    
    def add_effect(self, effect):
        self.anim.add_effect(effect)

    def has_weapon(self):
        return self.anim.has_weapon()
    
    def get_range(self):
        return self.__range
    
    def get_attack_speed(self):
        return self.__speed_attack
    
    def get_dame(self):
        return self.__dame



    

    