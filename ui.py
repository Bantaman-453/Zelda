import pygame
from settings import *


class UI:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, FONT_SIZE)

        # bar setup
        self.HEALTH_BAR = pygame.Rect(10, 10, HEALTH_BAR_WIDTH, BAR_HEIGHT)

    def show_bar(self, current, max_amount, bg_rect, color):
        # draw bg
        pygame.draw.rect(self.display_surface, UI_BG, bg_rect)

        # convert the stats to pixels
        ratio = current/max_amount
        current_width = bg_rect.width * ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width

        # draw the bar
        pygame.draw.rect(self.display_surface, color, current_rect)
        pygame.draw.rect(self.display_surface, UI_BORDER, bg_rect, 3)

    def display(self, player):
        self.show_bar(player.health, player.stats['health'], self.HEALTH_BAR, HEALTH)