# 発展：bouncingballs.pyで物理シミュレーションを作る

## このページの目的

このページでは、`bouncingballs.py`を使って複数のボールが動く世界を作る方法を紹介する。完成したゲームを配布することが目的ではなく、画面上の物体、時間の進み方、外力、衝突、描画をどのように分けて考えるかを知るための発展資料である。

このページは必修の手順ではない。コードの一部だけを使ったり、数字を変えたり、構造を参考にして別の作品を作ったりしてよい。

```{figure} ./images/media/bb-sample.png
:align: center
:label: fig-bb-1
`bouncingballs.py`と`bb-sample.py`によるボールの運動描画例。
```

## bouncingballs.pyの全体像

`bouncingballs.py`は、pygame-ceで複数のボールを扱うための小さな物理エンジンである。主な役割は次のとおりである。

- `Ball`：位置、速度、半径、質量、色など、一つのボールの状態を保持する
- `World`：画面の大きさ、ボールの集合、時間発展、壁反射、衝突、描画を管理する
- `force()`：各ボールに働く外力を差し替えるためのフック
- `step(dt)`：時間を`dt`秒進める
- `draw(surface)`：現在のボールを画面へ描画する

更新処理と描画処理を分けることで、「世界のルール」と「画面にどう見せるか」を別々に考えられる。

## BallとWorld

`Ball`はデータクラスであり、ボールの状態を一つにまとめている。

```python
from bouncingballs import Ball, World

world = World(width=800, height=600, restitution=0.9)
world.add_ball(
    Ball(x=200, y=100, vx=150, vy=0, r=20, m=10, color=(255, 50, 50))
)
```

`x`と`y`は位置、`vx`と`vy`は速度、`r`は半径、`m`は質量である。座標はpygameの標準に合わせ、左上を原点とし、右向きと下向きを正とする。

## Worldを作る

`World`には画面の幅と高さ、反発係数を与える。反発係数`restitution`は、衝突時にどの程度跳ね返るかを表す値である。

```python
world = World(width=800, height=600, restitution=0.9)
```

メインループでは、pygameの時計から経過時間を秒単位で取り出し、`step(dt)`で世界を進め、`draw(screen)`で描画する。

```python
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dt = clock.tick(60) / 1000.0
    world.step(dt)
    screen.fill((255, 255, 255))
    world.draw(screen)
    pygame.display.flip()
```

## ボールを追加する

複数のボールを追加すると、`World`がそれぞれの時間発展と衝突をまとめて処理する。

```python
world.add_ball(Ball(x=200, y=100, vx=150, vy=0,
                    r=20, m=10, color=(255, 50, 50)))
world.add_ball(Ball(x=400, y=150, vx=-50, vy=30,
                    r=30, m=20, color=(50, 255, 50)))
world.add_ball(Ball(x=500, y=200, vx=0, vy=-80,
                    r=25, m=15, color=(50, 50, 255)))
```

マウスクリックのイベントを使えば、クリックした位置に新しいボールを追加できる。

```python
if event.type == pygame.MOUSEBUTTONDOWN:
    mx, my = pygame.mouse.get_pos()
    world.add_ball(
        Ball(x=mx, y=my, vx=0, vy=0, r=15, m=10, color=(255, 255, 0))
    )
```

## `force()`による力のモデル

`World.force()`は、ボールに働く外力を返すメソッドである。標準の`World`では外力は`(0.0, 0.0)`であり、重力やばねなどを自分で追加できる。

```python
def force(self, i, x_list, y_list, vx_list, vy_list):
    return (0.0, 0.0)
```

`step(dt)`は、現在の位置・速度と`force()`の値から時間を進める。実装では改良Euler法を使い、壁反射とボール同士の衝突も処理する。

## 重力を加える

`World`を継承し、`force()`を上書きすると、重力のある世界を作れる。

```python
from bouncingballs import World

class GravityWorld(World):
    def force(self, i, x_list, y_list, vx_list, vy_list):
        g = 400.0
        m = self.balls[i].m
        return (0.0, m * g)

world = GravityWorld(width=800, height=600, restitution=0.8)
```

pygameでは下向きが正なので、`fy`に正の値を与えると下向きの重力になる。画面上の単位はピクセルを基準にしているため、`g`は動きが分かりやすくなるように設定する。

## ばねと減衰

ばねの力と速度に比例する抵抗を組み合わせると、ボールが初期位置の周囲で揺れ、次第に落ち着く世界を作れる。

```python
class SpringWorld(World):
    def __init__(self, width, height, restitution=0.9):
        super().__init__(width, height, restitution)
        self.x0 = []
        self.y0 = []

    def add_ball(self, ball):
        super().add_ball(ball)
        self.x0.append(ball.x)
        self.y0.append(ball.y)

    def force(self, i, x_list, y_list, vx_list, vy_list):
        k = 50.0
        c = 5.0
        dx = x_list[i] - self.x0[i]
        dy = y_list[i] - self.y0[i]
        return (-k * dx - c * vx_list[i],
                -k * dy - c * vy_list[i])
```

`k`を大きくするとばねが強くなり、`c`を大きくすると動きが早く減衰する。数値を変えて、動きの違いを確認してみよう。

## 残像を描く

`draw_trail_overlay()`は、前のフレームを白い半透明の面で少しずつ覆い、軌跡が残って見える効果を作る。

```python
# メインループに入る前に、背景を一度だけ初期化する
screen.fill((255, 255, 255))

# メインループ内（残像を使う場合）
world.draw_trail_overlay(screen, alpha=20)
world.draw(screen)
pygame.display.flip()
```

残像を使うフレームでは、`draw_trail_overlay()`の前に`screen.fill()`を実行しない。半透明の面で前フレームを少しずつ覆ってから、現在のボールを描画することで軌跡が残る。残像を使わず画面を毎フレーム消去する場合は、`screen.fill()`で背景を塗り直してから`world.draw()`を呼ぶ。

`alpha`を小さくすると長い軌跡が残り、大きくすると早く消える。

## 自分のWorldを作る

`World`を継承して、`force()`を変更すると、重力、ばね、風、抵抗、ボール同士の相互作用などを組み合わせられる。まずは既存の`GravityWorld`や`SpringWorld`の値を変え、次に自分のクラスを作ってみるとよい。

制作の過程では、次の点を自分の言葉で説明できるようにする。

- どのような世界を作ったか
- どのような力を加えたか
- ボールの動きや衝突をどのように変えたか
- どの入力や視覚効果を加えたか

## 発展課題・応用例

`bouncingballs.py`を使い、独自の世界を作成してみよう。`World`を継承したクラスを作り、`force()`を上書きして独自の物理を与える。マウスクリックやキー入力などのインタラクション、色・残像・サイズ変化などの視覚的な工夫も加えられる。

自由制作として提出する場合は、実行用スクリプト、必要な追加ファイル、作品の説明を一つのフォルダーにまとめる。提出方法や期限は、担当者から示された指示に従う。

## bouncingballs.pyへのリンク

- [`bouncingballs.py`](https://github.com/akonno/FluidSeminarMaterials/blob/main/PyGame/bouncingballs.py)
- [`bb-sample.py`](https://github.com/akonno/FluidSeminarMaterials/blob/main/PyGame/bb-sample.py)

上の2つのファイルを同じフォルダーに置き、`bb-sample.py`を実行すると、ボールが跳ね返りながら運動するシミュレーションを表示できる。

## ライセンス

```{note}
このページの本文と自作図版は [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.ja) のもとで提供されています。
コードやノートブックの例は MIT License に従います。
第三者の著作物を含む一部のスクリーンショット等は、CC BY-NC-SA 4.0の適用対象外です。詳細は [LICENSE-docs.md](https://github.com/akonno/FluidSeminarMaterials/blob/main/LICENSE-docs.md) を参照してください。
```
