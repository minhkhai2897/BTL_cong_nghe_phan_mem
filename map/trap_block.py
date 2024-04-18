import animation
from .block import Block

class TrapBlock(Block):
    def __init__(self, position: tuple[int, int]):
        super().__init__(animation.BackgroundAnimation("floor_spikes_anim", position, 0.5))
        self.enable = True

    def update(self, current_time: int):
        super().update(current_time)

 