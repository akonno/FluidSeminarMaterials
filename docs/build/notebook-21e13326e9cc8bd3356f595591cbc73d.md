# Notebookの使い方

JupyterLabのNotebookは、コード、実行結果、説明文を一つのファイルにまとめるための文書形式である。このページでは、Notebookを使って説明と実行結果を含むレポートを作る方法を扱う。

## Notebookの基本

Notebookは、コードセルとMarkdownセルを組み合わせて作成する。コードセルではPythonを実行し、Markdownセルでは見出し、説明、リスト、リンク、数式などを記述する。

JupyterLabで新しいNotebookを作成すると、ファイルは`.ipynb`形式で保存される。コードを実行した結果もNotebookに保存できるため、プログラムだけでなく、考え方や結果を含む記録として利用できる。

## Markdownセル

Markdownセルを選択して、次のような記法を入力する。セルを実行すると、整形された文書として表示される。

| 項目 | 書き方 | 備考 |
|---|---|---|
| 文章 | そのままセルに記入 |  |
| 見出し | `# 大見出し`、`## 中見出し`、`### 小見出し` | `#`の数で階層を表す |
| 箇条書き | `- 項目1` | インデントで階層化できる |
| 番号付きリスト | `1. 一つ目` | 自動的に番号が振られる |
| 強調 | `*イタリック*`、`**太字**` |  |
| リンク | `[リンクの文字](https://example.com)` |  |
| 画像 | `![代替テキスト](画像ファイルへのパス)` |  |
| コード表示 | `` `print("Hello")` `` | 行内コード |
| 複数行コード | 3個のバッククォートで囲む | Pythonコードを表示 |
| 数式 | `$E = mc^2$`、`$$E = mc^2$$` | LaTeX形式 |

```{figure} ./images/jupyterlab04.drawio.png
:align: center
:label: fig-jupyterlab4
Markdown形式で文書を書く方法。
```

```{figure} ./images/jupyterlab05.drawio.png
:align: center
:label: fig-jupyterlab5
Markdown形式で記述した文書を表示する方法。
```

## Notebookを保存して名前を変更する

新しいNotebookのファイル名は`Untitled.ipynb`になることがある。ファイルブラウザーでファイル名を右クリックし、名前を変更して保存する。後から内容を確認しやすいように、目的が分かる名前を付ける。

## GitHubから配布Notebookをダウンロードする

配布Notebookは、GitHubのファイル一覧から対象ファイルを開き、ダウンロードボタンを使って保存する。

```{figure} ./images/github-jupyterlab-notebook1.trimmed.png
:align: center
:label: fig-jupyterlab13
GitHubのNotebook配布ページで、ダウンロードしたい資料を選ぶ。
```

```{figure} ./images/github-jupyterlab-notebook2.drawio.png
:align: center
:label: fig-jupyterlab14
Notebookを表示し、右上のダウンロードボタンをクリックする。
```

## JupyterLabへアップロードして開く

GitHubからダウンロードしたNotebookは、JupyterLabのファイルブラウザーへドラッグ＆ドロップするか、アップロードボタンから追加する。

配布Notebook：<https://github.com/akonno/FluidSeminarMaterials/tree/main/JupyterLab>

```{figure} ./images/jupyterlab01f.drawio.png
:align: center
:label: fig-jupyterlab15
ファイルブラウザーが表示されていないときは、左上のフォルダーアイコンをクリックして開く。
```

```{figure} ./images/jupyterlab10.drawio.png
:align: center
:label: fig-jupyterlab16
新しいフォルダーを作成し、その中にNotebookやデータファイルをアップロードする。
```

```{figure} ./images/jupyterlab11.drawio.png
:align: center
:label: fig-jupyterlab17
作成したフォルダーを開く。
```

```{figure} ./images/jupyterlab12.drawio.png
:align: center
:label: fig-jupyterlab18
Notebookやデータファイルをドラッグ＆ドロップするか、アップロードボタンをクリックする。
```

```{figure} ./images/jupyterlab13ja.png
:align: center
:label: fig-jupyterlab19
アップロードしたNotebookをファイルブラウザーから開く。
```

```{figure} ./images/jupyterlab14ja.png
:align: center
:label: fig-jupyterlab20
保存された実行結果を含むNotebookを表示した例。
```

## 配布Notebookに取り組む

配布Notebookを開いたら、説明を読み、コードセルを上から順に実行する。課題がある場合は、指定されたセルや課題文を確認し、自分のNotebookとして保存する。

## 配布Notebookを使った課題

```{admonition} 課題
:class: assignment
以下の配布Notebookの課題に取り組み、作成したNotebookをKU-LMSから提出する。「Matplotlibでグラフを描く」の課題1と課題2は、一つのNotebookにまとめること。

1. [「Matplotlibでグラフを描く」](https://github.com/akonno/FluidSeminarMaterials/blob/main/JupyterLab/Matplotlib%E3%81%A7%E3%82%B0%E3%83%A9%E3%83%95%E3%82%92%E6%8F%8F%E3%81%8F.ipynb)の課題1および課題2に取り組む。
2. [「3次元のグラフを描く―Matplotlib_Plotly」](https://github.com/akonno/FluidSeminarMaterials/blob/main/JupyterLab/3%E6%AC%A1%E5%85%83%E3%81%AE%E3%82%B0%E3%83%A9%E3%83%95%E3%82%92%E6%8F%8F%E3%81%8F%E2%80%95Matplotlib_Plotly.ipynb)の課題に取り組む。

提出方法と提出期限はKU-LMSで確認する。
```

## ライセンス

```{note}
このページの本文と自作図版は [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.ja) のもとで提供されています。
コードやノートブックの例は MIT License に従います。
第三者の著作物を含む一部のスクリーンショット等は、CC BY-NC-SA 4.0の適用対象外です。詳細は [LICENSE-docs.md](https://github.com/akonno/FluidSeminarMaterials/blob/main/LICENSE-docs.md) を参照してください。
```
