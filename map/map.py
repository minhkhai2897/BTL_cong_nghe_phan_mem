import random
import animation
from enum import Enum
from map.trap_block import TrapBlock
from .block import Block
from .helper import MAP_WIDTH, MAP_HEIGHT

class TileType(Enum):
    FLOOR = 0
    WALL = 1
    SPIKE = 2

class Map():
    def __init__(self):
        self.__tuple, self.has_map, self.is_trap, self.__animated_block_positions = self.create_map()

    def __getitem__(self, index: int):
        return self.__tuple[index]

    def create_map(self):
        map = self.generate_map()
        return map
           
    
    def update(self, current_time):
        for position in self.__animated_block_positions:
            for block in self.__tuple[position[1]][position[0]]:
                block.update(current_time)
    
    def render(self, screen):
        for i in range(MAP_WIDTH):
            for j in range(MAP_HEIGHT):
                for block in self.__tuple[j][i]:
                    block.render(screen)

    def generate_map(self) -> tuple[tuple]:
        map = [[[] for i in range(MAP_WIDTH)] for j in range(MAP_HEIGHT)]
        animated_block_positions = []
        has_map, is_trap = self.init_random_map(0.7, 3, 0.012)
 
        # Thêm các block nền vào map.
        for i in range(MAP_HEIGHT):
            for j in range(MAP_WIDTH):
                if (has_map[i][j] == 1):
                    map[i][j] = [Block(animation.BackgroundAnimation("floor_1", (j * 32, i * 32), 1))]

                if (is_trap[i][j] == 1):
                    map[i][j] = [TrapBlock((j * 32, i * 32))]
                    animated_block_positions.append((j, i))

        # Thêm tường xung quanh map
        self.__add_wall_around_map(map, has_map, MAP_WIDTH, MAP_HEIGHT)


        

        # Trang trí cho các ô nền để tạo cảm giác ko nhàm chán.
        self.__decorate_map(map, has_map, is_trap, 0.3, MAP_WIDTH, MAP_HEIGHT)
        
        # Giữ map nguyên vẹn bằng cách chuyển map thành tuple.
        map = tuple(tuple(tuple(blocks) for blocks in map[i]) for i in range(len(map)))
        return map, has_map, is_trap, animated_block_positions 
    
    def init_random_map(self, floor_percent: float, smooth_times : int, trap_rate : float, width : int = MAP_WIDTH, height : int = MAP_HEIGHT) -> list[list[int]]:
        has_map = [[0 for i in range(width)] for j in range(height)]
        is_trap = [[0 for i in range(width)] for j in range(height)]
        prim_map = self.init_prim_map(floor_percent, smooth_times, width // 2, height // 2)
        ww, hh = width // 2, height // 2
        for i in range(hh):
            for j in range(ww):
                if (prim_map[i][j] == 1):
                    has_map[i * 2][j * 2] = 1
                    has_map[i * 2 + 1][j * 2] = 1
                    has_map[i * 2][j * 2 + 1] = 1
                    has_map[i * 2 + 1][j * 2 + 1] = 1

        traps = int(ww * hh * trap_rate)
        temp = tuple((i, j) for i in range(ww) for j in range(hh))
        temp = random.sample(temp, traps)
        for x, y in temp:
            if (has_map[y * 2][x * 2]): is_trap[y * 2][x * 2] = 1
            if (has_map[y * 2][x * 2 + 1]): is_trap[y * 2][x * 2 + 1] = 1
            if (has_map[y * 2 + 1][x * 2]): is_trap[y * 2 + 1][x * 2] = 1
            if (has_map[y * 2 + 1][x * 2 + 1]): is_trap[y * 2 + 1][x * 2 + 1] = 1

        return has_map, is_trap
    
    def init_prim_map(self, floor_percent: float, smooth_times : int, width : int, height : int) -> list[list[int]]:
        prim_map = [[0 for i in range(width)] for j in range(height)]
        floors = int(width * height * floor_percent)
        temp = tuple((i, j) for i in range(width) for j in range(height))
        temp = random.sample(temp, floors)
        for i, j in temp:
            prim_map[j][i] = 1
 
        # tạo 1 hình chữ nhật giữa bản đồ, tất cả các ô đều = 1
        ltx, lty = width // 4, height // 4
        w, h = width // 2,  height // 2
        for i in range(ltx, ltx + w):
            for j in range(lty, lty + h):
                prim_map[j][i] = 1
        for i in range(width):
            prim_map[0][i] = 0
            prim_map[height - 1][i] = 0
        for i in range(height):
            prim_map[i][0] = 0
            prim_map[i][width - 1] = 0
        for i in range(smooth_times):
            prim_map = self.__cellular_automata(width, height, prim_map)
        return prim_map

    def __count(self, x : int, y : int, map : list[list[int]]):
        """
        Đếm số lượng ô có giá trị khác 0 xung quanh ô (x, y) trong list 2 chiều map
        """
        count = 0
        HEIGHT = len(map)
        WIDTH = len(map[0])
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if (0 <= x + i < WIDTH) and (0 <= y + j < HEIGHT):
                    if map[y + j][x + i] != 0:
                        count += 1
        return count
        
    def __cellular_automata(self, width, height, map):
        temp_map = [[0 for i in range(width)] for j in range(height)]
        for i in range(width):
            for j in range(height):
                count = self.__count(i, j, map)
                if count <= 3:
                    temp_map[j][i] = 0
                elif count >= 6:
                    temp_map[j][i] = 1
                else: 
                    temp_map[j][i] = map[j][i]
        return temp_map
        
    def __decorate_map(self, map, has_map, is_trap, floor_percent, width, height):
        ww, hh = width // 2, height // 2
        temp = tuple((i, j) for i in range(hh) for j in range(ww))
        temp = random.sample(temp, int(ww * hh * floor_percent))
        for i, j in temp:
            p = random.randint(0, 8)
            if (p == 0):
                if (has_map[i * 2][j * 2] == 1 and is_trap[i * 2][j * 2] == 0 and
                    has_map[i * 2 + 1][j * 2] == 1 and is_trap[i * 2 + 1][j * 2] == 0 and
                    has_map[i * 2][j * 2 + 1] == 1 and is_trap[i * 2][j * 2 + 1] == 0 and
                    has_map[i * 2 + 1][j * 2 + 1] == 1 and is_trap[i * 2 + 1][j * 2 + 1] == 0): 
                        map[i * 2][j * 2][0] = Block(animation.BackgroundAnimation("floor_6", (j * 32 * 2, i * 32 * 2), 1))
                        map[i * 2 + 1][j * 2][0] = Block(animation.BackgroundAnimation("floor_7", (j * 32 * 2, i * 32 * 2 + 32), 1))
                        map[i * 2][j * 2 + 1][0] = Block(animation.BackgroundAnimation("floor_4", (j * 32 * 2 + 32, i * 32 * 2), 1))
                        map[i * 2 + 1][j * 2 + 1][0] = Block(animation.BackgroundAnimation("floor_8", (j * 32 * 2 + 32, i * 32 * 2 + 32), 1))
            else:
                if (has_map[i * 2][j * 2] == 1 and is_trap[i * 2][j * 2] == 0 and
                    has_map[i * 2 + 1][j * 2] == 1 and is_trap[i * 2 + 1][j * 2] == 0 and
                    has_map[i * 2][j * 2 + 1] == 1 and is_trap[i * 2][j * 2 + 1] == 0):
                        map[i * 2][j * 2][0] = Block(animation.BackgroundAnimation("floor_2", (j * 32 * 2, i * 32 * 2), 1))
                        map[i * 2 + 1][j * 2][0] = Block(animation.BackgroundAnimation("floor_5", (j * 32 * 2, i * 32 * 2 + 32), 1))
                        map[i * 2][j * 2 + 1][0] = Block(animation.BackgroundAnimation("floor_3", (j * 32 * 2 + 32, i * 32 * 2), 1))

    def __add_wall_around_map(self, map, has_map, width, height):
        for i in range(width):
            for j in range(height):
                if has_map[j][i] == 0:
                    if (0 <= j + 1 < height and has_map[j + 1][i] == 1):
                        if (0 <= i + 1 < width and has_map[j][i + 1] == 1):
                            map[j][i] = [Block(animation.BackgroundAnimation("wall_corner_front_right", (i * 32, j * 32), 1))]
                            map[j - 1][i].append(Block(animation.BackgroundAnimation("wall_corner_bottom_right", (i * 32, (j - 1) * 32), 1)))
                        elif (0 <= i - 1 < width and has_map[j][i - 1] == 1):
                            map[j][i] = [Block(animation.BackgroundAnimation("wall_corner_front_left", (i * 32, j * 32), 1))]
                            map[j - 1][i].append(Block(animation.BackgroundAnimation("wall_corner_bottom_left", (i * 32, (j - 1) * 32), 1)))
                        else:
                            p = random.randint(0, 100)
                            if (p < 5): map[j][i] = [Block(animation.BackgroundAnimation("wall_hole_1", (i * 32, j * 32), 1))]
                            elif (p < 10): map[j][i] = [Block(animation.BackgroundAnimation("wall_hole_2", (i * 32, j * 32), 1))]
                            else: map[j][i] = [Block(animation.BackgroundAnimation("wall_mid", (i * 32, j * 32), 1))]
                            map[j - 1][i].append(Block(animation.BackgroundAnimation("wall_top_mid", (i * 32, (j - 1) * 32), 1)))
                    if (0 <= j - 1 < height and has_map[j - 1][i]):
                        p = random.randint(0, 100)
                        if (p < 5): map[j][i] = [Block(animation.BackgroundAnimation("wall_hole_1", (i * 32, j * 32), 1))]
                        elif (p < 10): map[j][i] = [Block(animation.BackgroundAnimation("wall_hole_2", (i * 32, j * 32), 1))]
                        else: map[j][i] = [Block(animation.BackgroundAnimation("wall_mid", (i * 32, j * 32), 1))]

                        if has_map[j][i - 1]:
                            map[j - 1][i].append(Block(animation.BackgroundAnimation("wall_corner_top_left", (i * 32, (j - 1) * 32), 1)))
                        elif has_map[j][i + 1]:
                            map[j - 1][i].append(Block(animation.BackgroundAnimation("wall_corner_top_right", (i * 32, (j - 1) * 32), 1)))
                        else:
                            map[j - 1][i].append(Block(animation.BackgroundAnimation("wall_top_mid", (i * 32, (j - 1) * 32), 1)))
                    if (0 <= i + 1 < width and has_map[j][i + 1]):
                        if 0 <= j + 1 < height and has_map[j + 1][i]:
                            pass
                        else:
                            map[j][i].append(Block(animation.BackgroundAnimation("wall_side_mid_left", (i * 32, j * 32), 1)))
                            if not has_map[j + 1][i + 1]:
                                map[j + 1][i].append(Block(animation.BackgroundAnimation("wall_side_front_left", (i * 32, (j + 1) * 32), 1)))
                            if not has_map[j - 1][i + 1]:
                                map[j - 1][i].append(Block(animation.BackgroundAnimation("wall_side_mid_left", (i * 32, (j - 1) * 32), 1)))
                                map[j - 2][i].append(Block(animation.BackgroundAnimation("wall_side_top_left", (i * 32, (j - 2) * 32), 1)))
                    if 0 <= i - 1 < width and has_map[j][i - 1]:
                        if 0 <= j + 1 < height and has_map[j + 1][i]:
                            pass
                        else:
                            map[j][i].append(Block(animation.BackgroundAnimation("wall_side_mid_right", (i * 32, j * 32), 1)))
                            if not has_map[j + 1][i - 1]:
                                map[j + 1][i].append(Block(animation.BackgroundAnimation("wall_side_front_right", (i * 32, (j + 1) * 32), 1)))
                            if not has_map[j - 1][i - 1]:
                                map[j - 1][i].append(Block(animation.BackgroundAnimation("wall_side_mid_right", (i * 32, (j - 1) * 32), 1)))
                                map[j - 2][i].append(Block(animation.BackgroundAnimation("wall_side_top_right", (i * 32, (j - 2) * 32), 1)))
        
        
