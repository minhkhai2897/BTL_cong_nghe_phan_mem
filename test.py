import pygame
import animation
import map_test


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 700))
        self.clock = pygame.time.Clock()
        self.is_running = True

        self.knight_animation = animation.CharacterAnimation("knight_m")
        self.knight2_animaiton = animation.CharacterAnimation("knight_m")
        self.knight2_animaiton.set_state("idle_anim_left")
        self.big_demon_animation = animation.CharacterAnimation("big_demon")
        self.big_demon_animation.set_state("run_anim_right")
        self.wizzard_animation = animation.CharacterAnimation("wizzard_m")
        self.knight2_animaiton.add_effect(animation.EffectAnimation("thunder", 0.1, 10))

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
        self.knight_animation.update(pygame.time.get_ticks())
        self.knight2_animaiton.update(pygame.time.get_ticks())
        self.big_demon_animation.update(pygame.time.get_ticks())
        self.wizzard_animation.update(pygame.time.get_ticks())
        
    def render(self):
        self.screen.fill((255, 255, 255))
        map_test.render_map(self.screen)

        self.knight_animation.render(self.screen, (100, 100), 1, 1)
        self.knight2_animaiton.render(self.screen, (200, 100), 250, 200)
        self.big_demon_animation.render(self.screen, (300, 100), 1, 1)
        self.wizzard_animation.render(self.screen, (400, 100), 1, 1)

        pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()