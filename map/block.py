import animation

class Block():
    def __init__(self, anim: animation.BackgroundAnimation):
        self.anim = anim

    def update(self, current_time: int):
        self.anim.update(current_time)

    def render(self, screen):
        self.anim.render(screen)