# MiniforgeではじめるPythonプログラミング

このページでは、Miniforgeを用いてWindows 11を主対象としたPython環境を導入する方法を説明する。Windows 10でも基本的な操作は同様である。

## Pythonとは

Pythonは、読みやすい文法と豊富なライブラリを持つプログラミング言語である。教育、科学技術計算、データ分析、可視化、Web開発、自動化など、さまざまな用途で利用されている。

科学技術計算では、NumPyやSciPy、グラフ描画ではMatplotlibやPlotlyなどのライブラリを利用できる。JupyterLabと組み合わせれば、コード、実行結果、説明文を一つのNotebookにまとめることもできる。

## Python環境を管理する理由

Python本体だけでなく、目的に応じて多くのパッケージを追加して利用する。プロジェクトごとに必要なパッケージやバージョンが異なるため、すべてを一つの環境に追加すると、パッケージ同士が干渉することがある。

環境を分けて管理すると、授業用、研究用、別のプロジェクト用に異なる構成を用意できる。既存の環境を壊さずに試行でき、同じ構成を再現しやすくなる。

## Miniforgeとは

### conda

condaは、Python本体やパッケージを導入し、独立した環境を作成・管理するためのツールである。Windowsでは、パッケージが依存するライブラリもまとめて扱える点に利点がある。

### conda-forge

conda-forgeは、コミュニティによって管理されているパッケージ配布チャネルである。科学技術計算や可視化に使うパッケージが幅広く用意されている。

### Miniforgeを教材で採用する理由

Miniforgeは、conda-forgeを標準的な入手先として利用する最小構成の配布形態である。本教材では、次の理由からMiniforgeを採用する。

- 必要なものを追加して使える軽量な構成である
- conda-forgeを標準かつ一貫して利用できる
- Anaconda Academic Programなどへの登録に依存せずに利用できる
- 教育、研究、卒業後など所属環境が変わっても同じ考え方を使いやすい
- 利用条件と環境管理の考え方を比較的単純に説明できる

AnacondaやMinicondaにもそれぞれの用途があり、AnacondaにはAcademic Programも用意されている。本教材では、特定の登録制度に依存しない構成と、conda-forgeを一貫して使える点を重視してMiniforgeを選んでいる。

## Miniforgeのインストール

### Miniforgeインストーラーのダウンロードと起動

Miniforgeインストーラーを以下のサイトからダウンロードしてインストールする。

<https://github.com/conda-forge/miniforge>

```{figure} ./images/media/image1.png
:alt: MiniforgeのGitHubサイト
:align: center
:label: fig-miniforge-github
MiniforgeのGitHubサイト。ページ下部の「Install」のところまで移動する。
```

```{figure} ./images/github-miniforge2.drawio.png
:align: center
:label: fig-miniforge-install-inst
「Install」の直下にWindowsでのインストール方法が記載されている。「the Windows installer」をクリックしてダウンロードし、実行する。
```

### Miniforgeのインストール

インストールの手順を以下に示す。特に「Destination Folder」に注意すること。

```{figure} ./images/media/image3.png
:align: center
:label: fig-miniforge-install-ss3
インストール開始画面。「Next」をクリックして進む。
```

```{figure} ./images/media/image4.png
:align: center
:label: fig-miniforge-install-ss4
ライセンス確認画面。内容を確認し、問題なければ「I Agree」をクリックして進む。
```

```{figure} ./images/media/image5.png
:align: center
:label: fig-miniforge-install-ss5
インストールタイプの選択。「Just Me」を選択し、「Next」をクリックして進む。
```

```{figure} ./images/miniforge-install4.drawio.png
:align: center
:label: fig-miniforge-install-ss6
インストール場所の選択。日本語などの非ASCII文字を含まないパスを選ぶ。例として `C:\miniforge3` のような場所を指定する。
```

適切なパスを選択したら、「Next」をクリックして進む。

```{figure} ./images/media/image7.png
:align: center
:label: fig-miniforge-install-ss7
インストール場所に問題がある場合に表示されるエラーメッセージの例。
```

```{figure} ./images/miniforge-install6.drawio.png
:align: center
:label: fig-miniforge-install-ss8
インストールオプション選択画面。必要に応じて推奨項目を選択する。
```

「Install」をクリックするとインストールが始まる。

```{figure} ./images/media/image9.png
:align: center
:label: fig-miniforge-install-ss9
インストール中の画面。
```

```{figure} ./images/media/image10.png
:align: center
:label: fig-miniforge-install-ss10
インストール終了時の画面。
```

```{figure} ./images/media/image11.png
:align: center
:label: fig-miniforge-install-ss11
インストール終了画面。「Finish」をクリックして終了する。
```

## Miniforge Prompt

### Miniforge Promptを起動する

インストールが成功すると、スタートメニューにMiniforge Promptが追加される。

```{figure} ./images/Startmenu-Miniforge.drawio.png
:align: center
:label: fig-miniforge-startmenu
スタートメニューから「Miniforge Prompt」を起動する。
```

```{figure} ./images/Miniforge-prompt1.drawio.png
:align: center
:label: fig-miniforge-prompt1
Miniforge Promptを起動した画面。入力したコマンドをEnterキーで実行する。
```

### バージョンを確認する

Miniforge Promptで次のコマンドを実行する。

```powershell
python --version
conda --version
```

Pythonのバージョンとcondaのバージョンが表示されれば、コマンドを実行できる状態である。

### Python REPLを使う

Miniforge Promptで`python`と入力すると、Pythonの対話実行環境（REPL）に入る。

```powershell
python
```

```python
print("Hello, Python!")
exit()
```

`>>>`が表示されている間はPythonの命令を受け付ける。`exit()`でPythonを終了し、Miniforge Promptに戻る。

```{figure} ./images/Miniforge-prompt2.drawio.png
:align: center
:label: fig-miniforge-prompt2
Miniforge PromptでPythonを起動した例。
```

## conda環境とは

conda環境は、同じPCの中に独立したPython実行環境を作る仕組みである。環境ごとにPythonのバージョンやパッケージを分けて管理できる。

## 授業用環境EXERCISEを作る

Miniforge Promptで、次のコマンドを一度だけ実行する。環境名は必要に応じて変更してよい。

```powershell
conda create -n EXERCISE python=3.14
```

途中で`Proceed ([y]/n)?`と表示されたら、内容を確認して`y`またはEnterキーを入力する。

このコマンドでは、教材で使用するPython 3.14環境を作成している。作成が完了すると、環境を有効化するコマンドが表示される。

## 環境を有効化・無効化する

作成した環境を使い始めるには、次のコマンドを実行する。

```powershell
conda activate EXERCISE
```

Miniforge Promptの表示に`(EXERCISE)`が付けば、その環境が有効になっている。

環境を終了するときは次のコマンドを実行する。

```powershell
conda deactivate
```

作成済みの環境を一覧表示するには、次のコマンドを使う。

```powershell
conda env list
```

## パッケージを追加する

パッケージは、まずconda-forgeからcondaで導入する。本教材で使う主要パッケージの例を示す。

```powershell
conda install -c conda-forge jupyterlab jupyterlab-language-pack-ja-jp ipykernel numpy scipy matplotlib pandas plotly
```

conda-forgeに必要なパッケージがない場合や、本教材が別途指定する場合に限りpipを使う。pygame-ceは本教材ではPyPIから導入する。

```powershell
python -m pip install pygame-ce
```

pygame-ceをインストールしても、Pythonコードでのimport名は`pygame`である。

## conda自身の更新について

condaから更新の案内が表示された場合は、内容を確認したうえで、必要に応じてbase環境のcondaを更新する。

```powershell
conda update -n base -c conda-forge conda
```

授業で使っている環境を不用意に変更したくない場合は、更新内容を確認してから実行すること。

## 参考：Pythonの主な配布方法

| 入手方法 | 概要 | 特徴 | 本教材との関係 |
|---|---|---|---|
| 公式配布（python.org） | CPython本体と標準ライブラリ | 軽量で標準的。追加パッケージはpipやvenvで管理する | Python本体を個別に使いたい場合に適する |
| Microsoft Store版 | Windows向けの導入方法 | 導入は容易だが、複数環境やパスの扱いを確認する必要がある | 本教材では使用しない |
| Anaconda / Miniconda | Anaconda社の配布形態 | Anacondaは多数のパッケージを含み、Minicondaは小さな構成。Academic Programもある | 本教材では採用しないが、用途に応じて利用できる |
| Miniforge | conda-forgeを標準とする最小構成 | 必要なものを追加し、環境を分けて管理しやすい | 本教材で採用する |

```{note}
このページの本文と自作図版は [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.ja) のもとで提供されています。
コードやノートブックの例は MIT License に従います。  
第三者の著作物を含む一部のスクリーンショット等は、CC BY-NC-SA 4.0の適用対象外です。詳細は [LICENSE-docs.md](https://github.com/akonno/FluidSeminarMaterials/blob/main/LICENSE-docs.md) を参照してください。
```
