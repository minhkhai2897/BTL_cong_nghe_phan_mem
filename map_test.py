import animation



def render_map(screen):
    floor_animation = animation.BackgroundAnimation("floor_2")
    for i in range(100):
        for j in range(60):
            floor_animation.render(screen, (i * floor_animation.get_width(), j * floor_animation.get_height()))