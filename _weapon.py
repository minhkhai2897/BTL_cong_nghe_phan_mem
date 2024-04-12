##221

import _helper_for_weapon

class WeaponType:
    def __init__(self):
        WEAPON_SWORD_POINT = 0
        WEAPON_SWORD_RANGE = 1
        WEAPON_GUN_RANGE = 2
        WEAPON_GUN_POINT = 3
        WEAPON_GUN_POINT_MULTI = 4

class WeaponBuff:
    def __init__(self):
        self._chance = 0.0
        self._duration = 0
    
class Weapon:
    def __init__(self, wp: WeaponType):
        self._wp = wp
        self._shooting_range = 0
        self._effect_range = 0
        self._damage = 0
        self._gap = 0
        self._bullet_speed = 0