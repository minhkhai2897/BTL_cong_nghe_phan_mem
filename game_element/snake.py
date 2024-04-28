import pygame
import animation
from animation._helper import UNIT
from .character import Character
from .item import Item
from .data import DATA


class Snake():
    def __init__(self, name : str, position : tuple[int, int], direction, speed = 2):
        """
        'knight_m', 'wizzard_m', 'lizard_m', 'elf_m','big_demon', 'ogre', 'big_zombie', 'chort', 'wogol', 'necromancer', 'orc_shaman', 'orc_warrior', 'masked_orc', 'ice_zombie', 'zombie'
        """
        self.__distance_between_characters = UNIT # + self.speed
        self.__list = self.__init_snake(name, position, direction)
        self.speed = speed
        self.__live = True

    def __init_snake(self, name, position, direction):
        snake = []
        for i in range(DATA.get_snaker(name)['length']):
            character = Character(name, position, direction)
            character.move(-i * self.__distance_between_characters)
            snake.append(character)
        return snake

    def __getitem__(self, index: int):
        return self.__list[index]

    def add_character(self, name, position):
        pass

    def add_item(self, Item):
        pass

    def die(self):
        self.__live = False

    def add_character(self, character : Character):
        character.change_direction(self.__list[0].get_direction())
        character.set_position(self.__list[0].get_position())
        character.move(self.__distance_between_characters)
        self.__list = [character] + self.__list

    def update(self, current_time):
        self.remove_character_die()
        for character in self.__list:
            character.update(current_time)

        # self.__live = not self.check_self_eat()
        if self.__live:
            self.move()

    # hàm kiểm tra xem con rắn có tự ăn chính nó không
    def check_self_eat(self):
        for i in range(1, len(self.__list)):
            if self.__list[0].check_collision(self.__list[i]):
                return True
        return False

    def render(self, screen):
        for character in self.__list:
            character.render(screen)

    def remove_character_die(self):
        self.__list = [character for character in self.__list if character.get_current_hp() > 0]

    def handle_keyboard_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and self.__list[0].get_direction() != "right":
                self.__list[0].change_direction("left")
            elif event.key == pygame.K_RIGHT and self.__list[0].get_direction() != "left":
                self.__list[0].change_direction("right")
            elif event.key == pygame.K_UP and self.__list[0].get_direction() != "down":
                self.__list[0].change_direction("up")
            elif event.key == pygame.K_DOWN and self.__list[0].get_direction() != "up":
                self.__list[0].change_direction("down")
    
    def move(self):
        for i in range(len(self.__list) - 1, 0, -1):
            dx = self.__list[i - 1].get_position()[0] - self.__list[i].get_position()[0]
            dy = self.__list[i - 1].get_position()[1] - self.__list[i].get_position()[1]
            d = abs(dx) + abs(dy)
            if (self.__list[i].get_direction() == "left"):
                if (dx >= 0):                
                    if (dy > 0):
                        self.__list[i].change_direction("down")
                    elif (dy < 0):
                        self.__list[i].change_direction("up")
                else: 
                    if (self.__list[i - 1].get_direction() == "left"):
                        if (dy > 0):
                            self.__list[i].change_direction("down")
                        elif (dy < 0):
                            self.__list[i].change_direction("up")
            elif (self.__list[i].get_direction() == "right"):
                if (dx <= 0):
                    if (dy > 0):
                        self.__list[i].change_direction("down")
                    elif (dy < 0):
                        self.__list[i].change_direction("up")
                else:
                    if (self.__list[i - 1].get_direction() == "right"):
                        if (dy > 0):
                            self.__list[i].change_direction("down")
                        elif (dy < 0):
                            self.__list[i].change_direction("up")
            elif (self.__list[i].get_direction() == "up"):
                if (dy >= 0):
                    if (dx > 0):
                        self.__list[i].change_direction("right")
                    elif (dx < 0):
                        self.__list[i].change_direction("left")
                else:
                    if (self.__list[i - 1].get_direction() == "up"):
                        if (dx > 0):
                            self.__list[i].change_direction("right")
                        elif (dx < 0):
                            self.__list[i].change_direction("left")
            elif (self.__list[i].get_direction() == "down"):
                if (dy <= 0):
                    if (dx > 0):
                        self.__list[i].change_direction("right")
                    elif (dx < 0):
                        self.__list[i].change_direction("left")
                else:
                    if (self.__list[i - 1].get_direction() == "down"):
                        if (dx > 0):
                            self.__list[i].change_direction("right")
                        elif (dx < 0):
                            self.__list[i].change_direction("left")

        for charactor in self.__list:
            charactor.move(self.speed)


    

            
