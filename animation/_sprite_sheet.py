import pygame
from ._helper import FileReader, ImageProcessor, SCALE_RATIO

class SpriteSheet: 
    def __init__(self):
        self.__characters = {
                "knight_m": ("knight_m_idle_anim", "knight_m_run_anim", "knight_m_hit_anim"),
                "knight_f": ("knight_f_idle_anim", "knight_f_run_anim", "knight_f_hit_anim"),
                "wizzard_m": ("wizzard_m_idle_anim", "wizzard_m_run_anim", "wizzard_m_hit_anim"),
                "wizzard_f": ("wizzard_f_idle_anim", "wizzard_f_run_anim", "wizzard_f_hit_anim"),
                "lizard_m": ("lizard_m_idle_anim", "lizard_m_run_anim", "lizard_m_hit_anim"),
                "lizard_f": ("lizard_f_idle_anim", "lizard_f_run_anim", "lizard_f_hit_anim"),
                "elf_m": ("elf_m_idle_anim", "elf_m_run_anim", "elf_m_hit_anim"),
                "elf_f": ("elf_f_idle_anim", "elf_f_run_anim", "elf_f_hit_anim"),
                "big_demon": ("big_demon_idle_anim", "big_demon_run_anim"),
                "ogre": ("ogre_idle_anim", "ogre_run_anim"),
                "big_zombie": ("big_zombie_idle_anim", "big_zombie_run_anim"),
                "chort": ("chort_idle_anim", "chort_run_anim"),
                "wogol": ("wogol_idle_anim", "wogol_run_anim"),
                "necromancer": ("necromancer_idle_anim", "necromancer_run_anim"),
                "orc_shaman": ("orc_shaman_idle_anim", "orc_shaman_run_anim"),
                "orc_warrior": ("orc_warrior_idle_anim", "orc_warrior_run_anim"),
                "masked_orc": ("masked_orc_idle_anim", "masked_orc_run_anim"),
                "ice_zombie": ("ice_zombie_idle_anim", "ice_zombie_run_anim"),
                "zombie": ("zombie_idle_anim", "zombie_run_anim"),
                "swampy": ("swampy_idle_anim", "swampy_run_anim"),
                "muddy": ("muddy_idle_anim", "muddy_run_anim"),
                "skelet": ("skelet_idle_anim", "skelet_run_anim"),
                "imp": ("imp_idle_anim", "imp_run_anim"),
                "goblin": ("goblin_idle_anim", "goblin_run_anim"),
                "tiny_zombie": ("tiny_zombie_idle_anim", "tiny_zombie_run_anim")
            }
        
        self.__weapons = {
            "knife": ("weapon_knife",),
            "rusty_sword": ("weapon_rusty_sword",),
            "regular_sword": ("weapon_regular_sword",),
            "red_gem_sword": ("weapon_red_gem_sword",),
            "big_hammer": ("weapon_big_hammer",),
            "hammer": ("weapon_hammer",),
            "baton_with_spikes": ("weapon_baton_with_spikes",),
            "mace": ("weapon_mace",),
            "katana": ("weapon_katana",),
            "saw_sword": ("weapon_saw_sword",),
            "anime_sword": ("weapon_anime_sword",),
            "axe": ("weapon_axe",),
            "machete": ("weapon_machete",),
            "cleaver": ("weapon_cleaver",),
            "duel_sword": ("weapon_duel_sword",),
            "knight_sword": ("weapon_knight_sword",),
            "golden_sword": ("weapon_golden_sword",),
            "lavish_sword": ("weapon_lavish_sword",),
            "red_magic_staff": ("weapon_red_magic_staff",),
            "green_magic_staff": ("weapon_green_magic_staff",),
            "spear": ("weapon_spear",),
            "purple_staff": ("weapon_purple_staff",),
            "thunder_staff": ("weapon_thunder_staff",),
            "bow": ("weapon_bow",),
            "holy_sword": ("weapon_holy_sword",),
            "fire_sword": ("weapon_fire_sword",),
            "ice_sword": ("weapon_ice_sword",),
            "grass_sword": ("weapon_grass_sword",),
            "iron_sword": ("weapon_iron_sword",),
        }

        self.__effects = {
            "attack_up" : ("attack_up",),
            "blood1" : ("blood1",),
            "blood2" : ("blood2",),
            "blood3" : ("blood3",),
            "blood4" : ("blood4",),
            "bloodBound" : ("BloodBound",),
            "clawfx" : ("ClawFx",),
            "clawfx2" : ("ClawFx2",),
            "cross_hit" : ("cross_hit",),
            "explosion2" : ("explosion-2",),
            "fireball_explosion1" : ("fireball_explosion1",),
            "golden_cross_hit" : ("golden_cross_hit",),
            "halo_explosion1" : ("halo_explosion1",),
            "halo_explosion2" : ("halo_explosion2",),
            "holy_shield" : ("HolyShield",),
            "hp_med" : ("HpMed",),
            "ice" : ("Ice",),
            "iceShatter" : ("IceShatter",),
            "purple_ball" : ("purple_ball",),
            "purple_exp" : ("purple_exp",),
            "shine" : ("Shine",),
            "solidfx" : ("SolidFx",),
            "solid_greenfx" : ("SolidGreenFx",),
            "swordfx" : ("SwordFx",),
            "thunder" : ("Thunder",),
            "thunder_yellow" : ("Thunder_Yellow",),
        }

        self.__bullets = {
            "arrow": ("arrow",),
            "axe": ("Axe",),
            "fireball": ("fireball",),
            "ice_pick": ("IcePick",),
        }

        self.__items = {
            "chest_empty_open_anim": ("chest_empty_open_anim",),
            "chest_full_open_anim": ("chest_full_open_anim",),
            "chest_mimic_open_anim": ("chest_mimic_open_anim",),
            "flask_big_red": ("flask_big_red",),
            "flask_big_blue": ("flask_big_blue",),
            "flask_big_green": ("flask_big_green",),
            "flask_big_yellow": ("flask_big_yellow",),
            "flask_red": ("flask_red",),
            "flask_blue": ("flask_blue",),
            "flask_green": ("flask_green",),
            "flask_yellow": ("flask_yellow",),
            "skull": ("skull",),
            "crate": ("crate",),
            "coin_anim": ("coin_anim",),
            "ui_heart_full": ("ui_heart_full",),
            "ui_heart_half": ("ui_heart_half",),
            "ui_heart_empty": ("ui_heart_empty",),
        }

        self.__backgrounds = {
            "wall_top_left": ("wall_top_left",),
            "wall_top_mid": ("wall_top_mid",),
            "wall_top_right": ("wall_top_right",),
            "wall_left": ("wall_left",),
            "wall_mid": ("wall_mid",),
            "wall_right": ("wall_right",),
            "wall_fountain_top": ("wall_fountain_top",),
            "wall_fountain_mid_red_anim": ("wall_fountain_mid_red_anim",),
            "wall_fountain_basin_red_anim": ("wall_fountain_basin_red_anim",),
            "wall_fountain_mid_blue_anim": ("wall_fountain_mid_blue_anim",),
            "wall_fountain_basin_blue_anim": ("wall_fountain_basin_blue_anim",),
            "wall_hole_1": ("wall_hole_1",),
            "wall_hole_2": ("wall_hole_2",),
            "wall_banner_red": ("wall_banner_red",),
            "wall_banner_blue": ("wall_banner_blue",),
            "wall_banner_green": ("wall_banner_green",),
            "wall_banner_yellow": ("wall_banner_yellow",),
            "column_top": ("column_top",),
            "column_mid": ("column_mid",),
            "coulmn_base": ("coulmn_base",),
            "wall_column_top": ("wall_column_top",),
            "wall_column_mid": ("wall_column_mid",),
            "wall_coulmn_base": ("wall_coulmn_base",),
            "wall_goo": ("wall_goo",),
            "wall_goo_base": ("wall_goo_base",),
            "floor_1": ("floor_1",),
            "floor_2": ("floor_2",),
            "floor_3": ("floor_3",),
            "floor_4": ("floor_4",),
            "floor_5": ("floor_5",),
            "floor_6": ("floor_6",),
            "floor_7": ("floor_7",),
            "floor_8": ("floor_8",),
            "floor_ladder": ("floor_ladder",),
            "floor_spikes_anim": ("floor_spikes_anim",),
            "wall_side_top_left": ("wall_side_top_left",),
            "wall_side_top_right": ("wall_side_top_right",),
            "wall_side_mid_left": ("wall_side_mid_left",),
            "wall_side_mid_right": ("wall_side_mid_right",),
            "wall_side_front_left": ("wall_side_front_left",),
            "wall_side_front_right": ("wall_side_front_right",),
            "wall_corner_top_left": ("wall_corner_top_left",),
            "wall_corner_top_right": ("wall_corner_top_right",),
            "wall_corner_left": ("wall_corner_left",),
            "wall_corner_right": ("wall_corner_right",),
            "wall_corner_bottom_left": ("wall_corner_bottom_left",),
            "wall_corner_bottom_right": ("wall_corner_bottom_right",),
            "wall_corner_front_left": ("wall_corner_front_left",),
            "wall_corner_front_right": ("wall_corner_front_right",),
            "wall_inner_corner_l_top_left": ("wall_inner_corner_l_top_left",),
            "wall_inner_corner_l_top_rigth": ("wall_inner_corner_l_top_rigth",),
            "wall_inner_corner_mid_left": ("wall_inner_corner_mid_left",),
            "wall_inner_corner_mid_rigth": ("wall_inner_corner_mid_rigth",),
            "wall_inner_corner_t_top_left": ("wall_inner_corner_t_top_left",),
            "wall_inner_corner_t_top_rigth": ("wall_inner_corner_t_top_rigth",),
            "edge": ("edge",),
            "hole": ("hole",),
            "doors_all": ("doors_all",),
            "doors_frame_left": ("doors_frame_left",),
            "doors_frame_top": ("doors_frame_top",),
            "doors_frame_righ": ("doors_frame_righ",),
            "doors_leaf_closed": ("doors_leaf_closed",),
            "doors_leaf_open": ("doors_leaf_open",),
            "floor_exit": ("floor_exit",),
            "floor_spike_disabled": ("floor_spike_disabled",),
            "floor_spike_enabled": ("floor_spike_enabled",),
            "floor_spike_out_ani": ("floor_spike_out_ani",),
            "floor_spike_in_ani": ("floor_spike_in_ani",),
        }
        
    def get_characters(self):
        characters_states = {}
        for key, value in self.__characters.items():
            characters_states[key] = []
            for state in value:
                characters_states[key].append(state + "_right")
                characters_states[key].append(state + "_left")
            characters_states[key] = tuple(characters_states[key])
        return characters_states
    
    def get_weapons(self):
        characters_states = {}
        for key, value in self.__weapons.items():
            characters_states[key] = []
            for state in value:
                characters_states[key].append(state + "_right")
                characters_states[key].append(state + "_left")
            characters_states[key] = tuple(characters_states[key])
        return characters_states
    
    def get_effects(self):
        return self.__effects
    
    def get_bullets(self):
        return self.__bullets

    def get_items(self):
        return self.__items
    
    def get_backgrounds(self):
        return self.__backgrounds

    def extract_images_from_file(self, path: str):
        lines = FileReader.read_line(path)
        lines = [line.split(" ") for line in lines]
        image = pygame.image.load(path + ".png")
        images = {}
        for line in lines:
            images[line[0]] = []
            for i in range(int(line[5])):
                images[line[0]].append(image.subsurface((int(line[1]) + i * int(line[3]), int(line[2]), int(line[3]), int(line[4]))))
            images[line[0]] = tuple(images[line[0]])
        return images

    def extract_images_from_files(self, path: str):
        lines = FileReader.read_line(path)
        dict_images = {}
        for line in lines:
            mini_dict_images = self.extract_images_from_file(line)
            dict_images.update(mini_dict_images)
        return dict_images

    def extract_images_from_files_and_process(self, path: str):
        dict_images = self.extract_images_from_files(path)
        for states in self.__characters.values():
            for state in states:
                dict_images[state + "_right"] = ImageProcessor.process_images(dict_images[state], flip=False, scaled=SCALE_RATIO, angle=0)
                dict_images[state + "_left"] = ImageProcessor.process_images(dict_images[state], flip=True, scaled=SCALE_RATIO, angle=0)
                dict_images.pop(state)
        
        for states in self.__weapons.values():
            for state in states:
                dict_images[state + "_right"] = ImageProcessor.process_images(dict_images[state], flip=False, scaled=SCALE_RATIO, angle=0)
                dict_images[state + "_left"] = ImageProcessor.process_images(dict_images[state], flip=True, scaled=SCALE_RATIO, angle=0)
                dict_images.pop(state)

        for states in self.__effects.values():
            for state in states:
                dict_images[state] = ImageProcessor.process_images(dict_images[state], flip=False, scaled=SCALE_RATIO, angle=0)

        for states in self.__bullets.values():
            for state in states:
                dict_images[state] = ImageProcessor.process_images(dict_images[state], flip=False, scaled=SCALE_RATIO, angle=0)

        for states in self.__items.values():
            for state in states:
                dict_images[state] = ImageProcessor.process_images(dict_images[state], flip=False, scaled=SCALE_RATIO, angle=0)

        for states in self.__backgrounds.values():
            for state in states:
                dict_images[state] = ImageProcessor.process_images(dict_images[state], flip=False, scaled=SCALE_RATIO, angle=0)
        
        return dict_images
    