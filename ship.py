import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,ai_settings,screen):
        """初始化飞船，并设置其实位置"""
        super(Ship,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings


        self.image = pygame.image.load('images/ship.png')#加载图片
        self.image = pygame.transform.scale(self.image, (50, 80))#调整飞船图片大小
        self.rect = self.image.get_rect() #获取rect
        self.screen_rect = screen.get_rect()

        # 将飞船放在屏幕中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #在飞船属性center中存储小数值
        self.center = float(self.rect.centerx)

        #移动标识符
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据标志调整飞船位置"""
        #更新飞船的center值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
            # self.rect.centerx += 1
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
            # self.rect.centerx -= 1

        # 根据self.center更新react对象
        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        """让飞船在屏幕居中"""
        self.center = self.screen_rect.centerx
