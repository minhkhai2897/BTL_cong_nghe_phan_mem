from ._sprite import SPRITE
from ._animation import Animation

class EffectAnimation(Animation):
    def __init__(self, name : str, position : tuple[float, float] = (0, 0), frame_speed = 0.1, life_span : int = 1):
        """
        ['attack_up', 'blood1', 'blood2', 'blood3', 'blood4', 'bloodBound', 'clawfx', 'clawfx2', 'cross_hit', 'explosion2', 'fireball_explosion1', 'golden_cross_hit', 'halo_explosion1', 'halo_explosion2', 'holy_shield', 'hp_med', 'ice', 'iceShatter', 'purple_ball', 'purple_exp', 'shine', 'solidfx', 'solid_greenfx', 'swordfx', 'thunder', 'thunder_yellow']
        """
        state_list = SPRITE.get_effects(name)
        super().__init__(state_list, position, frame_speed)
        self.__life_span = life_span
        self.__is_end = False
        self.__time_initialized = -1
        self._name = name

    def is_end(self) -> bool:
        return self.__is_end
    
    def set_state(self, state: str):
        """ Không set_state cho effect animation"""
        return 

    def update(self, current_time: int): 
        super().update(current_time)

        if self.__time_initialized == -1:
            self.__time_initialized = current_time
        else:
            elapsed_time = current_time - self.__time_initialized
            if elapsed_time >= (self.__life_span * len(self._images) * self._frame_speed * 1000): 
                self.__is_end = True



    
    