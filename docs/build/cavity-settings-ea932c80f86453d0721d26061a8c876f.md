# cavityの計算条件を変更する

この章では、cavity caseの設定ファイルを読み、粘性係数、Reynolds数、メッシュ、時間刻み、計算領域を変更する。設定を変えたとき、流れや計算結果がどう変化するかを確認しよう。

## 設定ファイルを編集する

OpenFOAMの設定ファイルはテキストファイルであり、テキストエディタで編集できる。blueCFD-Core 2024-1に付属するNotepad2は手軽な選択肢だが、使用するエディタは限定しない。Windowsの「メモ帳」やVS Codeなど、ほかのテキストエディタを使ってもよい。

### Notepad2で設定ファイルを開く

配布ZIPを展開したディレクトリでblueCFD-Core terminalを開き、`cavity` caseへ移動してNotepad2を起動する。

```sh
cd cavity
notepad2
```

起動直後は空の編集画面が表示される。Notepad2のメニューから **File → Open** を選び、case内の`constant/physicalProperties`を開く。

```{figure} ./images/cavity/notepad2-start.png
:alt: 起動直後のNotepad2の空の編集画面
:align: center

Notepad2を起動した直後の画面。
```

開いたファイルでは、`nu`の行に動粘性係数が設定されている。たとえば初期値は`0.01`であり、Reynolds数に合わせてこの数値を変更し、保存する。

```{figure} ./images/cavity/notepad2-physicalproperties.png
:alt: Notepad2で開いたphysicalPropertiesファイルのnu設定行
:align: center

Notepad2で`constant/physicalProperties`を開いた画面。`nu`の数値を編集できる。
```

`notepad2`で起動すると、Notepad2を閉じるまでblueCFD-Core terminalは次のコマンドを受け付けない。エディタを開いたままterminalを使う場合は、末尾に`&`を付けて起動する。

```sh
notepad2 &
```

`&`はコマンドをバックグラウンドで実行する指定である。

### Windows側から設定ファイルを開く

Windowsのエディタで編集したい場合は、caseのディレクトリで次を実行すると、その場所をエクスプローラーで開ける。

```sh
explorer.exe .
```

エクスプローラーから`constant/physicalProperties`などを選び、任意のテキストエディタで編集してよい。

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

メッシュ解像度が計算結果に与える影響は、[「計算結果を信用する前に」](cavity-validation.md)で比較している。

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

計算終了時刻が短すぎる場合の影響や定常判定については、[「計算結果を信用する前に」](cavity-validation.md)を参照する。

## 計算領域を変更する

`blockMeshDict`の`vertices`を変更すると、正方形のcavityを長方形へ変更できる。座標、`convertToMeters`、分割数、上面速度、境界条件を一貫して見直す。

計算領域を入口・出口のある流れへ変更する場合は、次の設定を一緒に変更する必要がある。

1. `blockMeshDict`で入口・出口のpatchを定義する。
2. `0/U`と`0/p`で各patchの境界条件を指定する。
3. 物性、時間刻み、終了時刻を流れの条件に合わせる。
4. `blockMesh`と`foamRun`を実行し、結果をParaViewで確認する。

patchとblockの定義は、次章のチャネルとblockMeshの説明につながる。

## Ghia benchmarkとの比較

Ghia et al. (1982) の結果をbenchmarkとして参照し、計算条件、メッシュ、時間発展の扱いをレポートに明記する。

```{note}
図は Ghia et al. (1982) の原図を転載したものではない。Linux上のOpenFOAM 14による計算速度場からstreamfunctionを再構成した自作図であり、Ghia et al.の研究はベンチマークとして参照している。
```

図はRe=400、1000、3200、5000のstreamfunction contourを比較している。2次元非圧縮流れでは、streamfunctionが一定の線（`ψ = const.`）は流線に相当する。4ケースすべて、定常性を確認した速度場から再構成した。Re=400と1000は無次元時刻 `t*=80`、Re=3200は `t*=200`、Re=5000は `t*=290` の場を用いている。

contour levelは等間隔ではない。Ghia et al. (1982) のFig. 3およびTable IIIの見せ方を参考に、主渦の内側、外殻、隅の渦を少数の線で示し、各ReのOpenFOAM場に応じてlevelを選んだ。Ghia原図の線位置をトレースしたものではない。

```{figure} ./images/cavity/cavity-streamfunction-contours.png
:alt: OpenFOAMの速度場から再構成したRe=400、1000、3200、5000のcavity streamfunction contour
:align: center
:width: 100%

OpenFOAMの定常lid-driven cavity速度場から再構成したstreamfunction contour。Re=400、1000、3200、5000を比較している。Ghia et al. (1982) の原図は転載せず、各Reの計算結果から作成した自作図である。
```

比較の参考文献: [Ghia, U., Ghia, K. N., and Shin, C. T. (1982), “High-Re solutions for incompressible flow using the Navier–Stokes equations and a multigrid method,” *Journal of Computational Physics*, 48(3), 387–411](https://doi.org/10.1016/0021-9991%2882%2990058-4)。

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
