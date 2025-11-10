# JupyterLabの導入

MiniforgeにJupyterLabを導入し、かんたんなPythonプログラムを記述、実行するとともに、説明テキストを含めたノートブックの作成・提出を目指す。

## JupyterLabとは何か

JupyterLabはPythonの実行環境のひとつであり、ブラウザ上で利用することができる。コードを入力して実行すると、その結果がすぐに画面に表示され、さらに解説文や数式、図表などを同じファイルにまとめて保存できる点が特徴である。コードと結果、説明を一体化できるため、学習記録や研究の再現性確保に大きな利点を持つ。

JupyterLabでは、複数のノート、テキストエディタ、ターミナルなどをタブやペインとして自由に並べて扱うことができる。これにより、ひとつのブラウザ画面の中でコード実行、文章記述、ファイル操作を効率的に行える。NumPyやmatplotlibなどのライブラリと組み合わせることで、数値計算やデータの可視化を容易に実施でき、教育から研究まで幅広い場面で活用されている。

教育的な利点として、学生は自分が試したコードとその結果をまとめたノートを提出できるため、教員は過程と成果を同時に確認できる。学生自身にとっても作業履歴がそのままレポートとなり、学習内容を整理する助けとなる。研究活動においても、解析の手順と結果を記録し、卒業研究や論文執筆における再現性を高める手段として有効である。

もっとも、JupyterLabは主にデータ処理や可視化に適した環境であり、リアルタイムに描画を更新するゲームやインタラクティブアートの制作には不向きである。そのため、本講義では前半の演習環境としてJupyterLabを用いるが、後半では表現力の高い専用のライブラリや環境に移行する予定である。

## JupyterLabをはじめる

Miniforge
Promptを起動し、EXERCISE環境に入る。そこでjupyterlabパッケージをインストールする。ここではjupyterlabに加えて日本語パックjupyterlab-language-pack-ja-JPをインストールしている．

```powershell
conda install jupyterlab jupyterlab-language-pack-ja-JP
```

インストールに成功したら、jupyter
labコマンドを実行する。このときはjupyterとlabの間にスペースが入ることに注意。

```powershell
jupyter lab
```

初めて起動した際は、どのブラウザで開くかを問い合わせるウィンドウが開くはずである。ふだん使っているウェブブラウザを選べば良い。

もしブラウザが自動で開かなかった場合は、Miniforge
Promptの画面に以下のように表示されるので、
Ctrlキーを押しながらアドレスをクリックしてブラウザを起動する。どのアドレスをクリックしても良い。

```powershell
To access the server, open this file in a browser:
    file:///C:/Users/konno/AppData/Roaming/jupyter/runtime/jpserver-20560-open.html
Or copy and paste one of these URLs:
    http://localhost:8888/lab?token=d2dbc583f5df64abe28cf820ea5c5fcf1c8fcf5743fbe04c
    http://127.0.0.1:8888/lab?token=d2dbc583f5df64abe28cf820ea5c5fcf1c8fcf5743fbe04c
```

（初めて起動したときは、"Would you like to get notified about official
Jupyter
news?"という問い合わせパネルが表示されるかもしれない。適宜選択すれば良い。）

```{figure} ./images/jupyterlab01en.png
JupyterLabを起動した画面
```

## JupyterLabの日本語化

JupyterLabは日本語パックをインストールすると，日本語での表示に変更できる．JupyterLabの画面でSettings 🡪 Languageから日本語を選ぶ．

```{figure} ./images/media/image31.png
日本語パックを入れたあとで，Settings 🡪
Languageを選ぶと日本語が選択できるようになっている．
```

```{figure} ./images/media/image32.png
日本語を選択したとき表示される画面．"Change
and reload"をクリックすると画面が更新される．
```

```{figure} ./images/media/image33.png
日本語化された画面
```

## はじめてのJupyterLabプログラミング

JupyterLabが起動したら"Notebook"の"Python 3
(ipykernel)"をクリックして新しいノートブックを作成し、そこにコードを記入して実行してみよう。

```{figure} ./images/jupyterlab01.drawio.png
JupyterLabを起動した画面。"Notebook"の"Python 3
(ipykernel)"をクリックして新しいノートブックを作成する。
```

```{figure} ./images/media/image16.png
新しい「ノートブック」が作成される。JupyterLabのノートブックは
.ipynb
という形式のファイルで、JupyterLabの中で開いて編集・実行できる。ノートブックの中では、青く囲まれた「セル」にコードを書き込んで実行できる。
```

```{figure} ./images/jupyterlab03.drawio.png
コードを実行している例。セルにコードを書き込み、上段の►マークをクリックするとコードが実行される。
```

JupyterLabはPythonのコードを記述・実行できるだけでなく、Markdown（マークダウン）形式で文書を記述できる。このため作業レポートの作成や実行結果の記録・報告などに非常に役立つ。この授業でもレポートをJupyterLabのノートブックとして作成、提出してもらう予定なので、Markdownの基礎も習得してほしい。文末の「補足：Markdownの初歩（JupyterLab用）」を参考にせよ。

```{figure} ./images/jupyterlab04.drawio.png
Markdown形式で文書を書く方法
```

```{figure} ./images/jupyterlab05.drawio.png
Markdown形式で記述した文書をフォーマットして表示する方法
```

ノートブックのファイル名は"Untitled.ipynb"となっているはずである。（複数のノートブックを作っていた場合は、Untitled1.ipynbなど番号のついた名前になっているかもしれない。）ファイル名を変更するには、左側のファイルが表示されている部分で当該ファイルを右クリックして"Rename"する。

なお右クリックしたときにブラウザのメニューが表示され、RenameなどJupyterLabの操作ができないことがある。その場合は何度か右クリックして試してみよ。

KU-LMSでJupyterノートブックのサンプル（フィボナッチ数列）を配布しているので、それをJupyterLabで表示し、内容を確認せよ。

```{figure} ./images/jupyterlab06f.drawio.png
ファイルブラウザーが表示されていないときは，左のフォルダーアイコンをクリックする
```

```{figure} ./images/jupyterlab07.drawio.png
ノートブックのファイル名を変更する方法その1：ファイルブラウザーでファイル名を右クリック
```

```{figure} ./images/jupyterlab08.drawio.png
ノートブックのファイル名を変更する方法その2：「名前を変更」をクリックしファイル名を変更．なおファイルを削除したいときは"Move to Trash"を選択する
```

```{figure} ./images/jupyterlab09.drawio.png
ノートブックのファイル名が変更されたことを確認
```

```{figure} ./images/media/image22.png
サンプルとして配布しているフィボナッチ数列のノートブック
```

## 課題：最大公約数の求め方・ユークリッドの互除法

「ユークリッドの互除法」とは最大公約数を求める方法のひとつである。これについて以下の課題を実施せよ。

提出方法と提出期限はKU-LMSに掲載する。

1.  「ユークリッドの互除法」について調べよ。

2.  「ユークリッドの互除法」を説明するレポートを、JupyterLabのノートブックとして作成せよ。以下の内容を盛り込むこと。

    A)  「ユークリッドの互除法」の説明。適宜章立てして詳細に説明すること。

    B)  「ユークリッドの互除法」により、与えられた2つの数値の最大公約数を求めるPythonプログラム

    C)  上のプログラムより求められた、指定された2数値の最大公約数。指定数値はKU-LMSに掲載している。

3.  作成したノートブック（.ipynbファイル）を提出せよ。

```{figure} ./images/media/image23.png
最大公約数を求めるレポート課題のJupyterノートブック例（一部伏せ字）
```

## 補足：Markdownの初歩（JupyterLab用）

| 項目 | 書き方 | 備考 |
|------|----------|------|
| 文章 | そのままセルに記入 |  |
| 見出し | `# 大見出し`<br>`## 中見出し`<br>`### 小見出し` | 「#」の数でレベルを下げる。 |
| 箇条書き | `- 項目1`<br>`- 項目2`<br>&nbsp;&nbsp;`- サブ項目` | 「- 」や「* 」でリストになる。インデントで階層化できる。 |
| 番号付きリスト | `1. 一つ目`<br>`2. 二つ目` | 自動的に番号が振られる。 |
| 強調 | `*イタリック*`<br>`**太字**` | アスタリスクで囲む。 |
| リンク | `[リンクの文字](https://example.com)` |  |
| 画像 | `![代替テキスト](画像ファイルへのパス)` |  |
| コード表示（行内） | `` `print("Hello")` `` | バッククオートで囲む |
| コード表示（複数行） | ``` ```python<br>print("Hello")<br>``` ``` | バッククオート3個で囲む |
| 数式（行内） | `$E = mc^2$` | LaTeX 形式で数式を書ける。$...$ で囲む。 |
| 数式（ブロック数式） | `$$E = mc^2$$` | ブロック数式は $$ ... $$ で囲む。 |


```{figure} ./images/media/image24.png
JupyterLabのMarkdownセルにMarkdown形式で記入しフォーマットした例
```

# 配布されたJupyterLabノートブックを開くには

前回の授業で導入したMiniforgeとJupyterLabを用い，Pythonプログラミングを学習する．教材はJupyterLabノートブックとして配布するので，ここではダウンロードしたノートブックを自分のJupyterLabにアップロードする方法を説明する．

## GitHubからノートブックをダウンロード


これ以降では講義資料をJupyterLabノートブックとしてGitHubで配布するので，それを学習し，課題に取り組んでほしい．
ここではGitHubのJupyterLabノートブック配布サイトからノートブックをダウンロードする方法を示す．


```{figure} ./images/github-jupyterlab-notebook1.trimmed.png
GitHubのJupyterLabノートブック配布サイト．ダウンロードしたい資料をクリックする
```
```{figure} ./images/github-jupyterlab-notebook2.drawio.png
資料が表示される．右上のダウンロードボタンをクリックし，ダウンロードする
```


## 配布されたノートブックをアップロードして開く
ここでは配布されたノートブックを自分のJupyterLabにアップロードし，開く方法を示す．と言ってもGitHubからダウンロードしたファイルを，ファイルブラウザーにドラッグ＆ドロップして入れるだけなので，簡単である．

JupyterLabノートブック配布サイト：<https://github.com/akonno/FluidSeminarMaterials/tree/main/JupyterLab>

```{figure} ./images/jupyterlab01f.drawio.png
ファイルブラウザーが表示されていないときは，左上のフォルダーのアイコンをクリックして開く．
```

```{figure} ./images/jupyterlab10.drawio.png
今回は新しいフォルダーを作り，その中にノートブックやデータファイルをアップロードすることにする．そのためにはフォルダーに＋がついたマークをクリックする．
```

```{figure} ./images/jupyterlab11.drawio.png
新しいフォルダー（この例では"EXERCISE"）が作られたので，ダブルクリックして中に入る．
```

```{figure} ./images/jupyterlab12.drawio.png
"EXERCISE"に入っていることを確認し（①，②），ファイルブラウザーにアップロードしたいノートブックやファイルをドラッグアンドドロップする（③）．またはアップロードボタン（④）をクリックし，ノートブックやファイルをアップロードする．
```

```{figure} ./images/jupyterlab13ja.png
アップロードしたファイルがファイルブラウザーに表示される．見たいノートブックをダブルクリックする．
```

```{figure} ./images/jupyterlab14ja.png
ノートブックが表示される．実行結果も含めて保存されているノートブックであれば，実行結果のグラフなども（自分で実行しなくとも）表示される．
```

## 課題

1.  [GitHubで配布しているJupyterLabノートブック](https://github.com/akonno/FluidSeminarMaterials/tree/main/JupyterLab)「Matplotlibでグラフを描く」に掲載されている課題1および課題2に取り組み，作成したJupyterLabノートブックをKU-LMSから提出せよ．課題1と課題2を合わせてひとつのJupyterLabノートブックとすること．

2.  [GitHubで配布しているJupyterLabノートブック](https://github.com/akonno/FluidSeminarMaterials/tree/main/JupyterLab)「3次元のグラフを描く―Matplotlib
    /
    Plotly」に掲載されている課題に取り組み，作成したJupyterLabノートブックをKU-LMSから提出せよ．

提出期限はKU-LMSにて指示する．

```{note}
このページの本文と図版は [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.ja)
のもとで提供されています。  
コードやノートブックの例は MIT License に従います。  
一部の画像（表で「CC ライセンス適用外」と明記されたスクリーンショットなど）は除外されます。  
詳細は [LICENSE-docs.md](https://github.com/akonno/FluidSeminarMaterials/blob/main/LICENSE-docs.md) を参照してください。
```
