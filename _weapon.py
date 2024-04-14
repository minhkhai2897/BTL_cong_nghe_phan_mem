##221
from animation import _animation, _weapon_animation
import _helper_for_weapon

class WeaponType:
    def __init__(self):
        WEAPON_SWORD_POINT = 0
        WEAPON_SWORD_RANGE = 1
        WEAPON_GUN_RANGE = 2
        WEAPON_GUN_POINT = 3
        WEAPON_GUN_POINT_MULTI = 4

class WeaponBuff:
    def __init__(self,chance: float, duration: int):
        self._chance = chance
        self._duration = duration
    
class Weapon:
    def __init__(self, weapon: WeaponType, birth_texture_id: int, death_texture_id: int, fly_texture_id: int):
        self._weapon = weapon
        self._shooting_range = 0
        self._effect_range = 0
        self.__damage = 0
        self.__gap = 0
        self._bullet_speed = 0
        self._birth_animation = _animation()
        self._death_animation = _animation()
        self._fly_animation   = _animation()
        self._set_animation_for_weapon(birth_texture_id, death_texture_id, fly_texture_id)
        self._birth_audio = 0
        self._death_audio = 0
        self._effect = WeaponBuff()

    def _set_animation_for_weapon(self, birth_texture_id: int, death_texture_id: int, fly_texture_id: int):

        if birth_texture_id != -1:
            birth_animation = _weapon_animation()
        
        if death_texture_id != -1:
            death_animation = _weapon_animation()

        if fly_texture_id != -1:
            fly_animation = _weapon_animation()
        
        self._weapon = WeaponType.WEAPON_SWORD_POINT
        self._shooting_range = 32 * 2
        self._effect_range = 40
        self.__damage = 10
        self.__gap = 60
        self._bullet_speed = 6
        self._birth_animation = birth_animation
        self._death_animation = death_animation
        self._fly_animation = fly_animation
        self._birth_audio = -1
        self._death_audio = _helper_for_weapon.AUDIO_CLAW_HIT


    def _init_weapons(self):
        self.__init__(weapons[_helper_for_weapon.WEAPON_SWORD], -1, _helper_for_weapon.RES_SwordFx, -1)
        self._damage = 30
        self._shooting_range = 32 * 3
        self._death_animation.scaled = false
        self._death_animation.angle = -1
        self.deathAudio = _helper_for_weapon.AUDIO_SWORD_HIT

        self.__init__(weapons[_helper_for_weapon.WEAPON_MONSTER_CLAW], -1, _helper_for_weapon.RES_CLAWFX2, -1)
        self._weapon = WeaponType.WEAPON_SWORD_RANGE
        self._shooting_range = 32 * 3 + 16
        self._damage = 24
        self._death_animation.angle = -1
        self._death_animation.at = AT_CENTER
        self.deathAudio = _helper_for_weapon.AUDIO_CLAW_HIT_HEAVY

        self.__init__(weapons[_helper_for_weapon.WEAPON_FIREBALL], _helper_for_weapon.RES_Shine, _helper_for_weapon.RES_HALO_EXPLOSION1,
                    _helper_for_weapon.RES_FIREBALL)
        self._weapon = WeaponType.WEAPON_GUN_RANGE
        self._damage = 45
        self._effect_change = 50
        self._shooting_range = 256
        self._gap = 180
        self._death_animation.angle = -1
        self._death_animation.at = AT_CENTER
        self._birth_animation.duration = 24
        self.birthAudio = _helper_for_weapon.AUDIO_SHOOT
        self.deathAudio = _helper_for_weapon.AUDIO_FIREBALL_EXP

        self.__init__(weapons[_helper_for_weapon.WEAPON_THUNDER], _helper_for_weapon.RES_BLOOD_BOUND, _helper_for_weapon.RES_Thunder, -1)
        self._weapon = WeaponType.WEAPON_SWORD_RANGE
        self._damage = 80
        self._shooting_range = 128
        self._gap = 120
        self._death_animation.angle = -1
        self._death_animation.scaled = false
        self.deathAudio = _helper_for_weapon.AUDIO_THUNDER

        self.__init__(weapons[_helper_for_weapon.WEAPON_THUNDER_STAFF], -1, _helper_for_weapon.RES_THUNDER_YELLOW, -1)
        self._weapon = WeaponType.WEAPON_SWORD_RANGE
        self._damage = 50
        self._shooting_range = 128
        self._gap = 120
        self._death_animation.angle = -1
        self._death_animation.scaled = false
        self.deathAudio = _helper_for_weapon.AUDIO_THUNDER

        self.__init__(weapons[_helper_for_weapon.WEAPON_ARROW], -1, _helper_for_weapon.RES_HALO_EXPLOSION2, _helper_for_weapon.RES_ARROW)
        self._weapon = WeaponType.WEAPON_GUN_POINT
        self._gap = 40
        self._damage = 10
        self._shooting_range = 200
        self.bulletSpeed = 10
        self._death_animation.angle = -1
        self._death_animation.at = AT_CENTER
        self.flyAni.scaled = false
        self.birthAudio = _helper_for_weapon.AUDIO_LIGHT_SHOOT
        self.deathAudio = _helper_for_weapon.AUDIO_ARROW_HIT

        self.__init__(weapons[_helper_for_weapon.WEAPON_POWERFUL_BOW], -1, _helper_for_weapon.RES_HALO_EXPLOSION2,
                    _helper_for_weapon.RES_ARROW)
        self._weapon = WeaponType.WEAPON_GUN_POINT
        self._gap = 60
        self._damage = 25
        self._shooting_range = 320
        self.bulletSpeed = 7
        self._death_animation.angle = -1
        self._death_animation.at = AT_CENTER
        self.birthAudio = _helper_for_weapon.AUDIO_LIGHT_SHOOT
        self.deathAudio = _helper_for_weapon.AUDIO_ARROW_HIT
        self._effects[_helper_for_weapon.BUFF_ATTACK] = WeaponBuff.__init__(0.5, 240)

        self.__init__(weapons[_helper_for_weapon.WEAPON_MONSTER_CLAW2], -1, _helper_for_weapon.RES_CLAWFX, -1)

        self.__init__(weapons[_helper_for_weapon.WEAPON_THROW_AXE], -1, _helper_for_weapon.RES_CROSS_HIT, _helper_for_weapon.RES_AXE)
        self._weapon = WeaponType.WEAPON_GUN_POINT
        self._damage = 12
        self._shooting_range = 160
        self.bulletSpeed = 10
        self.flyAni.duration = 24
        self.flyAni.angle = -1
        self.flyAni.scaled = false
        self._death_animation.scaled = false
        self._death_animation.at = AT_CENTER
        self.birthAudio = _helper_for_weapon.AUDIO_LIGHT_SHOOT
        self.deathAudio = _helper_for_weapon.AUDIO_ARROW_HIT

        self.__init__(weapons[_helper_for_weapon.WEAPON_MANY_AXES], -1, _helper_for_weapon.RES_CROSS_HIT, _helper_for_weapon.RES_AXE)
        self._weapon = WeaponType.WEAPON_GUN_POINT_MULTI
        self._shooting_range = 180
        self._gap = 70
        self._effect_change = 50
        self._damage = 50
        self.bulletSpeed = 4
        self.flyAni.duration = 24
        self.flyAni.angle = -1
        self._death_animation.at = AT_CENTER
        self.birthAudio = _helper_for_weapon.AUDIO_LIGHT_SHOOT
        self.deathAudio = _helper_for_weapon.AUDIO_ARROW_HIT

        self.__init__(weapons[_helper_for_weapon.WEAPON_SOLID], -1, _helper_for_weapon.RES_SOLIDFX, -1)
        self._death_animation.scaled = false
        self._death_animation.angle = -1
        self._effects[_helper_for_weapon.BUFF_SLOWDOWN] = WeaponBuff.__init__(0.3, 180)

        self.__init__(weapons[_helper_for_weapon.WEAPON_SOLID_GREEN], -1, _helper_for_weapon.RES_SOLID_GREENFX, -1)
        self._shooting_range = 96
        self._death_animation.scaled = false
        self._death_animation.angle = -1
        self._effects[_helper_for_weapon.BUFF_SLOWDOWN] = WeaponBuff.__init__(0.3, 180)

        self.__init__(weapons[_helper_for_weapon.WEAPON_SOLID_CLAW], -1, _helper_for_weapon.RES_SOLID_GREENFX, -1)
        self._weapon = WeaponType.WEAPON_SWORD_RANGE
        self._shooting_range = 32 * 3 + 16
        self._damage = 35
        self._death_animation.scaled = false
        self._death_animation.angle = -1
        self.deathAudio = _helper_for_weapon.AUDIO_CLAW_HIT_HEAVY
        self._effects[_helper_for_weapon.BUFF_SLOWDOWN] = WeaponBuff.__init__(0.7, 60)
        self.__init__(weapons[_helper_for_weapon.WEAPON_ICEPICK], -1, _helper_for_weapon.RES_ICESHATTER, _helper_for_weapon.RES_ICEPICK)
        self._weapon = WeaponType.WEAPON_GUN_RANGE
        self._damage = 30
        self._effect_change = 50
        self._shooting_range = 256
        self._gap = 180
        self.bulletSpeed = 8
        self._death_animation.angle = -1
        self.flyAni.scaled = false
        self._death_animation.at = AT_CENTER
        self._effects[_helper_for_weapon.BUFF_FROZEN] = WeaponBuff.__init__(0.2, 60)        
        self.birthAudio = _helper_for_weapon.AUDIO_ICE_SHOOT
        self.__init__(weapons[_helper_for_weapon.WEAPON_PURPLE_BALL], -1, _helper_for_weapon.RES_PURPLE_EXP, _helper_for_weapon.RES_PURPLE_BALL)
        self._weapon = WeaponType.WEAPON_GUN_RANGE
        self._damage = 20
        self._effect_change = 50
        self._shooting_range = 256
        self._gap = 100
        self.bulletSpeed = 6
        self._death_animation.angle = -1
        self._death_animation.scaled = false
        self.flyAni.scaled = false
        self._death_animation.at = AT_CENTER
        self.birthAudio = _helper_for_weapon.AUDIO_ICE_SHOOT
        self.deathAudio = _helper_for_weapon.AUDIO_ARROW_HIT

        self.__init__(weapons[_helper_for_weapon.WEAPON_PURPLE_STAFF], -1, _helper_for_weapon.RES_PURPLE_EXP, _helper_for_weapon.RES_PURPLE_BALL)
        self._weapon = WeaponType.WEAPON_GUN_POINT_MULTI
        self._damage = 45
        self._effect_change = 50
        self._shooting_range = 256
        self._gap = 100
        self.bulletSpeed = 7
        self._death_animation.angle = -1
        self._death_animation.scaled = false
        self.flyAni.scaled = false
        self._death_animation.at = AT_CENTER
        self.birthAudio = _helper_for_weapon.AUDIO_ICE_SHOOT
        self.deathAudio = _helper_for_weapon.AUDIO_ARROW_HIT

        self.__init__(weapons[_helper_for_weapon.WEAPON_HOLY_SWORD], -1, _helper_for_weapon.RES_GOLDEN_CROSS_HIT, -1)
        self._weapon = WeaponType.WEAPON_SWORD_RANGE
        self._damage = 30
        self._shooting_range = 32 * 4
        self._effects[_helper_for_weapon.BUFF_DEFFENCE] = WeaponBuff.__init__(0.6, 180)

        self.__init__(weapons[_helper_for_weapon.WEAPON_ICE_SWORD], -1, _helper_for_weapon.RES_ICESHATTER, -1)
        self._weapon = WeaponType.WEAPON_SWORD_RANGE
        self.._shooting_range = 32 * 3 + 16
        self.__damage = 80
        self.__gap = 30
        self._death_animation.angle = -1
        self._death_animation.at = AT_CENTER
        self._effects[_helper_for_weapon.BUFF_FROZEN] = WeaponBuff.__init__(0.6, 80)
        self._deathAudio = _helper_for_weapon.AUDIO_SWORD_HIT