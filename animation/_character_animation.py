import pygame
from ._sprite import SPRITE
from ._animation import Animation
from ._effect_animation import EffectAnimation

class CharacterAnimation(Animation):
    def __init__(self, name: str, frame_speed = 0.1):
        """
        Parameters:
            name: Tên nhân vật (str).
            frame_speed: Tốc độ chuyển đổi giữa các frame (frame/s)

        Characters:
            ['knight_m', 'knight_f', 'wizzard_m', 'wizzard_f', 'lizard_m', 'lizard_f', 'elf_m', 'elf_f']

            ['big_demon', 'ogre', 'big_zombie', 'chort', 'wogol', 'necromancer', 'orc_shaman', 'orc_warrior', 'masked_orc', 'ice_zombie', 'zombie', 'swampy', 'muddy', 'skelet', 'imp', 'goblin', 'tiny_zombie']
        """
        state_list = SPRITE.get_characters(name)
        super().__init__(state_list, frame_speed)
        self._effects = []
        self._name = name

    def add_effect(self, effect: EffectAnimation):
        """ Thêm hiệu ứng cho nhân vật."""
        self._effects.append(effect)

    def __remove_effect_end(self):
        """ Xóa hiệu ứng sau khi đã chạy đủ life_span. """
        self._effects = [effect for effect in self._effects if not effect.is_end()]

    def update(self, current_time: int):
        """ Cập nhật hình ảnh hiện tại và các hiệu ứng của nhân vật."""
        super().update(current_time)
        for effect in self._effects:
            effect.update(current_time)
        self.__remove_effect_end()

    def render(self, screen: pygame.surface.Surface, position: tuple[float, float], hp, max_hp):
        """ Hiển thị hình ảnh hiện tại lên màn hình và các hiệu ứng của nhân vật."""
        super().render(screen, position)
        self.__render_hp(screen, position, hp, max_hp)
        self.__render_effects(screen, position)

    def __render_effects(self, screen: pygame.surface.Surface, position: tuple[float, float]):
        """ Hiển thị các hiệu ứng của nhân vật."""
        for effect in self._effects:
            if (effect.get_name() == "thunder") or (effect.get_name() == "thunder_yellow"):
                x = position[0] + (self._current_img.get_width() - effect.get_width()) / 2
                y = position[1] - effect.get_height() + self.get_height() / 2
                effect.render(screen, (x, y))
            else:
                x = position[0] + self._current_img.get_width() / 2
                y = position[1] + self._current_img.get_height() / 2
                effect.render_center(screen, (x, y))

    def __render_hp(self, screen: pygame.surface.Surface, position: tuple[float, float], hp: int, max_hp: int):
        """ Hiển thị thanh máu của nhân vật."""
        if (hp <= 0) or (max_hp <= 0):
            return
        
        LENGTH = min(28, self._current_img.get_width())
        DISTANCE_y = 3

        if (hp < max_hp):
            start_pos = (position[0] + ((self._current_img.get_width() - LENGTH) / 2), position[1])
            end_pos = (start_pos[0] + (LENGTH * hp / max_hp), start_pos[1])
            pygame.draw.line(screen, (255, 0, 0), start_pos, end_pos, 2)
        elif (hp > max_hp):
            z1 = (hp - max_hp) // max_hp
            z2 = hp % max_hp
            for i in range(z1):
                start_pos = (position[0] + ((self._current_img.get_width() - LENGTH) / 2), position[1] - DISTANCE_y * (i))
                end_pos = (start_pos[0] + LENGTH, start_pos[1])
                pygame.draw.line(screen, (0, 0, 255), start_pos, end_pos, 2)
            if (z2 > 0):
                start_pos = (position[0] + ((self._current_img.get_width() - LENGTH) / 2), position[1] - DISTANCE_y * (z1))
                end_pos = (start_pos[0] + (LENGTH * z2 / max_hp), start_pos[1])
                pygame.draw.line(screen, (0, 0, 255), start_pos, end_pos, 2)                      
            
    def set_state(self, state: str):
        """
        States: 
            - idle_anim_left
            - run_anim_left
            - hit_anim_left
            - idle_anim_right
            - run_anim_right
            - hit_anim_right

        Các nhân vật kẻ thù không có hit_anim
        """
        return super().set_state(self._name + "_" + state)
    
    def get_current_state(self) -> str:
        """ 
        Trả về tên của trạng thái hiện tại. 
        
        ['idle_anim_left', 'run_anim_left', 'hit_anim_left', 'idle_anim_right', 'run_anim_right', 'hit_anim_right']
        """
        return self._current_state[len(self._name + "_"):]


    