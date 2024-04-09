from ._animation import Animation
from ._sprite import SPRITE

class BackgroundAnimation(Animation):
    def __init__(self, name: str, frame_speed = 0.1):
        """        
        ['edge', 'hole']

        ['column_top', 'column_mid', 'coulmn_base']

        ['doors_all', 'doors_frame_left', 'doors_frame_top', 'doors_frame_righ', 'doors_leaf_closed', 'doors_leaf_open']
        
        ['floor_1', 'floor_2', 'floor_3', 'floor_4', 'floor_5', 'floor_6', 'floor_7', 'floor_8', 'floor_ladder', 'floor_spikes_anim', 'floor_exit', 'floor_spike_disabled', 'floor_spike_enabled', 'floor_spike_out_ani', 'floor_spike_in_ani']
        
        ['wall_top_left', 'wall_top_mid', 'wall_top_right', 'wall_left', 'wall_mid', 'wall_right', 'wall_fountain_top', 'wall_fountain_mid_red_anim', 'wall_fountain_basin_red_anim', 'wall_fountain_mid_blue_anim', 'wall_fountain_basin_blue_anim', 'wall_hole_1', 'wall_hole_2', 'wall_banner_red', 'wall_banner_blue', 'wall_banner_green', 'wall_banner_yellow', 'wall_column_top', 'wall_column_mid', 'wall_coulmn_base', 'wall_goo', 'wall_goo_base',  'wall_side_top_left', 'wall_side_top_right', 'wall_side_mid_left', 'wall_side_mid_right', 'wall_side_front_left', 'wall_side_front_right', 'wall_corner_top_left', 'wall_corner_top_right', 'wall_corner_left', 'wall_corner_right', 'wall_corner_bottom_left', 'wall_corner_bottom_right', 'wall_corner_front_left', 'wall_corner_front_right', 'wall_inner_corner_l_top_left', 'wall_inner_corner_l_top_rigth', 'wall_inner_corner_mid_left', 'wall_inner_corner_mid_rigth', 'wall_inner_corner_t_top_left', 'wall_inner_corner_t_top_rigth']
        """
        state_list = SPRITE.get_backgrounds(name)
        super().__init__(state_list, frame_speed)
        self._name = name

