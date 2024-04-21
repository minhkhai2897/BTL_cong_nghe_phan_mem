import pygame
import animation
from game_element.weapon import Weapon
from .entity import Entity
from .data import DATA

class Character(Entity):
    def __init__(self, name, position, direction : str = "left"):
        """
        ['knight_m', 'wizzard_m', 'lizard_m', 'elf_m']

        ['big_demon', 'ogre', 'big_zombie', 'chort', 'wogol', 'necromancer', 'orc_shaman', 'orc_warrior', 'masked_orc', 'ice_zombie', 'zombie',]
        """
        self.character_infor = DATA.get_character_info(name)
        super().__init__(animation.CharacterAnimation(self.character_infor['name'], position, self.character_infor['frame_speed']))
        self.__max_hp = self.character_infor['max_hp']
        self.__hp = self.character_infor['max_hp']
        self.__dame = self.character_infor['dame']
        self.__range = self.character_infor['range']
        self.__speed_attack = self.character_infor['speed_attack']
        self.__direction = direction
        self.__weapon = None
        self.__effect = []

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
        if (self.__weapon != None):
            self.__weapon.set_center(self.get_center())
            self.__weapon.update(current_time)
        for effect in self.__effect:
            effect.set_center(self.get_center())
            effect.update(current_time)
            if (effect.is_end()):
                self.__effect.remove(effect)

    def render(self, screen):
        self.anim.render(screen, self.__hp, self.__max_hp)
        if (self.__weapon != None):
            self.__weapon.render(screen)
        for effect in self.__effect:
            effect.render(screen)

    def move(self, dx, dy):
        self.anim.move(dx, dy)

    def __add_weapon_buff(self, weapon : Weapon):
        self.__range += weapon.range
        self.__dame += weapon.dame
        self.__speed_attack += weapon.speed_attack
    
    def add_effect(self, effect):
        self.anim.add_effect(effect)

    def has_weapon(self):
        """ Kiểm tra nhân vật có vũ khí không."""
        if (self.__weapon is None):
            return False
        return True
    
    def add_weapon(self, weapon : Weapon) -> bool:
        if (self.__weapon is None) and (weapon.get_name() in self.character_infor['weapons']):
            self.__weapon = weapon
            self.__add_weapon_buff(weapon)
            return True
        return False
    
    def get_range(self):
        return self.__range
    
    def get_attack_speed(self):
        return self.__speed_attack
    
    def get_dame(self):
        return self.__dame



    

    