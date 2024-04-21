import animation
from .block import Block

class TrapBlock(Block):
    def __init__(self, position: tuple[int, int]):
        super().__init__("floor_spikes_anim", position)
        self.enable = True

    def update(self, current_time: int):
        super().update(current_time)

 