# 指定形状まわりの2次元外部流れ

この課題では、自分で決めた2次元形状を方眼紙などで設計し、blockMeshで流体領域を定義して物体まわりの流れを解析する。実行可能なcaseは、課題条件に合わせて自分で作成する。

## 課題の位置づけ

前章の[角柱まわり流れ](blockmesh-boundary.md)では、配布されたchannel caseを土台に8ブロックのメッシュと境界条件を設計する。ここではその考え方を発展させ、単純な直方体などを避け、自分で決めた2次元形状を流体領域の中に配置する。

## 方眼紙で形状を設計する

次の順に設計する。

1. 物体の輪郭と流れの向きを決める。
2. 物体の周囲を複数のblockへ分割する。
3. 各blockのverticesと分割数を決める。
4. inlet、outlet、wall、`frontAndBack`をpatchとして分類する。
5. `0/U`、`0/p`、`system`の設定を整合させる。

blockMeshを実行したら、まずメッシュの形と境界patchをParaViewで確認する。その後に流れを計算し、圧力や速度場を可視化する。

## 形状設計と解析結果の例

以下に、3つの障害物を配置した形状について、方眼紙によるブロック配置の設計から、メッシュ生成、流れ解析、可視化までの例を示す。これは作成例の一つであり、課題では各自で形状とブロック配置を考えること。

```{figure} ./images/external-2d/three-obstacles-layout-sketch.png
:alt: 方眼紙上で設計した3つの障害物と計算領域のブロック配置
:width: 100%

図1 方眼紙上で設計した、3つの障害物を持つ計算領域のブロック配置。
```

```{figure} ./images/external-2d/three-obstacles-mesh.png
:alt: blockMeshで生成した3つの障害物を含む計算メッシュ
:width: 100%

図2 `blockMesh`で生成した計算メッシュ。
```

```{figure} ./images/external-2d/three-obstacles-pressure.png
:alt: 3つの障害物まわりの最終時刻の圧力分布
:width: 100%

図3 最終時刻 $t=0.1$ における圧力分布。
```

```{figure} ./images/external-2d/three-obstacles-streamlines.png
:alt: 3つの障害物まわりの最終時刻の流線。色は流速の大きさを表す
:width: 100%

図4 最終時刻 $t=0.1$ における流線。色は流速の大きさを表す。
```

## 解析の実行

前章「blockMeshと境界条件」で`channel`から作成した`square-cylinder` caseを、新しい形状用にコピーする。`square-cylinder`は配布caseではなく、前章で作成した作業用caseである。`square-cylinder`があるディレクトリで、元のcaseを残したまま別名のcaseを作る。ここでは新しいcase名を`custom-shape`とする。

```sh
cp -r square-cylinder custom-shape
cd custom-shape
```

OpenFOAMは、計算結果をcaseディレクトリ内の時刻名のディレクトリに保存する。例えば`0.1/`には時刻0.1、`0.2/`には時刻0.2の`U`や`p`などが保存され、`paraFoam`はこれらを読み込んで可視化する。実際に作られる時刻ディレクトリは`system/controlDict`の出力設定によって異なる。

新しい形状を時刻0から計算する場合は、まず操作場所がコピー先の`custom-shape`であることを確認する。そのうえで、`custom-shape`内にある`0/`以外の数値名の計算結果ディレクトリ（例えば`0.1/`、`0.2/`）をすべて削除する。元の`square-cylinder`には手を加えない。初期条件の`0/`と、物性値・メッシュを置く`constant/`、計算条件を置く`system/`は削除しない。さらに、`system/controlDict`を次の設定にする。

```foam
startFrom   startTime;
startTime   0;
```

コピーしたcaseの`system/blockMeshDict`を、方眼紙で設計した形状に合わせて編集する。頂点座標、blockの配置、各blockのセル分割数、境界面を設定する。`0/U`、`0/p`などの境界条件も確認・調整し、`blockMeshDict`で定義したpatch名と、各フィールドの`boundaryField`にあるpatch名を一致させる。

設定を確認したら、OpenFOAM 12の`foamRun` workflowで解析する。

```sh
blockMesh
checkMesh
paraFoam
```

`blockMesh`と`checkMesh`の後、`paraFoam`で計算前のメッシュとpatchを確認する。問題がなければ計算し、結果をParaViewで可視化する。

```sh
foamRun
```

必要に応じて計算後に渦度を生成する。

```sh
postProcess -func vorticity
paraFoam
```

角柱のケース構築は[前章の手順](blockmesh-boundary.md)を参考にする。

## 課題

自分で決めた2次元形状について、流れ解析を実施する。単純な形状は対象から除外する。

レポートには少なくとも次を含める。

- 解析対象の形状と、形状を選んだ理由
- 方眼紙または同等の方法で設計したblock構成
- meshとpatchの定義
- Reynolds数などの解析条件
- 圧力場、速度場、その他の観察結果

提出方法と期限はKU-LMSで確認する。

## ライセンス

```{note}
このページの本文と自作図版は [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.ja) のもとで提供されています。
コードやノートブックの例は MIT License に従います。
第三者の著作物を含む一部のスクリーンショット等は、CC BY-NC-SA 4.0の適用対象外です。詳細は [LICENSE-docs.md](https://github.com/akonno/FluidSeminarMaterials/blob/main/LICENSE-docs.md) を参照してください。
```
