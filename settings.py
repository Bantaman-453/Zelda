WIDTH = 1280
HEIGHT = 720
FPS = 30
TILE_SIZE = 64

# UI
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 400
MAGIC_BAR_WIDTH = 140
ITEM_BOX = 80
UI_FONT = 'C:/Users/Jared.Banta/PycharmProjects/Zelda Project/font/SanstainaRegular-52e8.ttf'
FONT_SIZE = 18

# general colours
WATER = '#71ddee'
UI_BG = '#222222'
UI_BORDER = '#111111'
TEXT = '#EEEEEE'

# UI colours
HEALTH = 'red'
MAGIC = 'blue'
UI_ACTIVE_BORDER = 'gold'

# Weapon data
Weapon_Data = {
    'Big sword': {'cooldown': 150, 'damage': 40, 'graphic': 'C:/Users/Jared.Banta/PycharmProjects/Zelda Project/Weapons/Big sword/full.png'},
    'Spear': {'cooldown': 400, 'damage': 32, 'graphic': 'C:/Users/Jared.Banta/PycharmProjects/Zelda Project/Weapons/Spear/full.png'},
    'Sai': {'cooldown': 15, 'damage': 12, 'graphic': 'C:/Users/Jared.Banta/PycharmProjects/Zelda Project/Weapons/Sai/full.png'},
    'Bow': {'cooldown': 550, 'damage': 28, 'graphic': 'C:/Users/Jared.Banta/PycharmProjects/Zelda Project/Weapons/Bow/full.png'},
    'Master Sword': {'cooldown': 250, 'damage': 200, 'graphic': 'C:/Users/Jared.Banta/PycharmProjects/Zelda Project/Weapons/'}
}

# Monster Data
Monster_Data = {
    'Beast': {'health': 500, 'exp': 15, 'damage': 70, 'attack_type': 'claw', 'speed': 5, 'knockback': 4, 'attack_radius': 45, 'notice_radius': 400},
    'octopus': {'health': 50, 'exp': 15, 'damage': 70, 'attack_type': 'claw', 'speed': 3, 'knockback': 3, 'attack_radius': 120, 'notice_radius': 600},
    'tree': {'health': 50, 'exp': 15, 'damage': 70, 'attack_type': 'claw', 'speed': 3, 'knockback': 3, 'attack_radius': 120, 'notice_radius': 600},
    'dragon': {'health': 50, 'exp': 15, 'damage': 70, 'attack_type': 'claw', 'speed': 3, 'knockback': 3, 'attack_radius': 120, 'notice_radius': 600},
    'fish': {'health': 50, 'exp': 15, 'damage': 70, 'attack_type': 'claw', 'speed': 3, 'knockback': 3, 'attack_radius': 120, 'notice_radius': 600}
}

World_Map = [
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'e', 'x'],
    ['x', ' ', 'p', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', 'x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', 'x', 'x', 'x', ' ', 'x', 'x', 'x', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', 'x', 'x', ' ', 'x', 'x', 'x', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x', ' ', 'x'],
    ['x', ' ', ' ', ' ', 'x', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'e', ' ', ' ', ' ', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', 'x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', 'x', ' ', ' ', 'x', ' ', 'e', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'e', ' ', 'x'],
    ['x', 'e', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ]
