# CFD教材 Phase 2A: technical validation and case-distribution design

調査日: 2026-09-15

このレポートは、Word/PDFで運用中のblueCFD-Core / OpenFOAM教材をMySTへ移行する前の技術検証と配布設計をまとめたものである。教材本文、DOCX、PDF、外部case repositoryは変更していない。

本文中では、実機またはファイルで確認できた事項を **Verified**、将来の移行に向けた判断を **Recommendation**、確認できなかった事項を **Not verified** と記載する。

## 1. Environment

### Verified: local machine

| Item | Result |
| --- | --- |
| OS | Windows 11 Pro 25H2, build 26200.9457（build/DisplayVersionによる識別） |
| blueCFD-Core installation | `C:\blueCFD-Core\2024` |
| blueCFD environment | OpenFOAM 12 mingw-w64 Double Precision (`of12-64`) |
| OpenFOAM | OpenFOAM-12, build `12-8e8552546d20` |
| bundled ParaView | 5.11.2（`paraFoam -help`および同梱`pvpython`で確認） |
| standalone ParaView found | 5.11.2および6.1.1 |
| bundled editor | `C:\blueCFD-Core\2024\AddOns\notepad2\notepad2.exe` |
| bundled Git | 公式release notesでは2.45.2。ローカルMsys2 Gitの直接起動は権限エラーで再確認できず |

### Verified: official information checked

- blueCFD-Core Projectの公式Downloadsページは、調査日時点でWindows 10/11 64-bit向けの`blueCFD-Core 2024-1`を掲載している。掲載内容はOpenFOAM 12、ParaView 5.11.2、MS-MPI 10.1.2である。
- 公式ページはインストール先として、空白を含まない例（`C:\blueCFD-Core\2024\`）を示している。
- blueCFD-Core 2024-1の公式release notesには、OpenFOAM 12、GCC 12.2、Git 2.45.2、Python 3.11.9、Notepad2 4.2.25、ParaView 5.11.2が記載されている。

参照:

- [blueCFD-Core Downloads](https://bluecfd.github.io/Core/Downloads/)
- [blueCFD-Core 2024-1 release notes](https://bluecfd.github.io/Core/ReleaseNotes/bluecfd-core-2024-1/)

### Recommendation

2026年版のWindows主経路は、現時点で公式に掲載されている`blueCFD-Core 2024-1 / OpenFOAM 12`を対象として明示的に検証するのが安全である。Foundation版OpenFOAMの最新版とは系統とversionが異なるため、「OpenFOAM 12」と「OpenFOAM最新版」を同一視しない。

## 2. blueCFD-Core status

### Verified

`C:\blueCFD-Core\2024`には、次の構成が存在する。

```text
C:\blueCFD-Core\2024\
  AddOns\
  docs\
  msys64\
  ofuser-of12\
  OpenFOAM-12\
  shortcuts\
  Start Menu\
  ThirdParty-12\
  setvars_OF12.bat
  blueCFD-Core_MSys2_mingw64.bat
  blueCFD-Core-Portable.exe
  DOS_Mode_OF12.bat
```

`setvars_OF12.bat`とMsys2のlogin shellを使うと、blueCFD用のOpenFOAM 12環境を起動できる。環境名ファイルには次の表示がある。

```text
OpenFOAM 12 mingw-w64 Double Precision (of12-64)
```

### Recommendation

教材ではインストール先を固定的な必須条件にせず、`$FOAM_RUN`、`$FOAM_TUTORIALS`などの環境変数を主に説明する。ただし、blueCFD-Core公式ページが空白を含まないパスを案内しているため、Windows側の例として`C:\blueCFD-Core\2024`を示すことは妥当である。

## 3. OpenFOAM version and environment variables

### Verified: blueCFD shell

blueCFD-Core 2024-1のlogin shellで確認した値は次のとおり。

```text
WM_PROJECT_VERSION=12
FOAM_RUN=/home/ofuser/blueCFD/ofuser-of12/run
FOAM_TUTORIALS=/home/ofuser/blueCFD/OpenFOAM-12/tutorials
blockMesh=/home/ofuser/blueCFD/OpenFOAM-12/platforms/mingw_w64Gcc122DPInt32Opt/bin/blockMesh
icoFoam=/home/ofuser/blueCFD/OpenFOAM-12/platforms/mingw_w64Gcc122DPInt32Opt/bin/icoFoam
paraFoam=/home/ofuser/blueCFD/OpenFOAM-12/bin/paraFoam
postProcess=/home/ofuser/blueCFD/OpenFOAM-12/bin/postProcess
notepad2=/home/ofuser/AddOns/notepad2/notepad2
explorer.exe=/c/Windows/explorer.exe
```

`paraFoam`は`paraFoam -builtin -minpath`として定義されたaliasである。`foamVersion`は`OpenFOAM-12`を返し、`icoFoam -help`は`Using: OpenFOAM-12`およびbuild `12-8e8552546d20`を表示した。

### Recommendation

環境変数と`which`相当の確認はそのまま移行できる。WindowsのPowerShellとblueCFDのMsys2 shellでは、パス表記が異なるため、教材ではblueCFD terminal内の表記を主例にする。

## 4. cavity tutorial validation

### Verified: tutorial path

教材記載の次のpathは、実機のblueCFD-Core 2024-1に存在した。

```text
$FOAM_TUTORIALS/legacy/incompressible/icoFoam/cavity/cavity
```

一方、次のpathはインストール済みtutorial treeには存在しなかった。

```text
$FOAM_TUTORIALS/incompressible/icoFoam/cavity/cavity
```

したがって、`legacy/incompressible/icoFoam/cavity/cavity`は現行のblueCFD-Core 2024-1 / OpenFOAM 12で実在する教材対象pathである。

### Verified: minimum E2E test

repository外の一時ディレクトリへ、インストール済みtutorialのcavityをコピーして検証した。

```text
C:\Users\konno\AppData\Local\Temp\fluid-cfd-phase2a-e2e-17037c7146b8414aae8a6bed03924b17
```

結果:

| Step | Result |
| --- | --- |
| `blockMesh` | 成功。400 cells、movingWall/fixedWalls/frontAndBackを生成 |
| `icoFoam` | 成功。`0.1`から`0.5`まで計算し、各time directoryを生成 |
| `U` / `p` | `0`および計算後の各time directoryに生成 |
| `cavity.foam` | ParaView確認用として一時ディレクトリ内に作成 |
| Fatal error | なし |

`paraFoam -help`もstatus 0で、`-builtin`、`-touch`、`-minpath`を表示し、最後にParaView 5.11.2を起動する旨を表示した。

### Recommendation

Phase 2Bでは、cavityの実行手順をOpenFOAM 12の実機検証済みpathに合わせて維持できる。ただし、外部case repositoryのcavityは`foamRun` / `incompressibleFluid`へ移行済みであり、tutorialを使う本文の`icoFoam`と配布caseのsolverを同じ説明にするかは、章設計時に明示する必要がある。

## 5. vorticity post-processing

### Verified

先のcavity計算結果に対して、次を実行した。

```bash
postProcess -func vorticity
```

結果はstatus 0で、time directory `0`から`0.5`に`vorticity` fieldが生成された。生成fieldのheaderは次の性質を持つ。

```text
class      volVectorField
object     vorticity
dimensions [0 0 -1 0 0 0 0]
```

2D cavityの今回の結果では、非ゼロの主成分はz成分であった。ParaViewで表示する場合は、z componentまたはmagnitudeを選択する必要がある。

### Verified: legacy command

`vorticity` executableも存在しstatus 0だったが、次のメッセージを表示するだけである。

```text
vorticity has been superseded by the postProcess utility:
postProcess -func vorticity
```

### Recommendation

2026年版では`postProcess -func vorticity`を主経路とし、`vorticity`は旧版互換の注記に留めるのがよい。本文を更新する際は、2Dでどのcomponentを表示するかを明記する。

## 6. ParaView

### Verified: installed versions and reader

- blueCFD-Core同梱版はParaView 5.11.2である。
- standaloneの`C:\Program Files\ParaView 5.11.2\bin\pvpython.exe`は5.11.2を返した。
- standaloneの`C:\Program Files\ParaView 6.1.1\bin\pvpython.exe`は6.1.1を返した。
- 空の`cavity.foam`を入口に、5.11.2および6.1.1のPython環境でOpenFOAM readerを生成でき、`MeshRegions=['internalMesh']`と`U`、`p`、`vorticity`のfieldを認識できた。
- `Glyph`、`StreamTracer`、`SaveScreenshot`のAPI object/callableを確認した。

### Feature check

| Feature | Result |
| --- | --- |
| OpenFOAM reader | Verified。5.11.2/6.1.1でfieldを認識 |
| Mesh Regions | Verified。readerの`MeshRegions`に`internalMesh` |
| Glyph | Verified。pipeline objectを生成可能 |
| Stream tracer / streamlines | Verified。`StreamTracer` objectを生成可能 |
| Save Screenshot | Verified。API callableを確認 |
| Surface With Edges | GUIでの目視操作は未完了。ParaViewの標準表示機能としての詳細操作はPhase 2Bで確認 |
| GUIの全手順 | Not verified。自動化したのはreader/APIの存在まで |

### Official information

公式ニュースではParaView 6.1.0が2026-03-31にreleaseされている。今回のローカル環境には6.1.1も存在する。公式download page上で、原教材に記載された特定の`Python3.12`、`msvc2017`等のinstaller filenameが現行の固定名として継続しているかは確認できなかった。

参照:

- [ParaView official download page](https://www.paraview.org/download/)
- [ParaView 6.1.0 release announcement](https://discourse.paraview.org/t/paraview-6-1-0-has-been-released/17500)

### Recommendation

blueCFD-Core経由の標準手順は同梱ParaView 5.11.2を対象として維持する。standalone補足は特定installer filenameを固定せず、公式download pageと`cavity.foam`を用いる一般的な接続方法へ整理する。

## 7. Alternative OpenFOAM environments

### Verified: official routes

| Route | Officially observed information | Classification |
| --- | --- | --- |
| blueCFD-Core on Windows | 2024-1 / OpenFOAM 12 / ParaView 5.11.2 | **main path** |
| Windows WSL2 | Foundation pageはUbuntu 22.04 LTSを`wsl --install -d Ubuntu-22.04`で導入する経路を案内。現在のFoundation pageはv14を案内 | **supported alternative**, but version compatibility must be separately checked |
| Native Linux | Foundation packages/pages provide Linux/Ubuntu routes。v14とv12の環境は別version | **supported alternative** |
| macOS | Foundation pageはCanonical Multipass経由のUbuntu 22.04 LTSを案内 | **supported alternative for advanced users** |
| Docker | FoundationのDocker scripts pageは5--11/dev系を掲載しているが、今回のv14/blueCFD 12のmain pathではない | **advanced/legacy alternative** |

Foundationの現行download pageはOpenFOAM v14を対象としており、OpenFOAM 12はarchiveに位置づけられている。Foundation版のv14は、blueCFD-Core 2024-1のOpenFOAM 12をそのまま置換するものではない。

参照:

- [OpenFOAM Foundation download](https://openfoam.org/download/)
- [OpenFOAM Foundation Windows / WSL](https://openfoam.org/download/windows/)
- [OpenFOAM Foundation macOS / Multipass](https://openfoam.org/download/macos/)
- [OpenFOAM Foundation archive](https://openfoam.org/download/archive/)
- [OpenFOAM Foundation Docker scripts](https://dl.openfoam.org/docker/)

### Recommendation

初学者向けの主経路はblueCFD-Coreに絞る。WSL、native Linux、macOSは補足として分類し、同じcaseがそのまま動くと約束しない。Dockerは今回の教材主経路から外し、必要な受講者向けの高度な選択肢とする。

## 8. Editor and Windows integration

### Verified

- blueCFD shellで`notepad2`が解決され、`C:\blueCFD-Core\2024\AddOns\notepad2\notepad2.exe`が存在した。
- `notepad2 &`を実行するためのshell command形は利用可能だが、今回の自動検証ではGUI windowの操作までは確認していない。
- `explorer.exe`は`/c/Windows/explorer.exe`として解決された。ExplorerのGUI表示自体は今回自動確認していない。

### Recommendation

Notepad2はblueCFD-Coreに同梱された例として残せるが、教材の技術的必須条件にはしない。設定ファイルを編集できるWindows側のテキストエディタを主概念とし、Notepad2を同梱環境での具体例、VS Code等を補足例として扱うのが合理的である。`explorer.exe .`はWindowsファイル操作の補足として残せる。

## 9. Distributed case archives

### Verified: discovery

次の二つのarchiveを`C:\Users\konno\Downloads`で発見した。blueCFDのrun directoryにも同じSHA-256のコピーが存在した。

| Archive | Path | Size | SHA-256 |
| --- | --- | ---: | --- |
| `channel_2024.tgz` | `C:\Users\konno\Downloads\channel_2024.tgz` | 1,707 bytes | `883240B1BED50313BF06E471105781EC20585EF36ADA5187E7161B41528D3BCB` |
| `vehicle_2025.tgz` | `C:\Users\konno\Downloads\vehicle_2025.tgz` | 7,690,441 bytes | `E79813EEE94C6AD7FD6B5AEEDB870F1F066B43125EE591239625F27C571007F2` |

同一内容のrun directory側の候補は次の場所にある。

```text
C:\blueCFD-Core\2024\ofuser-of12\run\channel_2024.tgz
C:\blueCFD-Core\2024\ofuser-of12\run\vehicle_2025.tgz
```

archiveは次のrepository外temporary directoryへ展開した。原archiveは変更していない。

```text
C:\Users\konno\AppData\Local\Temp\fluid-cfd-phase2a-channel-8fc28bd9718642f282a25c56c80d0fba
C:\Users\konno\AppData\Local\Temp\fluid-cfd-phase2a-vehicle-a6eb264075f24abc8ddc3ab0a9e057ea
```

### Recommendation

年度名を含むtgzを公開教材の固定配布方法にせず、case repositoryのversioned releaseへ移行する。archiveのSHA-256は、Phase 2Bでrelease assetを作る場合の移行照合用に保持する。

## 10. channel case

### Verified: archive contents

`channel_2024.tgz`の内容は次のとおりである。

```text
channel/
  0/p
  0/U
  constant/physicalProperties
  system/blockMeshDict
  system/controlDict
  system/fvSchemes
  system/fvSolution
```

archiveには`Allrun`、`Allclean`、`README.md`、`constant/momentumTransport`は含まれない。`controlDict`は旧形式の`icoFoam`を指定し、`fvSolution`には旧形式のPISO設定が残っていた。`foamRun` / `incompressibleFluid`の設定は、後続のcase repository側で更新された`channel`に属する。

### Verified: execution

- archiveをtemporary directoryへ展開し、`blockMesh`を実行すると成功した。メッシュは400 cells、領域は概ね`0..1 x 0..0.1 x 0..0.01`で、inlet/outlet/fixedWalls/frontAndBack patchを生成した。
- archiveで`foamRun`を実行するとstatus 1で、旧`icoFoam` caseの設定が現行の`foamRun` workflowと互換でないことを確認した。
- `foamRun -solver incompressibleFluid`もstatus 1で、archiveの`system/fvSolution`に現行workflowが必要とするPIMPLE keywordがないことを報告した。

### Verified: current case repository comparison

発見した外部case repositoryの`channel`は、archiveとは別の更新済み内容である。commit `ce32c20`では`constant/momentumTransport`が追加され、`fvSolution`が現在の`foamRun`用に更新されている。repository側のchannelをtemporary directoryへコピーした検証では、`blockMesh`と`foamRun`がともに成功し、`0.1`から`0.5`のtime directoryと`U`/`p`を生成した。

### Recommendation

`channel_2024.tgz`は現行blueCFD/OpenFOAM 12の配布caseとしてそのまま再利用しない。Phase 2Bでは、外部repositoryの更新済み`channel`を正とするか、archiveを現行caseに同期するかを決定する必要がある。今回の調査ではどちらのファイルも変更していない。

## 11. vehicle case

### Verified: archive contents

`vehicle_2025.tgz`は次の構造を持つ。

```text
vehicle/
  0/{k,nut,nuTilda,p,U}
  0/include/{fixedInlet,frontBackUpperPatches,initialConditions}
  Allclean
  Allrun
  constant/{momentumTransport,physicalProperties}
  model/concept_car_038-mod.stl
  system/{blockMeshDict,controlDict,cutPlane,decomposeParDict,
          forceCoeffs,functions,fvSchemes,fvSolution,
          snappyHexMeshDict,streamlines}
```

`controlDict`は`foamRun` / `incompressibleFluid`、`momentumTransport`はRASのSpalart--Allmarasを指定する。`Allrun`は`blockMesh`、`decomposePar`、parallel `snappyHexMesh`、`renumberMesh`、`potentialFoam`、solver、`reconstructPar`の順で実行する。`Allclean`はcaseをcleanするが、意図的に配置するSTLを削除しない。

### Verified: required STL flow and safe tests

- `Allrun` / `Allclean`は`sh -n`でsyntax errorなし。
- archive展開直後は`constant/geometry/STLObject.stl`がないため、`./Allrun`は期待どおりstatus 1で停止し、STLを所定位置へ用意する必要があると表示した。
- temporary copyで`model/concept_car_038-mod.stl`を`constant/geometry/STLObject.stl`へコピーした後、`blockMesh`は成功した。meshは1,280 cells、bboxは`(-5 -4 0) (15 4 8)`だった。
- `snappyHexMesh`を含む全`Allrun`は計算負荷を考慮して完走確認していない。したがってvehicleのfull E2EはNot verifiedである。

STLをコピーしたのはtemporary copyだけであり、archive、外部repository、教材repositoryは変更していない。展開したSTLのSHA-256は、外部repositoryの`vehicle/model/concept_car_038-mod.stl`と比較した範囲で一致した。

### Recommendation

学生配布では、現在のREADMEにある「`model/`から`constant/geometry/STLObject.stl`へコピーしてから`Allclean`、`Allrun`」の順序を明記する。可能なら将来のcase repositoryで、STLを同梱する形と、受講者がコピーする形のどちらを正式手順とするかをrelease単位で固定する。

## 12. Third-party STL / Sketchfab

### Verified: source page claim

原教材記載の概念車両に対応するSketchfab pageとして、次のページを確認した。

[FREE Concept Car 038 - public domain (CC0)](https://sketchfab.com/3d-models/free-concept-car-038-public-domain-cc0-0b4ca2a15ba7478db2a42ac9f0e687bf)

ページ上の表示は、titleに`public domain (CC0)`を含み、作者表示はUnity Fan / `@unityfan777`、download可能、attribution不要という説明である。

### Not verified

Web page上の表示を超えて、将来のrepositoryに加工済み`concept_car_038-mod.stl`を再配布する法的判断を確定したわけではない。元モデルと加工済みSTLの同一性、ページの将来変更、platformの利用条件、第三者権利の不存在は別途確認が必要である。

### Recommendation

STLを配布する場合は、source URL、title、author、取得日、表示されていたCC0説明、加工の事実を`vehicle/model/README.md`とlicense bundleに記録する。CC0表示を根拠に追加のattributionを必須とは断定しないが、教育配布上は出典を残す。確認が完了するまでは、STLの配布形態を教員判断事項として扱う。

## 13. Case repository discovery

### Verified

ローカルに、OpenFOAM演習caseを含むcloneを発見した。

```text
Local path:
C:\blueCFD-Core\2024\ofuser-of12\run\OpenFOAM-exercises

Remote:
https://github.com/Kogakuin-FEL/OpenFOAM-exercises.git

Branch:
main

HEAD:
ce32c204f71f1d1a56a6db4567eab8f3a18d525d
```

local cloneのstatusはcleanで、`origin/main`は同じ`ce32c20`を指している。root READMEは、fluid-mechanics education用のcase repositoryであり、course PDF、提出、deadline、course administrationは別管理と説明している。

treeの概要:

```text
OpenFOAM-exercises/
  README.md
  LICENSES/{GPL-3.0-or-later.txt,README.md}
  cavity/{README.md,0,constant,system}
  channel/{README.md,0,constant,system}
  vehicle/{README.md,0,constant,system,Allrun,Allclean,model}
```

含まれているcaseは`cavity`、`channel`、`vehicle`である。`vehicle`には`snappyHexMeshDict`、parallel用の`decomposeParDict`、`Allrun`、`Allclean`、STL model READMEがある。square-cylinder専用caseは、確認したtreeには存在しなかった。

### Not verified

- GitHub APIは、`gh auth status`で既存credentialがinvalidと表示され、API callもproxy接続失敗となった。
- unauthenticated HTTP requestは404となった。private repositoryの非公開応答とも整合するが、これだけでvisibilityを確定できない。
- したがって、このrepositoryのpublic/private、GitHub Teamのread access、学生アカウントでのRelease asset download可否は未確認である。
- remoteのbranch参照は認証済みgit credentialで確認できたが、tags/releases一覧は今回のネットワーク失敗により確定していない。

### Recommendation

候補名を推測して新repositoryを作成する必要はない。発見した`Kogakuin-FEL/OpenFOAM-exercises`を正式な配布repository候補として、owner/adminにvisibility、Team access、release運用を確認するのが次の手順である。

## 14. Proposed case repository structure

### Verified: current structure

現在のrepositoryは、caseごとのdirectory分離、case README、`vehicle`のrun/clean script、license directoryをすでに採用している。これはPhase 1の設計案に近い。

### Recommendation

現行treeを基礎に、将来の配布版は次の構造を基本とする。

```text
OpenFOAM-exercises/
  README.md
  LICENSES/
    GPL-3.0-or-later.txt
    README.md
  cavity/
    README.md
    0/
    constant/
    system/
  channel/
    README.md
    0/
    constant/
    system/
  square-cylinder/
    README.md
    0/
    constant/
    system/
  vehicle/
    README.md
    0/
    constant/
    system/
    Allrun
    Allclean
    model/
      concept_car_038-mod.stl
      README.md
```

判断:

| Design item | Recommendation |
| --- | --- |
| case directory | case単位で分ける。現在の`cavity`/`channel`/`vehicle`方式を維持 |
| repository全体ZIP | 教員向け・管理用には可。ただし学生の主配布には選択しない |
| student ZIP | releaseごとにcurated ZIPを生成し、READMEと必要caseだけ含める |
| case README | 各caseに置く。solver、version、実行順、既知の注意点を記載 |
| solution files | 学生配布caseと教員用solutionを分離。今回のtreeにないsolutionは勝手に追加しない |
| STL | ライセンス確認済みのものだけ配布。large fileなのでサイズとchecksumをrelease noteに記載 |
| scripts | `Allrun`/`Allclean`はcase内で保持し、対象OpenFOAM versionをREADMEで固定 |

## 15. GitHub Release distribution

### Verified: GitHub behavior relevant to design

GitHubはbranch/tag/commitからSource code ZIPを自動生成でき、Releaseには別途Release assetを添付できる。GitHub公式文書は、安定した配布物やsecurity上の理由ではRelease利用を推奨している。private repositoryのReleaseは、repository read accessを持つGitHub accountでのloginが前提になる。

### Comparison

| Item | A. GitHub-generated Source code ZIP | B. Release Asset ZIP |
| --- | --- | --- |
| Student clarity | repository全体のsnapshotで、root名や含有物を説明しにくい | `OpenFOAM-exercises-2026.1.zip`のように目的と版を明示できる |
| Unnecessary files | `.github`、開発用ファイル、将来のsolution等が混入し得る | case、README、license等を選択的に含められる |
| Directory name | GitHubのowner/repository/tagに依存 | 任意の安定したroot directoryを設計できる |
| Version identification | tag/branch snapshot名に依存 | filename、release title、tagを同時に明示できる |
| Teacher update | tagを作るだけでも生成可能 | ZIP生成・checksum・release noteが必要 |
| Reproducibility | tagが動かされなければ再現可能 | assetを差し替えずimmutable運用すれば明確 |
| Private repository | browser loginとread accessが必要 | 同じくbrowser loginとread accessが必要 |
| blueCFD terminal auth | browserで先にdownloadすれば不要 | browserで先にdownloadすれば不要 |

### Recommendation

学生の主経路は **B. 手動またはCI生成のRelease Asset ZIP** とする。

推奨手順:

1. 学生がbrowserでGitHubへloginする。
2. `OpenFOAM-exercises`の指定Releaseを開く。
3. `OpenFOAM-exercises-2026.1.zip`をdownloadする。
4. Windows上で展開する。blueCFD公式のpath制約を考慮し、短く空白のないpathを推奨する。
5. blueCFD-Core terminalで展開先caseへ`cd`し、READMEの手順を実行する。

Release assetには、選択したcase、root README、`LICENSES`、manifest/checksumを含める。source code ZIPは、教員・開発者がtag全体を取得する補助手段とする。

### Not verified

学生Team所属accountでprivate Release assetを実際にdownloadする試験は、今回のGitHub credential/API状態では実施できなかった。公開前に、教員accountと学生相当accountでdownload、ZIP展開、GitHub loginなしのblueCFD実行を確認する必要がある。

参照:

- [Downloading source code archives](https://docs.github.com/en/repositories/working-with-files/using-files/downloading-source-code-archives)
- [About releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)
- [Linking to releases](https://docs.github.com/en/repositories/releasing-projects-on-github/linking-to-releases)
- [Organization repository roles](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization)

## 16. Versioning strategy

### Recommendation

case教材はAPIやlibraryのsemantic compatibilityを提供するものではなく、年度と授業中の配布snapshotを管理するものなので、semantic versioningより年度ベースのversionが適する。

```text
2026.1
2026.2
2026.3

OpenFOAM-exercises-2026.1.zip
```

`v2026.1`とするか`2026.1`とするかはGitHub tagの見た目の選択であり、どちらかに統一すればよい。ここでは、tagは`2026.1`、Release titleとasset filenameも`2026.1`を推奨する。

Release noteには最低限、次を含める。

- 対象blueCFD-Core / OpenFOAM version
- 含まれるcase一覧と実行済みcase
- 変更されたcase/file
- 既知の制約と予想計算時間
- STLの出典・license note
- ZIPのSHA-256
- 以前のreleaseから更新する学生向けの注意

授業途中でcaseを更新する場合は、旧releaseを上書きせず`2026.2`を新規公開し、KU-LMSで使用版を明示する。学生には既存展開先を削除・置換する必要があるかをrelease noteで指示する。

## 17. KU-LMS / GitHub / FluidSeminarMaterials responsibility split

### Recommendation

Phase 1で想定した次の分担は妥当である。

| Location | Responsibility |
| --- | --- |
| `FluidSeminarMaterials` | 理論説明、コマンドの意味、図、課題文、case repositoryと指定Releaseへのlink |
| `OpenFOAM-exercises` | `0/`、`constant/`、`system/`、STL、`Allrun`、`Allclean`、case README、versioned Release |
| KU-LMS | 提出先、締切、履修者限定動画、年度固有のお知らせ、使用するRelease番号の告知 |

Verifiedなcase repository READMEも、course PDF・submission・deadlineをcase repositoryから分離する方針を示している。したがって、公開教材にKU-LMS URLを必須実行手順として埋め込まず、課題の提出運用はKU-LMSに残す構成がよい。

## 18. Changes required in the existing Word material

ここでは本文を変更せず、Phase 2Bで確認・変更が必要な箇所だけを列挙する。

### Verified findings

1. `legacy/incompressible/icoFoam/cavity/cavity`はblueCFD-Core 2024-1で存在し、`blockMesh` + `icoFoam`が完走した。
2. `postProcess -func vorticity`はOpenFOAM 12で動作し、`vorticity`を生成した。
3. `vorticity`はsuperseded wrapperである。
4. `channel_2024.tgz`は`blockMesh`までは動くが、現行`foamRun`でsolver実行できない。
5. case repositoryの更新済み`channel`は`foamRun`で動作した。
6. vehicleはSTLを`constant/geometry/STLObject.stl`に用意する前提で、`Allrun`を開始できる。全計算は未検証。
7. blueCFD同梱ParaViewは5.11.2で、OpenFOAM reader、field、Glyph、stream tracer、screenshot APIを確認できた。
8. 原教材のstandalone ParaViewの具体的installer filenameは時点依存である。

### Recommendation

- blueCFD-Core 2024-1 / OpenFOAM 12を主対象として更新日付きで明示する。
- `channel_2024.tgz`ではなく、検証済みのcase repository releaseを配布する経路へ置き換える。
- channelのsolver説明を`icoFoam`と`foamRun`のどちらに統一するかを決定する。現在のcavity tutorialとcase repositoryでは両者が異なる。
- vorticityは`postProcess -func vorticity`を主例にする。
- ParaView補足は版固定のinstaller filenameではなく、公式download pageと`.foam` fileを使う説明へ整理する。
- vehicleはSTL copy、license、計算時間、並列実行の前提をcase READMEと本文で役割分担する。
- Ghia図の最終置換は、検証済みcavity条件（Re、mesh、solver）を記録したうえで実施する。

## 19. Decisions ready for Phase 2B

今回の確認結果だけから、次の判断はPhase 2Bへ進められる。

1. **主対象環境:** blueCFD-Core 2024-1 / OpenFOAM 12 / bundled ParaView 5.11.2。
2. **cavity tutorial:** `$FOAM_TUTORIALS/legacy/incompressible/icoFoam/cavity/cavity`を対象pathとする。
3. **vorticity:** `postProcess -func vorticity`を採用し、legacy `vorticity`は注記扱いにする。
4. **配布単位:** case repositoryのcase directoryとversioned Releaseを単位にする。
5. **学生配布:** GitHub browser login後のcurated Release Asset ZIPを主経路にする。
6. **version:** 年度ベース`2026.1`方式を採用する。
7. **役割分担:** 公開MySTは説明・課題、case repositoryは実行データ、KU-LMSは提出・動画・年度運用とする。
8. **Ghia:** 原図をそのまま再利用せず、検証済みOpenFOAM結果から自作図を作る方針を維持できる。

## 20. Remaining open issues

### Not verified

1. `Kogakuin-FEL/OpenFOAM-exercises`のpublic/private visibility。
2. GitHub Education Teamがこのrepositoryにread accessを持つか。
3. 学生相当accountでprivate Release assetをbrowserからdownloadできるか。
4. case repositoryの正式なRelease/tag一覧と、student ZIPが既に存在するか。
5. vehicleの`snappyHexMesh`からsolver、`reconstructPar`までのfull E2E所要時間と成功結果。
6. standalone ParaView現行版の公式installer filenameと、原教材の`Python3.12` / `msvc2017`記述との正確な対応。
7. `Surface With Edges`、Mesh Regions、Glyph、streamline、Save ScreenshotのGUI操作を人間が一連に行ったときの画面状態。
8. SketchfabのCC0表示を将来のSTL再配布の根拠として固定するためのlicense保存方法。
9. KU-LMS上の動画URL、提出先、期限、過去archiveの正式な配布履歴。
10. square-cylinder caseがcase repositoryへ追加される時期と、現在のWord教材の角柱課題をどの形式で配布するか。

### Next step

Phase 2Bでは、上記のうち教材本文のversion policy、channelの現行case採用、vehicle Release内容、STL再配布、GitHub Teamによるdownloadを教員・repository管理者の判断で確定してからMyST変換へ進む。

### Evidence boundary

このPhase 2Aで実行したcaseはすべてrepository外のtemporary copyであり、元のDOCX/PDF、教材repository、外部case repositoryは変更していない。Ghia et al.の再計算、streamfunction作図、OpenFOAM教材本文の更新は行っていない。
