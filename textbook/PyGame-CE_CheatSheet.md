
# 🧭 PyGame-CE チートシート（開発者・教材制作用）

## 1. 基本構造
```python
import pygame
pygame.init()

# 画面を作る
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")

# 時計オブジェクト（フレーム制御）
clock = pygame.time.Clock()

running = True
while running:
    # 1. イベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. 更新（位置，情報など）
    # アニメーションしたいときなどは，ここで座標や変数を変える．

    # 3. 描画
    screen.fill((0, 0, 0))  # 背景を塗りつぶす
    pygame.draw.circle(screen, (255, 0, 0), (400, 300), 50)
    pygame.display.flip()   # 画面に反映

    # 4. フレームレート制御
    clock.tick(60)          # 60FPSに保つ

pygame.quit()
```

## 2. 画面・ウィンドウ
| 機能 | コード | 備考 |
|------|---------|------|
| ウィンドウ作成 | `pygame.display.set_mode((w,h))` | 引数はタプル |
| タイトル | `pygame.display.set_caption("Title")` | |
| 全画面表示 | `pygame.display.set_mode((0,0), pygame.FULLSCREEN)` | ESCで閉じられない場合あり |
| 表示更新 | `pygame.display.flip()` / `pygame.display.update()` | flipは全体更新 |

## 3. 色と座標
- 色: RGB タプル (0–255)
- 座標: 左上が (0,0)、右が＋x、下が＋y。

## 4. 図形描画関数
| 図形 | 構文 | 備考 |
|------|------|------|
| 線 | `pygame.draw.line(screen, color, start, end, width=1)` | |
| 円 | `pygame.draw.circle(screen, color, center, radius, width=0)` | |
| 楕円 | `pygame.draw.ellipse(screen, color, (x,y,w,h), width=0)` | |
| 矩形 | `pygame.draw.rect(screen, color, (x,y,w,h), width=0)` | |
| 多角形 | `pygame.draw.polygon(screen, color, point_list, width=0)` | |

`(x,y,w,h)`は描画する座標（図形の左上位置を指定）および幅と高さである．円は中心指定で描くが，楕円や矩形は左上位置の座標を指定する点に注意せよ．

`width`は線の太さを設定する．円などでwidth=0の場合は線で描画せず，塗りつぶしで描画する．

## 5. 入力処理
### キーボード
```python
for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            print("Space pressed")
```
### マウス
```python
mx, my = pygame.mouse.get_pos()
if pygame.mouse.get_pressed()[0]:
    print("左クリック中")
```

## 6. サウンド
```python
pygame.mixer.init()
sound = pygame.mixer.Sound("se.wav")
sound.play()
```

## 7. 当たり判定
```python
r1 = pygame.Rect(x1, y1, w1, h1)
r2 = pygame.Rect(x2, y2, w2, h2)
if r1.colliderect(r2):
    print("Hit!")
```

## 8. 推奨設定
```python
screen = pygame.display.set_mode((800, 600), pygame.SCALED | pygame.DOUBLEBUF | pygame.VSYNC)
```
