# blockMeshと境界条件

この章では、流れ場の形状をblockMeshで定義する方法を学ぶ。原資料pp.24--31の、チャネル流れ、blockとpatch、角柱まわり流れ、渦度の可視化、課題をまとめている。

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

2026年版のchannel caseは、`OpenFOAM-exercises`のRelease Assetに含まれている。古い`channel_2024.tgz`を使わず、次のReleaseから取得する。

<a href="https://github.com/Kogakuin-FEL/OpenFOAM-exercises/releases/tag/v2026.1" target="_blank" rel="noopener">OpenFOAM-exercises v2026.1 Release</a>

```text
OpenFOAM-exercises-2026.1.zip
```

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

チャネル流れの境界条件を示す原資料の説明図。実際のcaseでは、配布された`0/`と設定ファイルを正として確認する。
```

旧版資料では`tar xf channel_2024.tgz`と`icoFoam`を案内していたが、旧archiveは現行caseのsourceではない。2026年版ではRelease Assetの`channel`を使い、OpenFOAM 12の`foamRun` workflowを実行する。

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

## 角柱まわり流れの考え方

原資料では、8個のblockで角柱まわりの2次元流れ場を作り、後流の圧力、速度、渦度を調べている。

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

2026.1 Releaseには、検証済みのsquare-cylinder caseは含まれていない。ここではblockMesh、patch、後流、カルマン渦を考える例として説明する。配布caseとして実行できると誤解しないこと。

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

旧資料にある単独の`vorticity`コマンドは、OpenFOAM 5以前を対象としたlegacy情報である。2026年版の手順では`postProcess -func vorticity`を使う。

## 課題

角柱まわり流れについて、次の内容をレポートにまとめる。

1. 天井駆動cavityと角柱まわり流れで、境界条件がどのように異なるか説明する。
2. 角柱や円柱の後流にカルマン渦が現れるReynolds数の範囲を文献で調べる。
3. 角柱まわり流れを解析する。カルマン渦が現れる条件を試みるが、観察できない場合も結果として記録する。
4. 解析条件、メッシュ、可視化結果を適切にレポートへまとめる。

2026.1 Releaseにはsquare-cylinder caseがないため、ケース配布と実行手順は別途用意されるまで保留である。提出方法と期限はKU-LMSで確認する。

## ライセンス

```{note}
このページの本文と自作図版は [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.ja) のもとで提供されています。
コードやノートブックの例は MIT License に従います。
第三者の著作物を含む一部のスクリーンショット等は、CC BY-NC-SA 4.0の適用対象外です。詳細は [LICENSE-docs.md](https://github.com/akonno/FluidSeminarMaterials/blob/main/LICENSE-docs.md) を参照してください。
```
