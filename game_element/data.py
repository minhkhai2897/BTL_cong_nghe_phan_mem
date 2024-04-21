class Data:
    def __init__(self):
        

        self.__character_info = {
            'knight_m': {
                'name': 'knight_m',
                'max_hp': 100,
                'speed': 1,
                'dame': 1,
                'range': 100,
                'speed_attack': 1,
                'frame_speed': 0.1,
            },
            'wizzard_m': {
                'name': 'wizzard_m',
                'max_hp': 100,
                'speed': 1,
                'dame': 1,
                'range': 100,
                'speed_attack': 1,
                'frame_speed': 0.1,
            },
            'lizard_m': {
                'name': 'lizard_m',
                'max_hp': 100,
                'speed': 1,
                'dame': 1,
                'range': 100,
                'speed_attack': 1,
                'frame_speed': 0.1,
            },
            'elf_m': {
                'name': 'elf_m',
                'max_hp': 100,
                'speed': 1,
                'dame': 1,
                'range': 100,
                'speed_attack': 1,
                'frame_speed': 0.1,
            },
            'big_demon': {
                'name': 'big_demon',
                'max_hp': 100,
                'speed': 1,
                'dame': 1,
                'range': 100,
                'speed_attack': 1,
                'frame_speed': 0.1,
            },
            'ogre': {
                'name': 'ogre',
                'max_hp': 100,
                'speed': 1,
                'dame': 1,
                'range': 100,
                'speed_attack': 1,
                'frame_speed': 0.1,
            },
            'big_zombie': {
                'name': 'big_zombie',
                'max_hp': 100,
                'speed': 1,
                'dame': 1,
                'range': 100,
                'speed_attack': 1,
                'frame_speed': 0.1,
            },
            'chort': {
                'name': 'chort',
                'max_hp': 100,
                'speed': 1,
                'dame': 1,
                'range': 100,
                'speed_attack': 1,
                'frame_speed': 0.1,
            },
            'wogol': {
                'name': 'wogol',
                'max_hp': 100,
                'speed': 1,
                'dame': 1,
                'range': 100,
                'speed_attack': 1,
                'frame_speed': 0.1,
            },
            'necromancer': {
                'name': 'necromancer',
                'max_hp': 100,
                'speed': 1,
                'dame': 1,
                'range': 100,
                'speed_attack': 1,
                'frame_speed': 0.1,
            },
            'orc_shaman': {
                'name': 'orc_shaman',
                'max_hp': 100,
                'speed': 1,
                'dame': 1,
                'range': 100,
                'speed_attack': 1,
                'frame_speed': 0.1,
            },
            'orc_warrior': {
                'name': 'orc_warrior',
                'max_hp': 100,
                'speed': 1,
                'dame': 1,
                'range': 100,
                'speed_attack': 1,
                'frame_speed': 0.1,
            },
            'masked_orc': {
                'name': 'masked_orc',
                'max_hp': 100,
                'speed': 1,
                'dame': 1,
                'range': 100,
                'speed_attack': 1,
                'frame_speed': 0.1,
            },
            'ice_zombie': {
                'name': 'ice_zombie',
                'max_hp': 100,
                'speed': 1,
                'dame': 1,
                'range': 100,
                'speed_attack': 1,
                'frame_speed': 0.1,
            },
            'zombie': {
                'name': 'zombie',
                'max_hp': 100,
                'speed': 1,
                'dame': 1,
                'range': 100,
                'speed_attack': 1,
                'frame_speed': 0.1,
            },
        }
        
        self.__weapon_info = {
        # ['knife', 'rusty_sword', 'regular_sword', 'red_gem_sword', 'big_hammer', 'hammer', 'baton_with_spikes', 'mace', 'katana', 'saw_sword', 'anime_sword', 'axe', 'machete', 'cleaver', 'duel_sword', 'knight_sword', 'golden_sword', 'lavish_sword', 'red_magic_staff', 'green_magic_staff', 'spear', 'purple_staff', 'thunder_staff', 'bow', 'holy_sword', 'fire_sword', 'ice_sword', 'grass_sword', 'iron_sword']
            'sword': {
                'name': 'sword',
                'dame': 10,
                'range': 10,
                'speed_attack': 1,
                'frame_speed': 0.1,
            },
            'axe': {
                'name': 'axe',
                'dame': 20,
                'range': 10,
                'speed_attack': 1,
                'frame_speed': 0.1,
            },
            'bow': {
                'name': 'bow',
                'dame': 30,
                'range': 10,
                'speed_attack': 1,
                'frame_speed': 0.1,
            },
            'ice_sword': {
                'name': 'ice_sword',
                'dame': 40,
                'range': 10,
                'speed_attack': 1,
                'frame_speed': 0.1,
            },
            'holy_sword': {
                'name': 'holy_sword',
                'dame': 50,
                'range': 10,
                'speed_attack': 1,
                'frame_speed': 0.1,
            },
            'purple_staff': {
                'name': 'purple_staff',
                'dame': 60,
                'range': 10,
                'speed_attack': 1,
                'frame_speed': 0.1,
            },
        }

        self.__item_info = {}

        self.__effect_info = {
        # ['attack_up', 'blood1', 'blood2', 'blood3', 'blood4', 'bloodBound', 'clawfx', 'clawfx2', 'cross_hit', 'explosion2', 'fireball_explosion1', 'golden_cross_hit', 'halo_explosion1', 'halo_explosion2', 'holy_shield', 'hp_med', 'ice', 'iceShatter', 'purple_ball', 'purple_exp', 'shine', 'solidfx', 'solid_greenfx', 'swordfx', 'thunder', 'thunder_yellow']
            'attack_up': {
                'name': 'attack_up',
                'frame_speed': 0.1,
                'life_span': 1,
                
            },
        }

        self.__background_info = {
            'floor_1': {
                'name': 'floor_1',
                'frame_speed': 0.1,
            },
            'floor_2': {
                'name': 'floor_2',
                'frame_speed': 0.1,
            },
            'floor_3': {
                'name': 'floor_3',
                'frame_speed': 0.1,
            },
            'floor_4': {
                'name': 'floor_4',
                'frame_speed': 0.1,
            },
            'floor_5': {
                'name': 'floor_5',
                'frame_speed': 0.1,
            },
            'floor_6': {
                'name': 'floor_6',
                'frame_speed': 0.1,
            },
            'floor_7': {
                'name': 'floor_7',
                'frame_speed': 0.1,
            },
            'floor_8': {
                'name': 'floor_8',
                'frame_speed': 0.1,
            },
            'wall_corner_front_right': {
                'name': 'wall_corner_front_right',
                'frame_speed': 0.1,
            },
            'wall_corner_bottom_right': {
                'name': 'wall_corner_bottom_right',
                'frame_speed': 0.1,
            },
            'wall_corner_front_left': {
                'name': 'wall_corner_front_left',
                'frame_speed': 0.1,
            },
            'wall_corner_bottom_left': {
                'name': 'wall_corner_bottom_left',
                'frame_speed': 0.1,
            },
            'wall_hole_1': {
                'name': 'wall_hole_1',
                'frame_speed': 0.1,
            },
            'wall_hole_2': {
                'name': 'wall_hole_2',
                'frame_speed': 0.1,
            },
            'wall_mid': {
                'name': 'wall_mid',
                'frame_speed': 0.1,
            },
            'wall_top_mid': {
                'name': 'wall_top_mid',
                'frame_speed': 0.1,
            },
            'wall_corner_top_left': {
                'name': 'wall_corner_top_left',
                'frame_speed': 0.1,
            },
            'wall_corner_top_right': {
                'name': 'wall_corner_top_right',
                'frame_speed': 0.1,
            },
            'wall_side_mid_left': {
                'name': 'wall_side_mid_left',
                'frame_speed': 0.1,
            },
            'wall_side_front_left': {
                'name': 'wall_side_front_left',
                'frame_speed': 0.1,
            },
            'wall_side_top_left': {
                'name': 'wall_side_top_left',
                'frame_speed': 0.1,
            },
            'wall_side_mid_right': {
                'name': 'wall_side_mid_right',
                'frame_speed': 0.1,
            },
            'wall_side_front_right': {
                'name': 'wall_side_front_right',
                'frame_speed': 0.1,
            },
            'wall_side_top_right': {
                'name': 'wall_side_top_right',
                'frame_speed': 0.1,
            },
            'floor_spikes_anim': {
                'name': 'floor_spikes_anim',
                'frame_speed': 0.5,
            },
        }

        self.__bullet_info = {

        }

    def get_character_info(self, name):
        return self.__character_info[name]
    
    def get_weapon_info(self, name):
        return self.__weapon_info[name]
    
    def get_item_info(self, name):
        return self.__item_info[name]
    
    def get_effect_info(self, name):
        return self.__effect_info[name]
    
    def get_background_info(self, name):
        return self.__background_info[name]
    
    def get_bullet_info(self, name):
        return self.__bullet_info[name]
    
DATA = Data()