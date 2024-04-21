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
                'weapons': set(['holy_sword', 'ice_sword']),
            },
            'wizzard_m': {
                'name': 'wizzard_m',
                'max_hp': 100,
                'speed': 1,
                'dame': 1,
                'range': 100,
                'speed_attack': 1,
                'frame_speed': 0.1,
                'weapons': set(['purple_staff']),
            },
            'lizard_m': {
                'name': 'lizard_m',
                'max_hp': 100,
                'speed': 1,
                'dame': 1,
                'range': 100,
                'speed_attack': 1,
                'frame_speed': 0.1,
                'weapons': set(['axe']),
            },
            'elf_m': {
                'name': 'elf_m',
                'max_hp': 100,
                'speed': 1,
                'dame': 1,
                'range': 100,
                'speed_attack': 1,
                'frame_speed': 0.1,
                'weapons': set(['bow']),
            },
            'big_demon': {
                'name': 'big_demon',
                'max_hp': 100,
                'speed': 1,
                'dame': 1,
                'range': 100,
                'speed_attack': 1,
                'frame_speed': 0.1,
                'weapons': set(),
            },
            'ogre': {
                'name': 'ogre',
                'max_hp': 100,
                'speed': 1,
                'dame': 1,
                'range': 100,
                'speed_attack': 1,
                'frame_speed': 0.1,
                'weapons': set(),
            },
            'big_zombie': {
                'name': 'big_zombie',
                'max_hp': 100,
                'speed': 1,
                'dame': 1,
                'range': 100,
                'speed_attack': 1,
                'frame_speed': 0.1,
                'weapons': set(),
            },
            'chort': {
                'name': 'chort',
                'max_hp': 100,
                'speed': 1,
                'dame': 1,
                'range': 100,
                'speed_attack': 1,
                'frame_speed': 0.1,
                'weapons': set(),
            },
            'wogol': {
                'name': 'wogol',
                'max_hp': 100,
                'speed': 1,
                'dame': 1,
                'range': 100,
                'speed_attack': 1,
                'frame_speed': 0.1,
                'weapons': set(),
            },
            'necromancer': {
                'name': 'necromancer',
                'max_hp': 100,
                'speed': 1,
                'dame': 1,
                'range': 100,
                'speed_attack': 1,
                'frame_speed': 0.1,
                'weapons': set(),
            },
            'orc_shaman': {
                'name': 'orc_shaman',
                'max_hp': 100,
                'speed': 1,
                'dame': 1,
                'range': 100,
                'speed_attack': 1,
                'frame_speed': 0.1,
                'weapons': set(),
            },
            'orc_warrior': {
                'name': 'orc_warrior',
                'max_hp': 100,
                'speed': 1,
                'dame': 1,
                'range': 100,
                'speed_attack': 1,
                'frame_speed': 0.1,
                'weapons': set(),
            },
            'masked_orc': {
                'name': 'masked_orc',
                'max_hp': 100,
                'speed': 1,
                'dame': 1,
                'range': 100,
                'speed_attack': 1,
                'frame_speed': 0.1,
                'weapons': set(),
            },
            'ice_zombie': {
                'name': 'ice_zombie',
                'max_hp': 100,
                'speed': 1,
                'dame': 1,
                'range': 100,
                'speed_attack': 1,
                'frame_speed': 0.1,
                'weapons': set(),
            },
            'zombie': {
                'name': 'zombie',
                'max_hp': 100,
                'speed': 1,
                'dame': 1,
                'range': 100,
                'speed_attack': 1,
                'frame_speed': 0.1,
                'weapons': set(),
            },
        }
        
        self.__weapon_info = {            
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
            'attack_up': {
                'name': 'attack_up',
                'frame_speed': 0.1,
                'life_span': 1,
            },
            'blood1': {
                'name': 'blood1',
                'frame_speed': 0.1,
                'life_span': 1,
            },
            'blood2': {
                'name': 'blood2',
                'frame_speed': 0.1,
                'life_span': 1,
            },
            'blood3': {
                'name': 'blood3',
                'frame_speed': 0.1,
                'life_span': 1,
            },
            'blood4': {
                'name': 'blood4',
                'frame_speed': 0.1,
                'life_span': 1,
            },
            'bloodBound': {
                'name': 'bloodBound',
                'frame_speed': 0.1,
                'life_span': 1,
            },
            'clawfx': {
                'name': 'clawfx',
                'frame_speed': 0.1,
                'life_span': 1,
            },
            'clawfx2': {
                'name': 'clawfx2',
                'frame_speed': 0.1,
                'life_span': 1,
            },
            'cross_hit': {
                'name': 'cross_hit',
                'frame_speed': 0.1,
                'life_span': 1,
            },
            'explosion2': {
                'name': 'explosion2',
                'frame_speed': 0.1,
                'life_span': 1,
            },
            'fireball_explosion1': {
                'name': 'fireball_explosion1',
                'frame_speed': 0.1,
                'life_span': 1,
            },
            'golden_cross_hit': {
                'name': 'golden_cross_hit',
                'frame_speed': 0.1,
                'life_span': 1,
            },
            'halo_explosion1': {
                'name': 'halo_explosion1',
                'frame_speed': 0.1,
                'life_span': 1,
            },
            'halo_explosion2': {
                'name': 'halo_explosion2',
                'frame_speed': 0.1,
                'life_span': 1,
            },
            'holy_shield': {
                'name': 'holy_shield',
                'frame_speed': 0.1,
                'life_span': 1,
            },
            'hp_med': {
                'name': 'hp_med',
                'frame_speed': 0.1,
                'life_span': 1,
            },
            'ice': {
                'name': 'ice',
                'frame_speed': 0.1,
                'life_span': 1,
            },
            'iceShatter': {
                'name': 'iceShatter',
                'frame_speed': 0.1,
                'life_span': 1,
            },
            'purple_ball': {
                'name': 'purple_ball',
                'frame_speed': 0.1,
                'life_span': 1,
            },
            'purple_exp': {
                'name': 'purple_exp',
                'frame_speed': 0.1,
                'life_span': 1,
            },
            'shine': {
                'name': 'shine',
                'frame_speed': 0.1,
                'life_span': 1,
            },
            'solidfx': {
                'name': 'solidfx',
                'frame_speed': 0.1,
                'life_span': 1,
            },
            'solid_greenfx': {
                'name': 'solid_greenfx',
                'frame_speed': 0.1,
                'life_span': 1,
            },
            'swordfx': {
                'name': 'swordfx',
                'frame_speed': 0.1,
                'life_span': 1,
            },
            'thunder': {
                'name': 'thunder',
                'frame_speed': 0.1,
                'life_span': 1,
            },
            'thunder_yellow': {
                'name': 'thunder_yellow',
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