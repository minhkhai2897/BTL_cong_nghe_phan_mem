import animation
from helper import MAP_WIDTH, MAP_HEIGHT


# map: 45 x 28

has_map = [[0 for i in range(MAP_WIDTH)] for j in range(MAP_HEIGHT)]


def render_map(screen):
    floor_animation = animation.BackgroundAnimation("floor_2")
    for i in range(MAP_WIDTH):
        for j in range(MAP_HEIGHT):
            floor_animation.render(screen, (i * floor_animation.get_width(), j * floor_animation.get_height()))