# 形状を指定する3次元外部流れ

原資料pp.40--42では、車両caseのSTLを自分で作成または入手した形状へ置き換え、任意の3次元物体まわり流れを解析する。ここでは既存caseの物理設定を不用意に変えず、形状データを準備する手順に集中する。

## STLを置き換える

まず、`external-flow-3d.md`の手順で車両caseを一度実行できることを確認する。次に、解析したい形状をSTL形式で用意し、caseが読む名前へ置く。

```sh
cd vehicle
cp path/to/your-model.stl constant/geometry/STLObject.stl
./Allclean
./Allrun
```

Windows側でファイルをコピーする場合は、`explorer.exe .`で現在のcaseを開く方法もある。実行前にファイル名が正確に`STLObject.stl`であることを確認する。

## 寸法と単位

STLには、教材で想定するメートル単位の寸法と異なるモデルがある。CADソフトやオンラインモデルでは、ミリメートル単位で作られていることもあるため、次を確認する。

- 物体の全長・全幅・全高
- 流れ方向
- 原点と座標軸
- 解析領域に対する大きさ
- 法線の向きと閉じた表面かどうか

形状が大きすぎる、小さすぎる、または流れ方向と合わない場合は、CADソフト等で拡大・縮小、平行移動、回転を行う。変換後のSTLを`STLObject.stl`として配置する。

```{figure} ./images/external-3d-custom/vehicle-dimensions.png
:alt: Concept Car 038の寸法と座標
:align: center

元資料で示されていた車両形状の寸法・座標。2026年版では、モデルの単位と座標を確認するための例として扱う。
```

`STLObject.stl`に置き換える形状は、解析領域との大きさ、流れ方向、原点、座標軸を確認する。元資料の寸法図をそのまま再利用できない場合でも、これらの確認項目を満たすことが重要である。

```{figure} ./images/external-3d-custom/custom-domain-dimensions.png
:alt: 3次元外部流れの計算領域の寸法と座標
:align: center

3次元外部流れで形状と計算領域の関係を確認するための寸法・座標図。
```

## 課題

自分で解析したい3次元形状を用いて外部流れを解析し、レポートを作成する。直方体や円柱などの単純形状は対象から除外する。

レポートには少なくとも次を含める。

1. 解析対象と入手先または作成方法
2. 解析条件（Reynolds数など）
3. STLの寸法、単位、座標、変換内容
4. メッシュと計算結果
5. 形状を選択した理由と結果の考察

インターネット上のモデルを使う場合は、公開条件と出典URLを記録する。KU-LMSの動画教材や提出方法、期限は授業時の案内を確認する。

```{figure} ./images/placeholders/unknown-model-placeholder.png
:alt: 出典未確認の3Dモデルを公開版に掲載しないことを示すplaceholder
:align: center

元資料には出典未確認の3Dモデルによる解析結果例があるが、公開版では掲載しない。解析対象には出典とライセンスを確認できるモデルを使う。
```

## ライセンス

```{note}
このページの本文と自作図版は [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.ja) のもとで提供されています。
コードやノートブックの例は MIT License に従います。
第三者の著作物を含む一部のスクリーンショット等は、CC BY-NC-SA 4.0の適用対象外です。詳細は [LICENSE-docs.md](https://github.com/akonno/FluidSeminarMaterials/blob/main/LICENSE-docs.md) を参照してください。
```
