# blockMeshと境界条件

この章では、流れ場の形状をblockMeshで定義する方法を学ぶ。チャネル流れを例にblockとpatch、境界条件、メッシュ生成、角柱まわり流れのケース構築を確認する。

## この章の目標

- `vertices`、`blocks`、`edges`、`boundary`の役割を説明できる。
- 2次元caseの`frontAndBack` patchを理解する。
- inlet、outlet、wallの境界条件をcaseへ対応づけられる。
- `blockMesh`と`foamRun`の結果をParaViewで確認できる。

## cavityからチャネルへ

天井駆動cavityでは、上面の移動壁によって流れが生じる。一方、Hagen--Poiseuille流れでは、入口から流体が入り、出口から流出する。

```{figure} ./images/blockmesh/cavity-channel-comparison.png
:alt: 天井駆動cavityとHagen--Poiseuille流れの比較
:align: center

天井駆動cavityと2次元チャネル流れの概念比較。
```

形状を変更するだけでなく、patch名と`0/U`、`0/p`の境界条件を流れ場に合わせる必要がある。

## チャネルcaseを実行する

`channel` caseは、前の[「cavityを実行して可視化する」](cavity.md)の章でダウンロードした`OpenFOAM-exercises-2026.1.zip`に含まれている。すでにダウンロード・展開している場合は、その中の`channel`を使えばよく、再ダウンロードは不要である。

まだ入手していない場合は、次のReleaseから取得する。

<a href="https://github.com/Kogakuin-FEL/OpenFOAM-exercises/releases/tag/v2026.1" target="_blank" rel="noopener">OpenFOAM-exercises v2026.1 Release</a>

```text
OpenFOAM-exercises-2026.1.zip
```

Releaseページが404になる場合は、[「cavityを実行して可視化する」の章にある注意事項](cavity.md)を確認する。

展開後、blueCFD-Core terminalで実行する。

```sh
cd channel
blockMesh
foamRun
paraFoam
```

このcaseは、inlet、outlet、wall、`frontAndBack`を持つ2次元の層流チャネルである。`frontAndBack`は`empty`として扱われ、厚さ方向の変化を解かない。

```{figure} ./images/blockmesh/channel-boundary-conditions.png
:alt: チャネル流れの境界条件
:align: center

チャネル流れの境界条件の概念図。実際のcaseでは、配布された`0/`と設定ファイルを確認する。
```

## blockMeshDictの基本

`system/blockMeshDict`では、まず頂点を定義し、それらを組み合わせてhex blockを作り、外側の面をpatchとして名前付けする。

```foam
vertices
(
    (0 0 0)
    (1 0 0)
    (1 1 0)
    (0 1 0)
    (0 0 0.1)
    (1 0 0.1)
    (1 1 0.1)
    (0 1 0.1)
);

blocks
(
    hex (0 1 2 3 4 5 6 7) (20 20 1) simpleGrading (1 1 1)
);
```

`vertices`の各行には、記述した順に0から頂点番号が付く。`blocks`の`hex`では、この番号を使ってblockの8頂点を指定する。次の図は、上のコードの座標と頂点番号の対応を示している。

```{figure} ./images/blockmesh/cavity-vertices.png
:alt: cavityの直方体に付けた頂点番号と座標軸
:align: center
:width: 70%

`vertices`の記述順に割り当てられる頂点番号と、直方体上の位置との対応。
```

この例の`hex (0 1 2 3 4 5 6 7)`では、頂点番号の順序によってblockの局所座標系とセル分割方向が決まる。`hex`の番号は任意の順に並べず、図と対応する順序で指定する。

- `vertices`：座標を持つ頂点の一覧。番号は記述順に付く。
- `blocks`：頂点番号を使って定義するblockと、その内部のセル分割。
- `edges`：直線以外の辺が必要な場合の定義。
- `boundary`：外側の面をpatchへ分類する定義。

これまで扱った`cavity`と`channel`では、計算領域全体を1個のblockで表していた。`blockMeshDict`では複数のblockを組み合わせることもできる。その具体例を、後述する角柱まわり流れで見ていく。

## 2次元patch

厚さ方向を1セルにした2次元caseでは、前後面を`empty`にする。境界面は、その面を構成する頂点番号を`boundary`の`faces`に指定してpatchへ分類する。キャビティでは、上面が`movingWall`、底面と左右側面が`fixedWalls`、厚さ方向の2面が`frontAndBack`に対応する。

```{figure} ./images/blockmesh/cavity-boundary-patches.png
:alt: cavityの直方体と境界面を指定する頂点番号
:align: center
:width: 70%

キャビティの頂点番号。上部に分けて示した面が`movingWall`、底面と左右側面が`fixedWalls`、厚さ方向の前後面が`frontAndBack`に対応する。
```

例えば、上面の`movingWall`は次のように指定する。

```foam
movingWall
{
    type wall;
    faces
    (
        (3 7 6 2)
    );
}
```

`boundary`の`faces`には、境界面を構成する頂点番号を指定する。少なくともOpenFOAM Foundation 12以降では、同じ面を構成する頂点番号であれば、その記述順序は問われない。

```foam
frontAndBack
{
    type empty;
    faces
    (
        (0 3 2 1)
        (4 5 6 7)
    );
}
```

`frontAndBack`は厚さ方向の前後面を表し、2次元caseでは`empty`にする。patchの型と`0/U`、`0/p`の組み合わせが整合していることを確認する。

## チャネル内流れから角柱まわり流れへ

ここまでは、チャネル内を流れる流体を解析した。次は、先ほど使用した`channel` caseをもとに計算領域を変更し、流れの中に置かれた角柱のまわりを流体が通過する場合を解析してみよう。角柱内部は流体領域に含めず、その周囲の流体領域を8個のblockで構成する。

以下に角柱まわり流れのblock分割例を示す。

```{figure} ./images/blockmesh/square-cylinder-blocks.png
:alt: 角柱まわり流れのblock分割
:align: center

角柱まわり流れのblock分割例。図中のblockは流体領域を表す。
```

`cavity`や`channel`では`blocks`の中に`hex`の定義が1個だけだったが、複数のblockを使う場合は、blockごとに`hex`を定義して並べる。この角柱まわり流れでは8個のblockを使うため、`blocks`の中に8個の`hex`定義を書く。

次の例は8個の定義の構造を示すための省略表記である。`...`を含むため、実行できる`blockMeshDict`ではない。頂点番号、分割数、gradingは自分で設定する。1個の`hex`は1個のblockを表し、1個の計算セルを意味するわけではない。各blockの内部は指定した分割数で細分化される。隣接するblockでは、共有面の頂点とセル分割が整合するように設計する。

```foam
blocks
(
    hex (...) (...) simpleGrading (...)
    hex (...) (...) simpleGrading (...)
    hex (...) (...) simpleGrading (...)
    hex (...) (...) simpleGrading (...)
    hex (...) (...) simpleGrading (...)
    hex (...) (...) simpleGrading (...)
    hex (...) (...) simpleGrading (...)
    hex (...) (...) simpleGrading (...)
);
```

続いて、解析格子と計算結果の例を示す。

```{figure} ./images/blockmesh/square-cylinder-mesh.png
:alt: 角柱後流の解析格子
:align: center

角柱後流の解析格子の例。
```

```{figure} ./images/blockmesh/square-cylinder-pressure.png
:alt: 角柱後流の圧力場
:align: center

角柱後流の圧力場の例。
```

```{figure} ./images/blockmesh/square-cylinder-speed.png
:alt: 角柱後流の速度絶対値
:align: center

角柱後流の速度絶対値を示す例。
```

### channel caseを複製して作業用caseを作る

ZIPを展開したディレクトリで、元の`channel`を残したままコピーを作り、コピー先で作業する。

```sh
cp -r channel square-cylinder
cd square-cylinder
```

入口、出口、角柱表面、上下境界、前後面をpatchとして定義し、各patch名と`0/U`、`0/p`の境界条件を一致させる。

主に見直すファイルは次のとおりである。

- `system/blockMeshDict`：頂点、block、分割数、patch
- `0/U`、`0/p`：各patchの速度・圧力境界条件
- `constant/physicalProperties`：動粘性係数とReynolds数
- `system/controlDict`：時間刻み、終了時刻、出力間隔
- `constant/momentumTransport`：流れのモデル
- 必要に応じて`system/fvSchemes`、`system/fvSolution`：離散化・solver設定

### メッシュを作り、計算する

1. `blockMeshDict`と境界条件を編集する。
2. `blockMesh`を実行し、`checkMesh`でメッシュを確認する。
3. `paraFoam`でメッシュとpatchを確認する。問題があればcaseを修正して`blockMesh`からやり直す。
4. `foamRun`で計算する。
5. 必要に応じて渦度を計算し、ParaViewで後流とカルマン渦を確認する。
6. 計算条件、メッシュ、可視化結果を記録する。

## 渦度を後処理する

OpenFOAM 12では、計算終了後に次を実行して渦度を生成する。

```sh
postProcess -func vorticity
paraFoam
```

渦度はベクトル量である。2次元caseでは、厚さ方向（通常はz方向）の成分を表示すると、後流の回転構造を確認しやすい。

```{figure} ./images/blockmesh/square-cylinder-vorticity.png
:alt: 角柱後流の渦度
:align: center

`postProcess -func vorticity`で生成した渦度を表示した例。
```

## 課題

角柱まわり流れについて、次の内容をレポートにまとめる。

1. 天井駆動cavityと角柱まわり流れで、境界条件がどのように異なるか説明する。
2. 角柱や円柱の後流にカルマン渦が現れるReynolds数の範囲を文献で調べる。
3. 角柱まわり流れを解析する。カルマン渦が現れる条件を試みるが、観察できない場合も結果として記録する。
4. 解析条件、メッシュ、可視化結果を適切にレポートへまとめる。

任意形状へ発展させる課題は[指定形状まわりの2次元外部流れ](external-flow-2d.md)を参照する。提出方法と期限はKU-LMSで確認する。

## ライセンス

```{note}
このページの本文と自作図版は [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.ja) のもとで提供されています。
コードやノートブックの例は MIT License に従います。
第三者の著作物を含む一部のスクリーンショット等は、CC BY-NC-SA 4.0の適用対象外です。詳細は [LICENSE-docs.md](https://github.com/akonno/FluidSeminarMaterials/blob/main/LICENSE-docs.md) を参照してください。
```
