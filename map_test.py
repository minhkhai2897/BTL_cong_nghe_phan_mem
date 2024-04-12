import animation
from block import Block
from helper import MAP_WIDTH, MAP_HEIGHT

class Map():
    def __init__(self):
        self.__tuple = self.create_map()
    
    def __getitem__(self, index: int):
        return self.__tuple[index]

    def create_map(self):
        map = [[None for i in range(MAP_WIDTH)] for j in range(MAP_HEIGHT)]

        for i in range(MAP_HEIGHT):
            for j in range(MAP_WIDTH):
                map [i][j] = (Block(animation.BackgroundAnimation("floor_1", (j * 32, i * 32), 1)))

        for i in range(MAP_HEIGHT):
            map[i] = tuple(map[i])
        map = tuple(map)
        
        return map    
    
    
    def update(self, current_time):
        for i in range(MAP_WIDTH):
            for j in range(MAP_HEIGHT):
                if not self.__tuple[j][i] is None:
                    self.__tuple[j][i].update(current_time)
    
    def render(self, screen):
        for i in range(MAP_WIDTH):
            for j in range(MAP_HEIGHT):
                if not self.__tuple[j][i] is None:
                    self.__tuple[j][i].render(screen)

    