import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # 创建一个新的子弹对象
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event,ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings,screen,ship,bullets):
    """响应案件和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)

def update_screen(ai_settings,screen,ship,aliens,bullets):
    """"更新屏幕上的图像，并切换到新屏幕"""
    #每次循环重绘屏幕
    screen.fill(ai_settings.bg_color)
    #在飞船和外星人后面重绘所有子弹
    for bullets in bullets.sprites():
        bullets.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    # aliens.blitme()
    #让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    #删除已经消失的子弹
def fire_bullet(ai_settings,screen,ship,bullets):
    """如果还没达到限制，就发射一颗子弹"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        # 将新子弹添加到子弹组中
        bullets.add(new_bullet)
def create_fleet(ai_settings,screen,aliens):
    """创建外星人人群"""
    #创建一个外星人，并计算一行可以容纳多少个外星人
    #外星人间距为外星人宽度
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width -2*alien_width
    number_aliens_x = int(available_space_x/(2*alien_width))

    for alien_number in range(number_aliens_x):
        #创建一个外星人并将其假如当前行
        alien = Alien(ai_settings,screen)
        alien.x = alien_width +2*alien_width*alien_number
        alien.rect.x = alien.x
        aliens.add(alien)


