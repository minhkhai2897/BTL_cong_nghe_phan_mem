import animation

class Block():
    def __init__(self, anim: animation.BackgroundAnimation):
        self.__animation = anim

    def update(self, current_time: int):
        self.__animation.update(current_time)

    def render(self, screen):
        self.__animation.render(screen)