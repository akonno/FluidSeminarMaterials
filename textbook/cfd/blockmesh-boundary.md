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

- `vertices`：座標を持つ節点。
- `blocks`：節点を順序づけて作る流体領域。
- `edges`：直線以外の辺が必要な場合の定義。
- `boundary`：外側の面をpatchへ分類する定義。

## 2次元patch

厚さ方向を1セルにした2次元caseでは、前後面を`empty`にする。入口・出口・壁のpatchには、それぞれの物理条件に合った型と場の境界条件を指定する。

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

点の並びは、使用するOpenFOAM版のblockMeshの規則に従う。patchの型と`0/U`、`0/p`の組み合わせが整合していることを確認する。

## チャネル内流れから角柱まわり流れへ

ここまでは、チャネル内を流れる流体を解析した。次は、このチャネルの計算領域を変更し、流れの中に置かれた角柱のまわりを流体が通過する場合を解析してみよう。

先ほど使用した`channel` caseをコピーし、計算領域を変更して角柱まわり流れの計算caseを作成しよう。角柱の周囲は、図に示すように8個のblockに分けて構成できる。`blockMeshDict`と境界条件は自分で設計する。

以下に角柱まわり流れのblock分割と解析結果の例を示す。

```{figure} ./images/blockmesh/square-cylinder-blocks.png
:alt: 角柱まわり流れのblock分割
:align: center

角柱まわり流れのblock分割例。図中のblockは流体領域を表す。
```

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

角柱を含む流体領域では、角柱内部にセルを作らず、その周囲の流体領域を8個のblockに分ける。頂点番号、hexの接続、block間の面、セル分割数を整合させる。入口、出口、角柱表面、上下境界、前後面をpatchとして定義し、各patch名と`0/U`、`0/p`の境界条件を一致させる。

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
