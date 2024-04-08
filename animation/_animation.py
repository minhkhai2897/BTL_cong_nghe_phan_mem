import pygame
from ._sprite import SPRITE

class Animation:
    def __init__(self, state_list = list[str], frame_speed: int = 0.1):
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
        self._current_frame = 0  
        self._last_update_time = 0  
        self._frame_speed = frame_speed 
        self._name = ""
    
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

    def get_current_state(self) -> str:
        """ Trả về tên của trạng thái hiện tại."""
        return self._current_state

    def render(self, screen: pygame.surface.Surface, position: tuple[float, float]):
        """ Hiển thị hình ảnh hiện tại lên màn hình."""
        screen.blit(self._current_img, position)

    def update(self, current_time: int):
        """ Cập nhật hình ảnh hiện tại."""
        if (self._is_change_state):
            self._current_frame = 0
            self._is_change_state = False
            self._last_update_time = current_time
        else:
            elapsed_time = current_time - self._last_update_time
            if elapsed_time >= (self._frame_speed * 1000):
                self._last_update_time = current_time
                self._current_frame = (self._current_frame + 1) % len(self._images)
        self._current_img = self._images[self._current_frame]

