import pygame
import animation
from .character import Character

class Snake():
    def __init__(self, speed = 3.2):
        self.__list = [Character('knight_m', (1000, 100), 100), Character('knight_m', (1036, 100), 100), 
                       Character('knight_m', (1072, 100), 100), Character('knight_m', (1108, 100), 100),
                       Character('knight_m', (1144, 100), 100), Character('knight_m', (1180, 100), 100),
                       Character('knight_m', (1212, 100), 100), Character('knight_m', (1248, 100), 100),]
        self.speed = speed
        self.distance_between_characters = 32 + self.speed

    def __getitem__(self, index: int):
        return self.__list[index]

    def add_character(self, name, position):
        pass

    def add_character(self, character : Character):
        self.__list = [character] + self.__list
        if self.__list[1].get_direction() == "left":
            self.__list[0].change_direction("left")
            self.__list[0].set_position((self.__list[1].get_position()[0] - self.distance_between_characters, 
                                          self.__list[1].get_position()[1]))
        elif self.__list[1].get_direction() == "right":
            self.__list[0].change_direction("right")
            self.__list[0].set_position((self.__list[1].get_position()[0] + self.distance_between_characters, 
                                          self.__list[1].get_position()[1]))
        elif self.__list[1].get_direction() == "up":
            self.__list[0].change_direction("up")
            self.__list[0].set_position((self.__list[1].get_position()[0], 
                                          self.__list[1].get_position()[1] - self.distance_between_characters))
        elif self.__list[1].get_direction() == "down":
            self.__list[0].change_direction("down")
            self.__list[0].set_position((self.__list[1].get_position()[0], 
                                          self.__list[1].get_position()[1] + self.distance_between_characters))

    def update(self, current_time):
        self.remove_character_die()
        for character in self.__list:
            character.update(current_time)
        self.move()

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
        self.__move_help()  

    def __move_help(self):
        for i in range(len(self.__list) - 1, 0, -1):
            dx = self.__list[i - 1].get_position()[0] - self.__list[i].get_position()[0]
            dy = self.__list[i - 1].get_position()[1] - self.__list[i].get_position()[1]

            if (self.__list[i].get_direction() == "left") and (dx >= 0):                
                if (dy > 0):
                    self.__list[i].change_direction("down")
                elif (dy < 0):
                    self.__list[i].change_direction("up")
            elif (self.__list[i].get_direction() == "right") and (dx <= 0):
                if (dy > 0):
                    self.__list[i].change_direction("down")
                elif (dy < 0):
                    self.__list[i].change_direction("up")
            elif (self.__list[i].get_direction() == "up") and (dy >= 0):
                if (dx > 0):
                    self.__list[i].change_direction("right")
                elif (dx < 0):
                    self.__list[i].change_direction("left")
            elif (self.__list[i].get_direction() == "down") and (dy <= 0):
                if (dx > 0):
                    self.__list[i].change_direction("right")
                elif (dx < 0):
                    self.__list[i].change_direction("left")

        for charactor in self.__list:
            if charactor.get_direction() == "left":
                charactor.move(-self.speed, 0)
            elif charactor.get_direction() == "right":
                charactor.move(self.speed, 0)
            elif charactor.get_direction() == "up":
                charactor.move(0, -self.speed)
            elif charactor.get_direction() == "down":
                charactor.move(0, self.speed)

    


    

            
