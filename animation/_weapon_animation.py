from ._animation import Animation
from ._sprite import SPRITE

class WeaponAnimation(Animation):
    def __init__(self, name : str, position : tuple[float, float] = (0, 0), frame_speed : float = 0.1):
        """
        ['knife', 'rusty_sword', 'regular_sword', 'red_gem_sword', 'big_hammer', 'hammer', 'baton_with_spikes', 'mace', 'katana', 'saw_sword', 'anime_sword', 'axe', 'machete', 'cleaver', 'duel_sword', 'knight_sword', 'golden_sword', 'lavish_sword', 'red_magic_staff', 'green_magic_staff', 'spear', 'purple_staff', 'thunder_staff', 'bow', 'holy_sword', 'fire_sword', 'ice_sword', 'grass_sword', 'iron_sword']
        """
        state_list = SPRITE.get_weapons(name)
        super().__init__(state_list, position, frame_speed)
        self._name = name

    def set_state(self, state: str):
        """
        States: 
            - left
            - right
        """
        super().set_state("weapon_" + self._name + "_" + state)
    
    def _get_current_state(self) -> str:
        """ 
        Trả về tên của trạng thái hiện tại.
        
        ['left', 'right']
        """
        return self._current_state[len("weapon_" + self._name + "_"):]