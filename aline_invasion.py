import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien

def run_game():
    #初始化游戏并且创建一个屏幕对象
    pygame.init()
    # screen = pygame.display.set_mode((1200,800))
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings,screen)
    #创建一个存储子弹的编组
    bullets = Group()
    bg_color = (230,233,230)
    #创建一组外星人
    # alien = Alien(ai_settings,screen)
    aliens = Group()
    gf.create_fleet(ai_settings,screen,aliens,ship)
    #开始游戏的主循环
    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(ai_settings,aliens)
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)
run_game()
