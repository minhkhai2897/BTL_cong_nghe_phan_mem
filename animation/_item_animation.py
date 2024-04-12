from ._animation import Animation
from ._sprite import SPRITE

class ItemAnimation(Animation):
    def __init__(self, name: str, position : tuple[float, float] = (0, 0), frame_speed : float = 0.1):
        """
        ['chest_empty_open_anim', 'chest_full_open_anim', 'chest_mimic_open_anim']
        
        ['flask_big_red', 'flask_big_blue', 'flask_big_green', 'flask_big_yellow', 'flask_red', 'flask_blue', 'flask_green', 'flask_yellow']
        
        ['skull', 'crate', 'coin_anim']
        
        ['ui_heart_full', 'ui_heart_half', 'ui_heart_empty']
        """
        state_list = SPRITE.get_items(name)
        super().__init__(state_list, position, frame_speed)
        self._name = name
