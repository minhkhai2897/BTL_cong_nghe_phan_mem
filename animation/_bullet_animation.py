from ._animation import Animation
from ._sprite import SPRITE
from ._helper import ImageProcessor

class BulletAnimation(Animation):
    def __init__(self, name: str, angle : float = 0.0, frame_speed = 0.1):
        """
        ['arrow', 'axe', 'fireball', 'ice_pick']
        """
        self.__angle = angle
        state_list = SPRITE.get_bullets(name)
        super().__init__(state_list, frame_speed)
        self._name = name

    def update(self, current_time: int):
        super().update(current_time)
        self._current_img = ImageProcessor.rotate(self._current_img, self.__angle)

    def set_angle(self, angle: float):
        self.__angle = angle