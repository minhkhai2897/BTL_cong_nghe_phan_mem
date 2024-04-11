import pygame
from ._sprite import SPRITE
from ._animation import Animation
from ._effect_animation import EffectAnimation
from ._weapon_animation import WeaponAnimation

class CharacterAnimation(Animation):
    def __init__(self, name: str, position : tuple[float, float] = (0, 0), frame_speed = 0.1):
        """
        Parameters:
            name: Tên nhân vật (str).
            frame_speed: Tốc độ chuyển đổi giữa các frame (frame/s)

        Characters:
            ['knight_m', 'knight_f', 'wizzard_m', 'wizzard_f', 'lizard_m', 'lizard_f', 'elf_m', 'elf_f']

            ['big_demon', 'ogre', 'big_zombie', 'chort', 'wogol', 'necromancer', 'orc_shaman', 'orc_warrior', 'masked_orc', 'ice_zombie', 'zombie', 'swampy', 'muddy', 'skelet', 'imp', 'goblin', 'tiny_zombie']
        """
        state_list = SPRITE.get_characters(name)
        super().__init__(state_list, position, frame_speed)
        self.__effects = []
        self.__weapon = None
        self._name = name
        self.__left = False
        self.__right = False

    def add_effect(self, effect: EffectAnimation):
        """ Thêm hiệu ứng cho nhân vật."""
        self.__effects.append(effect)

    def add_weapon(self, weapon : WeaponAnimation):
        """ Thêm vũ khí cho nhân vật."""
        if (self.__weapon is None):
            self.__weapon = weapon
    
    def has_weapon(self):
        """ Kiểm tra nhân vật có vũ khí không."""
        if (self.__weapon is None):
            return False
        return True

    def __remove_effect_end(self):
        """ Xóa hiệu ứng sau khi đã chạy đủ life_span. """
        self.__effects = [effect for effect in self.__effects if not effect.is_end()]

    def update(self, current_time: int):
        """ Cập nhật hình ảnh hiện tại và các hiệu ứng của nhân vật."""
        super().update(current_time)
        self.__update_state()
        if self.__weapon is not None:
            self.__weapon.update(current_time)
        for effect in self.__effects:
            effect.update(current_time)
        self.__remove_effect_end()

    def __update_state(self):
        if self.__left:
            self.set_state("run_anim_left")
            self.__update_weapon_state("left")
        elif self.__right:
            self.set_state("run_anim_right")
            self.__update_weapon_state("right")

    def __update_weapon_state(self, direction : str):
        if self.__weapon is None:
            return
        self.__weapon.set_state(direction)

    def render(self, screen: pygame.surface.Surface, hp, max_hp):
        """ Hiển thị hình ảnh hiện tại lên màn hình và các hiệu ứng của nhân vật."""
        super().render(screen)
        self.__render_hp(screen, hp, max_hp)
        self.__render_weapon(screen)

        self.__render_effects(screen)

    def __render_effects(self, screen: pygame.surface.Surface):
        """ Hiển thị các hiệu ứng của nhân vật."""
        for effect in self.__effects:
            if (effect.get_name() == "thunder") or (effect.get_name() == "thunder_yellow"):
                x = self.get_position()[0] + (self._current_img.get_width() - effect.get_width()) / 2
                y = self.get_position()[1] - effect.get_height() + self.get_height() / 2
                effect.set_position((x, y))
                effect.render(screen)
            else:
                effect.set_center(self.get_center())
                effect.render(screen)

    def __render_hp(self, screen: pygame.surface.Surface, hp: int, max_hp: int):
        """ Hiển thị thanh máu của nhân vật."""
        if (hp <= 0) or (max_hp <= 0):
            return
        
        LENGTH = min(28, self._current_img.get_width())
        DISTANCE_y = 3

        if (hp < max_hp):
            start_pos = (self.get_position()[0] + ((self._current_img.get_width() - LENGTH) / 2), self.get_position()[1])
            end_pos = (start_pos[0] + (LENGTH * hp / max_hp), start_pos[1])
            pygame.draw.line(screen, (255, 0, 0), start_pos, end_pos, 2)
        elif (hp > max_hp):
            z1 = (hp - max_hp) // max_hp
            z2 = hp % max_hp
            for i in range(z1):
                start_pos = (self.get_position()[0] + ((self._current_img.get_width() - LENGTH) / 2), self.get_position()[1] - DISTANCE_y * (i))
                end_pos = (start_pos[0] + LENGTH, start_pos[1])
                pygame.draw.line(screen, (0, 0, 255), start_pos, end_pos, 2)
            if (z2 > 0):
                start_pos = (self.get_position()[0] + ((self._current_img.get_width() - LENGTH) / 2), self.get_position()[1] - DISTANCE_y * (z1))
                end_pos = (start_pos[0] + (LENGTH * z2 / max_hp), start_pos[1])
                pygame.draw.line(screen, (0, 0, 255), start_pos, end_pos, 2)

    def __render_weapon(self, screen):
        if (self.__weapon is None):
            return
        self.__weapon.set_center(self.get_center())
        self.__weapon.render(screen)
            
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
        super().set_state(self._name + "_" + state)
    
    def _get_current_state(self) -> str:
        """ 
        Trả về tên của trạng thái hiện tại. 
        
        ['idle_anim_left', 'run_anim_left', 'hit_anim_left', 'idle_anim_right', 'run_anim_right', 'hit_anim_right']
        """
        return self._current_state[len(self._name + "_"):]

    def move(self, dx, dy):
        if (dx > 0):
            self.__left = False
            self.__right = True
        elif (dx < 0):
            self.__left = True
            self.__right = False
        super().move(dx, dy)

    