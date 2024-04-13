import pygame
import math
from ._animation import Animation
from ._sprite import SPRITE

class BulletAnimation(Animation):
    def __init__(self, name: str, position : tuple[float, float] = (0, 0), frame_speed : float = 0.1):
        """
        ['arrow', 'axe', 'fireball', 'ice_pick']
        """
        self.__angle = 0
        state_list = SPRITE.get_bullets(name)
        super().__init__(state_list, position, frame_speed)
        self._name = name

    def update(self, current_time: int):
        super().update(current_time)
        self.rotate()

    def move(self, dx: float, dy: float):
        self.__get_angle(dx, dy)
        super().move(dx, dy)

    def __get_angle(self, dx: float, dy: float):
        if dx == 0:
            if dy > 0:
                self.__angle = 270
            else:
                self.__angle = 90
        else:
            self.__angle = - math.atan(dy / dx) * 180 / math.pi
        # chưa hoàn thành.
    
    def rotate(self):
        self._current_img = pygame.transform.rotate(self._images[self._current_frame], self.__angle)
