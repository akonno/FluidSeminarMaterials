# 指定形状まわりの2次元外部流れ

原資料pp.32--34では、方眼紙とblockMeshを使って自分で2次元形状を定義し、物体まわりの流れを解析する。ここでは、その課題の考え方と提出内容をまとめる。実行可能なcaseは、課題条件に合わせて学生が作成する。

## 課題の位置づけ

前章の角柱は、blockとpatchの定義を学ぶための単純な例だった。今回は、単純な直方体などを避け、自分で決めた2次元形状を流体領域の中に配置する。

## 方眼紙で形状を設計する

次の順に設計する。

1. 物体の輪郭と流れの向きを決める。
2. 物体の周囲を複数のblockへ分割する。
3. 各blockのverticesと分割数を決める。
4. inlet、outlet、wall、`frontAndBack`をpatchとして分類する。
5. `0/U`、`0/p`、`system`の設定を整合させる。

blockMeshを実行したら、まずメッシュの形と境界patchをParaViewで確認する。その後に流れを計算し、圧力や速度場を可視化する。

```{admonition} 課題例について
過去の学生作品を参考例として使用していたが、公開教材では掲載しない。必要な提出内容は本文中の条件に従うこと。
```

## 解析の実行

学生が作成したcaseでは、まず`blockMeshDict`と境界条件を確認し、次の順に実行する。solverの設定は2026年版のOpenFOAM 12 / `foamRun` workflowに合わせる。

```sh
blockMesh
foamRun
paraFoam
```

`blockMesh`の終了後にメッシュとpatchを確認し、計算が終了してから圧力場、速度場、必要に応じて渦度を表示する。square-cylinderの配布caseはないため、この章のcaseは各自が設計する。

```{figure} ./images/placeholders/student-example-placeholder.png
:alt: 過去の学生作成例を掲載しないことを示すplaceholder
:align: center

元資料では学生作成のblock設計図と解析結果を参考例として示していたが、公開教材では掲載しない。図の代わりに、この章の手順と課題条件を用いる。
```

## 課題

自分で決めた2次元形状について、流れ解析を実施する。単純な形状は対象から除外する。

レポートには少なくとも次を含める。

- 解析対象の形状と、形状を選んだ理由
- 方眼紙または同等の方法で設計したblock構成
- meshとpatchの定義
- Reynolds数などの解析条件
- 圧力場、速度場、その他の観察結果

学生が作成した図は、公開教材へ転載する前に本人の許諾と出典表示を確認する。ここでは個別の学生作成図を掲載しない。

提出方法と期限はKU-LMSで確認する。

## ライセンス

```{note}
このページの本文と自作図版は [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.ja) のもとで提供されています。
コードやノートブックの例は MIT License に従います。
第三者の著作物を含む一部のスクリーンショット等は、CC BY-NC-SA 4.0の適用対象外です。詳細は [LICENSE-docs.md](https://github.com/akonno/FluidSeminarMaterials/blob/main/LICENSE-docs.md) を参照してください。
```
