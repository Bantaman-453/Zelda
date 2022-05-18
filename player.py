import pygame
from settings import *
from support import import_folder
from Entity import Entity
from pygame.locals import (
    K_w,
    K_s,
    K_a,
    K_d
)


class Player(Entity):
    def __init__(self, pos, groups, obstacle_sprites, create_attack, Destroy_attack):
        super().__init__(groups)
        self.image = pygame.image.load("C:/Users/Jared.Banta/PycharmProjects"
                                       "/Zelda Project/Player/Player.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -26)

        # Graphics setup
        self.import_player_assets()
        self.status = 'down_idle'

        # Movement
        self.speed = 9
        self.attacking = False
        self.attack_cooldown = 200
        self.attack_time = None
        self.obstacle_sprites = obstacle_sprites

        # weapon selection
        self.create_attack = create_attack
        self.Destroy_attack = Destroy_attack
        self.weapon_index = 2
        self.weapon = list(Weapon_Data.keys())[self.weapon_index]
        print(self.weapon)

        # stats
        self.stats = {'health': 100, 'attack': 10}
        self.health = self.stats['health']

    def import_player_assets(self):
        character_path = 'C:/Users/Jared.Banta/PycharmProjects/Zelda Project/Player/'
        self.animations = {'up': [], 'down': [], 'left': [], 'right': [],
                           'up_idle': [], 'down_idle': [], 'left_idle': [], 'right_idle': [],
                           'up_attack': [], 'down_attack': [], 'left_attack': [], 'right_attack': []}
        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[K_w]:
            self.direction.y = -1
            self.status = 'up'
        elif keys[K_s]:
            self.direction.y = 1
            self.status = 'down'
        else:
            self.direction.y = 0

        if keys[K_d]:
            self.direction.x = 1
            self.status = 'right'
        elif keys[K_a]:
            self.direction.x = -1
            self.status = 'left'
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE] and not self.attacking:
            self.attacking = True
            self.attack_time = pygame.time.get_ticks()
            self.create_attack()

        if keys[pygame.K_m] and not self.attacking:
            self.attacking = True
            self.attack_time = pygame.time.get_ticks()

    def get_status(self):
        if self.direction.x == 0 and self.direction.y == 0:
            if not ('idle' in self.status or 'attack' in self.status):
                self.status = self.status + "_idle"

        if self.attacking:
            self.direction.x = 0
            self.direction.y = 0
            if not ('attack' in self.status):
                if 'idle' in self.status:
                    self.status = self.status.replace('_idle', '_attack')
                else:
                    self.status = self.status + "_attack"
        else:
            if 'attack' in self.status:
                self.status = self.status.replace('_attack', '')

    def cooldown(self):
        current_time = pygame.time.get_ticks()
        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown + Weapon_Data[self.weapon]['cooldown']:
                self.attacking = False
                self.Destroy_attack()

    def animate(self):
        animation = self.animations[self.status]

        # loop over frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center=self.hitbox.center)

    def get_full_damage(self):
        base_damage = self.stats['attack']
        weapon_damage = Weapon_Data[self.weapon]['damage']
        return base_damage + weapon_damage

    def update(self):
        self.input()
        self.cooldown()
        self.get_status()
        self.animate()
        self.move(self.speed)
