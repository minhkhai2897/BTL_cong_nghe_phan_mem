import pygame
import animation
from helper import SCREEN_WIDTH, SCREEN_HEIGHT



class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.is_running = True





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
            


    def update(self):
        pass

        
    def render(self):
        self.screen.fill((255, 255, 255))
        






        
        pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()