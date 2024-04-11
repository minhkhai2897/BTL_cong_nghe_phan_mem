import pygame
from ._animation import Animation
from ._sprite import SPRITE

class BulletAnimation(Animation):
    def __init__(self, name: str, position : tuple[float, float] = (0, 0), angle : float = 0.0, frame_speed = 0.1):
        """
        ['arrow', 'axe', 'fireball', 'ice_pick']
        """
        self.__angle = angle
        state_list = SPRITE.get_bullets(name)
        super().__init__(state_list, position, frame_speed)
        self._name = name

    def update(self, current_time: int):
        super().update(current_time)
        self.rotate()

    def get_angle(self) -> float:
        return self.__angle
    
    def rotate(self):
        pass
