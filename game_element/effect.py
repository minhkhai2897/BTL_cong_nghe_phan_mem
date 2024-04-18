import pygame
import animation
from .entity import Entity

class Effect(Entity):
    def __init__(self, name, position, life_span : int = 1):
        """
        ['attack_up', 'blood1', 'blood2', 'blood3', 'blood4', 'bloodBound', 'clawfx', 'clawfx2', 'cross_hit', 'explosion2', 'fireball_explosion1', 'golden_cross_hit', 'halo_explosion1', 'halo_explosion2', 'holy_shield', 'hp_med', 'ice', 'iceShatter', 'purple_ball', 'purple_exp', 'shine', 'solidfx', 'solid_greenfx', 'swordfx', 'thunder', 'thunder_yellow']
        """
        super().__init__(animation.EffectAnimation(name, position, frame_speed = 0.1, life_span=life_span))
    
    def update(self, current_time):
        self.anim.update(current_time)
    
    def render(self, screen):
        self.anim.render(screen)

    def is_end(self):
        return self.anim.is_end()