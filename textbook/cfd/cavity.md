# cavityを実行して可視化する

この章では、天井駆動キャビティ流れの小さなcaseを使って、OpenFOAMのcase構造、メッシュ生成、計算、ParaViewによる可視化を一通り確認する。原資料pp.1、5--13を、OpenFOAM 12の`foamRun` workflowに合わせて整理している。

## この章の目標

- OpenFOAM caseのディレクトリ構造を説明できる。
- `blockMesh`でメッシュを生成できる。
- `foamRun`で計算を実行できる。
- `paraFoam`からParaViewを起動し、圧力と速度を確認できる。

## 学生用caseの入手

2026年版の実行可能caseは、教材本文と分離したcase repositoryで管理している。授業で指定されたReleaseページを開き、GitHubが自動生成する`Source code (zip)`ではなく、Release Assetをダウンロードする。

<a href="https://github.com/Kogakuin-FEL/OpenFOAM-exercises/releases/tag/v2026.1" target="_blank" rel="noopener">OpenFOAM-exercises v2026.1 Release</a>

ダウンロードするファイルは次のものである。

```text
OpenFOAM-exercises-2026.1.zip
```

Windows上で展開したら、blueCFD-Core terminalから展開先の`cavity`ディレクトリへ移動する。提出方法、締切、授業年度固有のお知らせはKU-LMSで確認する。

## Caseの構造

最低限、次の3つのディレクトリを確認する。

```text
cavity/
├── 0/
│   ├── U
│   └── p
├── constant/
│   ├── momentumTransport
│   └── physicalProperties
└── system/
    ├── blockMeshDict
    ├── controlDict
    ├── fvSchemes
    └── fvSolution
```

- `0/`：初期時刻の場。速度`U`と圧力`p`の境界条件を含む。
- `constant/`：物性と乱流・層流モデルなど、計算中に使う物理設定。
- `system/`：メッシュ、時間刻み、離散化、方程式の解法に関する設定。

このcaseは、blueCFD-Core 2024-1 / OpenFOAM 12向けに用意された小規模な層流caseである。`system/controlDict`には`foamRun`と`incompressibleFluid`が指定されている。

## メッシュを生成する

caseディレクトリで、次を順に実行する。

```sh
cd cavity
blockMesh
```

`blockMesh`は`system/blockMeshDict`を読み、計算領域をセルへ分割する。成功すると、case内に`constant/polyMesh`が生成される。

## 計算を実行する

次に、OpenFOAM 12のcase設定に従って計算を実行する。

```sh
foamRun
```

このcaseの初期設定では、`nu = 0.01 m^2/s`、上面速度`U = 1 m/s`、代表長さ`L = 0.1 m`である。計算は`0.5`まで進み、時刻ディレクトリに`U`と`p`が書き出される。

旧版資料では、付属tutorialの`$FOAM_TUTORIALS/legacy/incompressible/icoFoam/cavity/cavity`をコピーして`icoFoam`を実行していた。これは旧tutorialを説明するlegacy情報であり、2026年版の標準手順ではない。現在はRelease Assetに含まれるcaseを使い、`foamRun`を実行する。

## ParaViewで結果を見る

計算が終わったら、同じcaseディレクトリで次を実行する。

```sh
paraFoam
```

ParaViewが起動したら、次の順で確認する。

1. Pipeline Browserでcaseを選び、`Apply`をクリックする。
2. Coloringで圧力`p`を選び、圧力場を表示する。
3. `Glyph`フィルターを追加し、速度`U`を矢印で表示する。
4. 必要に応じて`Surface With Edges`を選び、メッシュを確認する。
5. `File` → `Save Screenshot`で結果を保存する。

```{figure} ./images/cavity/cavity-goal.png
:alt: cavityの圧力と速度ベクトルを表示した目標画面
:align: center

圧力場と速度ベクトルを表示する目標画面の例。図は原資料の解析結果を再利用したもので、UIはParaViewの版によって異なる。
```

```{figure} ./images/cavity/paraview-pressure.png
:alt: ParaViewで表示したcavityの圧力場
:align: center

ParaViewで表示したcavityの圧力場の例。
```

```{figure} ./images/cavity/cavity-velocity-vectors.png
:alt: cavityの速度ベクトル
:align: center

Glyphで表示したcavityの速度ベクトルの例。
```

独立したParaViewを使う場合は、caseディレクトリで空の`cavity.foam`を作って開く方法もある。この補助ファイルは計算結果ではなく、可視化の入口を示すためのものである。

```sh
touch cavity.foam
```

## 課題

`cavity`を実行し、圧力場と速度ベクトルを含む可視化結果を作成する。提出する画像または動画の形式、提出先、提出期限はKU-LMSで確認する。

## 次に読む章

次章では、`physicalProperties`、`blockMeshDict`、`controlDict`を編集し、粘性係数、Reynolds数、メッシュ、時間刻みを変更する。

## ライセンス

```{note}
このページの本文と自作図版は [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.ja) のもとで提供されています。
コードやノートブックの例は MIT License に従います。
第三者の著作物を含む一部のスクリーンショット等は、CC BY-NC-SA 4.0の適用対象外です。詳細は [LICENSE-docs.md](https://github.com/akonno/FluidSeminarMaterials/blob/main/LICENSE-docs.md) を参照してください。
```
