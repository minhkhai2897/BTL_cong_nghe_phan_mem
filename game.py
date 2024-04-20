import pygame
import animation
from map import Map
from helper import SCREEN_WIDTH, SCREEN_HEIGHT
from game_element.snake import Snake
from game_element.character import Character
from game_element.effect import Effect
from game_element.item import Item
from game_element.bullet import Bullet
from game_element.weapon import Weapon

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.is_running = True

        self.map = Map() # trong này sẽ có map hiện tại, và các mảng 2 chiều chứa vị trị đinh, ...
        self.idle_characters = [Character("knight_m", (100, 100), 100), Character("wizzard_m", (200, 200), 100)]
        
        self.effects = [Effect("thunder", (300, 300), 5), Effect("thunder", (400, 400), 1)]
        self.items = [Item("chest_empty_open_anim", (500, 500)), Item("chest_full_open_anim", (600, 600)), Item("ui_heart_full", (700, 700))]
        self.bullets = [Bullet("arrow", (500, 500), angle=270), Bullet("axe", (750, 750)), Bullet("fireball", (550, 550)), Bullet("ice_pick", (450, 450))]
        self.weapons = [Weapon("katana", (50, 50)), Weapon("katana", (50, 200)), Weapon("purple_staff", (150, 150)), Weapon("thunder_staff", (250, 250))]
        self.enemies = []
        self.players = [Snake()]

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
        self.map.update(pygame.time.get_ticks())

        
        # xử lý tương tác giữa các list đặt ở đây
        self.handle_collision_players_and_map()





        self.handle_collision_players_and_weapons()
        self.handle_collision_players_and_characters()




        self.remove_effect_end()









        for player in self.players:
            player.update(pygame.time.get_ticks())
        for character in self.idle_characters:
            character.update(pygame.time.get_ticks())
        for enemy in self.enemies:
            enemy.update(pygame.time.get_ticks())
        for item in self.items:
            item.update(pygame.time.get_ticks())
        for weapon in self.weapons:
            weapon.update(pygame.time.get_ticks())
        for bullet in self.bullets:
            bullet.update(pygame.time.get_ticks())
        for effect in self.effects:
            effect.update(pygame.time.get_ticks())
        

    def render(self):
        self.screen.fill((0, 0, 0))
        
        self.map.render(self.screen)
        for item in self.items:
            item.render(self.screen)
        for player in self.players:
            player.render(self.screen)
        for character in self.idle_characters:
            character.render(self.screen)
        for enemy in self.enemies:
            enemy.render(self.screen)
        for weapon in self.weapons:
            weapon.render(self.screen)
        for bullet in self.bullets:
            bullet.render(self.screen)
        for effect in self.effects:
            effect.render(self.screen)        
        pygame.display.flip()


    def remove_effect_end(self):
        self.effects = [effect for effect in self.effects if not effect.is_end()]


    def handle_collision_players_and_map(self):
        for player in self.players:
            x = player[0].get_center()[0] // 32
            y = player[0].get_center()[1] // 32
            if (not self.map.has_map[y][x]):
                player.die()

    def handle_collision_players_and_weapons(self):
        for player in self.players:
            characters = [character for character in player if not character.has_weapon()]
            for weapon in self.weapons:
                if (player[0].check_collision(weapon)):
                    for character in characters:
                        if character.has_weapon():
                            continue
                        if (character.get_name() in ("knight_m", "knight_f")) and (weapon.get_name() in ("katana")):
                            character.add_weapon(weapon)
                            self.weapons.remove(weapon)
                            # thêm xử lý ...buff, ...
                            break
                        # if ...

    def handle_collision_players_and_characters(self):
        for player in self.players:
            for character in self.idle_characters:
                if (player[0].check_collision(character)):
                    player.add_character(character)
                    self.idle_characters.remove(character)

                            

if __name__ == "__main__":
    game = Game()
    game.run()