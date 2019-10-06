"""
                飞机的基类
我方飞机  敌方的小飞机  敌方的中飞机  敌方的大飞机
"""
import random

import pygame
import PlaneWar.constants as constants
from PlaneWar.game.bullet import Bullet


class Plane(pygame.sprite.Sprite):
    """
    飞机的基类
    """
    # 飞机的图片
    plane_images = []
    # 飞机爆炸图片
    destroy_images = []
    # 坠毁的音乐地址
    down_sound_src = None
    # 飞机的状态 True活得 False 死的
    activate = True
    # 该飞机发射的子弹精灵组
    bullets = pygame.sprite.Group()

    def __init__(self, screen, speed=None):
        super().__init__()
        self.screen = screen
        # 加载的静态资源
        self.img_list = []
        self._destroy_img_list = []
        self.down_sound = None
        self.load_src()
        # 飞机飞行的速度
        self.speed = speed or 10
        # 获取飞机的位置
        self.rect = self.img_list[0].get_rect()

        self.p_width, self.p_height = self.img_list[0].get_size()
        # 界面的宽度和高度
        self.s_width, self.s_height = screen.get_size()

        # 改变飞机的初始位置
        self.rect.left = int((self.s_width - self.p_width) / 2)
        self.rect.top = int(self.s_height / 2)

    def load_src(self):
        """加载静态资源"""
        # 飞机图像
        for img in self.plane_images:
            self.img_list.append(pygame.image.load(img))
        # 飞机坠毁的图像
        for img in self.destroy_images:
            self._destroy_img_list.append(pygame.image.load(img))
        # 坠毁音乐
        if self.down_sound_src:
            self.down_sound = pygame.mixer.Sound(self.down_sound_src)

    @property
    def image(self):
        return self.img_list[0]

    def blit_me(self):
        self.screen.blit(self.image, self.rect)

    def move_up(self):
        """飞机向上移动"""
        self.rect.top -= self.speed

    def move_down(self):
        """飞机向下移动"""
        self.rect.top += self.speed

    def move_left(self):
        """飞机向左移动"""
        self.rect.left -= self.speed

    def move_right(self):
        """飞机向右移动"""
        self.rect.left += self.speed

    def broken_down(self):
        """飞机坠毁效果"""
        # 1、播放坠毁音乐
        if self.down_sound:
            self.down_sound.play()
        # 2、坠毁的动画
        for img in self._destroy_img_list:
            self.screen.blit(img, self.rect)
        # 3、坠毁后
        self.activate = False

    def shoot(self):
        """飞机发射子弹"""
        bullet = Bullet(self.screen, self, 15)
        self.bullets.add(bullet)


class OurPlane(Plane):
    """我方的飞机"""
    plane_images = constants.OUR_PLANE_IMG_LIST
    # 飞机爆炸图片
    destroy_images = constants.OUR_DESTROY_IMG_LIST
    # 坠毁的音乐地址
    down_sound_src = None

    def update(self, war):
        # 更新飞机的动画效果
        self.move(war.key_down)
        # 1、切换飞机的动画效果
        if war.frame % 5:
            self.screen.blit(self.img_list[0], self.rect)
        else:
            self.screen.blit(self.img_list[1], self.rect)

        # 2、飞机撞击检测
        rest = pygame.sprite.spritecollide(self, war.enemies, False)
        if rest:
            # 1、游戏结束
            war.status = war.OVER
            # 2、敌方的飞机清除
            war.enemies.empty()
            war.small_enemies.empty()
            # 3、我方飞机坠毁效果
            self.broken_down()
            # 4、记录游戏成绩

    def move(self, key):
        """飞机移动自动控制"""
        if key == pygame.K_w or key == pygame.K_UP:
            self.move_up()
        elif key == pygame.K_s or key == pygame.K_DOWN:
            self.move_down()
        elif key == pygame.K_a or key == pygame.K_LEFT:
            self.move_left()
        elif key == pygame.K_d or key == pygame.K_RIGHT:
            self.move_right()

    def move_up(self):
        super().move_up()
        if self.rect.top <= 0:
            self.rect.top = 0

    def move_down(self):
        super().move_down()
        if self.rect.top >= self.s_height - self.p_height:
            self.rect.top = self.s_height - self.p_height

    def move_left(self):
        super().move_left()
        if self.rect.left <=0:
            self.rect.left = 0

    def move_right(self):
        super().move_right()
        if self.rect.left >= self.s_width - self.p_width:
            self.rect.left = self.s_width - self.p_width


class SmallEnemyPlane(Plane):
    """地方小型飞机类"""
    # 飞机的图片
    plane_images = constants.SMALL_ENEMY_PLANE_IMG_LIST
    # 飞机爆炸图片
    destroy_images = constants.SMALL_ENEMY_DESTROY_IMG_LIST
    # 坠毁的音乐地址
    down_sound_src = constants.SMALL_ENEMY_PLANE_DOWN_SOUND

    def __init__(self, screen, speed):
        super().__init__(screen, speed)
        # 每次生成新的小型飞机时，随机位置生成
        self.inti_pos()

    def update(self, *args):
        """
        更新飞机的移动
        :param args:
        :return:
        """
        super().move_down()
        # 画在屏幕上
        self.blit_me()
        # 超出范围时如何处理
        # 1、重用
        if self.rect.top >= self.s_height:
            self.activate = False
            self.reset()
            # self.kill()
        # 2、多线程、多进程

    def inti_pos(self):
        # 屏幕的宽度减去飞机宽度
        self.rect.left = random.randint(0, self.s_width - self.p_width)
        # 屏幕之外随机高度
        self.rect.top = random.randint(-5 * self.p_height, -self.p_height)

    def reset(self):
        """重置飞机的状态，达到服用的效果"""
        self.activate = True
        self.inti_pos()

    def broken_down(self):
        """飞机爆炸"""
        super().broken_down()
        self.reset()