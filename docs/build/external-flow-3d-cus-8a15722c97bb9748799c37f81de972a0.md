# 形状を指定する3次元外部流れ

車両caseのSTLを自分で作成または入手した形状へ置き換え、任意の3次元物体まわり流れを解析する。ここでは既存caseの物理設定を不用意に変えず、形状データを準備する手順に集中する。

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

Concept Car 038の寸法と座標。STLの単位や向きを確認するときの参考例。
```

`STLObject.stl`に置き換える形状は、解析領域との大きさ、流れ方向、原点、座標軸を確認する。寸法図がない場合も、モデルの単位と大きさを調べ、caseの座標系に合うように準備する。

```{figure} ./images/external-3d-custom/custom-domain-dimensions.png
:alt: 3次元外部流れの計算領域の寸法と座標
:align: center

3次元外部流れで形状と計算領域の関係を確認するための寸法・座標図。
```

## 解析例：潜水艇まわりの流れ

ここでは、複雑な形状をCFDに利用する工程の参考例として、Codels Submarineを使った教員側の解析を紹介する。学生がこのモデルを使う必要はなく、自分で選んだ形状を課題に用いる。

### オリジナルモデル

解析対象は、船体、司令塔、マスト、フィン、窓、プロペラなどを備えたCodels Submarineである。公開モデルはGLB形式で、公開ページでは寸法がメートル単位、前方が+Z方向とされている。

```{figure} ./images/external-3d-custom/submarine-original-snapshot.png
:alt: Codels Submarineのオリジナル3Dモデル
:align: center

解析対象として選んだ潜水艇のオリジナル3Dモデル（GLB形式）。
```

モデル出典：[Codels Submarine](https://codels.download/models/submarine)。公開ページではCC0 1.0で、帰属表示は不要と案内されている。ここでは出典の追跡のために記載する（[CC0 1.0 Universalの条文](https://creativecommons.org/publicdomain/zero/1.0/legalcode)）。モデルの利用条件と教材本文・図版のライセンスは別である。

### CFD用形状の準備

`snappyHexMesh`はSTLまたはOBJ形式の三角形表面を扱うが、GLB形式は直接読み込めない（[OpenFOAM v12 User Guide](https://doc.cfd.direct/openfoam/user-guide-v12/snappyhexmesh)）。一方、今回使う`vehicle` caseは`system/snappyHexMeshDict`で`STLObject.stl`を読み込む設定である。今回、GLBからSTLへの直接変換に使ったソフトウェアや操作は記録から確認できなかった。解析には、GLBの非退化三角形との形状対応を照合した3Dプリンター用STLを使った。モデルを入手するときは、形式に加えて出典や利用条件も確認する。

潜水艇の長軸をx軸に合わせ、船首が流入側（−x方向）を向くように配置した。解析用の全長は約3.8 mに設定したが、実艇の寸法を表すものではない。プロペラブレード4枚を除去し、船尾の軸・キャップ・ハブ状部分は残した。修復前のSTLには開いた境界や部品の重なり、自己交差があったため、[FormWare Online STL Repair](https://formware.co/onlinestlrepair)で修復した。修復後は、穴のない、一続きの閉じた表面メッシュが得られた。ただし、`surfaceCheck -checkSelfIntersection`では、修復後も93件の自己交差が検出された。表面が閉じていることと自己交差がないことは別々に確認する。自動修復ですべての欠陥が解消するとは限らないため、修復後も検査が必要である。

FormWareは形状データを外部のオンラインサービスへ送信して処理する。企業や研究室の非公開モデルなどは、外部へ送信してよいか事前に確認する。公開モデルでも、ライセンスや利用条件を確認する。

```{figure} ./images/external-3d-custom/submarine-surface.png
:alt: CFD用に準備したプロペラなし潜水艇の表面形状
:align: center

CFD解析用に整備した潜水艇の表面形状。プロペラブレードを除き、表面修復を行った。軸・ハブ状部分は残している。
```

### 表面メッシュ

修復後のSTLを使い、OpenFOAMの`snappyHexMesh`で計算メッシュを生成した。格子生成前にblueCFD-Core terminalでcaseのルートへ移動し、`surfaceCheck`でSTL表面の閉鎖や開境界、非多様体エッジを確認する。自己交差は追加オプションで調べる。

```sh
surfaceCheck constant/geometry/STLObject.stl
surfaceCheck -checkSelfIntersection constant/geometry/STLObject.stl
```

`surfaceCheck`はSTLなどの表面形状を検査するコマンドである。計算メッシュの品質は、`snappyHexMesh`で格子を生成した後に`checkMesh`で調べる。今回のblueCFD-Coreでは、通常検査に加えて次のオプションによる全幾何・全トポロジー検査を実行した記録がある。

```sh
checkMesh
checkMesh -allGeometry -allTopology
```

今回のメッシュは約188万セルで、通常の`checkMesh`では`Mesh OK`だった。一方、全幾何・全トポロジー検査ではconcave cellsが53,694個（全セルの約2.86%）報告された。この結果だけで計算全体が無効とはいえないが、メッシュを生成できたことや通常検査の`Mesh OK`だけで、品質上の問題がないとも判断できない。

次の全体図では艇の表面に沿うメッシュを、拡大図では窓枠や司令塔の付け根などの細部に対する形状追従を確認できる。

```{figure} ./images/external-3d-custom/submarine-surface-wedges.png
:alt: 潜水艇表面全体の計算メッシュ
:align: center

snappyHexMeshによって生成した潜水艇表面の計算メッシュ。
```

```{figure} ./images/external-3d-custom/submarine-surface-wedges-zoomed.png
:alt: 窓枠と司令塔付け根付近の表面メッシュ拡大図
:align: center

潜水艇表面メッシュの拡大図。窓枠や司令塔の付け根周辺で、表面に沿ってセルが配置されている。
```

### 計算結果

水中の流入速度を2 m/sとし、OpenFOAM Foundation 12の定常RANSで解析した。乱流モデルはSpalart–Allmaras、メッシュは約188万セルで、Linux環境で8並列計算を行った。以下は3000反復時点の可視化である。

```{figure} ./images/external-3d-custom/submarine-p.png
:alt: 3000反復時点の潜水艇表面の運動学的圧力分布
:align: center

潜水艇表面の運動学的圧力 p（m²/s²）の分布。定常RANS計算の3000反復時点を示す。pはPa単位の圧力ではない。
```

```{figure} ./images/external-3d-custom/submarine-streamline100.png
:alt: 潜水艇の周囲を通る流線と艇体表面圧力
:align: center

艇体中央部付近から生成した流線と表面圧力。流線の色は速度の大きさ |U|（m/s）、艇体表面の色は運動学的圧力 p（m²/s²）を示す。
```

このような事例を参考に、各自が選んだ三次元形状について、出典、単位、座標変換、表面修復、メッシュで再現できた細部を記録し、流れ場の特徴と解析上の限界を考察する。

```{note}
この計算は定常反復を3000回行ったが、流体力と後流速度には変動が残り、定常収束したとは判断できない。したがって、抵抗値の定量予測例としては扱わない。流線はある反復時点の速度場を可視化したもので、流体粒子の時間軌跡や時間発展を示すものではない。ここでは、複雑な三次元形状に対するメッシュ生成と、流れ場の可視化の進め方を示す参考例として紹介する。
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

## ライセンス

```{note}
このページの本文と自作図版は [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.ja) のもとで提供されています。
コードやノートブックの例は MIT License に従います。
第三者の著作物を含む一部のスクリーンショット等は、CC BY-NC-SA 4.0の適用対象外です。詳細は [LICENSE-docs.md](https://github.com/akonno/FluidSeminarMaterials/blob/main/LICENSE-docs.md) を参照してください。
```
