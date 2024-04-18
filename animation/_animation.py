import pygame
from abc import ABC
from ._sprite import SPRITE

class Animation(ABC):
    def __init__(self, state_list : tuple[str], position : tuple[float, float], frame_speed: float):
        """ 
        Parameters:
            state_list: Danh sách các trạng thái của đối tượng (list[str])
            frame_speed: Tốc độ chuyển đổi giữa các frame (frame/s)
        """
        self._state_list = state_list
        self._current_state = self._state_list[0]
        self._images = SPRITE.get_images(self._current_state)
        self._is_change_state = False
        self._current_img = self._images[0]
        self._current_img_rect = self._current_img.get_rect()
        self.set_position(position)
        self._current_frame = 0  
        self._last_update_time = 0  
        self._frame_speed = frame_speed 
        self._name = ""
    
    def set_frame_speed(self, frame_speed: float):
        """ Thiết lập tốc độ chuyển đổi giữa các frame (frame/s)."""
        self._frame_speed = frame_speed

    def get_frame_speed(self) -> float:
        """ Trả về tốc độ chuyển đổi giữa các frame (frame/s)."""
        return self._frame_speed

    def get_name(self) -> str:
        """ Trả về tên của đối tượng."""
        return self._name
    
    def set_state(self, state: str):
        """ Thiết lập trạng thái mới. """
        if (state not in self._state_list):
            raise ValueError(f"State {state} is not in the state_list")
        if (self._current_state != state):
            self._current_state = state
            self._images = SPRITE.get_images(self._current_state)
            self._is_change_state = True

    def get_width(self) -> int:
        """ Trả về chiều rộng của hình ảnh hiện tại."""
        return self._current_img.get_width()
    
    def get_height(self) -> int:
        """ Trả về chiều dài của hình ảnh hiện tại."""
        return self._current_img.get_height()
    
    def get_rect(self) -> pygame.Rect:
        """ Trả về hình chữ nhật bao quanh hình ảnh hiện tại (bouding box)."""
        return self._current_img_rect
    
    def check_collision(self, other: 'Animation') -> bool:
        """ Kiểm tra va chạm với một bouding box khác."""
        return self._current_img_rect.colliderect(other.get_rect())

    def _get_current_state(self) -> str:
        """ Trả về tên của trạng thái hiện tại."""
        return self._current_state

    def render(self, screen: pygame.surface.Surface):
        """ Hiển thị hình ảnh hiện tại lên màn hình."""
        screen.blit(self._current_img, self._current_img_rect)

    def update(self, current_time: int):
        """ Cập nhật hình ảnh hiện tại."""
        if (self._is_change_state):
            self._current_frame = 0
            self._is_change_state = False
            self._last_update_time = current_time
            self.__set_current_image()
        else:
            SECOND_MS = 1000
            elapsed_time = current_time - self._last_update_time
            if elapsed_time >= (self._frame_speed * SECOND_MS):
                self._last_update_time = current_time
                self._current_frame = (self._current_frame + 1) % len(self._images)
                self.__set_current_image()

    def __set_current_image(self):
        self._current_img = self._images[self._current_frame]
        # position = self._current_img_rect.topleft
        # self._current_img_rect = self._current_img.get_rect()
        # self.set_position(position)

    def move(self, dx : float, dy : float):
        """ Di chuyển hình ảnh hiện tại."""
        # self._current_img_rect.move_ip(dx, dy)
        self._current_img_rect.topleft = (self._current_img_rect.left + dx, self._current_img_rect.top + dy)
    
    def get_position(self) -> tuple[float, float]:
        return self._current_img_rect.topleft
    
    def set_position(self, position : tuple[float, float]):
        self._current_img_rect.topleft = position

    def get_center(self) -> tuple[float, float]:
        return self._current_img_rect.center
    
    def set_center(self, center : tuple[float, float]):
        self._current_img_rect.center = center


    
