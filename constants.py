import os

# 项目根目录
import pygame

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 静态文件的目录
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

# 背景图片
BG_IMG = os.path.join(ASSETS_DIR, "images/background.png")
BG_OVER_IMG = os.path.join(ASSETS_DIR, "images/game_over.png")
# 标题图片
IMG_GAME_TITLE = os.path.join(ASSETS_DIR, "images/game_title.png")
# 开始游戏的按钮
IMG_GAME_START_BTN = os.path.join(ASSETS_DIR, "images/game_start.png")
# 背景音乐
BG_MUSIC = os.path.join(ASSETS_DIR, "sounds/game_bg_music.mp3")
# 游戏分数颜色
TEXT_SCORE_COLOR = pygame.Color(255, 0, 0)
# 击中小型飞机分数
SCORE_SHOOT_SMALL = 10
# 游戏结果存储的文件地址
PLAY_RESULT_STORE_FILE = os.path.join(BASE_DIR, "store/rest.txt")

# 我放飞机的静态资源
OUR_PLANE_IMG_LIST = [
    os.path.join(ASSETS_DIR, "images/hero1.png"),
    os.path.join(ASSETS_DIR, "images/hero2.png")
]
OUR_DESTROY_IMG_LIST = [
    os.path.join(ASSETS_DIR, "images/hero_broken_n1.png"),
    os.path.join(ASSETS_DIR, "images/hero_broken_n2.png"),
    os.path.join(ASSETS_DIR, "images/hero_broken_n3.png"),
    os.path.join(ASSETS_DIR, "images/hero_broken_n4.png")
]

# 子弹图片
BULLET_IMG = os.path.join(ASSETS_DIR, "images/bullet1.png")
BULLET_SHOOT_SOUND = os.path.join(ASSETS_DIR, "sounds/bullet.wav")

# 敌方小型飞机静态资源
SMALL_ENEMY_PLANE_IMG_LIST = [os.path.join(ASSETS_DIR, "images/enemy1.png")]
SMALL_ENEMY_DESTROY_IMG_LIST = [
    os.path.join(ASSETS_DIR, "images/enemy1_down1.png"),
    os.path.join(ASSETS_DIR, "images/enemy1_down2.png"),
    os.path.join(ASSETS_DIR, "images/enemy1_down3.png"),
    os.path.join(ASSETS_DIR, "images/enemy1_down4.png")
]
# 敌方小型飞机音效
SMALL_ENEMY_PLANE_DOWN_SOUND = os.path.join(ASSETS_DIR, "sounds/enemy1_down.wav")