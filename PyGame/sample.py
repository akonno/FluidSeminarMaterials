import pygame
import random
import time

from bouncingballs import World, Ball

def main():
    pygame.init()

    WIDTH = 800
    HEIGHT = 600
    FPS = 60

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("bouncingballs.py test")

    clock = pygame.time.Clock()

    # Worldを作成（反発係数 e=0.9 など）
    world = World(width=WIDTH, height=HEIGHT, restitution=0.9)

    # ランダムなボールをいくつか投入
    # m<0 は無効扱いなので、ここは正の質量を入れる。:contentReference[oaicite:2]{index=2}
    for _ in range(10):
        r = random.uniform(10, 30)
        m = r * 0.5  # 適当に「半径に比例した質量」など
        x = random.uniform(r, WIDTH - r)
        y = random.uniform(r, HEIGHT - r)
        vx = random.uniform(-200, 200)  # px/s
        vy = random.uniform(-200, 200)  # px/s
        color = (
            random.randint(50, 255),
            random.randint(50, 255),
            random.randint(50, 255),
        )
        world.add_ball(Ball(x=x, y=y, vx=vx, vy=vy, r=r, m=m, color=color))

    # 残像効果を使ってみたい場合は True にする
    use_trail = True

    running = True
    prev_time = time.perf_counter()

    while running:
        # 経過時間 dt[s] を計算
        now = time.perf_counter()
        dt = now - prev_time
        prev_time = now

        # イベント処理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # 左クリックで新しいボールを追加する例
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = pygame.mouse.get_pos()
                r = random.uniform(10, 20)
                m = r * 0.5
                vx = random.uniform(-150, 150)
                vy = random.uniform(-150, 150)
                color = (
                    random.randint(50, 255),
                    random.randint(50, 255),
                    random.randint(50, 255),
                )
                world.add_ball(Ball(x=mx, y=my, vx=vx, vy=vy, r=r, m=m, color=color))

        # 物理ステップを進める
        # step() 内で:
        #  - 改良Euler法による位置・速度の更新
        #  - 壁反射
        #  - 多球衝突(反発係数eと質量による速度更新)
        # が走る。:contentReference[oaicite:3]{index=3}
        world.step(dt)

        # 画面を更新
        if use_trail:
            # 前フレームの残像を少しずつ白で飛ばす（fadeToWhite相当の再現）
            # 元のbouncingballs.jsのfadeToWhite()は白半透明の矩形を重ねていた。:contentReference[oaicite:4]{index=4}
            world.draw_trail_overlay(screen, alpha=30)
        else:
            # 普通に背景を塗りつぶす
            screen.fill((255, 255, 255))

        # ボールを描画
        world.draw(screen)

        # 画面を反映
        pygame.display.flip()

        # フレームレートをある程度で固定
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
