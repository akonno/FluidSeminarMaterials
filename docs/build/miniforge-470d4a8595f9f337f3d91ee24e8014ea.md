# MiniforgeではじめるPythonプログラミング

この文書ではMiniforgeを用いてWindows
10/11にPython環境を導入する方法を説明する。

2025年度授業終了後に要見直し．継ぎ足しで作ったため教材の順番が悪い．

## Pythonとは? Miniforgeとは?

### プログラミング言語Python

Pythonは現在、世界で最も広く使われているプログラミング言語の一つである。文法がシンプルで読みやすく、初心者でも学びやすいという特徴から、多くの学校や大学で入門用の言語として採用されている。加えて、豊富なライブラリや活発なコミュニティに支えられており、教育から最先端の研究、産業応用まで幅広く利用されている。主な応用分野を以下に示す。

データサイエンスと機械学習  
: Pythonにはデータ解析のためのライブラリ（Pandas, NumPy,
Scikit-learnなど）や、ディープラーニング向けのフレームワーク（TensorFlow,
PyTorch）が揃っている。これにより、大規模データの処理、予測モデルの構築、画像認識や自然言語処理などのタスクを容易に実現できる。

ウェブ開発  
: DjangoやFlaskなどのウェブフレームワークが広く使われており、堅牢かつ拡張性の高いウェブアプリケーションを効率的に開発できる。

科学技術計算と可視化  
: SciPyやMatplotlibなどのライブラリを利用することで、複雑な数値計算やシミュレーション、グラフ描画やデータ可視化が可能である。また、Jupyter
Notebook環境を用いることで、対話的に実験・解析を行いながら結果を共有できる。

自動化とスクレイピング  
: Pythonはファイル操作やWebスクレイピング（ウェブページから必要なデータを自動で抜き出す技術）、業務の自動化にも活用されており、研究・実務の効率化に役立っている。

### Miniforge

Python の実行環境には複数の配布形態が存在する。その中で Miniforge
は、研究や教育の場面で広く推奨される配布形態である。

Python の「全部入り環境」としては Anaconda
がよく知られており、多くの入門書や講習会がそれを前提にしてきた。しかし、Anaconda
は近年ライセンスが変更され、研究や教育において自由に利用するには制約が生じるようになった。また、配布サイズも大きいため、授業で全員に導入させるには負担が大きいという問題もある。

これに対して Miniforge は、conda-forge
コミュニティによって提供される最小構成の Python
環境である。2020年前後から整備が進み、現在では研究・教育においてAnacondaに代わる標準的な環境として定着している。Miniforge
には依存関係を解決する conda と、その高速版である mamba
が含まれており、追加パッケージの入手先は conda-forge チャネル
に統一されている。conda-forge
には最新の科学技術系ライブラリが広く整備されており、Windows
を含む主要な環境で安定して利用できる。

このように Miniforge
は、ライセンス上の制約を気にせずに利用でき、再現性のある研究環境を学生から研究者まで共通に整えられる点で優れている。授業で使用する演習環境と研究室での解析環境を同一の基盤にできるため、学習から応用への接続も容易である。

他の配布形態（公式版、Microsoft
Store版、Anaconda/Miniconda）との違いについては、文末の比較表を参照されたい。本授業では教育と研究を一貫して支える基盤として
Miniforge を使用する。

## Miniforgeのインストール

### Miniforgeインストーラーのダウンロードと起動

Miniforgeインストーラーを以下のサイトからダウンロードしてインストールする。

<https://github.com/conda-forge/miniforge>

```{figure} ./images/media/image1.png
:alt: MiniforgeのGitHubサイト
:align: center
:label: fig-miniforge-github
MiniforgeのGitHubサイト。なおこの図はWindowsの画面表示を「ライト」にしている場合である。「ダーク」にしている場合は画面表示が暗くなる。このページ下部の「Install」のところまで行く。
```

```{figure} ./images/github-miniforge2.drawio.png
:align: center
:label: fig-miniforge-install-inst
「Install」の直下にWindowsでのインストール方法が記載されている。「the
Windows
installer」をクリックしてダウンロードし、実行するとインストーラーが起動する。
```

### Miniforgeのインストール

インストールの手順を以下に示す。特に"Destination
Folder"に気をつけること。

```{figure} ./images/media/image3.png
:align: center
:label: fig-miniforge-install-ss3
インストール開始画面。「Next」をクリックして進む。
```

```{figure} ./images/media/image4.png
:align: center
:label: fig-miniforge-install-ss4
ライセンス確認画面。内容を確認し、問題なければ「I
Agree」をクリックして進む。
```

```{figure} ./images/media/image5.png
:align: center
:label: fig-miniforge-install-ss5
インストールタイプの選択。「Just
Me」を選択し（当初からそちらが選ばれているはず）、「Next」をクリックして進む。
```

```{figure} ./images/miniforge-install4.drawio.png
:align: center
:label: fig-miniforge-install-ss6
インストール場所の選択。"Destination
Folder"に**日本語文字など非ASCII文字が含まれている場合にはインストールを続行できない**ため、もし含まれている場合は英数字のみで構成されているフォルダ名、たとえば"C:\\ｍiniforge3"などにすること。なお\\（円記号）はパスの区切りである。
```

適切なパスを選択したら、「Next」をクリックして進む。

```{figure} ./images/media/image7.png
:align: center
:label: fig-miniforge-install-ss7
"Destination
Folder"に日本語文字など非ASCII文字が含まれていた場合は、このようなエラーメッセージのパネルが表示される。表示されたら適宜修正すること。
```

```{figure} ./images/miniforge-install6.drawio.png
:align: center
:label: fig-miniforge-install-ss8
インストールオプション選択画面。標準ではいちばん上の項目のみにチェックが入っているはずである。下段の項目の中で"Recommended"になっている項目にチェックを入れることを勧める。（任意。図は"Recommended"の項目を選んだ状態）
```

選択したら「Install」をクリック。

```{figure} ./images/media/image9.png
:align: center
:label: fig-miniforge-install-ss9
インストール中の画面
```

```{figure} ./images/media/image10.png
:align: center
:label: fig-miniforge-install-ss10
インストール作業終了時の画面。インストール終了後は「Next」をクリックして進む。
```

```{figure} ./images/media/image11.png
:align: center
:label: fig-miniforge-install-ss11
インストール終了画面。「Finish」をクリックして終了する。
```

### Miniforge Promptの起動とPython・conda動作確認

インストールが成功していれば、スタートメニューにMiniforge
Promptが追加されているはずなので、これを起動する。

```{figure} ./images/Startmenu-Miniforge.drawio.png
:align: center
:label: fig-miniforge-startmenu
:alt: fig-win-startmenu
スタートメニューから「Miniforge Prompt」を起動する。
```

```{figure} ./images/Miniforge-prompt1.drawio.png
:align: center
:label: fig-miniforge-prompt1
Miniforge
Promptを起動した画面。「プロンプト」が表示され、そこにキーボードからコマンドを入力してEnterキーを押すと、そのコマンドが実行される。（ウィンドウの色やフォントは「ターミナル」の設定に依るので、この画面とは異なる可能性がある。）
```

Miniforge
PromptはWindowsのコマンドラインインターフェイス（ターミナル）である。Pythonを使えるようになっているが、Pythonそのものではない。Miniforge
Promptが起動したら、pythonコマンドを実行してみよ。つまりプロンプトにpythonと打ち、Enterキーを押してみよ。Python環境に入り、Pythonのプロンプトが表示されるはずである。

```{figure} ./images/Miniforge-prompt2.drawio.png
:align: center
:label: fig-miniforge-prompt2
Miniforge Promptでpythonを起動した例。この例ではPython
3.12.11が起動していることが分かる。その後exit()でpythonを終了している。
```

青下線部がキーボードから入力したコマンドである。"\>\>\>
"はPythonのプロンプトで、Miniforge
Promptのプロンプトとは異なりPythonのコマンドを受けつける。

また、condaコマンドも実行してみよ。condaの使い方が表示されるはずである。condaはWindowsの実行コマンドとして登録されるので、Miniforge
Promptのプロンプトから（つまり、Pythonから抜けた状態で）実行すること。

## 「仮想環境」の作成と利用

Python
には「仮想環境」という仕組みがある。仮想環境とは、1台のPCの中に独立したPythonの実行環境を複数作る仕組みであり、プロジェクトごとに異なるライブラリやバージョンを分けて管理できる。

仮想環境を用いず、同じ環境に多数のライブラリを追加して使おうとすると、異なる授業や研究で必要とするライブラリ同士が衝突し、動作不良の原因となる。仮想環境を利用すれば、環境ごとに必要なライブラリだけを用意でき、他のプロジェクトに影響を与えずに作業を進められる。

科学技術計算や教育研究の現場では、依存関係の解決が容易な conda や mamba
を用いた仮想環境管理が広く利用されており、特に Windows
環境で有効である。本授業でもこの流れに沿い、condaによりこの授業専用の環境を構築・管理し、その上で演習を行う。仮想環境を利用することで、環境を壊す心配なく、安心してプログラミング演習を進めることができる。

### 仮想環境の作成（1回だけ行う）

Miniforge
Promptで以下のコマンドを実行する。ここでは「EXERCISE」という名前の環境を作成しているが、名称は自由に決めて良い。

```powershell
conda create -n EXERCISE python=3.13
```

途中で"`Proceed
(\[y\]/n)?`"と表示されて止まる。Enterキーを押すと続行する。

ここではインストールするPythonのバージョンを3.13と指定している．2025年10月現在の最新のPythonは3.14だが，JupyterLabが正常に動作しないので，1つ前のバージョンである3.13を使っている．詳細はあとで説明している．

成功すると、以下のようなメッセージが表示された後、プロンプトに戻るはずである。

```powershell
done
#
# To activate this environment, use
#
#     $ conda activate EXERCISE
#
# To deactivate an active environment, use
#
#     $ conda deactivate
```

エラーが出るなどこの表示とは異なる表示だった場合は、コマンドに間違いがあると推測される。漫然と言われたことを実行するのではなく、**コマンドを理解しながら進め、また出力（特にエラー出力）に注意を払う**こと。

"`conda create...`"は仮想環境を作るコマンドで、1回だけ行えば良い。

### Pythonのバージョンについて

2025年10月14日現在，最新のcondaを用いて新しい環境を作ると，Python
3.14.0がインストールされるようである．Python
3.14.0は2025年10月7日にリリースされたばかりの最新版で，JupyterLabがまだ対応していないため，バージョンを指定しないで新しい環境を作り，JupyterLabをインストールして使おうとすると正しく動作しないようである．

当面の間はひとつ前のバージョンであるPython
3.13を使うことを推奨する．前回の授業で作成した環境を使い続ける場合は特にやり直す必要はないが，新たに環境を作るときは，以下のようにしてPythonのバージョンを指定するとよい．

conda create -n EXERCISE python=3.13

末尾に"=3.13"とあるのがバージョン指定である．これを指定しておくと，JupyterLabの不具合を回避できる．

### 仮想環境を使う（Miniforge Promptを起動するごとに行う）

表示されたメッセージから分かるように、仮想環境は作っただけではまだ使いはじめることができない。Miniforge
Promptで以下のコマンドを実行し、仮想環境に入る。

```powershell
conda activate EXERCISE
```

"`conda
activate ...`"はその仮想環境を利用しはじめる（有効にする）ためのコマンドで、こちらはMiniforge
Promptを起動する度ごとに実行する必要があるので注意せよ。標準では"base"環境に入っているので、そこから抜けてEXERCISE環境に入るためである。

以降ではEXERCISE環境に入っている前提で説明する。Miniforge
Promptのプロンプトに"(base)"と表示されていたのが"(EXERCISE)"に変わるはずである。これとは異なる名称の環境を構築した場合には、適宜読み替えること。

### 補足：condaのアップデート

conda実行中に、以下のようにcondaのバージョンアップを促すメッセージが表示されるかもしれない。

```powershell
==> WARNING: A newer version of conda exists. <==
    current version: 25.3.1
    latest version: 25.7.0

Please update conda by running
    $ conda update -n base -c conda-forge conda
```

この場合は、メッセージに記載されているとおりのコマンドを実行して、condaを最新版にアップデートしておくと良い。

```powershell
conda update -n base -c conda-forge conda
```

## 参考：Pythonの入手方法と比較

2025年9月現在

| 入手方法 | 概要 | 利点 | 欠点 | 研究での適正 |
|-----------|------|------|------|---------------|
| 公式配布（python.org から入手） | CPython 本体＋標準ライブラリのみ | ● 純正で信頼性が高い<br>● 軽量・クリーン<br>● OS を問わず安定 | ● パッケージマネージャーは pip のみ<br>● 科学技術系ライブラリ導入で失敗しやすい（特に Windows）<br>● 環境管理は venv 中心で弱い | 入門用には良いが科学技術系演習や研究には不便 |
| Microsoft Store 版（Windows 用） | 導入が容易。Microsoft 標準 | ● インストールが非常に簡単<br>● 自動更新される | ● 特殊な場所に入るため pip で失敗しやすい<br>● 複数環境の切替不可 | 科学技術系演習や研究には不向き |
| Anaconda / Miniconda | Anaconda 社提供。Anaconda ＝ 多数の科学技術系ライブラリを一括同梱。Miniconda ＝ 最小構成。 | ● conda 環境を利用可能<br>● Anaconda は「全部入り」で初心者がすぐ使える | ● 配布サイズが大きい（Anaconda）<br>● ライセンス制限（商用・研究利用に注意）<br>● Miniconda は defaults チャネル依存で古めのパッケージも多い | かつて広く使われたが、ライセンス問題を考えると今後は非推奨 |
| Miniforge | conda-forge コミュニティが提供する最小配布。conda＋mamba を同梱、チャネルは conda-forge 固定 | ● 最新で豊富な科学技術系ライブラリ<br>● ライセンス制限なし<br>● 環境を分けて再現性を確保可能 | ● インストールサイズは公式 Python より大きい<br>● conda 環境の学習コストがある | ライセンス制限や環境管理の容易さから、科学技術系演習や研究で最も適切 |

```{note}
このページの本文と図版は [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.ja)
のもとで提供されています。  
コードやノートブックの例は MIT License に従います。  
一部の画像（表で「CC ライセンス適用外」と明記されたスクリーンショットなど）は除外されます。  
詳細は [LICENSE-docs.md](https://github.com/akonno/FluidSeminarMaterials/blob/main/LICENSE-docs.md) を参照してください。
```
