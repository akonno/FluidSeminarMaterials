import pygame

# 初期化
pygame.init()

# 400ピクセル×400ピクセルのウィンドウをつくる
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PyGame-CE Program sample: colored rects")

clock = pygame.time.Clock()
running = True
font = pygame.font.SysFont(None, 16)  # 標準フォント・サイズ36

# メインループ
while running:
    # 1. イベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # ウィンドウ右上の×で終了
        # 教員用ホットキー: Sキーでスクショ保存
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            pygame.image.save(screen, "colorsample.png")
            print("Saved screenshot to colorsample.png.")
        # 教員用ホットキー: 終了
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            running = False

    # 2. 背景を塗る
    screen.fill((220, 220, 220))  # R,G,B [0-255]

    x = 25
    y = 25

    for rgb in ((255, 0, 0), (0, 255, 0), (0, 0, 255),
                (255, 255, 0), (255, 0, 255), (0, 255, 255), \
                (0, 0, 0), (128, 128, 128), (255, 255, 255)):
        
        text_surface = font.render(f'RGB: {rgb}', True, (0, 0, 0))
        screen.blit(text_surface, (x, y-16))
        # 四角形 (幅100, 高さ100)
        pygame.draw.rect(screen, rgb, (x, y, 100, 100))
        x += 125
        if x >= WIDTH:
            x = 25
            y += 125

    # 画面を反映
    pygame.display.flip()

    # 5. フレームレート制御 (1秒あたり60フレーム程度)
    clock.tick(60)

# 終了処理
pygame.quit()