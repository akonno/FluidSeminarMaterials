# JupyterLabの導入と基本操作

MiniforgeにJupyterLabを導入し、Pythonプログラムを記述・実行するための基本操作を確認する。

## JupyterLabとは何か

JupyterLabは、ブラウザ上でPythonのコードを実行できる開発環境である。コード、実行結果、説明文、数式、図表などをまとめて扱えるため、学習記録や実験結果の整理にも利用できる。

JupyterLabでは、Notebook、テキストエディタ、ターミナルなどをタブやペインに並べて操作できる。NumPyやMatplotlibなどのパッケージと組み合わせれば、数値計算や可視化も行える。

## JupyterLabをインストールして起動する

Miniforge Promptを起動し、`EXERCISE`環境を有効にする。次のコマンドでJupyterLabと日本語language packをconda-forgeから導入する。

```powershell
conda activate EXERCISE
conda install -c conda-forge jupyterlab jupyterlab-language-pack-ja-jp
```

上の操作は、手動で作成する方法で`EXERCISE`環境を準備した場合に行う。`environment.yml`から授業用環境を作成した場合は、JupyterLabと日本語language packがすでにインストールされているため、このインストール操作は不要である。いずれの場合も、`conda activate EXERCISE`の後に`jupyter lab`を実行して起動する。

インストール後、次のコマンドでJupyterLabを起動する。

```powershell
jupyter lab
```

ブラウザが自動で開かない場合は、Miniforge Promptに表示された`http://localhost:8888/lab?...`または`http://127.0.0.1:8888/lab?...`のURLをブラウザで開く。

```{figure} ../images/jupyterlab01en.png
:align: center
:label: fig-jupyterlab1en
JupyterLabを起動した画面。
```

## JupyterLabを日本語で表示する

日本語language packをインストールした後、JupyterLabのSettings → Languageから日本語を選ぶ。「Change and reload」が表示された場合はクリックして画面を更新する。

```{figure} ../images/media/image31.png
:align: center
:label: fig-jupyterlab31
Settings → Languageから日本語を選択する画面。
```

```{figure} ../images/media/image32.png
:align: center
:label: fig-jupyterlab32
日本語を選択した後に表示される画面。
```

```{figure} ../images/media/image33.png
:align: center
:label: fig-jupyterlab33
日本語化されたJupyterLabの画面。
```

## LauncherからNotebookを作成する

JupyterLabのLauncherにある「Notebook」から「Python 3 (ipykernel)」を選ぶと、新しいNotebookを作成できる。

```{figure} ../images/jupyterlab01.drawio.png
:align: center
:label: fig-jupyterlab1ja
Launcherの「Notebook」から「Python 3 (ipykernel)」を選ぶ。
```

```{figure} ../images/media/image16.png
:align: center
:label: fig-jupyterlab2
新しいNotebook。Notebookは`.ipynb`形式で保存され、セルにコードを記述する。
```

## セルを実行する

コードセルにPythonコードを記述し、上部の実行ボタンをクリックする。実行結果はセルの下に表示される。

```{figure} ../images/jupyterlab03.drawio.png
:align: center
:label: fig-jupyterlab3
コードセルを実行している例。
```

Notebookの内容やMarkdownセルについては、[Notebookの使い方](./notebook)を参照する。

## ファイルを操作する

JupyterLab左側のファイルブラウザーでは、フォルダーやファイルを作成、移動、名前変更、削除できる。新しく作ったNotebookの名前は`Untitled.ipynb`になることがあるため、内容が分かる名前に変更して保存する。

```{figure} ../images/jupyterlab06f.drawio.png
:align: center
:label: fig-jupyterlab6
ファイルブラウザーが表示されていないときは、左のフォルダーアイコンをクリックする。
```

```{figure} ../images/jupyterlab07.drawio.png
:align: center
:label: fig-jupyterlab7
ファイルブラウザーでファイル名を右クリックして名前を変更する。
```

```{figure} ../images/jupyterlab08.drawio.png
:align: center
:label: fig-jupyterlab8
「名前を変更」を選んでファイル名を変更する。削除するときは「Move to Trash」を選ぶ。
```

```{figure} ../images/jupyterlab09.drawio.png
:align: center
:label: fig-jupyterlab9
ファイル名が変更されたことを確認する。
```

Notebookのダウンロード、アップロード、Markdownによるレポート作成は、[Notebookの使い方](./notebook)で説明する。

## ライセンス

```{note}
このページの本文と自作図版は [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.ja) のもとで提供されています。
コードやノートブックの例は MIT License に従います。
第三者の著作物を含む一部のスクリーンショット等は、CC BY-NC-SA 4.0の適用対象外です。詳細は [LICENSE-docs.md](https://github.com/akonno/FluidSeminarMaterials/blob/main/LICENSE-docs.md) を参照してください。
```
