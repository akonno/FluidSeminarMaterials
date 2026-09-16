# cavityの計算条件を変更する

この章では、cavity caseの設定ファイルを読み、粘性係数、Reynolds数、メッシュ、時間刻み、計算領域を変更する。原資料pp.14--23を、OpenFOAM 12のcase構造に合わせて整理している。

## 設定ファイルを編集する

設定ファイルはテキストファイルなので、blueCFD-Coreに付属するエディタ、Windowsの任意のテキストエディタ、またはVS Codeなどで開ける。教材では特定のエディタを必須にしない。

```sh
cd cavity
explorer.exe .
```

開く主なファイルは次のとおりである。

| ファイル | 役割 |
| --- | --- |
| `constant/physicalProperties` | 動粘性係数`nu` |
| `constant/momentumTransport` | 層流・乱流モデル |
| `system/blockMeshDict` | 頂点、ブロック、パッチ、分割数 |
| `system/controlDict` | 時間刻み、終了時刻、書き出し間隔 |
| `0/U`, `0/p` | 初期場と境界条件 |

## Reynolds数を変更する

cavityの代表速度を`U`、代表長さを`L`、動粘性係数を`\nu`とすると、Reynolds数は次で表される。

$$
Re = \frac{UL}{\nu}
$$

2026年版caseの初期値は次のとおりである。

```text
nu = 0.01 m^2/s
U  = 1 m/s
L  = 0.1 m
Re = 1 * 0.1 / 0.01 = 10
```

`constant/physicalProperties`の`nu`を変更すると、同じ形状・速度でもReynolds数を変更できる。目標のReynolds数を`Re_target`とすると、代表速度と長さを変えない場合は、次の値を設定する。

$$
\nu = \frac{UL}{Re_{\mathrm{target}}}
$$

設定を変更したら、メッシュ生成と計算をやり直す。

```sh
foamListTimes -rm
blockMesh
foamRun
paraFoam
```

`foamListTimes -rm`は生成済みの数値時刻ディレクトリを削除する。trackedな`0/`初期条件は削除しない。

## メッシュを詳細化する

`system/blockMeshDict`の`blocks`には、現在のcavityで次の分割数が指定されている。

```foam
blocks
(
    hex (0 1 2 3 4 5 6 7) (20 20 1) simpleGrading (1 1 1)
);
```

`(20 20 1)`は、x方向20、y方向20、z方向1の分割を表す。2次元caseではz方向を1セルとし、前後面を`empty`にする。高Reynolds数の計算では、流れの変化を解像するためメッシュを細かくする必要があるが、セル数の増加に伴って計算量も増える。

## 時間刻みとCourant数

Courant数の代表的な見積もりは次の式である。

$$
C = \frac{U\Delta t}{\Delta x}
$$

- `U`：代表速度
- `\Delta t`：時間刻み
- `\Delta x`：最小格子幅

Courant数が大きくなると、計算が不安定になったり、期待しない結果になったりする。これはCFL条件として知られている。OpenFOAMでは`system/controlDict`の`deltaT`を変更する。

現在のcaseは次の設定である。

```foam
deltaT          0.005;
```

領域の長さが`0.1 m`、x方向の分割数が20、代表速度が`1 m/s`なら、単純な見積もりでは`\Delta x = 0.005 m`、`C = 1`となる。分割数を増やす場合は、`deltaT`を小さくすることも検討し、実際の計算中の安定性を確認する。`C = 1`を別のcaseやsolverへそのまま適用してはいけない。

## 計算領域を変更する

`blockMeshDict`の`vertices`を変更すると、正方形のcavityを長方形へ変更できる。座標、`convertToMeters`、分割数、上面速度、境界条件を一貫して見直す。

計算領域を入口・出口のある流れへ変更する場合は、次の設定を一緒に変更する必要がある。

1. `blockMeshDict`で入口・出口のpatchを定義する。
2. `0/U`と`0/p`で各patchの境界条件を指定する。
3. 物性、時間刻み、終了時刻を流れの条件に合わせる。
4. `blockMesh`と`foamRun`を実行し、結果をParaViewで確認する。

patchとblockの定義は、次章のチャネルとblockMeshの説明につながる。

## Ghia benchmarkとの比較

原資料では、Re=400、1000を必須、Re=3200、5000を任意とする比較課題を扱っている。Ghia et al.の結果はbenchmarkとして参照し、計算条件、メッシュ、時間発展の扱いをレポートに明記する。

```{note}
Ghia et al. (1982) の原図は、公開教材へそのまま転載しない。ここには、OpenFOAMの速度場から再構成した等間隔のstreamfunction contourを掲載する予定である。原図を掲載せず、文献と比較条件だけを残す。
```

```{figure} ./images/placeholders/ghia-streamfunction-placeholder.png
:alt: Ghia benchmark replacement placeholder
:align: center

Ghia et al. (1982) の原図は転載せず、OpenFOAMの計算結果から自作する等流関数コンターへ置き換える予定である。
```

比較課題では、Reynolds数だけでなく、メッシュ分割数、`deltaT`、終了時刻、比較した量を記録する。

## 課題

次の条件でcavityを計算し、結果を比較する。

- Re=400
- Re=1000
- 余力があればRe=3200、5000

ParaViewで流線や速度場を表示する方法は、授業時にKU-LMSで案内する補助資料も参照する。提出方法と期限はKU-LMSで確認する。

## ライセンス

```{note}
このページの本文と自作図版は [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.ja) のもとで提供されています。
コードやノートブックの例は MIT License に従います。
第三者の著作物を含む一部のスクリーンショット等は、CC BY-NC-SA 4.0の適用対象外です。詳細は [LICENSE-docs.md](https://github.com/akonno/FluidSeminarMaterials/blob/main/LICENSE-docs.md) を参照してください。
```
