# CFD教材 Phase 2B: Word/PDF → MyST Markdown移植

調査・移植日: 2026-09-16

## Source files

- `数値流体解析演習_blueCFD2024編.docx`：段落、表、画像、OMML数式の主ソース。
- `数値流体解析演習_blueCFD2024編.pdf`：42ページのレイアウト、図配置、キャプション、章境界の照合用。
- `migration/cfd-materials-inventory.md`：Phase 1で確定した構造、provenance、未解決事項。

DOCXはPandoc 3.10で一時変換し、PDFの42ページ構成と照合した。DOCX/PDF本体は変更していない。

## Conversion method

Pandocによる初期Markdown化と`--extract-media`での画像抽出を行い、最終MarkdownはMySTの見出し、code block、directiveへ手動で整理した。DOCXの表から得たOpenFOAM dictionaryはMarkdown tableではなく、必要な部分をfenced code blockへ移した。OMMLのCourant数式とReynolds数の説明はLaTeX形式へ正規化した。

## Chapter mapping

| MyST file | Source pages | Phase 2B status |
| --- | --- | --- |
| `bluecfd-install.md` | pp.1--4 | 初期移植完了 |
| `cavity.md` | pp.1、5--13 | 初期移植完了 |
| `cavity-settings.md` | pp.14--23 | 初期移植完了 |
| `blockmesh-boundary.md` | pp.24--31 | 初期移植完了 |
| `external-flow-2d.md` | pp.32--34 | 課題、実行手順、学生作成図の非掲載方針を反映 |
| `external-flow-3d.md` | pp.35--39 | Release取得、STL準備、実行・可視化手順、車両図を反映 |
| `external-flow-3d-custom.md` | pp.40--42 | STL差し替え、寸法・座標、課題、出典不明図の非掲載方針を反映 |

授業回を示す「前回」「今回」「次回」は、章名や節名を参照する表現へ置き換えた。

## Figures migrated

Phase 2Bでは、教員作成の説明図、OpenFOAM/ParaViewの解析結果、操作手順の理解に必要な一部のスクリーンショットを、意味のある英語名へ変更して`textbook/cfd/images/`へ配置した。`image32.png`/`image33.png`の重複は一つに統合した。

移行した主な画像は次のとおりである。

- blueCFD terminal初回画面
- cavityの目標画面、圧力場、速度ベクトル
- cavityとchannelの概念比較
- channel境界条件
- square-cylinderのblock、mesh、圧力、速度、vorticityの説明図

図版方針の確認後、CC0のConcept Car 038に関係する車両形状・表面メッシュ・解析結果（`vehicle-model.png`、`vehicle-surface-mesh.png`、`vehicle-mesh.png`、`vehicle-pressure-velocity.png`）と、寸法・座標の説明図（`vehicle-dimensions.png`、`custom-domain-dimensions.png`）を追加した。権利上そのまま掲載しない図の位置には、Ghia、学生作成例、出典未確認モデル用のplaceholderを配置した。

### Human-confirmed provenance updates

次の画像については、2026-09-16に教材作成者へ確認した。`image40.png`、`image41.png`はCC0のConcept Car 038をユーザー本人がParaViewで表示・撮影した画像、`image44.png`、`image45.png`は同じモデルを用いたユーザー本人のOpenFOAM / ParaView結果、`image46.png`、`image47.png`はユーザー本人が作成した寸法・座標図である。これらは、元モデルの出典と、可視化・説明図の作成者を区別して記録した。

- `image40.png` → `vehicle-model.png`：CC0モデルの表示例。Sketchfabのsource URLを本文とcase repositoryに記録。
- `image41.png` → `vehicle-surface-mesh.png`：同じCC0モデルの表面メッシュ表示。
- `image44.png` → `vehicle-mesh.png`：同じCC0モデルのOpenFOAM / ParaView解析メッシュ。
- `image45.png` → `vehicle-pressure-velocity.png`：同じCC0モデルの圧力場・速度ベクトル結果。
- `image46.png` → `vehicle-dimensions.png`：車両寸法・座標の自作説明図。
- `image47.png` → `custom-domain-dimensions.png`：透明背景の自作線図を白背景へ合成した公開用派生PNG。原図はDOCX sourceに保持。

### Per-file provenance

以下の11点は、DOCXの`word/media/`内の元ファイルを確認してから、意味のある名前へコピーした。分類は、DOCX内の用途、PDFでの配置、図の内容を基準にしている。解析結果や説明図について、元データの作成履歴まではDOCXから確認できない場合がある。

| File | Original source | Classification | Publication status | Notes |
| --- | --- | --- | --- | --- |
| `textbook/cfd/images/bluecfd-install/bluecfd-terminal-first-run.png` | DOCX `word/media/image6.png` | blueCFD-Core UI screenshot | included | 初回terminal画面。対象versionに依存するため、将来の2026環境で再撮影候補。 |
| `textbook/cfd/images/cavity/cavity-goal.png` | DOCX `word/media/image1.png` | ParaView result screenshot; authorship not independently verified | included | cavityの圧力・速度ベクトルの到達目標。原資料の解析結果を再利用。 |
| `textbook/cfd/images/cavity/cavity-velocity-vectors.png` | DOCX `word/media/image12.png` | ParaView result screenshot; authorship not independently verified | included | Glyphによる速度ベクトル表示。UIはParaView版に依存する。 |
| `textbook/cfd/images/cavity/paraview-pressure.png` | DOCX `word/media/image10.png` | ParaView result screenshot; authorship not independently verified | included | cavityの圧力場表示。計算結果の再現条件は別途確認が必要。 |
| `textbook/cfd/images/blockmesh/cavity-channel-comparison.png` | DOCX `word/media/image23.png` | explanatory figure; authorship not independently verified | included | cavityとHagen--Poiseuille流れの概念比較図。 |
| `textbook/cfd/images/blockmesh/channel-boundary-conditions.png` | DOCX `word/media/image26.png` | explanatory figure; authorship not independently verified | included | channelの境界条件説明図。実caseの設定ファイルを正とする。 |
| `textbook/cfd/images/blockmesh/square-cylinder-blocks.png` | DOCX `word/media/image27.png` | explanatory figure; authorship not independently verified | included | 角柱まわりのblock分割説明。square-cylinder caseはv2026.1未収録。 |
| `textbook/cfd/images/blockmesh/square-cylinder-mesh.png` | DOCX `word/media/image33.png` | OpenFOAM result visualization | included | 角柱後流の解析格子。`image32.png`と同内容の重複mediaは採用していない。 |
| `textbook/cfd/images/blockmesh/square-cylinder-pressure.png` | DOCX `word/media/image34.png` | OpenFOAM result visualization | included | 角柱後流の圧力コンター。作成条件は原資料由来で、再計算図ではない。 |
| `textbook/cfd/images/blockmesh/square-cylinder-speed.png` | DOCX `word/media/image35.png` | OpenFOAM result visualization | included | 角柱後流の速度絶対値コンター。作成条件は原資料由来で、再計算図ではない。 |
| `textbook/cfd/images/blockmesh/square-cylinder-vorticity.png` | DOCX `word/media/image36.png` | ParaView result screenshot; authorship not independently verified | included | `postProcess -func vorticity`後の表示例。UIは対象versionに依存する。 |

## Figures withheld / replaced

- Ghia et al. (1982)の原図2点は転載せず、`cavity-settings.md`に自作再計算図へのplaceholderを置いた。
- `image2.png`のblueCFD公式Web screenshotは転載せず、公式Downloadsページへのリンクに置き換えた。
- `image37.png`--`image39.png`の同一卒業済み学生による課題例は、公開許諾が困難なため掲載していない。課題条件は文章で残した。
- CC0のConcept Car 038に関係する`image40.png`、`image41.png`、`image44.png`、`image45.png`は、sourceとユーザー作成の可視化を区別して記録した。
- `image48.png`は、可視化の作成者は確認できるが元3Dモデルの出典・ライセンスが未確認のため、placeholderへ置き換えた。
- 古いParaView UIを含む図は、2026環境で再撮影するまで主要手順の根拠にしない。

## Equations converted

- `Re = UL/nu`
- `C = U Delta t / Delta x`
- `nu = UL/Re_target`

数式は画像化せず、MySTのinline/display mathとして記述した。

## Legacy commands updated

- 旧資料の`icoFoam`実行は、2026年版の標準手順では`foamRun`へ更新した。
- 旧`channel_2024.tgz`、`vehicle_2025.tgz`の展開手順は、`OpenFOAM-exercises v2026.1` Release Assetへのリンクへ置き換えた。
- 渦度の後処理は`postProcess -func vorticity`を主経路とし、単独の`vorticity`はlegacy情報として区別した。
- 現行cavityの設定ファイル名として`physicalProperties`、`momentumTransport`、`controlDict`、`blockMeshDict`を示した。

## OpenFOAM 12 changes

現在のcase repositoryを参照し、cavityとchannelは`foamRun` / `incompressibleFluid`、層流設定は`constant/momentumTransport`を使う形で説明した。cavityの初期値は`nu=0.01`、`U=1`、`L=0.1`、`Re=10`として記載した。vehicleはRelease Assetの`Allrun`を使う手順へ整理した。

## Release links added

caseを使う章から次のReleaseページへリンクした。

<https://github.com/Kogakuin-FEL/OpenFOAM-exercises/releases/tag/v2026.1>

学生用ファイルは`OpenFOAM-exercises-2026.1.zip`であり、GitHub自動生成の`Source code (zip)`ではないことを明記した。

## Unresolved issues

- Ghia benchmarkの自作再計算図は未作成。
- `square-cylinder` caseは`v2026.1`に含まれていない。
- 学生作成画像は公開教材へ掲載せず、課題条件の文章だけを提供する。将来再利用する場合の許諾・クレジットは未確定。
- `image48.png`の元3Dモデルの出典・ライセンスは未確認のため、公開教材へ掲載しない。
- blueCFD-Core、ParaView、Windows UIスクリーンショットは将来の対象環境で再撮影する余地がある。
- 後半3章は初期移植を補強した段階であり、caseとの詳細な対応や図版の完全更新はPhase 2B後半で行う。
- WSL/Linux/macOS、standalone ParaView、Notepad2などの補足は、主経路と重複しない形への最終整理が必要。
