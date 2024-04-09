import pygame
from ._sprite_sheet import SpriteSheet

class Sprite():
    def __init__(self):
        # khởi tạo đối tượng SpriteSheet
        self.__sprite_sheet = SpriteSheet()

        # images là 1 dict chứa các list ảnh cho từng trạng thái của các nhân vật, hiệu ứng, vật phẩm, ...
        self.__images = self.__sprite_sheet.extract_images_from_files_and_process("res/drawable/path_list")

        # danh sách các trạng thái của các nhân vật
        self.__characters = self.__sprite_sheet.get_characters()

        # danh sách các trạng thái của các hiệu ứng
        self.__effects = self.__sprite_sheet.get_effects()

        # danh sách các trạng thái của các vũ khí
        self.__weapons = self.__sprite_sheet.get_weapons()

        # danh sách các trạng thái của các loại đạn
        self.__bullets = self.__sprite_sheet.get_bullets()

        # danh sách các trạng thái của các vật phẩm
        self.__items = self.__sprite_sheet.get_items()

        # danh sách các trạng thái của các vật khác
        self.__backgrounds = self.__sprite_sheet.get_backgrounds()

    def get_images(self, name: str) -> tuple[pygame.surface.Surface]:
        """ Trả về tuple ảnh cho trạng thái name. """
        return self.__images[name]
        
    def get_characters(self, name: str) -> tuple[str]:
        """ trả về tuple trạng thái của nhân vật name. """
        return self.__characters[name]
    
    def get_effects(self, name: str) -> tuple[str]:
        """ Trả về tuple trạng thái của hiệu ứng name. """
        return self.__effects[name]
    
    def get_weapons(self, name: str) -> tuple[str]:
        """ Trả về tuple trạng thái của vũ khí name."""
        return self.__weapons[name]
    
    def get_bullets(self, name: str) -> tuple[str]:
        """ Trả về tuple trạng thái của đạn name. """
        return self.__bullets[name]
    
    def get_items(self, name: str) -> tuple[str]:
        """ Trả về tuple trạng thái của vật phẩm name. """
        return self.__items[name]
    
    def get_backgrounds(self, name: str) -> tuple[str]:
        """ Trả về tuple trạng thái của vật khác name. """
        return self.__backgrounds[name]

SPRITE = Sprite()
        
 