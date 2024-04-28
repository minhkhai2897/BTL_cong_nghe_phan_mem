import pygame
import animation
from map import Map
from helper import SCREEN_WIDTH, SCREEN_HEIGHT
from game_element.snake import Snake
from game_element.character import Character
from game_element import Effect
from game_element.item import Item
from game_element.bullet import Bullet
from game_element import Weapon
from animation._helper import UNIT

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.is_running = True

        self.map = Map() # trong này sẽ có map hiện tại, và các mảng 2 chiều chứa vị trị đinh, ...
        self.effects = []
        self.bullets = []
        self.enemies = []
        self.players = [Snake("knight_m", (500, 500), "left", 2)]
        self.current_time = 0
        self.last_update_time = 0

    def run(self):
        while self.is_running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60) 

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
        
            for player in self.players:
                player.handle_keyboard_events(event)


    def update(self):
        self.current_time = pygame.time.get_ticks()
        if (self.current_time - self.last_update_time > 10 * 1000):
            self.last_update_time = self.current_time
            self.map.add_new_idle_characters()
            self.map.add_new_items()
            self.map.add_new_weapons()
        self.map.update(pygame.time.get_ticks())

        
        # xử lý tương tác giữa các list đặt ở đây
        self.handle_collision_players_and_map()
        # self.handle_collision_players_and_weapons()
        # self.handle_collision_players_and_characters()




        self.remove_effect_end()









        for player in self.players:
            player.update(pygame.time.get_ticks())
        # update idle_characters
        for x, y in self.map.idle_characters_positions:
            self.map.idle_characters_map[y][x].update(pygame.time.get_ticks())
        # update items
        # for x, y in self.map.items_positions:
        #     self.map.items_map[y][x].update(pygame.time.get_ticks())
        # update weapons
        # for x, y in self.map.weapons_positions:
        #     self.map.weapons_map[y][x].update(pygame.time.get_ticks())

        for enemy in self.enemies:
            enemy.update(pygame.time.get_ticks())
        for bullet in self.bullets:
            bullet.update(pygame.time.get_ticks())
        for effect in self.effects:
            effect.update(pygame.time.get_ticks())
        

    def render(self):
        self.screen.fill((0, 0, 0))
        
        self.map.render(self.screen)
        # render weapons
        for x, y in self.map.weapons_positions:
            self.map.weapons_map[y][x].render(self.screen)
        # render items
        for x, y in self.map.items_positions:
            self.map.items_map[y][x].render(self.screen)
        for player in self.players:
            player.render(self.screen)
        # render idle_characters
        for x, y in self.map.idle_characters_positions:
            self.map.idle_characters_map[y][x].render(self.screen)
        for enemy in self.enemies:
            enemy.render(self.screen)
        for bullet in self.bullets:
            bullet.render(self.screen)
        for effect in self.effects:
            effect.render(self.screen)        
        pygame.display.flip()


    def remove_effect_end(self):
        self.effects = [effect for effect in self.effects if not effect.is_end()]


    def handle_collision_players_and_map(self):
        for player in self.players:
            # xử lý va chạm với map
            x = player[0].get_center()[0] // UNIT
            y = player[0].get_center()[1] // UNIT
            if (not self.map.has_map[y][x]):
                player.die()

            # xử lý va chạm với weapon
            if self.map.weapons_map[y][x] is not None:
                for character in player:
                    if character.add_weapon(self.map.weapons_map[y][x]):
                        self.map.remove_weapon(x, y)
                        break
            
            # Xử lý va chạm với item
            if self.map.items_map[y][x] is not None:
                player.add_item(self.map.items_map[y][x])
                self.map.remove_item(x, y)

            # Xử lý va chạm với idle character
            if (player[0].get_direction() == "left"):
                if not (self.map.idle_characters_map[y][x - 1] is None):
                    player.add_character(self.map.idle_characters_map[y][x - 1])
                    self.map.remove_idle_character(x - 1, y)
            elif (player[0].get_direction() == "right"):
                if not (self.map.idle_characters_map[y][x + 1] is None):
                    player.add_character(self.map.idle_characters_map[y][x + 1])
                    self.map.remove_idle_character(x + 1, y)
            elif (player[0].get_direction() == "up"):
                if not (self.map.idle_characters_map[y - 1][x] is None):
                    player.add_character(self.map.idle_characters_map[y - 1][x])
                    self.map.remove_idle_character(x, y - 1)
            elif (player[0].get_direction() == "down"):
                if not (self.map.idle_characters_map[y + 1][x] is None):
                    player.add_character(self.map.idle_characters_map[y + 1][x])
                    self.map.remove_idle_character(x, y + 1)


    def reset(self):
        pass
                            

if __name__ == "__main__":
    game = Game()
    game.run()