# 第5回: Pythonとpygame-ceでの描画入門

```{note}
この回のゴール:
1. pygame-ceでウィンドウを開ける
2. 背景色と図形（円・四角形）を描ける
3. スクリーンショットをLMSに提出できる
```

## 環境セットアップ (Windows 11, Miniforge)

ターミナルで以下を実行してください:

```bash
conda create -n pgce-env python=3.11 pip
conda activate pgce-env
python -m pip install --upgrade pip
python -m pip install pygame-ce
```

## 最初のプログラム

```python
import pygame
pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Lesson 1")
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((220, 220, 220))  # 背景色

    pygame.draw.circle(screen, (0, 0, 255), (200, 200), 30)   # 円
    pygame.draw.rect(screen, (255, 0, 0), (50, 50, 80, 80))   # 四角形

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

## 座標系について

- 画面左上が (0,0)
- 右方向が x+
- 下方向が y+

この座標は今後、物理シミュレーションでもそのまま使います。

# 課題 (LMSに提出)

背景色・円・四角形の色やサイズを変えて、自分なりの画像にする

実行中のウィンドウをスクリーンショットして提出する

