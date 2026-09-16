# CFD教材 DOCX media audit

## Scope and method

対象は `数値流体解析演習_blueCFD2024編.docx` と、対応する42ページの `数値流体解析演習_blueCFD2024編.pdf` である。DOCXの `word/media/`、`word/document.xml`、`word/_rels/document.xml.rels` を確認し、本文中の画像参照順と元media filenameを対応付けた。PDFは本文のキャプション、周辺説明、図の配置、およびPDF内部画像のページ情報を照合するために用いた。

DOCXには48個のmedia（PNG 46個、EMF 2個）がある。本文中の配置は49回で、`image1.png` がPDF p.1とp.10に再利用されている。`image32.png` と `image33.png` は同一バイト列（SHA-256: `4e17d11b04f8a53c0d0aac2ae173722c88244ff094302d12e50de0d968bec1d3`）である。EMFは確認用contact sheet作成時だけ一時的にPNGへレンダリングし、DOCX内の原mediaは変更していない。

「authorship not independently verified」は、DOCXの用途・PDFのキャプション・画像内容から種類を判断できても、画像の作成者や権利関係をDOCXだけでは独立確認できないことを示す。

2026-09-16に教材作成者へ確認した結果、`image40.png`、`image41.png`、`image44.png`--`image46.png`、`image47.png`は、CC0のConcept Car 038またはそのユーザー作成の可視化・説明図として公開可と判断した。`image47.png`は透明背景の原図を保持し、公開教材では白背景へ合成した派生PNGを使う。`image2.png`、`image19.emf`--`image20.emf`、`image37.png`--`image39.png`、`image48.png`は従来どおり転載・掲載しない。

## Full media inventory

| Media | PDF page | Description / surrounding context | Classification | Current MyST status | Current filename | Authorship / provenance | Recommended action |
| --- | ---: | --- | --- | --- | --- | --- | --- |
| `image1.png` | 1, 10 | cavityの圧力場と速度ベクトルを示す到達目標。p.10では再掲。 | B. OpenFOAM / ParaView result visualization | migrated | `cavity-goal.png` | DOCX/PDFでは解析結果として示されるが、著作者は独立確認していない。 | keep with provenance note |
| `image2.png` | 2 | blueCFD-Core ProjectのWebページ。ダウンロード案内の注釈を含む。 | F. third-party website screenshot | not migrated | — | 第三者Webページの画面。ユーザーによる注釈が加えられている。 | replace with text/link |
| `image3.png` | 3 | Windowsの「PCが保護されました」警告画面。 | E. Windows UI screenshot | not migrated | — | OSとセキュリティ設定に依存する画面。著作者は独立確認していない。 | replace with text/link |
| `image4.png` | 3 | Windows警告画面で「詳細情報」を開いた状態。 | E. Windows UI screenshot | not migrated | — | OSとセキュリティ設定に依存する画面。著作者は独立確認していない。 | replace with text/link |
| `image5.png` | 3 | blueCFD-Core installerのインストール先指定画面。 | D. blueCFD-Core UI screenshot | not migrated | — | blueCFD-Core installer UI。版によって表示が変わる。著作者は独立確認していない。 | replace with fresh screenshot |
| `image6.png` | 4 | blueCFD-Core terminalの初回起動画面。 | D. blueCFD-Core UI screenshot | migrated | `bluecfd-terminal-first-run.png` | ユーザー操作による画面と判断できるが、著作者は独立確認していない。 | keep with provenance note |
| `image7.png` | 4 | blueCFD-Core terminalの起動後画面。 | D. blueCFD-Core UI screenshot | not migrated | — | ユーザー操作による画面と判断できるが、著作者は独立確認していない。 | replace with fresh screenshot |
| `image8.png` | 7 | ParaViewのWelcomeパネルを含む起動画面。 | C. ParaView UI screenshot | not migrated | — | ParaView UI。版に依存する。著作者は独立確認していない。 | replace with fresh screenshot |
| `image9.png` | 7 | ParaViewでcavityを開いた直後の画面。 | C. ParaView UI screenshot | not migrated | — | ParaView UI。版に依存する。著作者は独立確認していない。 | replace with fresh screenshot |
| `image10.png` | 8 | ParaView UI上にcavityの圧力場を表示した画面。 | C. ParaView UI screenshot | migrated | `paraview-pressure.png` | 圧力結果を含むユーザー操作画面。著作者は独立確認していない。 | keep with provenance note |
| `image11.png` | 8 | ParaViewでGlyph表示を設定する操作画面。 | C. ParaView UI screenshot | not migrated | — | ParaView UI。版に依存する。著作者は独立確認していない。 | replace with fresh screenshot |
| `image12.png` | 9 | ParaView UI上にcavityの速度ベクトルを表示した画面。 | C. ParaView UI screenshot | migrated | `cavity-velocity-vectors.png` | 解析結果を含むユーザー操作画面。著作者は独立確認していない。 | keep with provenance note |
| `image13.png` | 12 | standalone ParaView起動後の画面。 | C. ParaView UI screenshot | not migrated | — | ParaView UI。版に依存する。著作者は独立確認していない。 | replace with fresh screenshot |
| `image14.png` | 13 | ParaViewのファイル選択画面。 | C. ParaView UI screenshot | not migrated | — | ParaViewおよびWindowsのUI。版に依存する。著作者は独立確認していない。 | replace with text/link |
| `image15.png` | 13 | `cavity.foam`を開いた後のParaView画面。 | C. ParaView UI screenshot | not migrated | — | ParaView UI。版に依存する。著作者は独立確認していない。 | replace with fresh screenshot |
| `image16.png` | 15 | Notepad2の起動画面。 | E. Windows UI screenshot | not migrated | — | Windows上のエディタUI。著作者は独立確認していない。 | replace with text/link |
| `image17.png` | 15 | Notepad2で `physicalProperties` を開いた画面。 | E. Windows UI screenshot | not migrated | — | Windows上のエディタUI。設定内容はコード例で示せる。著作者は独立確認していない。 | replace with text/link |
| `image18.png` | 17 | ParaViewのSurface with Edgesによるメッシュ確認画面。 | C. ParaView UI screenshot | not migrated | — | ParaView UIと計算メッシュ。版に依存し、著作者は独立確認していない。 | replace with fresh screenshot |
| `image19.emf` | 20 | Ghia et al. (1982)のRe=100, 400, 1000の図。 | G. Ghia et al. figure | not migrated | — | PDF本文でGhia et al.論文からの引用と明記。 | withhold |
| `image20.emf` | 21 | Ghia et al. (1982)のRe=3200, 5000の図。 | G. Ghia et al. figure | not migrated | — | PDF本文でGhia et al.論文からの引用と明記。 | withhold |
| `image21.png` | 22 | OpenFOAM（blueCFD-Core）で解析したRe=400 cavity結果。 | B. OpenFOAM / ParaView result visualization | not migrated | — | OpenFOAM / ParaViewの解析結果。ユーザー本人が作成した結果図であることを確認済み。現行環境での再計算図へ置き換える予定。 | replace with self-created figure |
| `image22.png` | 23 | `explorer.exe .` でOpenFOAM設定ファイルの場所を開いた画面。 | E. Windows UI screenshot | not migrated | — | Windows Explorer UI。版に依存する。著作者は独立確認していない。 | replace with text/link |
| `image23.png` | 24 | 天井駆動cavity流れとHagen–Poiseuille流れの概念比較。 | A. self-created explanatory figure | migrated | `cavity-channel-comparison.png` | 説明図と判断できるが、著作者は独立確認していない。 | keep with provenance note |
| `image24.png` | 25 | cavityのvertices指定を説明する図。 | A. self-created explanatory figure | not migrated | — | 説明図と判断できるが、著作者は独立確認していない。 | replace with self-created figure |
| `image25.png` | 25 | cavityのboundary/patch定義を説明する図。 | A. self-created explanatory figure | not migrated | — | 説明図と判断できるが、著作者は独立確認していない。 | replace with self-created figure |
| `image26.png` | 26 | Hagen–Poiseuille channelの境界条件。 | A. self-created explanatory figure | migrated | `channel-boundary-conditions.png` | 説明図と判断できるが、著作者は独立確認していない。 | keep with provenance note |
| `image27.png` | 27 | 角柱まわり流れのblock分割。 | A. self-created explanatory figure | migrated | `square-cylinder-blocks.png` | 説明図と判断できるが、著作者は独立確認していない。square-cylinder caseはv2026.1未収録。 | keep with provenance note |
| `image28.png` | 27 | 角柱まわり流れの境界条件。 | A. self-created explanatory figure | not migrated | — | 説明図と判断できるが、著作者は独立確認していない。 | replace with self-created figure |
| `image29.png` | 28 | blockの形状・番号を説明する図。 | A. self-created explanatory figure | not migrated | — | 説明図と判断できるが、著作者は独立確認していない。 | replace with self-created figure |
| `image30.png` | 28 | patchの形状・番号を説明する図。 | A. self-created explanatory figure | not migrated | — | 説明図と判断できるが、著作者は独立確認していない。 | replace with self-created figure |
| `image31.png` | 28 | 角柱まわり流れ用blockの手書きメモ。 | A. self-created explanatory figure | not migrated | — | PDFキャプションに作成者が示され、ユーザー本人の自作説明図であることを確認済み。現行教材へは図を移さず、説明文を使用する。 | replace with self-created figure |
| `image32.png` | 29 | 角柱後流の解析格子。`image33.png`と同一内容。 | K. duplicate media | not migrated | — | `image33.png`とバイト単位で同一。 | duplicate / do not use |
| `image33.png` | 29 | 角柱後流の解析格子。 | B. OpenFOAM / ParaView result visualization | migrated | `square-cylinder-mesh.png` | OpenFOAM結果図と判断できるが、著作者は独立確認していない。 | keep with provenance note |
| `image34.png` | 29 | 角柱後流の圧力場コンター。 | B. OpenFOAM / ParaView result visualization | migrated | `square-cylinder-pressure.png` | OpenFOAM結果図と判断できるが、著作者は独立確認していない。 | keep with provenance note |
| `image35.png` | 29 | 角柱後流の速度絶対値コンター。 | B. OpenFOAM / ParaView result visualization | migrated | `square-cylinder-speed.png` | OpenFOAM結果図と判断できるが、著作者は独立確認していない。 | keep with provenance note |
| `image36.png` | 30 | `postProcess -func vorticity`後のParaView画面。 | C. ParaView UI screenshot | migrated | `square-cylinder-vorticity.png` | 渦度結果を含むユーザー操作画面。著作者は独立確認していない。 | keep with provenance note |
| `image37.png` | 32 | 方眼紙で定義した2D blockの例。 | H. student-created figure | not migrated | — | 同一の卒業済み学生による課題例。公開許諾・クレジット未確認。 | withhold |
| `image38.png` | 33 | 学生作成blockに基づく圧力場の解析結果。 | H. student-created figure | not migrated | — | 同一の卒業済み学生による課題例。公開許諾・クレジット未確認。 | withhold |
| `image39.png` | 33 | 学生作成blockに基づく流速ベクトル場。 | H. student-created figure | not migrated | — | 同一の卒業済み学生による課題例。公開許諾・クレジット未確認。 | withhold |
| `image40.png` | 36 | Sketchfabで示された車両形状のレンダリング。 | I. Sketchfab-related image | migrated | `vehicle-model.png` | 元モデルはCC0のConcept Car 038。ユーザー本人がParaViewで表示・撮影した。モデルの出典と可視化の作成者を確認済み。 | keep with provenance note |
| `image41.png` | 36 | 車両表面メッシュの表示。 | I. Sketchfab-related image | migrated | `vehicle-surface-mesh.png` | 元モデルはCC0のConcept Car 038。ユーザー本人がParaViewで表示・撮影した。モデルの出典と可視化の作成者を確認済み。 | keep with provenance note |
| `image42.png` | 37 | ParaViewのMesh Regions設定前の画面。 | C. ParaView UI screenshot | not migrated | — | ParaView UI。版に依存する。著作者は独立確認していない。 | replace with fresh screenshot |
| `image43.png` | 37 | Mesh Regions設定後に車両・床・流出口を表示した画面。 | C. ParaView UI screenshot | not migrated | — | ParaView UIとユーザー操作結果。著作者は独立確認していない。 | replace with fresh screenshot |
| `image44.png` | 38 | 車両周辺の解析メッシュ。 | B. OpenFOAM / ParaView result visualization | migrated | `vehicle-mesh.png` | CC0のConcept Car 038を用いたOpenFOAM / ParaView結果。ユーザー本人が生成・撮影したことを確認済み。 | keep with provenance note |
| `image45.png` | 38 | 車両表面の圧力場と中央断面の速度ベクトル。 | B. OpenFOAM / ParaView result visualization | migrated | `vehicle-pressure-velocity.png` | CC0のConcept Car 038を用いたOpenFOAM / ParaView結果。ユーザー本人が生成・撮影したことを確認済み。 | keep with provenance note |
| `image46.png` | 40 | 車両形状の寸法・座標を示す図。 | A. self-created explanatory figure | migrated | `vehicle-dimensions.png` | ユーザー本人が作成した寸法・座標図であることを確認済み。 | keep with provenance note |
| `image47.png` | 41 | 任意形状用の計算領域寸法・座標を示す図。 | A. self-created explanatory figure | migrated | `custom-domain-dimensions.png` | ユーザー本人の自作線図。原図は透明背景で、公開教材では白背景の派生PNGを使用する。 | keep with provenance note |
| `image48.png` | 42 | 形状モデルだけを変更した3D外部流れの解析結果例。 | B. OpenFOAM / ParaView result visualization | not migrated | — | 解析・可視化はユーザー本人によるものだが、元3Dモデルの出典・ライセンスは未確認。 | withhold |

## Summary

Total: **48 media**（PNG 46、EMF 2）

### Current MyST status

- migrated: 17
- not migrated: 30
- duplicate / do not use: 1（`image32.png`。移行済みの `image33.png` と同一内容）

### Classification counts

| Category | Count |
| --- | ---: |
| A. self-created explanatory figure | 11 |
| B. OpenFOAM / ParaView result visualization | 8 |
| C. ParaView UI screenshot | 12 |
| D. blueCFD-Core UI screenshot | 3 |
| E. Windows UI screenshot | 5 |
| F. third-party website screenshot | 1 |
| G. Ghia et al. figure | 2 |
| H. student-created figure | 3 |
| I. Sketchfab-related image | 2 |
| J. unknown-source image | 0 |
| K. duplicate media | 1 |
| L. other | 0 |

### Recommended action counts

| Recommended action | Count |
| --- | ---: |
| keep with provenance note | 17 |
| replace with self-created figure | 7 |
| replace with fresh screenshot | 10 |
| replace with text/link | 7 |
| withhold | 6 |
| duplicate / do not use | 1 |
| needs human review | 0 |

## Human review shortlist

追加確認が必要なmediaはない。image2、Ghia原図、学生作成図、image48は方針を確定し、CC0車両関連画像とimage21/image31はユーザー確認済みのprovenanceに基づいて分類した。

## Contact sheet

全48 mediaを番号順に並べた確認用画像を作成した。EMF 2点はcontact sheet内でのみ一時PNGへレンダリングしている。

`migration/cfd-media-audit-contact-sheet.png`

この監査では、教材本文と既存MyST画像は変更していない。`migration/cfd-phase2b-migration.md`はprovenance整合化のため更新済みである。
