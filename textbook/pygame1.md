# PyGame-CEによるインタラクティブ表現入門その1：PyGame-CEのインストールと実行

```{note}
この回のゴール:
1. pygame-ceでウィンドウを開ける
2. 背景色と図形（円・四角形）を描ける
3. スクリーンショットをLMSに提出できる
```

## PyGameとPyGame-CEについて

**PyGame**（パイゲーム） は，Pythonというプログラミング言語でゲームやアニメーションを作るためのライブラリである．
ウィンドウを開いて図形を描いたり，マウスやキーボードの操作に反応させたり，音を鳴らしたりすることができる．
**PyGame-CE**（Community Edition） はPyGameを継承して改良を加えたコミュニティ版であり，最新のPython環境で安定して動作し，新しい機能も追加されている．
教育や創作の場で使いやすく，現在も開発が続けられている実用的な基盤である．

PyGame-CEを使うと，プログラムで動く世界を作ることができる．
画面上で形を動かしたり，操作に反応させたりしながら，動きの仕組みを直感的に学べる．
この教材ではPyGame-CEを使い，いくつかの演習を通じて，最終的に自分だけのインタラクティブアートや簡単なゲームを作ることを目指す．この教材に書かれている範囲を超えて自由に試し，動かしながら，プログラムで世界を作る感覚を楽しんでほしい．


## 環境セットアップ (Windows 11 + Miniforge)

Miniforge Promptを開き，EXERCISE環境に入って，以下のコマンドを実行する．PyGame-CEは`conda`ではインストールできないので（2025年11月現在），`pip`を用いてインストールする．

```powershell
conda activate EXERCISE     # EXERCISE環境に入る
python -m pip install --upgrade pip     # pipを最新版にアップグレード
python -m pip install pygame-ce         # pygame-ceをインストール
```

**pip**（ピップ） は，Pythonの外部ライブラリを追加・管理するための仕組みである．
conda と同じような役割をもつが，両者は参照しているリポジトリ（配布元）が異なる．
pipのほうがより多くのライブラリを扱える一方で，condaほど厳密には管理されていない場合もある．
そのためMiniforgeを用いている場合は，まずはcondaでインストールを試み，見つからないものをpipで導入する，という使い分けが一般的である．

必要なパッケージがインストールできたか，次のコマンドを実行して確認せよ．

```powershell
python -c "import sys, pygame; print(sys.version); print(pygame.version.ver)"
```

- Pythonのバージョンと pygame-ce のバージョンが表示されれば，適切にインストールできている．

### PyGame-CEのサンプルを実行

PyGame-CEにはゲームや画面表示のサンプルがいくつか付属しているので，正しくインストールできているかどうかをサンプルプログラムにより確認できる．たとえば以下のコマンドを実行して確認せよ．（最初の2つは音が出るので注意！）

```powershell
python -m pygame.examples.aliens
python -m pygame.examples.chimp
python -m pygame.examples.moveit
python -m pygame.examples.stars
```

## JupyterLabをエディタとして使う

### エディタ（テキストエディタ）とは

**エディタ（テキストエディタ）** とは，文字だけで書かれた文章やプログラムのコードを編集するためのソフトウェアである．
文書作成ソフトのような装飾機能はなく，文字を入力し，修正し，必要に応じて保存することに特化している．
プログラミングでは，エディタを使ってコードを記述し，それを実行して結果を確かめながら，少しずつ内容を整えていく．
コードがファイルとして保存されていれば，あとから再利用や改良もできる．

エディタは「プログラムを書くためのノート」であり，**考えを形にする入口**であるといえる．
どの言語を使う場合でも，エディタを自在に扱えることは，プログラミングの第一歩である．

現在，プログラミングには専用のエディタを用いるのが一般的である．
その中でも **Visual Studio Code（VS Code）** は最も広く使われており，多くの言語に対応し，拡張機能やデバッグ支援などが充実している．
本格的なプログラミングを行う際には，VS Codeの利用を推奨する．

ただし，本教材では環境構築の確実さと手軽さを重視し，すでに導入済みの **JupyterLab** に含まれるテキストエディタを用いる．
JupyterLabのエディタは軽量で安定しており，Pythonのコードを編集・保存し，同じ環境のターミナルからそのまま実行できる．
これにより，追加の設定を行うことなく，すぐにプログラミングの学習を始めることができる．

### スクリプトとは

Pythonのプログラムは，しばしば スクリプト（script） と呼ばれる．
これは，コンピュータに実行させたい手順を上から順に書いた「指示の台本」のようなものである．
スクリプトという言葉には，「自動的に処理を進めるための短いプログラム」という意味があり，Pythonのように手軽に実行できる言語に多く使われる．

つまり，Pythonのプログラムを書くことは，コンピュータにやらせたいことを順に書き並べたスクリプトを作ることである．

### JupyterLabのエディタとしての使い方

今回はJupyterLabをエディタとして使い，それとは別にMiniforge PromptでPythonプログラムを実行する．そのため，先ほど起動したMiniforge Promptとは別にもう一つ，Miniforge Promptを起動して，JupyterLabを起動する．手順は以前の教材で説明しているので，ここでは省略する．

```{figure} ./images/editor01.drawio.png
:align: center
:label: fig-jl-editor1
JupyterLabの画面．Pythonファイルを置きたい場所まで移動し（①），下段の「その他」のところにある「Pythonファイル」（②）をクリックする．
またはメニューからファイル --> 新規 --> Pythonファイルを選択しても良い．
```

```{figure} ./images/media/jupyterlab-editor3.png
:align: center
:label: fig-jl-editor3
untitled1.pyというファイルが作られ，その画面が開く．ファイル名を変えたいときは，ファイルブラウザーのファイル名を右クリックし「名前を変更」を選ぶ．前の教材で説明したとおりである．
```

```{figure} ./images/media/jupyterlab-editor6.png
:align: center
:label: fig-jl-editor6
実行したいプログラムを書く．
```

```{figure} ./images/editor04.drawio.png
:align: center
:label: fig-jl-editor4
JupyterLab Notebookのセルとは異なり，ファイルを保存しないと実行できない．メニューからファイル --> Python Fileを保存 を選び，保存する．
```

Miniforge Promptからいま書いたプログラムを実行してみよ．以下の例ではプログラムを`pytest1.py`というファイルに保存した場合である．

```powershell
python pytest1.py
```

**そのファイルを保存した場所**で実行すること．`dir`コマンドでいまいるディレクトリにあるファイルを確認し，実行すること．（ディレクトリの移動には`cd`コマンドを用いる．詳細は適宜調べること．）そのファイルがある場所で実行しなかった場合やファイル名を間違えた場合には，`[Error 2] No such file or directory`というエラーが表示される．ファイルを保存したのにこのエラーが出るのは，たいていの場合そのファイルがある場所まで移動せずに実行した場合である．

```{figure} ./images/terminal1.drawio.png
:label: fig-pygame-terminal1
Miniforge Promptで，作成したプログラムを実行している例．白文字で表示されているのがユーザーが入力する文字列である．
①EXERCISE環境に入り，②プログラムを置いているディレクトリまで`cd`コマンドを使って移動する．③`dir`コマンドでそのファイルがあるかどうかを確認し（③'），④そのプログラムをpythonコマンドに与えて実行して，結果を確認する（④'）．
```


## PyGame-CEによる最初のプログラム（ウィンドウを開く・図形を描く）

新しいPythonファイルを作り，そこに以下のプログラムを保存して，実行してみよう．

```python
import pygame

# 初期化
pygame.init()

# 400ピクセル×400ピクセルのウィンドウをつくる
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PyGame-CE Program 1: basic drawing")

clock = pygame.time.Clock()
running = True

# メインループ
while running:
    # 1. イベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # ウィンドウ右上の×で終了

    # 2. 背景を塗る
    screen.fill((220, 220, 220))  # R,G,B [0-255]

    # 3. 図形を描く
    # 青い円 (x=200, y=200, 半径30)
    pygame.draw.circle(screen, (0, 0, 255), (200, 200), 30)

    # 赤い四角形 (x=50, y=50, 幅80, 高さ80)
    pygame.draw.rect(screen, (255, 0, 0), (50, 50, 80, 80))

    # 4. 画面を更新
    pygame.display.flip()

    # 5. フレームレート制御 (1秒あたり60フレーム程度)
    clock.tick(60)

# 終了処理
pygame.quit()
```

下図のような画面が表示されることを確認せよ．
プログラムの詳細は今後学ぶこととし，いまは説明しない．

```{figure} ./images/media/pygame-ss1.png
:align: center
:label: fig-pygame-ss1-1
プログラムを実行すると表示されるはずのウィンドウ
```

## 課題（なし）

この教材には課題は設定されていない．

## ライセンス

```{note}
このページの本文と図版は CC BY-NC-SA 4.0 とします．  
サンプルコードは MIT License とします．  
提出物（あなた自身のコードやスクリーンショット）は，ポートフォリオや就職活動で自由に使ってよいものとします．
```
