import pygame
import animation
from .character import Character

class Snake():
    def __init__(self, speed = 2):
        self.__list = [Character('knight_m', (500, 500)), Character('knight_m', (532, 500)),
                       Character('knight_m', (564, 500)), Character('knight_m', (596, 500))]
        self.speed = speed
        self.distance_between_characters = 32 + self.speed
        self.__live = True

    def __getitem__(self, index: int):
        return self.__list[index]

    def add_character(self, name, position):
        pass

    def die(self):
        self.__live = False

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
    #     for i in range(1, len(self.__list)):
    #         dx = self.__list[i - 1].get_position()[0] - self.__list[i].get_position()[0]
    #         dy = self.__list[i - 1].get_position()[1] - self.__list[i].get_position()[1]
    #         if (self.__list[i - 1].get_direction() in ("left", "right")):
    #             if (dy > 0):
    #                 self.__list[i].change_direction("down")
    #             elif (dy < 0):
    #                 self.__list[i].change_direction("up")

    #         elif (self.__list[i - 1].get_direction() in ("up", "down")):
    #             if (dx > 0):
    #                 self.__list[i].change_direction("right")
    #             elif (dx < 0):
    #                 self.__list[i].change_direction("left")
                
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
            if charactor.get_direction() == "left":
                charactor.move(-self.speed, 0)
            elif charactor.get_direction() == "right":
                charactor.move(self.speed, 0)
            elif charactor.get_direction() == "up":
                charactor.move(0, -self.speed)
            elif charactor.get_direction() == "down":
                charactor.move(0, self.speed)


        # for i in range(len(self.__list) - 1, 0, -1):
        #     dx = self.__list[i - 1].get_position()[0] - self.__list[i].get_position()[0]
        #     dy = self.__list[i - 1].get_position()[1] - self.__list[i].get_position()[1]
        #     d = abs(dx) + abs(dy) - self.distance_between_characters
        #     if (self.__list[i].get_direction() == "left"):
        #         self.__list[i].move(-(self.speed + d), 0)
        #     elif (self.__list[i].get_direction() == "right"):
        #         self.__list[i].move(self.speed + d, 0)
        #     elif (self.__list[i].get_direction() == "up"):
        #         self.__list[i].move(0, -(self.speed + d))
        #     elif (self.__list[i].get_direction() == "down"):
        #         self.__list[i].move(0, self.speed + d)
        
        # if self.__list[0].get_direction() == "left":
        #     self.__list[0].move(-self.speed, 0)
        # elif self.__list[0].get_direction() == "right":
        #     self.__list[0].move(self.speed, 0)
        # elif self.__list[0].get_direction() == "up":
        #     self.__list[0].move(0, -self.speed)
        # elif self.__list[0].get_direction() == "down":
        #     self.__list[0].move(0, self.speed)
 

        
    



# for i in range(len(self.__list) - 1, 0, -1):
#             dx = self.__list[i - 1].get_position()[0] - self.__list[i].get_position()[0]
#             dy = self.__list[i - 1].get_position()[1] - self.__list[i].get_position()[1]
#             if (self.__list[i].get_direction() == "left"):
#                 if (dx >= 0):                
#                     if (dy > 0):
#                         self.__list[i].change_direction("down")
#                     elif (dy < 0):
#                         self.__list[i].change_direction("up")
#             elif (self.__list[i].get_direction() == "right"):
#                 if (dx <= 0):
#                     if (dy > 0):
#                         self.__list[i].change_direction("down")
#                     elif (dy < 0):
#                         self.__list[i].change_direction("up")
#             elif (self.__list[i].get_direction() == "up"):
#                 if (dy >= 0):
#                     if (dx > 0):
#                         self.__list[i].change_direction("right")
#                     elif (dx < 0):
#                         self.__list[i].change_direction("left")
#             elif (self.__list[i].get_direction() == "down"):
#                 if (dy <= 0):
#                     if (dx > 0):
#                         self.__list[i].change_direction("right")
#                     elif (dx < 0):
#                         self.__list[i].change_direction("left")

    

            
