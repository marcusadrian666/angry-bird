import pygame
import random

# 初始化游戏
pygame.init()

# 设置窗口尺寸
width = 800
height = 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("愤怒的小鸟")

# 加载背景图片
background = pygame.image.load("background.png")

# 加载小鸟图片
bird_img = pygame.image.load("bird.png")
bird_width = bird_img.get_width()
bird_height = bird_img.get_height()

# 加载炮弹图片
bullet_img = pygame.image.load("bullet.png")
bullet_width = bullet_img.get_width()
bullet_height = bullet_img.get_height()

# 设置小鸟的初始位置
bird_x = 50
bird_y = height // 2 - bird_height // 2
bird_vel = 0

# 设置炮弹的初始位置和速度
bullet_x = width
bullet_y = random.randint(0, height - bullet_height)
bullet_vel = -5

# 设置得分
score = 0
font = pygame.font.Font(None, 36)

# 游戏主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 处理鼠标点击事件
            if bird_y >= bird_height:
                bird_vel = -10

    # 更新小鸟的位置
    bird_y += bird_vel
    bird_vel += 0.5

    # 更新炮弹的位置
    bullet_x += bullet_vel

    # 绘制背景
    win.blit(background, (0, 0))

    # 绘制小鸟
    win.blit(bird_img, (bird_x, bird_y))

    # 绘制炮弹
    win.blit(bullet_img, (bullet_x, bullet_y))

    # 绘制得分
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    win.blit(score_text, (10, 10))

    # 检测碰撞
    bird_rect = pygame.Rect(bird_x, bird_y, bird_width, bird_height)
    bullet_rect = pygame.Rect(bullet_x, bullet_y, bullet_width, bullet_height)
    if bird_rect.colliderect(bullet_rect):
        score += 1
        bullet_x = width
        bullet_y = random.randint(0, height - bullet_height)

    # 更新窗口
    pygame.display.update()

# 退出游戏
pygame.quit()
