# CFD教材 Phase 1: inventory / migration design

調査日: 2026-09-15

この文書は、Word/PDFで運用されているblueCFD-Core / OpenFOAM教材を
`FluidSeminarMaterials`へ将来統合するためのPhase 1棚卸し結果である。
今回の調査では教材本文、既存のMySTファイル、画像ファイル、配布ケースを変更していない。
DOCXとPDFは読み取り専用で扱い、変換試験の生成物はリポジトリ外の一時ディレクトリに置いた。

## 1. Source files

| ファイル | 確認結果 | Phase 1での役割 |
| --- | --- | --- |
| `数値流体解析演習_blueCFD2024編.docx` | リポジトリ直下。Wordで一時コピーを読み取り専用に開いて再ページ計算した結果は42ページ。 | 変換元、段落・見出し・表・画像関係・数式形式の主ソース |
| `数値流体解析演習_blueCFD2024編.pdf` | リポジトリ直下。`pdfinfo`で42ページ、A4。 | 最終レイアウト、図配置、キャプション、改ページの照合用 |

DOCXの内部 `docProps/app.xml` には `Pages=1` と保存されているが、Word本体で再計算したページ数とは一致しない。これはWordの保存メタデータが更新されていない状態であり、ページ数の確認には使わない。

DOCXの直接解析では、本文の直接段落403、表8個、`word/media`内の画像ファイル48個（PNG 46、EMF 2）を確認した。画像参照は図1の再掲を含む。`image32.png` と `image33.png` は同じ段落にDrawingMLとVMLの別表現として置かれ、内容・寸法が同一であるため、移行時には一つの表示図として重複を避ける必要がある。

## 2. Current material structure

原資料は一つのDOCX/PDFだが、内容上は授業回に対応する六つのまとまりに分かれている。Wordの見出しstyleは主にHeading 2相当で、章ごとに図番号がリセットされる。Pandocの試験変換では見出し35個（空の見出し1個を含む）が認識された。

### 2.1 最初の演習: blueCFD-Coreからcavityの可視化まで（PDF pp.1--13）

- 到達目標: cavityの圧力場と流速ベクトルをParaViewで表示する。
- 全体の流れ、blueCFD-Coreのダウンロードとインストール。
- `C:\blueCFD-Core\2024`へのインストール、端末の初回起動とエラー例。
- `$FOAM_RUN`、`$FOAM_TUTORIALS`からcavityをコピーし、`blockMesh`、`icoFoam`、`paraFoam`を実行。
- ParaViewで圧力場、Glyphによる速度ベクトルを表示し、スクリーンショットを保存。
- cavityの可視化結果を提出する課題。
- WSL/Linux/macOSを使う場合の補足と、独立したParaViewを使う場合の補足。

### 2.2 cavityの計算条件変更（PDF pp.14--23）

- `physicalProperties`の動粘性係数`nu`を変えてReynolds数を変更。
- `blockMeshDict`の分割数を変えるメッシュ詳細化。
- `controlDict`の`deltaT`、Courant数、CFL条件。
- 計算領域を正方形から縦横比3:1の長方形へ変更する発展課題。
- cavityを流入・流出のある流れへ変更する発展説明。
- Re=400、1000を必須、Re=3200、5000を任意とするGhia et al.比較課題。
- Windowsから設定ファイルを見るための`explorer.exe .`の補足。

### 2.3 解析対象の形状変更と格子生成（PDF pp.24--31）

- Hagen--Poiseuille流れを使った2次元チャネルの例。`channel_2024.tgz`を展開して実行。
- blockMeshの頂点・block・patch定義。
- 2次元角柱まわり流れのblockMeshDict、境界条件、解析例。
- 圧力、速度のコンター、vorticityの生成とParaViewでの表示。
- 角柱後流とカルマン渦について調べ、解析・レポートを行う課題。

### 2.4 指定形状の2次元物体まわり流れ（PDF pp.32--34）

- 方眼紙と手作業で解析領域を設計する方法。
- 学生作成のblock定義と圧力・速度結果の例。
- 単純形状を除外し、自分で決めた2次元形状を解析してレポートにまとめる課題。

### 2.5 与えられた車両形状による3次元外部流れ（PDF pp.35--39）

- 3次元物体まわりの外部流れと計算時間への注意。
- `vehicle_2025.tgz`を展開し、`model/concept_car_038-mod.stl`を`constant/geometry/STLObject.stl`へコピー。
- `./Allclean`、`./Allrun`を使ったメッシュ生成・解析。
- ParaViewのMesh Regionsで車両、床、出口を表示し、圧力と断面速度を可視化。
- 車両まわり流れの可視化画像を提出する課題。

### 2.6 形状を指定する3次元外部流れ（PDF pp.40--42）

- 車両ケースの`STLObject.stl`を自分で用意した形状へ置換。
- STLの寸法、座標、単位、拡大・縮小、平行移動、回転。
- 自分で選んだ3次元形状を解析し、解析対象・条件・選択理由・結果をレポートに含める課題。

## 3. Proposed MyST structure

提示された7章案は、原資料の六つのまとまりを概念別に分離する構成として妥当である。特に、cavityの基本実行と設定変更を分け、2次元形状、与えられた3次元ケース、自作3次元形状を段階化できる。

| 提案ファイル | 原資料の対応 | 移行時の注意 |
| --- | --- | --- |
| `textbook/cfd/bluecfd-install.md` | pp.1--4のblueCFD-Core説明・インストール | `2024-1`、インストール先、警告画面は時点依存。WSL/Linux/macOS補足の置き場所も決める。 |
| `textbook/cfd/cavity.md` | pp.1、5--10のcavity実行・ParaView可視化・最初の課題 | `$FOAM_RUN`、tutorial path、`blockMesh`、`icoFoam`、`paraFoam`を一連の流れとして保持する。 |
| `textbook/cfd/cavity-settings.md` | pp.14--23の`physicalProperties`、メッシュ、CFL、領域・流れ変更、Ghia課題 | Ghia図、Re条件、`deltaT`、Windowsファイル操作をまとめる。基本cavityへの章参照を明示する。 |
| `textbook/cfd/blockmesh-boundary.md` | pp.24--31のHagen--Poiseuille、角柱、patch、vorticity | `channel_2024.tgz`のケース依存を外部ケースrepoへ分離する。cavity-settingsの流入・流出説明との境界を決める。 |
| `textbook/cfd/external-flow-2d.md` | pp.32--34の自作2次元形状と学生例 | 学生作成図の公開可否を確認する。方眼紙設計とレポート課題は残す。 |
| `textbook/cfd/external-flow-3d.md` | pp.35--39の`vehicle_2025.tgz`と可視化 | ケース本体、STL、`Allrun`、`Allclean`は別repositoryへ置き、本文からリンクする。 |
| `textbook/cfd/external-flow-3d-custom.md` | pp.40--42のSTL置換、寸法・姿勢変更、自作形状課題 | 3Dモデルの出典・ライセンスと、変換・配置動画のKU-LMS依存を整理する。 |

分割上の主な設計論点は二つある。第一に、ParaView最新版の補足はインストール章にも可視化章にも関係するため、blueCFDの基本導入と独立ParaViewの補足を重複させないこと。第二に、cavityを流入・流出へ変更する説明とHagen--Poiseuilleの配布ケースは近いが、前者を設定変更の概念説明、後者をblockMesh/patch実習として分けること。

## 4. Figure inventory

### 4.1 図・画像の一覧

下表はDOCX内部media名、PDF上のページ、キャプションまたは用途、暫定的な出典分類を対応づけたものである。図番号は原資料内でリセットされるため、移行時には章ごとのfigure labelを新しく付ける。

| DOCX media | 原資料の図・用途 | PDF page | 種類・出典分類 | 公開版での扱い候補 |
| --- | --- | ---: | --- | --- |
| `image1.png` | 図1 cavityの到達目標画面。p.10で再掲 | 1, 10 | OpenFOAM/ParaView結果の自作スクリーンショットまたは自作結果図 | cavity章の目標図として再利用。再掲はfigure参照にする。 |
| `image2.png` | 図2 blueCFD-Core Projectのウェブサイト | 2 | Webサイトスクリーンショット | URL、取得時点、スクリーンショットの権利を確認。必要なら現行画面へ更新。 |
| `image3.png`, `image4.png` | 図3 Windowsの保護警告と詳細情報画面 | 3 | Windows UI / blueCFDインストーラー起動時の自作スクリーンショット | 現在のWindows表示との一致をPhase 2で確認。 |
| `image5.png` | 図4 blueCFD-Coreインストール先指定 | 3 | blueCFDインストーラーUIの自作スクリーンショット | 固定パス説明と併せて更新要否を判断。 |
| `image6.png` | 図5 blueCFD-Core terminal初回起動画面 | 4 | blueCFD-Core UIの自作スクリーンショット | 対象versionを決めて再撮影または現行図を維持。 |
| `image7.png` | 図6 デフォルトインストール時のエラー・警告 | 4 | blueCFD-Core UIの自作スクリーンショット | エラーが現行版にも該当するか確認してから再利用。 |
| `image8.png` | ParaView Welcome画面 | 7 | ParaView UIの自作スクリーンショット | cavity章の可視化手順へ移行。 |
| `image9.png` | Welcomeを閉じたParaView画面 | 7 | ParaView UIの自作スクリーンショット | 同上。 |
| `image10.png` | cavityの圧力場表示 | 8 | ParaView UIと自作解析結果 | 同上。 |
| `image11.png` | Glyph設定画面 | 8 | ParaView UIの自作スクリーンショット | 同上。 |
| `image12.png` | cavityの流速ベクトル表示 | 9 | ParaView UIと自作解析結果 | 到達目標図との役割を整理。 |
| `image13.png` | standalone ParaView起動画面 | 12 | ParaView UIの自作スクリーンショット | 補足節へ移行。version確認が必要。 |
| `image14.png` | `cavity.foam`を開くファイルダイアログ | 13 | Windows/ParaView UIの自作スクリーンショット | standalone ParaView補足へ移行。 |
| `image15.png` | standalone ParaViewのApply画面 | 13 | ParaView UIの自作スクリーンショット | 同上。 |
| `image16.png` | 図1 Notepad2起動画面 | 15 | blueCFD付属エディタUIの自作スクリーンショット | Notepad2を前提にするか、一般のテキストエディタ説明へ整理。 |
| `image17.png` | 図2 `physicalProperties`編集画面 | 15 | Notepad2 UIの自作スクリーンショット | cavity-settingsへ移行。 |
| `image18.png` | 図4 Surface with Edgesによるメッシュ確認 | 17 | ParaView UIと自作メッシュ結果 | cavity-settingsへ移行。 |
| `image19.emf` | 図5 Ghia et al. Re=100, 400, 1000 | 20 | Ghia et al. (1982)の引用図 | 原図を最終公開版で使わず、再計算図へ置換。Ghia引用とbenchmark情報は残す。 |
| `image20.emf` | 図6 Ghia et al. Re=3200, 5000 | 21 | Ghia et al. (1982)の引用図 | `image19.emf`と同じ方針。EMF変換前に権利・引用方法を確定。 |
| `image21.png` | 図7 OpenFOAM/blueCFDのcavity Re=400 | 22 | 自作OpenFOAM計算結果 | Ghia再計算比較の説明と整合させる。 |
| `image22.png` | 図6 Windows Explorerで設定ファイルを表示 | 23 | Windows UIの自作スクリーンショット | cavity-settingsのファイル操作補足へ移行。 |
| `image23.png` | 図1 cavityとHagen--Poiseuille流れの比較 | 24 | 自作説明図 | blockmesh-boundaryへ移行。 |
| `image24.png`, `image25.png` | 図2 verticesとboundaryの定義 | 25 | 自作説明図とコード配置 | blockMeshのvertices/patch説明へ移行。 |
| `image26.png` | 図3 Hagen--Poiseuille流れの境界条件 | 26 | 自作説明図 | blockmesh-boundaryへ移行。 |
| `image27.png` | 図4 角柱まわり流れのblock定義 | 27 | 自作説明図 | blockmesh-boundaryへ移行。 |
| `image28.png` | 図5 角柱まわり流れの境界条件 | 27 | 自作説明図 | 同上。 |
| `image29.png`, `image30.png` | 図6 blockとpatchの定義方法 | 28 | 自作説明図 | 同上。 |
| `image31.png` | 図7 金野作成のblockメモ | 28 | 教員作成の作業メモ/説明図 | 教材として残す価値を確認し、必要なら清書または補助資料化。 |
| `image32.png`, `image33.png` | 図8 角柱後流の解析格子 | 29 | OpenFOAM計算結果。二つの埋込形式が同一内容 | 一つの図として移行。 |
| `image34.png` | 図9 角柱後流の圧力コンター | 29 | 自作OpenFOAM計算結果 | blockmesh-boundaryへ移行。 |
| `image35.png` | 図10 角柱後流の速度絶対値コンター | 29 | 自作OpenFOAM計算結果 | 同上。 |
| `image36.png` | 図11 `postProcess -func vorticity`後のParaView | 30 | ParaView UIと自作解析結果 | 現行commandの確認後に移行。 |
| `image37.png` | 図1 方眼紙で定義したblock例 | 32 | 学生作成図 | 公開許諾、匿名化、授業年度を確認。 |
| `image38.png`, `image39.png` | 図2 学生作成の圧力場・速度ベクトル場 | 33 | 学生作成図・解析結果 | 公開許諾と出典表示を確認。 |
| `image40.png`, `image41.png` | 図1 車両形状・表面メッシュ | 36 | Sketchfab由来形状の表示。スクリーンショット/解析結果 | SketchfabのCC0表示、元モデル、二次利用条件を記録。 |
| `image42.png` | 図2 ParaView初期表示 | 37 | ParaView UIの自作スクリーンショット | external-flow-3dへ移行。 |
| `image43.png` | 図3 Mesh Regions設定後 | 37 | ParaView UIの自作スクリーンショット | 同上。 |
| `image44.png` | 図4 車両ケースの解析メッシュ | 38 | 自作OpenFOAM/ParaView結果 | ケースrepoのversionと対応づける。 |
| `image45.png` | 図5 車両表面圧力と断面速度 | 38 | 自作OpenFOAM/ParaView結果 | 同上。 |
| `image46.png` | 図1 車両ケースの寸法 | 40 | 自作説明図 | external-flow-3d-customへ移行。 |
| `image47.png` | 図2 自作物体の寸法・座標 | 41 | 自作説明図 | 同上。 |
| `image48.png` | 図3 形状を差し替えた計算例 | 42 | 自作OpenFOAM/ParaView結果。ただし形状出典は未確認 | 出典とケース条件を確認後に移行。 |

画像の分類結果は、教員作成の説明図・自作解析結果・UIスクリーンショットが大部分である。要注意なのは、Ghia引用図2点、学生作成図3点、Sketchfab由来車両形状2点、出典未確認の最終3D例1点である。UIスクリーンショットは画像そのものの作者と、画面に表示されたソフトウェア・Webサイトの権利を分けて記録する必要がある。

### 4.2 画像ファイル名の移行案

Phase 2以降で、`imageN.png`のままではなく次のような章別ディレクトリと意味名へ移行する。今回renameは行っていない。

```text
textbook/cfd/images/
  bluecfd-install/
    bluecfd-project-site.png
    bluecfd-installer-warning-left.png
    bluecfd-installer-warning-details.png
    bluecfd-install-path.png
    bluecfd-terminal-first-run.png
    bluecfd-terminal-default-path-error.png
  cavity/
    cavity-goal-pressure-velocity.png
    paraview-pressure.png
    paraview-glyph-velocity.png
    cavity-velocity-vectors.png
  cavity-settings/
    notepad2-physical-properties.png
    cavity-mesh-surface-with-edges.png
    cavity-ghia-recomputed-re400.png
    cavity-ghia-recomputed-re1000.png
  blockmesh/
    hagen-poiseuille-boundary.png
    square-cylinder-blocks.png
    square-cylinder-boundary.png
    square-cylinder-vorticity.png
  external-2d/
    student-block-layout.png
    student-pressure-velocity.png
  external-3d/
    vehicle-model.png
    vehicle-surface-mesh.png
    vehicle-pressure-velocity.png
  external-3d-custom/
    custom-stl-dimensions.png
    custom-stl-result.png
```

## 5. Equations and numerical parameters

DOCX内で数式として保存されているOMMLは、主に3段落にまとまっている。Pandocの試験変換では、少なくとも以下をLaTeX相当の数式として取り出せた。

| 内容 | DOCXでの形式 | PDFとの照合 | 移行上の注意 |
| --- | --- | --- | --- |
| `C = U Δt / Δx` | OMMLの数式 | PDF p.17に分数表示 | MySTのdisplay mathへ変換できる。`U`、`Δt`、`Δx`の説明を本文に残す。 |
| `Δt = 0.005` | OMMLと本文 | PDF pp.17--18 | `controlDict`のコード例と混同しないようにする。 |
| `Δx = 0.1 / 20 = 0.005` | OMMLと本文 | PDF p.18 | mesh分割数、領域長さ、単位の説明と一体で移行する。 |
| `C = 1`、通常は`C < 1` | OMMLと本文 | PDF p.18 | PISOによる例外的説明を含め、技術更新時に再確認する。 |
| Reynolds数 | `Re=400`等の本文・キャプション表記。独立したRe公式は見当たらない | PDF pp.15、19--22、29、42 | `U=1 m/s`、代表長さ`0.1 m`、初期`nu=0.01`を使う説明がある。Re公式を補うかはPhase 2で判断する。 |

Ghia図のキャプションにはRe=100, 400, 1000およびRe=3200, 5000が記載される。Ghia図は画像内のプロットを含むため、本文の数式変換とは別に、benchmarkの引用情報と再計算図を管理する必要がある。

## 6. Commands

| コマンド | 初出PDF page | 目的・対応する将来章 |
| --- | ---: | --- |
| `mkdir -p $FOAM_RUN` | 5 | 実行用ディレクトリを作る。`cavity.md` |
| `cp -r $FOAM_TUTORIALS/legacy/incompressible/icoFoam/cavity/cavity $FOAM_RUN` | 5 | OpenFOAM tutorialのcavityを作業領域へコピーする。`cavity.md` |
| `cd $FOAM_RUN/cavity` | 5 | cavityケースへ移動する。`cavity.md` |
| `blockMesh` | 5 | blockMeshDictからメッシュを生成する。`cavity.md`以降の各実習 |
| `icoFoam` | 5 | 非定常・非圧縮・層流の解析を実行する。`cavity.md`以降の各実習 |
| `paraFoam` | 6 | OpenFOAM結果をParaViewで開く。`cavity.md` |
| `touch cavity.foam` | 12 | standalone ParaView用の空のfoamファイルを作る。`cavity.md`補足 |
| `notepad2` | 14 | `physicalProperties`を編集する。`cavity-settings.md` |
| `notepad2 &` | 16 | エディタをバックグラウンド起動する補足。`cavity-settings.md` |
| `explorer.exe .` | 23 | Windows Explorerで現在の設定ファイル位置を開く。`cavity-settings.md` |
| `tar xf channel_2024.tgz` | 26 | channelケースを展開する。`blockmesh-boundary.md`、外部case repo |
| `cd channel` | 26 | channelケースへ移動する。`blockmesh-boundary.md` |
| `postProcess -func vorticity` | 30 | 計算結果からvorticityを生成する。`blockmesh-boundary.md` |
| `vorticity` | 30 | blueCFD-Core 2017-2 / OpenFOAM 5以前のlegacy commandとして記載。維持可否要確認 |
| `tar xf vehicle_2025.tgz` | 35 | vehicleケースを展開する。`external-flow-3d.md`、外部case repo |
| `cd vehicle` | 35 | vehicleケースへ移動する。`external-flow-3d.md` |
| `./Allclean` | 35 | 既存の解析結果を削除する。`external-flow-3d.md`、外部case repo |
| `./Allrun` | 35 | vehicleケースの解析を実行する。`external-flow-3d.md`、外部case repo |
| `cp model/concept_car_038-mod.stl constant/geometry/STLObject.stl` | 36 | 解析対象STLをケースが期待する名前へコピーする。`external-flow-3d.md` |
| `ls` | 35 | 配布tgzの存在するディレクトリを確認する説明中に登場する。`external-flow-3d.md` |

`File -> Save Screenshot`、ParaViewの`Mesh Regions`や`Glyph`の操作はシェルコマンドではないが、cavity/vehicle章の手順として残す必要がある。

## 7. Time-sensitive information

| 記述 | 出現箇所 | 分類 | Phase 2以降の確認事項 |
| --- | --- | --- | --- |
| blueCFD-Core 2024-1 | pp.2--5、14--15 | 2026年現在の確認が必要 | Windows対応状況、インストーラー、OpenFOAM対応版、インストールパス。 |
| OpenFOAM version 12相当 | p.5、WSL/macOS補足 | 2026年現在の確認が必要 | blueCFD-CoreとFoundation版の対応関係、tutorial path。 |
| ParaView 5.11.2 | p.7、11 | 明らかにversion依存 | blueCFD同梱版とstandalone版の対象versionを確定。 |
| ParaView v6.0、`Python3.12` MSI名 | p.11 | 本稿執筆時点の明示的な時点依存 | 現行配布ファイル、OS、Python/MPIの選択説明を確認。 |
| 「本稿執筆時点で最新」 | p.2、11 | 明らかに時点依存 | 固定version説明へするか、更新日付き注記にするか判断。 |
| blueCFD-Core 2017-2向け外部解説 | p.2 | legacy情報として残す可能性あり | リンクの存続、2024-1以降への適用可否。 |
| OpenFOAM 5以前の`vorticity` command | p.30 | legacy情報として残す可能性あり | 現行版では`postProcess -func vorticity`を主経路にするか確認。 |
| `icoFoam`と`legacy/incompressible`のpath | pp.5、26--30 | 2026年現在の確認が必要 | 選定するOpenFOAM版のsolver名・tutorial構造。 |
| Windows 10/11、WSL、Linux、macOS Docker | pp.11、13 | 2026年現在の確認が必要 | 主対象OSと補足の範囲、各公式手順。 |
| `C:\blueCFD-Core\2024`、`/home/ofuser/blueCFD/ofuser-of12/run` | pp.3、5、13 | 明らかに環境・version依存 | 固定パスを例示するか、環境変数中心に説明するか判断。 |
| `channel_2024.tgz`、`vehicle_2025.tgz` | pp.26、35 | ファイル配布時点・年度依存 | 2026版の配布名、内容、配布場所、外部repoへの移行。 |
| `postProcess -func vorticity` | p.30 | version・functionObject依存 | 選定caseとOpenFOAM版で実行確認。 |
| 外部blueCFD解説、OpenFOAM、ParaView、OpenFOAMユーザー会 | pp.2、5、11 | リンク確認が必要 | URL存続、内容、リンク先の利用条件。 |

ここでは技術的正誤の修正は行っていない。上表は、変換時にそのまま固定せず確認すべき記述の一覧である。

## 8. Lecture-sequence references

原資料には授業回を明示する表現が複数あり、章名への置換候補は次のとおりである。

| 原資料の位置 | 原文の参照 | 置換先候補 |
| --- | --- | --- |
| p.1 | 「初回の演習」 | `bluecfd-install.md`から`cavity.md`までの導入 |
| p.10 | 「今回の演習で到達目標」 | `cavity.md`の「この章の目標」 |
| pp.14--16 | 「前回の演習」「前章」「3.OpenFOAMの実行」「4.解析結果の可視化」 | `cavity.md`を明示リンク |
| p.23 | 「資料2」「OpenFOAMの計算条件設定を変更」 | `cavity-settings.md`を明示リンク |
| p.24 | 「前回まで」「今回解析する流れ場」「次の角柱」 | `cavity.md`、`blockmesh-boundary.md`を章名で参照 |
| p.26 | 「cavityのときと同じ」 | `cavity.md`の実行手順を明示参照 |
| p.31 | 「前回の演習で実施した天井駆動キャビティ流れ」「今回実施する角柱」 | `cavity.md`と`blockmesh-boundary.md` |
| pp.32--34 | 「今回の演習」「前回の角柱」 | `external-flow-2d.md`と`blockmesh-boundary.md` |
| pp.35--39 | 「これまでの演習」「今回実施する解析」「図2～5の手順」 | `external-flow-3d.md`内の節名・図参照 |
| pp.40--42 | 「前回の演習」「今回の演習」「資料2」 | `external-flow-3d.md`、`external-flow-3d-custom.md`、`cavity-settings.md` |

最終的には「前回」「今回」「次回」「前章」「前回まで」を、`cavityの実行と可視化`、`cavityの設定変更`、`角柱まわり流れ`などの節名・ファイルリンクに置換する方針が自然である。今回は置換していない。

## 9. Licensing / provenance

| 対象 | 該当media | 暫定分類 | 移行時に必要な確認 |
| --- | --- | --- | --- |
| 教員作成の説明図・メモ | `image23`--`image31`、`image46`、`image47` | 自作図・自作メモ | 作者、元データ、編集可能な原図の有無。 |
| 教員が実行した計算・可視化結果 | `image1`、`image21`、`image32`--`image36`、`image42`--`image45`、`image48` | 自作解析結果・自作スクリーンショット | 対応case、version、再現条件を外部case repoと対応づける。 |
| blueCFD-Core UI | `image5`--`image7` | ソフトウェアUIの自作スクリーンショット | 対象versionと現在のUI、商標・配布条件。 |
| ParaView UI | `image8`--`image15`、`image18`、`image36`、`image42`--`image45` | ソフトウェアUIの自作スクリーンショット | 対象version、画面の現行性、再撮影の要否。 |
| Windows UI | `image3`、`image4`、`image22` | OS UIの自作スクリーンショット | Windows版差、公開教材での利用可否。 |
| Webサイト | `image2` | Webサイトスクリーンショット | blueCFD ProjectのURL、取得時点、公開・引用条件。 |
| Ghia et al. (1982) | `image19.emf`、`image20.emf` | 第三者引用図 | 最終版ではOpenFOAM再計算図へ置換。Ghiaのbenchmark引用、Re、格子条件は残す。 |
| 学生作成図 | `image37`--`image39` | 学生作成物 | 個別の公開許諾、匿名化、年度・氏名情報、公開範囲。 |
| Sketchfabの車両モデル | `image40`、`image41`および`concept_car_038-mod.stl` | 第三者データ由来 | DOCXに次のURLが記載されている: `https://sketchfab.com/3d-models/concept-car-038-public-domain-cc0-0b4ca2a15ba7478db2a42ac9f0e687bf`。CC0表示と元作者・派生物の扱いを確認。 |
| 出典未確認のカスタム3D例 | `image48` | その他第三者素材の可能性あり | 形状データと計算caseの出典を確定してから公開判断。 |

原DOCXにはGhiaの引用記載とSketchfab URLはあるが、画像全体を分類したライセンス一覧はない。現行repositoryの`LICENSE-docs.md`へ対応づける作業はPhase 2で行う。

## 10. KU-LMS dependencies

| 依存内容 | 使用箇所 | 将来の置き場所・扱い |
| --- | --- | --- |
| 初回cavityの可視化結果の提出方法・期限 | p.10 | 本文には課題内容を残し、提出方法・期限はKU-LMS参照として明示。公開MySTから個別LMSへ直接依存しすぎない構成を検討。 |
| ParaViewで流線を表示する動画 | p.19 | `cavity-settings.md`の補助動画。URL、公開範囲、年度更新を確認。 |
| `channel_2024.tgz`の配布 | p.26 | KU-LMS配布物から外部case repositoryのversioned releaseへ移す候補。本文にはcase repoリンクを置く。 |
| 角柱まわり流れのレポート提出方法・期限 | p.30 | 課題本文はMyST、提出運用はKU-LMS。 |
| `vehicle_2025.tgz`の配布 | pp.35--36 | 外部case repositoryのcase/ archiveへ置く候補。現在の配布物の完全な内容を確認する。 |
| vehicleのParaView操作動画 | p.38 | `external-flow-3d.md`の補助教材。LMSの動画リンク管理が必要。 |
| 車両可視化画像の提出方法・期限 | p.39 | 課題本文はMyST、提出運用はKU-LMS。 |
| STLの拡大・縮小・回転・平行移動の動画 | p.41 | `external-flow-3d-custom.md`の補助教材。動画の公開範囲と更新を確認。 |
| 自作形状3Dレポートの提出方法・期限 | p.42 | 課題本文はMyST、提出運用はKU-LMS。 |

KU-LMS上の動画URL、提出先、期限、配布物の現在の版はDOCXからは確定できない。本文側で公開できるのは課題内容と依存する補助資料の種類までであり、アクセス制限のあるURLを公開repositoryの必須リンクにするかは教員判断が必要である。

## 11. External assets

| 外部資産 | 現資料での使用 | 現在確認できた配布元 | 将来の候補配置 |
| --- | --- | --- | --- |
| blueCFD-Core installer | Windowsインストール | blueCFD-Core ProjectのWebサイト。DOCXにはサイトスクリーンショットと外部解説URLがある | 本文は公式ダウンロードページへリンクし、installer本体は配布しない。 |
| OpenFOAM tutorial cavity | `$FOAM_TUTORIALS`からコピー | blueCFD-Core/OpenFOAMに付属する前提 | 本文はtutorial名・必要ファイルを説明し、caseの固定コピーは外部repoで管理。 |
| `channel_2024.tgz` | Hagen--Poiseuille流れの配布case | KU-LMS | `channel` caseとして外部case repoのreleaseまたは課題別ディレクトリへ。 |
| `vehicle_2025.tgz` | 3D車両case | KU-LMS | `vehicle` caseとして外部case repoへ。`0/`、`constant/`、`system/`、scripts、STLを含める候補。 |
| `STLObject.stl` | ケースが読み込む固定名のSTL | `vehicle_2025.tgz`内の`model`からコピー | 外部case repoでサンプルSTLと差し替え手順を管理。 |
| `concept_car_038-mod.stl` | vehicleのサンプル車両 | Sketchfab URLがDOCXに記載 | CC0表示と出典を確認し、外部repoに同梱するかリンク配布にするか決定。 |
| Ghia et al. (1982) | cavity benchmark図 | DOCXのEMF引用図 | 原図は最終版で使わず、自作再計算図を掲載。論文引用情報は残す。 |
| ParaView | 可視化 | blueCFD同梱版およびstandalone補足 | 対象versionを固定せず、対応version確認後に手順を整理。 |
| Notepad2 / Windows Explorer | 設定ファイル編集 | blueCFD/Windows環境 | 教材本文は特定エディタへの依存を必要最小限にするか判断。 |
| OpenFOAM Foundation / OpenFOAMユーザー会 | 参考情報 | DOCX中の外部URL | URL存続と内容を確認し、本文の参考リンクとして整理。 |
| KU-LMS動画 | ParaView操作、流線、STL変換 | KU-LMS | 本文の補助リンク。公開サイトのbuildを壊さない参照方法を決定。 |

## 12. Case repository

ローカルcloneの有無を確認するため、主に `C:\Users\konno\source\repos` 配下のgit repository、`Kogakuin-FEL`ディレクトリ、`FluidSeminarExamples`を確認した。また、存在する範囲でユーザーの`Documents\GitHub`と`Downloads`のトップレベルも確認した。

結果は次のとおり。

- `Kogakuin-FEL`はディレクトリとして存在するが、内部にファイルも`.git`もない。
- `FluidSeminarExamples`にはOpenFOAM case treeを確認できなかった。
- `Kogakuin-FEL/OpenFOAM-exercises`または同等のOpenFOAM演習case repositoryのローカルcloneは発見できなかった。
- したがって、repository名、remote URL、owner/org、public/private、default branch、directory tree、case一覧、README、LICENSEはローカル情報から確定できない。

今回、GitHub上の候補repositoryを名前で推測したり、外部repositoryをclone・変更したりしていない。外部case repositoryはPhase 2以降に、正式なownerと配布方針を決めたうえで別途確認する必要がある。

## 13. DOCX→MyST migration strategy

### 13.1 推奨方法

Pandocだけ、または`python-docx`だけに依存せず、次のハイブリッド方式が最も安全である。

1. PandocでDOCXからMarkdownへの初回変換を行い、`--extract-media`で`word/media`の画像を一時ディレクトリへ抽出する。
2. DOCX XML（`word/document.xml`、`word/_rels/document.xml.rels`、styles、tables）を使って、画像relationship、caption、表、OMMLの位置を補正する。
3. PDFのページ・図配置と照合し、Pandocが落としたキャプション、表内画像、改ページ、図番号を手動で確定する。
4. 最終MySTでは画像を意味のある名前にして`textbook/cfd/images/...`へ配置し、`figure` directiveとalt text、caption、出典注記を付ける。
5. OMMLはPandocが抽出したLaTeXを初期値として使い、`C = U\Delta t/\Delta x`などをMySTのdisplay mathに正規化する。PDFの見た目と記号・添字を再照合する。
6. `blockMeshDict`、境界条件、`controlDict`などのWord表は、PandocのHTML/Markdown表をそのまま採用せず、MySTのfenced code blockへ手動変換する。
7. 日本語本文と通常のhyperlinkはPandocで概ね保持できるが、外部URLの存続、URL表示の分割、全角記号、下線・太字は目視確認する。
8. Ghia図、学生図、第三者STLに対しては、変換前に出典・利用可否を確定する。

### 13.2 試験変換で確認できたこと

- Japanese本文はPandoc出力で保持された。
- Heading styleから見出しはある程度抽出できたが、章番号は再整理が必要で、空の`##`も一つ生成された。
- OMMLのCourant数式はLaTeX相当へ変換できた。
- figureはHTMLの`figure`/`figcaption`、Markdown画像、表内画像が混在した。figure directiveへ統一するには手動補正が必要。
- `image19.emf`、`image20.emf`はEMFのまま抽出されるため、Web掲載形式への変換と引用の確認が別途必要。
- 表内のblockMeshDictやboundary定義は、コードとして再利用するには手動でのfenced code化が必要。
- 改ページはMarkdownに直接対応しないため、PDFを参照して段落・図のまとまりを再構成する必要がある。

従って、Pandocは初回の本文・リンク・数式・画像対応の取得には有効だが、最終変換器にはしない。DOCX XMLを構造の監査、PDFを見た目の監査に使い、MyST側は手動で編集するのが推奨である。

## 14. Open issues / decisions needed

Phase 1の調査だけでは決められず、教員判断が必要な事項は次のとおりである。

1. 2026年版で対象とするblueCFD-Core、OpenFOAM、ParaViewの具体的なversionと、Windowsの主対象version。
2. `C:\blueCFD-Core\2024`のような固定インストールパスを教材に残すか、環境変数・実際のインストール先を中心にするか。
3. `icoFoam`、`legacy/incompressible`、`postProcess -func vorticity`を現行版で再検証する範囲と、legacyの`vorticity`説明を残すかどうか。
4. `channel_2024.tgz`、`vehicle_2025.tgz`の2026版の名称、内容、配布方法、外部case repositoryのowner/orgと公開範囲。
5. 外部case repositoryに`0/`、`constant/`、`system/`、`Allrun`、`Allclean`、STL、README、LICENSEをどの単位で配置するか。
6. 学生作成図（`image37`--`image39`）を公開教材へ掲載する許諾、匿名化、クレジット方法。
7. Sketchfabの車両モデルと`concept_car_038-mod.stl`を外部case repositoryへ含めるか、元ページへのリンクだけにするか。
8. Ghia et al. (1982)のbenchmark情報をどの範囲で引用し、OpenFOAM再計算図へ置換する際の比較項目をどこまで残すか。
9. KU-LMSの動画・提出方法・期限を公開MyST本文からどのように参照するか。
10. WordにあるParaView最新版、WSL/Linux/macOS、Notepad2などの補足を7章のどこへ置くか。

## 15. Phase 1 scope confirmation

- 新しいMyST教材ファイルは作成していない。
- `textbook/`、`PyGame/`、`JupyterLab/`、`docs/`、TOC、画像ファイルは変更していない。
- DOCX/PDFはgit addしていない。
- 生成した解析用テキスト、XML展開物、画像contact sheetはリポジトリ外の一時ディレクトリに置いた。
- このレポートだけがPhase 1のcommit対象である。
