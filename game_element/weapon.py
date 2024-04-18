import pygame
import animation
from .entity import Entity

class Weapon(Entity):
    def __init__(self, name, position, dame : int = 0, range : int = 0, speed_attack : float = 0):
        """
        ['knife', 'rusty_sword', 'regular_sword', 'red_gem_sword', 'big_hammer', 'hammer', 'baton_with_spikes', 'mace', 'katana', 'saw_sword', 'anime_sword', 'axe', 'machete', 'cleaver', 'duel_sword', 'knight_sword', 'golden_sword', 'lavish_sword', 'red_magic_staff', 'green_magic_staff', 'spear', 'purple_staff', 'thunder_staff', 'bow', 'holy_sword', 'fire_sword', 'ice_sword', 'grass_sword', 'iron_sword']
        """
        super().__init__(animation.WeaponAnimation(name, position))
        self.dame = dame
        self.range = range
        self.speed_attack = speed_attack

    def update(self, current_time):
        self.anim.update(current_time)

    def render(self, screen):
        self.anim.render(screen)


