# 与えられた車両形状による3次元外部流れ

原資料pp.35--39では、配布された車両形状を使って、3次元外部流れのメッシュ生成、計算、可視化を行う。2026年版では、case本体をKU-LMSのtgzではなく、OpenFOAM演習case repositoryのRelease Assetから配布する。

## Caseを入手する

<a href="https://github.com/Kogakuin-FEL/OpenFOAM-exercises/releases/tag/v2026.1" target="_blank" rel="noopener">OpenFOAM-exercises v2026.1 Release</a>から、次のZIPをダウンロードして展開する。

```text
OpenFOAM-exercises-2026.1.zip
```

GitHubの`Source code (zip)`は学生用case packageではない。展開後、blueCFD-Core terminalから`vehicle`へ移動する。

## STLを準備する

サンプルSTLは`model/`にあり、caseが読む固定名へコピーして使う。

```sh
cd vehicle
cp model/concept_car_038-mod.stl constant/geometry/STLObject.stl
```

`STLObject.stl`は、Gitで管理するサンプルをcase用の場所へ置く作業ファイルである。初期状態では意図的に`constant/geometry/`へコピーされていない。

車両モデルの出典は、case repositoryの[`vehicle/model/README.md`](https://github.com/Kogakuin-FEL/OpenFOAM-exercises/blob/main/vehicle/model/README.md)に記録されている。

## Allrunを実行する

```sh
./Allclean
./Allrun
```

`Allrun`は、概ね次の処理を行う。

1. `blockMesh`で背景メッシュを作る。
2. `decomposePar`で並列計算用に分割する。
3. `snappyHexMesh`でSTL形状を含むメッシュを生成する。
4. `renumberMesh`、`potentialFoam`を実行する。
5. `foamRun`を並列実行する。
6. `reconstructPar`で結果を再構成する。

このcaseは小さなcavityより計算時間とメモリを必要とする。実測では、対象環境で4並列のfull workflowが約16分23秒で完了したが、学生PCによって大きく異なる。

## ParaViewで確認する

`paraFoam`で結果を開き、必要に応じて`Mesh Regions`で`internalMesh`を非表示にする。車両表面、床、出口などのregionを選び、圧力場や断面の速度ベクトルを表示する。

最終時刻の`U`と`p`、力、streamline、cut-planeなどのfunction-object出力を確認する。設定と出力の詳細はcase repositoryの`VALIDATION.md`を参照する。

## 課題

3次元車両まわり流れを計算し、次を含む可視化結果をレポートする。

- 車両表面の圧力場
- 適切な断面の速度ベクトル
- 使用したcase、計算条件、メッシュの概要
- 計算に要した時間と、計算上の注意点

提出方法と期限はKU-LMSで確認する。

## ライセンス

```{note}
このページの本文と自作図版は [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.ja) のもとで提供されています。
コードやノートブックの例は MIT License に従います。
第三者の著作物を含む一部のスクリーンショット等は、CC BY-NC-SA 4.0の適用対象外です。詳細は [LICENSE-docs.md](https://github.com/akonno/FluidSeminarMaterials/blob/main/LICENSE-docs.md) を参照してください。
```
