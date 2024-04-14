import pygame
import player, sprite, ai, bullet, helper, map, net, render, res, weapon, types, audio
from types import Texture, LinkList, Effect, Weapon, Sprite, Animation, Block, Point
Item, Snake, Score, Direction, LinkNode
from player import Snake
import random 
import time
import pygame
import math
from enum import Enum

# from player import *
# from sprite import *
# from types import *
# from ai import *
# from bullet import *
# from helper import *
# from map import *
# from net import *
# from render import *
# from res import *
# from sprite import *
# from types import *
# from weapon import *
# ----------------------------------------------
# file constants
# Snake Game Constants
SPRITES_MAX_NUM = 1024
KEYPRESS_DELTA = 17
MAX_PLAYERS_NUM = 2

# Game Constants
# Spike
SPIKE_TIME_MASK = 600
SPIKE_OUT_INTERVAL = 120
SPIKE_ANI_DURATION = 20
SPRITE_EFFECT_DELTA = 20
# Bounder Box
BIG_SPRITE_EFFECT_DELTA = 25
SPRITE_EFFECT_VERTICAL_DELTA = 6
SPRITE_EFFECT_FEET = 12
GAME_BULLET_EFFECTIVE = 16
# Team
GAME_MONSTERS_TEAM = 9
# Buff
GAME_HP_MEDICINE_DELTA = 55
GAME_HP_MEDICINE_EXTRA_DELTA = 33
GAME_MAP_RELOAD_PERIOD = 120
GAME_BUFF_ATTACK_K = 2.5
GAME_BUFF_DEFENSE_K = 2
GAME_FROZEN_DAMAGE_K = 0.1

#----------------------------------------------
# External Constants
SCALE_FACTOR: int = render.SCALE_FACTOR  #render.c
n: int = res.n         #res.c
m: int = res.m      #res.c                       
MOVE_STEP: int = 2     #game.c

# External Arrays
textures: Texture = res.textures  #res.c
animationsList: LinkList = render.animationsList  #render.c
effects: Effect = res.effects  #res.c
weapons: Weapon = weapon.weapons  #weapon.c
commonSprites: Sprite = sprite.commonSprites  #sprite.c

# External Variables
renderFrames: int = render.renderFrames  #render.c

# Map
MAP_SIZE = map.MAP_SIZE
map: list[list[Block]] = [[0]*MAP_SIZE for _ in range(MAP_SIZE)]  
itemMap: list[list[Item]] = [[0]*MAP_SIZE for _ in range(MAP_SIZE)]  
hasMap = map.hasMap #map.c
hasEnemy: list[list[bool]] = [[0]*MAP_SIZE for _ in range(MAP_SIZE)]  
spikeDamage: int= 1

# Sprite
spriteSnake: list[Snake] = [0] * SPRITES_MAX_NUM
bullets: LinkList = None

COMMON_SPRITE_SIZE = res.COMMON_SPRITE_SIZE
SPRITE_KNIGHT = res.SPRITE_KNIGHT
SPRITE_ELF = res.SPRITE_ELF
SPRITE_WIZZARD = res.SPRITE_WIZZARD
SPRITE_LIZARD = res.SPRITE_LIZARD
SPRITE_TINY_ZOMBIE = res.SPRITE_TINY_ZOMBIE
SPRITE_GOBLIN = res.SPRITE_GOBLIN
SPRITE_IMP = res.SPRITE_IMP
SPRITE_SKELET = res.SPRITE_SKELET
SPRITE_MUDDY = res. SPRITE_MUDDY
SPRITE_SWAMPY = res.SPRITE_SWAMPY
SPRITE_ZOMBIE = res.SPRITE_ZOMBIE
SPRITE_ICE_ZOMBIE = res.SPRITE_ICE_ZOMBIE
SPRITE_MASKED_ORC = res.SPRITE_MASKED_ORC
SPRITE_ORC_WARRIOR = res.SPRITE_ORC_WARRIOR
SPRITE_ORC_SHAMAN = res.SPRITE_ORC_SHAMAN
SPRITE_NECROMANCER = res.SPRITE_NECROMANCER
SPRITE_WOGOL = res.SPRITE_WOGOL
SPRITE_CHROT = res.SPRITE_CHROT
SPRITE_BIG_ZOMBIE = res.SPRITE_BIG_ZOMBIE
SPRITE_ORGRE = res.SPRITE_ORGRE
SPRITE_BIG_DEMON = res.SPRITE_BIG_DEMON

#Screen
SCREEN_WIDTH = res.SCREEN_WIDTH
SCREEN_HEIGHT = res.SCREEN_HEIGHT
UNIT = res.UNIT

# Game Settings
gameLevel = 0
stage = 0
spritesCount = 0
playersCount = 0
flasksCount = 0
herosCount = 0
flasksSetting = 0
herosSetting = 0
spritesSetting = 0
bossSetting = 0

# Win
GAME_WIN_NUM = 0
termCount = 0
willTerm = False
status = 0

# Drop rate
GAME_LUCKY = 0.0
GAME_DROPOUT_YELLOW_FLASKS = 0.0
GAME_DROPOUT_WEAPONS = 0.0
GAME_TRAP_RATE = 0.0
AI_LOCK_LIMIT = ai.AI_LOCK_LIMIT #ai.c
GAME_MONSTERS_HP_ADJUST = 0.0
GAME_MONSTERS_WEAPON_BUFF_ADJUST = 0.0
GAME_MONSTERS_GEN_FACTOR = 0.0

# Render
RENDER_LIST_SPRITE_ID = render.RENDER_LIST_SPRITE_ID  #render.c

# Buff
BUFF_DEFFENCE = types.BUFF_DEFFENCE  #types.c

def setLevel(level):
    '''Set parameters according to the game level
    '''
    global gameLevel, spritesSetting, bossSetting, herosSetting, flasksSetting
    global GAME_LUCKY, GAME_DROPOUT_YELLOW_FLASKS, GAME_DROPOUT_WEAPONS, GAME_TRAP_RATE
    global GAME_MONSTERS_HP_ADJUST, GAME_MONSTERS_GEN_FACTOR, GAME_MONSTERS_WEAPON_BUFF_ADJUST
    global AI_LOCK_LIMIT, GAME_WIN_NUM

    gameLevel = level
    spritesSetting = 25
    bossSetting = 2
    herosSetting = 8
    flasksSetting = 6
    GAME_LUCKY = 1
    GAME_DROPOUT_YELLOW_FLASKS = 0.3
    GAME_DROPOUT_WEAPONS = 0.7
    GAME_TRAP_RATE = 0.005 * (level + 1)
    GAME_MONSTERS_HP_ADJUST = 1 + level * 0.8 + stage * level * 0.1
    GAME_MONSTERS_GEN_FACTOR = 1 + level * 0.5 + stage * level * 0.05
    GAME_MONSTERS_WEAPON_BUFF_ADJUST = 1 + level * 0.8 + stage * level * 0.02
    AI_LOCK_LIMIT = max(1, 7 - level * 2 - stage / 2)
    GAME_WIN_NUM = 10 + level * 5 + stage * 3

    if level == 1:
        GAME_DROPOUT_WEAPONS = 0.98
        herosSetting = 5
        flasksSetting = 4
        spritesSetting = 28
        bossSetting = 3
    elif level == 2:
        GAME_DROPOUT_WEAPONS = 0.98
        GAME_DROPOUT_YELLOW_FLASKS = 0.3
        spritesSetting = 28
        herosSetting = 5
        flasksSetting = 3
        bossSetting = 5

    spritesSetting += stage / 2 * (level + 1)
    bossSetting += stage / 3

def startGame(localPlayers: int, remotePlayers: int, localFirst: bool)-> list[Score]:
    '''Start the game
    Input: 
        localPlayers: int, the number of local players
        remotePlayers: int, the number of remote players
        localFirst: bool, whether the local players play first
    Return:
        list[Score], the scores of each player
    '''
    scores: list[Score] = []
    for i in range(localPlayers):
        scores.append(types.createScore())

    status = 0
    stage = 0
    while status == 0:
        initGame(localPlayers, remotePlayers, localFirst)
        setLevel(gameLevel)
        status = gameLoop()
        for i in range(localPlayers):
            types.addScore(scores[i], spriteSnake[i].score)
        destroyGame(status)
        stage += 1

    return scores

def appendSpriteToSnake(snake: Snake, sprite_id: int, x: int, y: int, direction: Direction):
    '''Append a sprite to the head of snake
    Input:
        snake: Snake, the snake to append the sprite
        sprite_id: int, the id of the sprite
        x: int, the x coordinate of the sprite
        y: int, the y coordinate of the sprite
        direction: Direction, the direction of the sprite
    return: None'''
    # x ,y, dir only matter when empty snake
    snake.num += 1
    snake.score.got += 1

    # at head
    node = LinkNode()
    types.initLinkNode(node)       # XXXXX maybe bug here  

    # create a sprite
    snakeHead: Sprite = None
    if snake.sprites.head:
        snakeHead = snake.sprites.head.element     # undifined type
        x, y = snakeHead.x, snakeHead.y
        delta: int = (snakeHead.ani.origin.width * SCALE_FACTOR +
                 commonSprites[sprite_id].ani.origin.width * SCALE_FACTOR) // 2
        if snakeHead.direction == Direction.LEFT:
            x -= delta
        elif snakeHead.direction == Direction.RIGHT:
            x += delta
        elif snakeHead.direction == Direction.UP:
            y -= delta
        else:
            y += delta
    sprite = sprite.createSprite(commonSprites[sprite_id], x, y)
    sprite.direction = direction
    if direction == Direction.LEFT:
        sprite.face = Direction.LEFT
    if snakeHead:
        sprite.direction = snakeHead.direction
        sprite.face = snakeHead.face
        sprite.ani.currentFrame = snakeHead.ani.currentFrame

    # insert the sprite
    node.element = sprite
    types.pushLinkNodeAtHead(snake.sprites, node)  # XXXXX maybe bug here

    # push ani
    types.pushAnimationToRender(RENDER_LIST_SPRITE_ID, sprite.ani) # XXXXX maybe bug here

    # apply buff
    if snake.buffs[BUFF_DEFFENCE]:
        shieldSprite(sprite, snake.buffs[BUFF_DEFFENCE])

def initPlayer(playerType):
    ''' Initialize a player with one hero: knight
    Input:
        playerType: PlayerType, the type of the player  '''
    global spritesCount, playersCount

    spritesCount += 1
    p = spriteSnake[playersCount] = player.createSnake(MOVE_STEP, playersCount, playerType)
    appendSpriteToSnake(p, SPRITE_KNIGHT, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + playersCount * 2 * UNIT, Direction.RIGHT)
    playersCount += 1


def generateHeroItem(x, y):
    '''Generate a hero at (x, y)'''
    heroId = random.randint(SPRITE_KNIGHT, SPRITE_LIZARD)       # alternate builded library
    ani: Animation = None
    itemMap[x][y] = Item(ITEM_HERO, heroId, 0, ani)               # item_hero is one element of enum itemtye
    types.copyAnimation(commonSprites[heroId].ani, ani)         # XXXXX maybe bug here
    x *= UNIT
    y *= UNIT
    # TODO: Dangerous
    ani.origin -= 1
    ani.x = x + UNIT // 2
    ani.y = y + UNIT - 3
    ani.at = AT_BOTTOM_CENTER             # AT_BOTTOM_CENTER is one element of enum At (types)
    render.pushAnimationToRender(RENDER_LIST_SPRITE_ID, ani)


def generateItem(x: int, y: int, type: ItemType):
    '''Generate an item at (x, y) with the given type'''
    textureId = RES_FLASK_BIG_RED # RES_FLASK_BIG_RED is one element in res
    id = 0
    belong = SPRITE_KNIGHT
    
    if type == ITEM_HP_MEDCINE:  # ITEM_HP_MEDCINE is one element in enum ItemType
        textureId = RES_FLASK_BIG_RED  # RES_FLASK_BIG_RED is one element in res
    elif type == ITEM_HP_EXTRA_MEDCINE:  # ITEM_HP_EXTRA_MEDCINE is one element in enum ItemType
        textureId = RES_FLASK_BIG_YELLOW  # RES_FLASK_BIG_YELLOW is one element in res
    elif type == ITEM_WEAPON:   # ITEM_WEAPON is one element in enum ItemType
        kind = random.randint(0, 5)                     #alternate builded library
        if kind == 0:
            textureId = RES_ICE_SWORD
            id = WEAPON_ICE_SWORD
            belong = SPRITE_KNIGHT
        elif kind == 1:
            textureId = RES_HOLY_SWORD
            id = WEAPON_HOLY_SWORD
            belong = SPRITE_KNIGHT
        elif kind == 2:
            textureId = RES_THUNDER_STAFF
            id = WEAPON_THUNDER_STAFF
            belong = SPRITE_WIZZARD
        elif kind == 3:
            textureId = RES_PURPLE_STAFF
            id = WEAPON_PURPLE_STAFF
            belong = SPRITE_WIZZARD
        elif kind == 4:
            textureId = RES_GRASS_SWORD
            id = WEAPON_SOLID_CLAW
            belong = SPRITE_LIZARD
        elif kind == 5:
            textureId = RES_POWERFUL_BOW
            id = WEAPON_POWERFUL_BOW
            belong = SPRITE_ELF
    
    ani = render.createAndPushAnimation(
        animationsList[RENDER_LIST_MAP_ITEMS_ID],       # RENDER_LIST_MAP_ITEMS_ID is one element in render
        textures[textureId], None, LOOP_INFI, 3,    # LOOP_INFI is one element in render types. looptype
        x * UNIT, y * UNIT, SDL_FLIP_NONE, 0, AT_BOTTOM_LEFT)  # SDL_FLIP_NONE is UNKNOWN, AT_BOTTOM_LEFT is one element in types.At
    
    itemMap[x][y] = Item(type, id, belong, ani)

def takeHpMedcine(snake:Snake, delta: int, extra: bool):
    '''Take the hp medicine
    Input:
        snake: Snake, the snake (heros) to take the medicine
        delta: int, the delta of hp
        extra: bool, whether the medicine is extra
    Return: None'''
    for p in snake.sprites.head:
        sprite = p.element
        if sprite.hp == sprite.totalHp and not extra:
            continue
        addHp = int(delta * sprite.totalHp / 100)
        if not extra:
            addHp = max(0, min(sprite.totalHp - sprite.hp, addHp))
        sprite.hp += addHp
        ani = render.createAndPushAnimation(
            animationsList[RENDER_LIST_EFFECT_ID],  # RENDER_LIST_EFFECT_ID is one element in render
            textures[RES_HP_MED], None, LOOP_ONCE, SPRITE_ANIMATION_DURATION,
            sprite.x, sprite.y, SDL_FLIP_NONE, 0, AT_BOTTOM_CENTER)
        render.bindAnimationToSprite(ani, sprite, False)
    
def takeWeapon(snake: Snake, weapon_item: Item)-> bool:
    '''
    Heros touch a weapon, if possible, take the weapon
    else leave it
    
    Input: 
        snake: Snake, the snake to take the weapon
        weapon_item: Item, the weapon item
    Return:
        bool, whether the weapon is taken
    '''
    weapon = weapons[weapon_item.id]
    taken = False
    p = snake.sprites.head
    while p:
        sprite = p.element
        if (sprite.ani.origin == commonSprites[weapon_item.belong].ani.origin and
            sprite.weapon == commonSprites[weapon_item.belong].weapon):
            sprite.weapon = weapon
            ani = render.create_and_push_animation(       #bug
                animationsList[RENDER_LIST_EFFECT_ID], weapon_item.ani.origin, None,
                LOOP_INFI, 3, sprite.x, sprite.y, SDL_FLIP_NONE, 0,
                AT_BOTTOM_CENTER)
            render.bind_animation_to_sprite(ani, sprite, True)   #bug
            sprite.hp += GAME_HP_MEDICINE_EXTRA_DELTA / 100.0 * sprite.totalHp * 5
            ani = render.create_and_push_animation(          #bug
                animationsList[RENDER_LIST_EFFECT_ID], textures[RES_HP_MED], None,
                LOOP_ONCE, SPRITE_ANIMATION_DURATION, 0, 0,
                SDL_FLIP_NONE, 0, AT_BOTTOM_CENTER)
            render.bind_animation_to_sprite(ani, sprite, True)   #bug
            taken = True
            break
        p = p.nxt
    return taken

def dropItemNearSprite(sprite: Sprite, item_type: ItemType):
    '''
    Drop an item near the sprite (in range  3 x 3) with the given type 
    Input: 
        sprite: Sprite, the sprite to drop the item
        item_type: ItemType, the type of the item
    Return: None'''
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            x = sprite.x // UNIT + dx
            y = sprite.y // UNIT + dy
            if helper.inr(x, 0, n - 1) and helper.in_range(y, 0, m - 1) and map.hasMap[x][y] and itemMap[x][y].type == ITEM_NONE:
                generateItem(x, y, item_type)            #bug
                return

def generateHeroItemAllMap():
    '''
    generate 1 hero item in the map
    condition: empty cell, no adjacent to other objects'''
    x, y = 0, 0
    while (not map.hasMap[x][y]) or (map[x][y].bp != BLOCK_FLOOR) or (itemMap[x][y].type != ITEM_NONE) or (not hasMap[x - 1][y] or not map.hasMap[x + 1][y] or  not map.hasMap[x][y + 1] or not has_map[x][y - 1]):
        x = rand_int(1, n - 2)
        y = rand_int(1, m - 2) 
        break;             
        
    generate_hero_item(x, y)
    

def clearItemMap():
    '''Clear the item map'''
    for i in range(n):
        for j in range(m):
            itemMap[i][j].type = ITEM_NONE
            
            
def initItemMap(hCount: int, fCount: int):
    '''
    Init the item map with hCount heros and fCount flasks
    Input:
        hCount: int, the number of heros
        fCount: int, the number of flasks
    
    Return: None
    eg:  initItemMap(herosSetting - herosCount, flasksSetting - flasksCount);
    

    '''
    x, y = 0, 0
    while hCount > 0:
        generateHeroItemAllMap()
        herosCount += 1
        hCount -= 1
    while fCount > 0:
        while True:
            x = random.randint(0, n - 1)
            y = random.randint(0, m - 1)        # alternate builded library
            if (hasMap[x][y] and map[x][y].bp == BLOCK_FLOOR and
                    itemMap[x][y].type == ITEM_NONE):
                break
        generateItem(x, y, ITEM_HP_MEDCINE)
        flasksCount += 1
        fCount -= 1

def generateEnemy(x: int, y: int, minLen: int, maxLen: int, minId: int, maxId: int, step: int):
    '''create an enemy team at (x, y) with the given parameters
    Input:
        x, y: int, the position of the enemy
        minLen, maxLen: int, the range of the length of the enemy
        minId, maxId: int, the range of the id of the enemy
        step: int, the step of the enemy
    Return: int, the length of the enemy team'''
    global spritesCount
    snake = spriteSnake[spritesCount]
    spriteSnake[spritesCount] = player.createSnake(step, GAME_MONSTERS_TEAM, COMPUTER) #bug
    spritesCount += 1
    hasEnemy[x][y] = 1
    vertical = random.randint(0, 1)
    len_ = 1
    if vertical:
        while (helper.inr(y + len_, 0, m - 1) and hasMap[x][y + len_] and   #bug
               map[x][y + len_].bp == BLOCK_FLOOR and
               itemMap[x][y + len_].type == ITEM_NONE and not hasEnemy[x][y + len_]):
            len_ += 1
    else:
        while (helper.inr(x + len_, 0, n - 1) and hasMap[x + len_][y] and   #bug
               map[x + len_][y].bp == BLOCK_FLOOR and
               itemMap[x + len_][y].type == ITEM_NONE and not hasEnemy[x + len_][y]):
            len_ += 1
    minLen = min(minLen, len_)
    maxLen = min(maxLen, len_)
    len_ = random.randint(minLen, maxLen)
    for i in range(len_):
        xx = x
        yy = y
        if vertical:
            yy += i
        else:
            xx += i
        hasEnemy[xx][yy] = 1
        xx *= UNIT
        yy *= UNIT
        yy += UNIT
        xx += UNIT // 2
        spriteId = random.randint(minId, maxId)
        appendSpriteToSnake(snake, spriteId, xx, yy, DOWN if vertical else RIGHT)
    return len_

def getAvailablePos() -> Point:
    '''
    Get an available position in the map
    '''
    x, y = 0, 0
    while True:
        x = random.randint(0, n - 1)              #alternate builded library
        y = random.randint(0, m - 1)
        if (hasMap[x][y] and map[x][y].bp == BLOCK_FLOOR and
                itemMap[x][y].type == ITEM_NONE and not hasEnemy[x][y] and
                (not hasMap[x - 1][y] or not hasMap[x + 1][y] or
                 not hasMap[x][y + 1] or not hasMap[x][y - 1])):
            break
    return Point(x, y)

def initEnemies(enemiesCount: int):
    '''Initialize the enemies with the given number 
    initialize boss with with given param: bossSetting
    
    Input: 
        enemiesCount: int, the number of enemies
    Return  None'''
    global hasEnemy
    hasEnemy = [[0] * m for _ in range(n)]
    for i in range(-2, 3):
        for j in range(-2, 3):
            hasEnemy[n // 2 + i][m // 2 + j] = 1
    i = 0
    while i < enemiesCount:
        random_ =  random.random() * GAME_MONSTERS_GEN_FACTOR       # alternate builded library
        pos = getAvailablePos()
        x, y = pos.x, pos.y
        minLen, maxLen, step = 2, 4, 1
        startId, endId = SPRITE_TINY_ZOMBIE, SPRITE_TINY_ZOMBIE
        if random_ < 0.3:
            startId, endId = SPRITE_TINY_ZOMBIE, SPRITE_SKELET
        elif random_ < 0.4:
            startId, endId = SPRITE_WOGOL, SPRITE_CHROT
            step = 2
        elif random_ < 0.5:
            startId, endId = SPRITE_ZOMBIE, SPRITE_ICE_ZOMBIE
        elif random_ < 0.8:
            startId, endId = SPRITE_MUDDY, SPRITE_SWAMPY
        else:
            startId, endId = SPRITE_MASKED_ORC, SPRITE_NECROMANCER
        i += generateEnemy(x, y, minLen, maxLen, startId, endId, step)
    for bossCount in range(bossSetting):
        pos = getAvailablePos()
        generateEnemy(pos.x, pos.y, 1, 1, SPRITE_BIG_ZOMBIE, SPRITE_BIG_DEMON, 1)

'''
 * Put buff animation on snake

'''
def freezeSnake(snake: Snake, duration: int):
    '''
    Freeze the snake with the given + duration
    Input:
        snake: Snake, the snake to freeze
        duration: int, the duration of the freeze'''
    # If snake is already frozen, return
    if snake.buffs[BUFF_FROZEN]:
        return
    
    # If snake has no defense, freeze it for the specified duration
    if not snake.buffs[BUFF_DEFFENCE]:
        snake.buffs[BUFF_FROZEN] += duration
    
    # If snake has defense, apply a temporary effect and set duration to 30
    effect = None
    if snake.buffs[BUFF_DEFFENCE]:
        effect = Effect()
        types.copyEffect(effects[EFFECT_VANISH30], effect)   #bug
        duration = 30
    
    # Apply freeze animation to each sprite in the snake
    for p in snake.sprites.head:
        sprite = p.element
        ani = render.createAndPushAnimation(
            animationsList[RENDER_LIST_EFFECT_ID], textures[RES_ICE], effect,
            LOOP_ONCE, duration, sprite.x, sprite.y, SDL_FLIP_NONE, 0,
            AT_BOTTOM_CENTER)
        ani.scaled = False
        if snake.buffs[BUFF_DEFFENCE]:
            continue
        render.bindAnimationToSprite(ani, sprite, True)       #bug
        
def slowDownSnake(snake: Snake, duration: int):
    '''
    Slow down the snake with the given duration
    
    Input:
        snake: Snake, the snake to slow down
        duration: int, the duration of the slow down
    '''
    # If snake is already slowed down, return
    if snake.buffs[BUFF_SLOWDOWN]:
        return
    
    # If snake has no defense, slow it down for the specified duration
    if not snake.buffs[BUFF_DEFFENCE]:
        snake.buffs[BUFF_SLOWDOWN] += duration
    
    # If snake has defense, apply a temporary effect and set duration to 30
    effect = None
    if snake.buffs[BUFF_DEFFENCE]:
        effect = Effect()
        types.copyEffect(effects[EFFECT_VANISH30], effect) #bug
        duration = 30
    
    # Apply slowdown animation to each sprite in the snake
    for p in snake.sprites.head:
        sprite = p.element
        ani = render.createAndPushAnimation(
            animationsList[RENDER_LIST_EFFECT_ID], textures[RES_SOLIDFX], effect,
            LOOP_LIFESPAN, 40, sprite.x, sprite.y, SDL_FLIP_NONE, 0,
            AT_BOTTOM_CENTER)
        ani.lifeSpan = duration
        ani.scaled = False
        if snake.buffs[BUFF_DEFFENCE]:
            continue
        render.bindAnimationToSprite(ani, sprite, True)
        
def shieldSprite(sprite: Sprite, duration: int):
    '''
    Attach a shield to the sprite with the given duration
    
    Input:
        sprite: Sprite, the sprite to attach the shield
        duration: int, the duration of the shield'''
    ani = render.createAndPushAnimation(
        animationsList[RENDER_LIST_EFFECT_ID], textures[RES_HOLY_SHIELD], None,
        LOOP_LIFESPAN, 40, sprite.x, sprite.y, SDL_FLIP_NONE, 0,
        AT_BOTTOM_CENTER)
    render.bindAnimationToSprite(ani, sprite, True)    #bug
    ani.lifeSpan = duration
    
def shieldSnake(snake: Snake, duration: int):
    '''
    Apply defense buff to the snake (heros) with the given duration
    '''
    # If snake already has defense buff, return
    if snake.buffs[BUFF_DEFFENCE]:
        return
    
    # Apply defense buff to the snake
    snake.buffs[BUFF_DEFFENCE] += duration
    
    # Apply shield animation to each sprite in the snake
    for p in snake.sprites.head:
        shieldSprite(p.element, duration)

    
def attackUpSprite(sprite: Sprite, duration: int):
    '''
    Attach an attack up effect to the sprite with the given duration
    
    Input:
        sprite: Sprite, the sprite to attach the effect
        duration: int, the duration of the effect'''
    ani = render.createAndPushAnimation(                  #bug
        animationsList[RENDER_LIST_EFFECT_ID], textures[RES_ATTACK_UP], None,
        LOOP_LIFESPAN, SPRITE_ANIMATION_DURATION, sprite.x, sprite.y,
        SDL_FLIP_NONE, 0, AT_BOTTOM_CENTER)
    render.bindAnimationToSprite(ani, sprite, True)
    ani.lifeSpan = duration

def attackUpSnake(snake: Snake, duration: int):
    '''
    Apply attack up buff to the snake (heros) with the given duration
    '''
    # If snake already has attack up buff, return
    if snake.buffs[BUFF_ATTACK]:
        return
    
    # Apply attack up buff to the snake
    snake.buffs[BUFF_ATTACK] += duration
    
    # Apply attack up animation to each sprite in the snake
    for p in snake.sprites.head:
        attackUpSprite(p.element, duration)
   
'''
  Initialize and deinitialize game and snake
'''     
def initGame(localPlayers: int, remotePlayers: int, localFirst: bool):
    '''Initialize the game with the given number of local players and remote players
    Input:
        localPlayers: int, the number of local players
        remotePlayers: int, the number of remote players
        localFirst: bool, whether the local players play first
    Return: None
    '''
    audio.randomBgm()               #bug
    global status, termCount, willTerm, spritesCount, playersCount, flasksCount, herosCount
    status = 0
    termCount = willTerm = 0
    spritesCount = playersCount = flasksCount = herosCount = 0
    render.initRenderer()   #bug
    render.initCountDownBar()

    # Create default hero at (w/2, h/2) and apply shield animation
    for i in range(localPlayers + remotePlayers):
        playerType = LOCAL if localFirst else REMOTE
        if (localFirst and i >= localPlayers) or (not localFirst and i < remotePlayers):
            playerType = REMOTE
        initPlayer(playerType)
        shieldSnake(spriteSnake[i], 300)
    
    render.initInfo()
    # Create map
    map.initRandomMap(0.7, 7, GAME_TRAP_RATE)

    clearItemMap()
    # Create enemies
    initEnemies(spritesSetting)
    map.pushMapToRender()
    global bullets
    bullets = types.createLinkList()       # ????


def destroyGame(status: int):
    '''Destroy the game with the given status : Clear game, end game
    Input:
        status: int, the status of the game
    '''
    global spritesCount, spriteSnake, animationsList, bullets, BLACK, WHITE

    # Destroy all snakes
    while spritesCount > 0:
        destroySnake(spriteSnake[spritesCount - 1])
        spriteSnake[spritesCount - 1] = None
        spritesCount -= 1

    # Destroy all animations
    for i in range(ANIMATION_LINK_LIST_NUM):
        types.destroyAnimationsByLinkList(animationsList[i])   #bug

    # Destroy all bullets
    p = bullets.head
    while p:
        bullet.destroyBullet(p.element)          #bug
        p.element = None
        p = p.nxt

    types.destroyLinkList(bullets)
    bullets = None

    # Display game status message
    render.blackout()                #bug
    msg = "Stage Clear" if status == 0 else "Game Over"
    text = types.createText(msg, WHITE)   #bug
    render.renderCenteredText(text, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 2)  #bug
    types.destroyText(text)             #bug
    SDL_RenderPresent(renderer)           #bug bug bug

    # Pause for a duration before clearing the renderer
    time.sleep(RENDER_GAMEOVER_DURATION)
    # sleep(RENDER_GAMEOVER_DURATION)               #bug
    render.clearRenderer()
    

def destroySnake(snake: Snake):
    '''
    Destroy the snake
    Input:
        snake: Snake, the snake to destroy'''
    global bullets

    # Remove snake as owner from bullets
    if bullets:
        p = bullets.head
        while p:
            bullet = p.element
            if bullet.owner == snake:
                bullet.owner = None
            p = p.nxt
    
    # Free memory for each sprite in the snake
    p = snake.sprites.head
    while p:
        sprite = p.element
        del sprite
        p.element = None
        p = p.nxt

    # Destroy the linked list of sprites
    types.destroyLinkList(snake.sprites)
    snake.sprites = None

    # Destroy the score associated with the snake
    types.destroyScore(snake.score)
    snake.score = None

    # Free memory for the snake itself
    del snake

def isPlayer(snake: Snake) -> bool:
    '''
    Check if the snake is a player
    '''
    return snake in spriteSnake[:playersCount]

def crushVerdict(sprite: Sprite, loose: bool, useAnimationBox: bool) -> bool:
    '''Check if the sprite is crushed by other sprites or blocks
    Input:
        sprite: Sprite, the sprite to check
        loose: bool, whether the sprite is loose
        useAnimationBox: bool, whether to use the animation box
    Return bool, whether the sprite is crushed
    '''
    x, y = sprite.x, sprite.y
    block = None
    box = helper.getSpriteAnimationBox(sprite) if useAnimationBox else helper.getSpriteFeetBox(sprite)
    #bug 
    # If the sprite is out of the map, then consider it as crushed
    
    if helper.inr(x // UNIT, 0, n - 1) and helper.inr(y // UNIT, 0, m - 1):  #bug
        pass
    else:
        return True
    
    # Loop over the cells nearby the sprite to know better if it falls out of map
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            xx, yy = x // UNIT + dx, y // UNIT + dy
            if helper.inr(xx, 0, n - 1) and helper.inr(yy, 0, m - 1):  #bug
                block = helper.getMapRect(xx, yy) #bug
                if helper.RectRectCross(box, block) and not hasMap[xx][yy]:  #bug
                    return True

    # If it has crushed on other sprites
    for i in range(spritesCount):
        self_ = False
        for p in spriteSnake[i].sprites.head:
            other = p.element
            if other != sprite:
                otherBox = helper.getSpriteAnimationBox(other) if useAnimationBox else helper.getSpriteFeetBox(other)  #bug
                if helper.RectRectCross(box, otherBox):  #bug
                    if (self_ and loose) or (p.pre and p.pre.element == sprite):
                        pass
                    else:
                        return True
            else:
                self_ = True
    
    return False


def dropItem(sprite: Sprite):
    '''
    Drop an item near the sprite'''
    random_ = random.random() * sprite.dropRate * GAME_LUCKY
    if random_ < GAME_DROPOUT_YELLOW_FLASKS:
        dropItemNearSprite(sprite, ITEM_HP_EXTRA_MEDCINE)
    elif random_ > GAME_DROPOUT_WEAPONS:
        dropItemNearSprite(sprite, ITEM_WEAPON)

def invokeWeaponBuff(src: Snake, weapon: Weapon, dest: Snake, damage: int):
    '''
    Invoke the weapon buff on the destination snake
    
    Input:
        src: Snake, the source snake doing the attack
        weapon: Weapon, the weapon to invoke
        dest: Snake, the destination snake receiving the attack
        damage: int, the damage of the weapon
    Return: None
    '''
    for i in range(BUFF_BEGIN, BUFF_END):
        random = random.random()  # alternate builded library
        if src and src.team == GAME_MONSTERS_TEAM:
            random *= GAME_MONSTERS_WEAPON_BUFF_ADJUST
        if random < weapon.effects[i].chance:
            if i == BUFF_FROZEN:
                freezeSnake(dest, weapon.effects[i].duration)
            elif i == BUFF_SLOWDOWN:
                slowDownSnake(dest, weapon.effects[i].duration)
            elif i == BUFF_DEFFENCE:
                if src:
                    shieldSnake(src, weapon.effects[i].duration)
            elif i == BUFF_ATTACK:
                if src:
                    attackUpSnake(src, weapon.effects[i].duration)
                    
def dealDamage(src: Snake, dest: Snake, target: Sprite, damage: int):
    '''
    Deal damage to the target sprite
    
    Input:
        src: Snake, the source snake doing the attack
        dest: Snake, the destination snake receiving the attack
        target: Sprite, the target sprite to attack
        damage: int, the damage to deal
    Return: None'''
    calcDamage = damage
    if dest.buffs[BUFF_FROZEN]:
        calcDamage *= GAME_FROZEN_DAMAGE_K
    if src and src != spriteSnake[GAME_MONSTERS_TEAM]:
        if src.buffs[BUFF_ATTACK]:
            calcDamage *= GAME_BUFF_ATTACK_K
    if dest != spriteSnake[GAME_MONSTERS_TEAM]:
        if dest.buffs[BUFF_DEFFENCE]:
            calcDamage /= GAME_BUFF_DEFENSE_K
    
    target.hp -= calcDamage
    
    if src:
        src.score.damage += calcDamage
        if target.hp <= 0:
            src.score.killed += 1
    
    dest.score.stand += damage
    
def makeSnakeCross(snake: Snake) -> bool:
    '''
    check if the snake is crossed with other sprites or blocks
    '''
    if not snake.sprites.head:
        return False

    for i in range(SCREEN_WIDTH // UNIT):
        for j in range(SCREEN_HEIGHT // UNIT):
            if hasMap[i][j]:
                # check crush with blocks trap
                # block = SDL_Rect(i * UNIT, j * UNIT, UNIT, UNIT)
                block = pygame.Rect(i * UNIT, j * UNIT, UNIT, UNIT)
                
                if map[i][j].bp == BLOCK_TRAP and map[i][j].enable:
                    for p in snake.sprites.head:
                        sprite = p.element
                        spriteRect = helper.getSpriteFeetBox(sprite)  #bug
                        if helper.RectRectCross(spriteRect, block):   #bug
                            dealDamage(None, snake, sprite, spikeDamage)
                
                # check crush with player item: hero, hp medicine, weapon
                if isPlayer(snake):
                    headBox = helper.getSpriteFeetBox(snake.sprites.head.element)  #bug
                    if itemMap[i][j].type != ITEM_NONE:
                        if helper.RectRectCross(headBox, block):    #bug
                            taken = True
                            ani = itemMap[i][j].ani
                            if itemMap[i][j].type == ITEM_HERO:
                                audio.playAudio(AUDIO_COIN)  #bug
                                appendSpriteToSnake(snake, itemMap[i][j].id, 0, 0, RIGHT)
                                herosCount -= 1
                                types.removeAnimationFromLinkList(animationsList[RENDER_LIST_SPRITE_ID], ani)  #bug
                            elif itemMap[i][j].type in [ITEM_HP_MEDCINE, ITEM_HP_EXTRA_MEDCINE]:
                                audio.playAudio(AUDIO_MED)  #bug
                                takeHpMedcine(snake, GAME_HP_MEDICINE_DELTA, itemMap[i][j].type == ITEM_HP_EXTRA_MEDCINE)
                                flasksCount -= 1 if itemMap[i][j].type == ITEM_HP_MEDCINE else 0
                                types.removeAnimationFromLinkList(animationsList[RENDER_LIST_MAP_ITEMS_ID], ani) #bug
                            elif itemMap[i][j].type == ITEM_WEAPON:
                                taken = takeWeapon(snake, itemMap[i][j])
                                if taken:
                                    audio.playAudio(AUDIO_MED)
                                    types.removeAnimationFromLinkList(animationsList[RENDER_LIST_MAP_ITEMS_ID], ani)
                            if taken:
                                itemMap[i][j].type = ITEM_NONE
    # check if heros die
    for p in snake.sprites.head:
        sprite = p.element
        if sprite.hp <= 0:
            audio.playAudio(AUDIO_HUMAN_DEATH)  #bug
            death = sprite.ani.origin
            if isPlayer(snake):
                death += 1
            dropItem(sprite)
            render.createAndPushAnimation(animationsList[RENDER_LIST_DEATH_ID], textures[RES_SKULL], None, LOOP_INFI, 1, sprite.x + randInt(-MAP_SKULL_SPILL_RANGE, MAP_SKULL_SPILL_RANGE), sprite.y + randInt(-MAP_SKULL_SPILL_RANGE, MAP_SKULL_SPILL_RANGE), SDL_FLIP_NONE if sprite.face == LEFT else SDL_FLIP_HORIZONTAL, 0, AT_BOTTOM_CENTER)
            render.createAndPushAnimation(animationsList[RENDER_LIST_DEATH_ID], death, effects[EFFECT_DEATH], LOOP_ONCE, SPRITE_ANIMATION_DURATION, sprite.x, sprite.y, SDL_FLIP_NONE if sprite.face == RIGHT else SDL_FLIP_HORIZONTAL, 0, AT_BOTTOM_CENTER)
            render.clearBindInAnimationsList(sprite, RENDER_LIST_EFFECT_ID)
            render.clearBindInAnimationsList(sprite, RENDER_LIST_SPRITE_ID)
            render.removeAnimationFromLinkList(animationsList[RENDER_LIST_SPRITE_ID], sprite.ani)
            sprite.ani = None
            snake.num -= 1

    # Update position of each sprite in the snake'''
    for p in snake.sprites.head:
        sprite = p.element
        if sprite.hp <= 0:
            for q in snake.sprites.tail:
                prevSprite = q.pre.element
                sprite = q.element
                sprite.direction = prevSprite.direction
                sprite.face = prevSprite.face
                sprite.posBuffer = prevSprite.posBuffer
                sprite.x = prevSprite.x
                sprite.y = prevSprite.y
            types.removeLinkNode(snake.sprites, p)  #bug
            del sprite

    # Check if the snake crush with other sprites or blocks
    if not snake.sprites.head:
        return False

    snakeHead = snake.sprites.head.element
    die = crushVerdict(snakeHead, not isPlayer(snake), False)
    if die:
        for p in snake.sprites.head:
            sprite = p.element
            sprite.hp = 0

    return die

def makeBulletCross(bullet: Bullet) -> bool:
    '''
    check if bullet is crossed with other sprites or blocks
    then deal damage and invoke weapon buff
    
    Input:
        bullet: Bullet, the bullet to check'''
    weapon = bullet.parent
    hit = False
    width = min(bullet.ani.origin.width, bullet.ani.origin.height) * (SCALE_FACTOR if bullet.ani.scaled else 1) * 0.8
    # bulletBox = SDL_Rect(bullet.x - width / 2, bullet.y - width / 2, width, width)
    bulletBox = pygame.Rect(bullet.x - width / 2, bullet.y - width / 2, width, width)

    # check if enemy is under bullet
    if not hasMap[bullet.x // UNIT][bullet.y // UNIT]:
        ani = Animation()
        types.copyAnimation(weapon.deathAni, ani)              #bug
        ani.x = bullet.x
        ani.y = bullet.y
        render.pushAnimationToRender(RENDER_LIST_EFFECT_ID, ani)             #bug
        hit = True

    # attack enemy if bullet range
    if not hit:
        for i in range(spritesCount):
            if bullet.team != spriteSnake[i].team:
                for p in spriteSnake[i].sprites.head:
                    target = p.element
                    box = helper.getSpriteBoundBox(target)   #bug
                    if helper.RectRectCross(box, bulletBox):  #bug
                        ani = Animation()
                        types.copyAnimation(weapon.deathAni, ani)   #bug
                        ani.x = bullet.x
                        ani.y = bullet.y 
                        render.pushAnimationToRender(RENDER_LIST_EFFECT_ID, ani)   #bug
                        hit = True
                        if weapon.wp in [WEAPON_GUN_POINT, WEAPON_GUN_POINT_MULTI]:
                            dealDamage(bullet.owner, spriteSnake[i], target, weapon.damage)
                            invokeWeaponBuff(bullet.owner, weapon, spriteSnake[i], weapon.damage)
                            return hit
                        break
    
    # attack enemy if bullet range
    if hit:
        audio.playAudio(weapon.deathAudio)   #bug
        for i in range(spritesCount):
            if bullet.team != spriteSnake[i].team:
                for p in spriteSnake[i].sprites.head:
                    target = p.element
                    if helper.distance(Point(target.x, target.y), Point(bullet.x, bullet.y)) <= weapon.effectRange:  #bug
                        dealDamage(bullet.owner, spriteSnake[i], target, weapon.damage)
                        invokeWeaponBuff(bullet.owner, weapon, spriteSnake[i], weapon.damage)

    return hit


def makeCross():
    '''
    Check if the sprites are crossed with other sprites or blocks
    check if the bullets are crossed with other sprites or blocks
    '''
    for i in range(spritesCount):
        makeSnakeCross(spriteSnake[i])

    p = bullets.head
    while p:
        nxt = p.nxt
        if makeBulletCross(p.element):
            bullet = p.element
            types.removeAnimationFromLinkList(animationsList[RENDER_LIST_EFFECT_ID], bullet.ani)
            types.removeLinkNode(bullets, p)  #bug
        p = nxt
        
def moveSprite(sprite, step):
    '''
    Move the sprite with the given step
    Input:
        sprite: Sprite, the sprite to move
        step: int, the step to move'''
    dir = sprite.direction
    if dir == LEFT:
        sprite.x -= step
    elif dir == RIGHT:
        sprite.x += step
    elif dir == UP:
        sprite.y -= step
    elif dir == DOWN:
        sprite.y += step

def moveSnake(snake):
    '''
    Move snake'''
    if snake.buffs[BUFF_FROZEN]:
        return

    step = snake.moveStep
    if snake.buffs[BUFF_SLOWDOWN]:
        step = max(step // 2, 1)

    p = snake.sprites.head
    while p:
        sprite = p.element
        for _ in range(step):
            b = sprite.posBuffer
            first_slot = b.buffer[0]
            while b.size and sprite.x == first_slot.x and sprite.y == first_slot.y:
                types.changeSpriteDirection(p, first_slot.direction)  #bug
                b.size -= 1
                b.buffer = b.buffer[1:]

                first_slot = b.buffer[0]        #??

            moveSprite(sprite, 1)
        p = p.nxt
        
        
def updateMap():
    '''
    Update traps in the map'''
    maskedTime = renderFrames % SPIKE_TIME_MASK
    for i in range(SCREEN_WIDTH // UNIT):
        for j in range(SCREEN_HEIGHT // UNIT):
            if hasMap[i][j] and map[i][j].bp == BLOCK_TRAP:
                if not maskedTime:
                    render.createAndPushAnimation(animationsList[RENDER_LIST_MAP_SPECIAL_ID],
                                           textures[RES_FLOOR_SPIKE_OUT_ANI], None,
                                           LOOP_ONCE, SPIKE_ANI_DURATION, i * UNIT,    #bug
                                           j * UNIT, SDL_FLIP_NONE, 0, AT_TOP_LEFT)
                elif maskedTime == SPIKE_ANI_DURATION - 1:
                    map[i][j].enable = True
                    map[i][j].ani.origin = textures[RES_FLOOR_SPIKE_ENABLED]
                elif maskedTime == SPIKE_ANI_DURATION + SPIKE_OUT_INTERVAL - 1:
                    render.createAndPushAnimation(animationsList[RENDER_LIST_MAP_SPECIAL_ID],
                                           textures[RES_FLOOR_SPIKE_IN_ANI], None,  #bug
                                           LOOP_ONCE, SPIKE_ANI_DURATION, i * UNIT,
                                           j * UNIT, SDL_FLIP_NONE, 0, AT_TOP_LEFT)
                    map[i][j].enable = False
                    map[i][j].ani.origin = textures[RES_FLOOR_SPIKE_DISABLED]


def updateBuffDuration():
    '''
    Update the duration of the all buffs of the all snakes'''
    global spritesCount, spriteSnake, BUFF_BEGIN, BUFF_END
    
    for i in range(spritesCount):
        snake = spriteSnake[i]
        for j in range(BUFF_BEGIN, BUFF_END):
            if snake['buffs'][j] > 0:
                snake['buffs'][j] -= 1




def makeSpriteAttack(sprite: Sprite, snake: Snake):
    '''
    Iterate over all the sprites in the snake and check if they can attack
    
    Input:
    snake: Snake, the snake to do attack
    sprite: Sprite, the sprite to do attack
    Return: None
    '''
    weapon = sprite.weapon
    if renderFrames - sprite.lastAttack < weapon.gap:
        return
    attacked = False
    for i in range(spritesCount):
        if snake.team != spriteSnake[i].team:
            for target in spriteSnake[i].sprites:
                if helper.distance((sprite.x, sprite.y), (target.x, target.y)) > weapon.shootRange: #bug
                    continue
                rad = math.atan2(target.y - sprite.y, target.x - sprite.x)
                if weapon.wp == WEAPON_SWORD_POINT or weapon.wp == WEAPON_SWORD_RANGE:
                    ani = Animation()
                    types.copyAnimation(weapon.deathAni, ani)   #bug
                    types.bindAnimationToSprite(ani, target, False)   #bug
                    if ani.angle != -1:
                        ani.angle = rad * 180 / math.pi
                    types.pushAnimationToRender(RENDER_LIST_EFFECT_ID, ani)  #bug
                    dealDamage(snake, spriteSnake[i], target, weapon.damage)
                    invokeWeaponBuff(snake, weapon, spriteSnake[i], weapon.damage)
                    attacked = True
                    if weapon.wp == WEAPON_SWORD_POINT:
                        attack_end(attacked, weapon, sprite, renderFrames)
                        # attack_end()
                else:
                    bullet = bullet.createBullet(snake, weapon, sprite.x, sprite.y, rad, snake.team, weapon.flyAni) #bug
                    bullets.append(bullet)
                    render.pushAnimationToRender(RENDER_LIST_EFFECT_ID, bullet.ani) #bug
                    attacked = True
                    if weapon.wp != WEAPON_GUN_POINT_MULTI:
                        attack_end(attacked, weapon, sprite, renderFrames)
                        attack_end()
                        
    def attack_end(attacked, weapon, sprite, renderFrames):   
        if attacked:
            if weapon.birthAni:
                ani = Animation()
                types.copyAnimation(weapon.birthAni, ani)   #bug
                render.bindAnimationToSprite(ani, sprite, True) #bug
                ani.at = AT_BOTTOM_CENTER
                render.pushAnimationToRender(RENDER_LIST_EFFECT_ID, ani) #bug
            if weapon.wp == WEAPON_SWORD_POINT or weapon.wp == WEAPON_SWORD_RANGE:
                audio.playAudio(weapon.deathAudio)   # bug
            else:
                audio.playAudio(weapon.birthAudio)    #bug
            sprite.lastAttack = renderFrames

def makeSnakeAttack(snake: Snake):
    '''
    Make the snake attack
    '''
    if snake.buffs[BUFF_FROZEN]:
        return
    
    p = snake.sprites.head
    while p.nxt is not None:
        makeSpriteAttack(p.element, snake)
        p = p.nxt
    
def isWin() -> bool:
    '''
    Check if the game is won
    '''
    
    if playersCount != 1:
        return False
    return spriteSnake[0].num >= GAME_WIN_NUM


class GameStatus(Enum):
    STAGE_CLEAR = 0
    GAME_OVER = 1
    

def setTerm(s: GameStatus):
    '''
    playe audio and set the game status'''
    audio.stopBgm()     #bug
    if s == GameStatus.STAGE_CLEAR:
        audio.playAudio(AUDIO_WIN) #bug
    else:
        audio.playAudio(AUDIO_LOSE) #bug
    status = s
    willTerm = True
    termCount = RENDER_TERM_COUNT
    
def pauseGame():
    '''
    Pause the game and wait for the user to resume'''
    audio.pauseSound()  #bug
    audio.playAudio(AUDIO_BUTTON1) #bug
    render.dim()     #bug
    msg = "Paused"
    text = types.createText(msg, WHITE)   #bug
    render.renderCenteredText(text, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 1)
    # SDL_RenderPresent(renderer) #bug bug bug
    pygame.display.update() 
    types.destroyText(text)      #bug
    # while not exit:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
    #             exit= True
    #         return
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
            break
    audio.resumeSound()     #bug
    audio.playAudio(AUDIO_BUTTON1)   #bug

def arrowsToDirection(keyValue: int) -> int:
    if keyValue == pygame.K_LEFT:
        return LEFT
    elif keyValue == pygame.K_RIGHT:
        return RIGHT
    elif keyValue == pygame.K_UP:
        return UP
    elif keyValue == pygame.K_DOWN:
        return DOWN
    return -1

def wasdToDirection(keyValue: int) -> int:
    if keyValue == pygame.K_a:
        return LEFT
    elif keyValue == pygame.K_d:
        return RIGHT
    elif keyValue == pygame.K_w:
        return UP
    elif keyValue == pygame.K_s:
        return DOWN
    return -1

def handleLocalKeypress():
    '''
    Handle the key press event for the local player
    '''
    quit = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True
            setTerm(GameStatus.GAME_OVER)
        elif event.type == pygame.KEYDOWN:
            keyValue = event.key
            if keyValue == pygame.K_ESCAPE:
                pauseGame()
            for id in range(min(2, playersCount)):
                player = spriteSnake[id]
                if player.playerType == LOCAL:
                    if not player.buffs[BUFF_FROZEN] and player.sprites.head is not None:
                        if id == 0:
                            direction = wasdToDirection(keyValue)
                        else:
                            direction = arrowsToDirection(keyValue)
                            
                        if direction >= 0:
                            net.sendPlayerMovePacket(id, direction)       #bug
                            types.changeSpriteDirection(player.sprites.head, direction)
    return quit
def handleLanKeypress():
    '''
    Handle the key press event for the remote player
    '''
    status, packet = net.recvLanPacket()
    if not status:
        return  # nop
    packet_type = packet.type
    if packet_type == HEADER_PLAYERMOVE:
        player_move_packet = packet
        player_id = player_move_packet.playerId
        direction = player_move_packet.direction
        print("recv: player move, {}, {}".format(player_id, direction))
        player = spriteSnake[player_id]
        if player.sprites.head:
            types.changeSpriteDirection(player.sprites.head, direction)        #bug
    elif packet_type == HEADER_GAMEOVER:
        print("recv: game over, -1")
        setTerm(GameStatus.GAME_OVER)


def gameLoop() -> int:
    # Game loop
    quit = False
    while not quit:
        quit = handleLocalKeypress()
        if quit:
            net.sendGameOverPacket(3)
        if net.lanClientSocket is not None:     #bug
            handleLanKeypress()

        updateMap()

        for i in range(spritesCount):
            if not spriteSnake[i].sprites.head:
                continue  # some snakes killed by before but not clean up yet
            if i >= playersCount and renderFrames % AI_DECIDE_RATE == 0:
                ai.AiInput(spriteSnake[i])   #bug
            moveSnake(spriteSnake[i])
            makeSnakeAttack(spriteSnake[i])
        
        p = bullets.head
        while p.nxt is not None:
            bullet.moveBullet(p.element)
            p = p.nxt
        
        if renderFrames % GAME_MAP_RELOAD_PERIOD == 0:
            initItemMap(herosSetting - herosCount, flasksSetting - flasksCount)
        
        for i in range(spritesCount):
            render.updateAnimationOfSnake(spriteSnake[i])   #bug
            if spriteSnake[i].buffs[BUFF_FROZEN]:
                for p in spriteSnake[i].sprites:
                    sprite = p.element
                    sprite.ani.currentFrame -= 1
        
        makeCross()
        render.render()
        updateBuffDuration()
        
        i = playersCount
        while i < spritesCount:
            if not spriteSnake[i].num:
                destroySnake(spriteSnake[i])
                del spriteSnake[i]
                spritesCount -= 1
            else:
                i += 1
        
        if willTerm:
            termCount -= 1
            if not termCount:
                break
        else:
            alivePlayer = -1
            for i in range(playersCount):
                if not spriteSnake[i].sprites.head:
                    setTerm(GameStatus.GAME_OVER)
                    net.sendGameOverPacket(alivePlayer)  #bug
                    break
                else:
                    alivePlayer = i
            if isWin():
                setTerm(GameStatus.STAGE_CLEAR)
    
    return status







