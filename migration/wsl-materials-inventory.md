# WSL / UBX教材 Phase 1: inventory・互換性監査・構成案

初回調査日: 2026-09-23 / archive追加調査・更新日: 2026-09-24
対象: 2025年度「WSL導入」「UBXを用いたUNIX（Linux）の基本操作習得」資料
状態: 調査・設計のみ。教材本文の移植・画像公開は未実施。

## 調査範囲と確認方法

- 原本は `D:\work\Dropbox\授業\セミナー\WSL導入`。読み取り専用として扱い、DOCX/PDFの解析と今回追加されたarchiveの確認は、原本外の作業コピーで行った。Tempの実パスは記録しない。
- DOCXはPandocで作業コピーからMarkdown/mediaへ展開し、DOCX内の画像関係と段落順を確認した。PDFは `pdfinfo` / `pdftotext` / `pdfimages` と目視でページ構成・図配置を照合した。
- 今回、`wsl_env_check.tgz` を原本外のTempへコピーし、コピーのSHA-256一致を確認してから内容一覧・展開物を確認した。`wsl_env_check.sh` は実行していない。
- UBXはローカル `kEduApps` cloneの `github/main` と実装を確認した。確認時の `github/main` とlocal `main` は `33fe7d269df072935cef4fe11086900300dd5dcc`（`Fix UBX first-run CLI flow and add version option`）で一致していた。
- `kEduApps` cloneには今回の作業以前から別件の変更・未追跡ファイルがあった。それらは変更していない。
- 学籍・アカウント・クラス参加情報・ワンタイム値は、原資料に存在していてもこの報告書へ転記しない。以下では種類だけを記し、必要に応じ `[REDACTED]` と表す。

## 1. Source files inventory

原本ディレクトリで確認した通常ファイルは13件（Word 1、PDF 2、PNG 9、TGZ 1）。Wordの一時ロックファイルは教材原本に数えず、開かずに除外した。

| File | Size | Source role / notes |
| --- | ---: | --- |
| `WSL.docx` | 2,074,340 bytes | 二つの授業単元と補足を含む編集可能な主ソース。Word上の更新日は2025-10-20。 |
| `25流体工学セミナー・第2回講義資料2（WSL）.pdf` | 4,698,375 bytes | WSL導入・基本操作の配布版。A4、9ページ。 |
| `25流体工学セミナー・第4回講義資料3（WSL）.pdf` | 1,219,676 bytes | UBXを使う基本操作単元の配布版。A4、10ページ。 |
| `タスクマネージャー・パフォーマンス画面.png` | 59,419 bytes | 仮想化確認の例。特定PCのCPU・メモリ・状態を含む。 |
| `WSL-terminal.png` | 68,113 bytes | Ubuntu/WSL terminalの初回画面例。ホスト固有表示を含む。 |
| `xlogo.png` | 2,205 bytes | X11小アプリの表示例。 |
| `xeyes.png` | 2,914 bytes | X11小アプリの表示例。 |
| `xclock.png` | 3,257 bytes | X11小アプリの表示例。 |
| `oclock.png` | 1,837 bytes | X11小アプリの表示例。 |
| `wsl_env_check.png` | 84,918 bytes | 旧確認スクリプト出力例。個別確認値等を含むため公開不可。 |
| `wsl_env_check.tgz` | 2,194 bytes | 旧確認課題のarchive。原本の更新日時は2025-09-22 21:55:51 UTC。内容は `wsl_env_check.sh` 1件。SHA-256: `ABBDF0C8ADAAC9D6C1F14EA4215E263560977751E30EFC13637B5EA0ABD65B22`。 |
| `wsl_error.png` | 33,301 bytes | 旧課題ファイル実行時のエラー例。terminal情報を含む。 |
| `wsl_venv.png` | 9,787 bytes | WSL上でvenvを有効化した例。ユーザー/ホスト表示を含む。 |

### 原本保全の確認

今回の調査開始時点での原本通常ファイル13件について、終了時に一覧・サイズ・更新日時がすべて一致した。`wsl_env_check.tgz` は今回の開始時点ですでに存在した入力であり、以前の棚卸し後に追加された意図的なsourceとして扱った。archiveのSHA-256は原本とTempコピーで一致した。原本を編集・移動・改名せず、archiveの展開もTempコピー側だけで行った。

## 2. Source material structure

DOCXは二つの授業資料をまとめた編集原稿であり、PDFは授業回ごとに分かれた配布版。DOCX末尾にはPDFに含まれない補足・非配付資料がある。

| Source section | PDF mapping | Main contents |
| --- | --- | --- |
| WSLの導入 | 第2回PDF pp.1–2 | WSLの位置づけ、仮想化の確認、Windows設定、Ubuntu導入への案内。 |
| WSLの実行と動作確認 | 第2回PDF pp.2–3 | Ubuntu起動、terminal/prompt、ログアウト、最初のコマンド。 |
| コマンドの実行 | 第2回PDF pp.3–4 | `date`、`cal`、`echo`、`yes`、Ctrl-C、CLIの導入。 |
| GUI環境の確認・Windowsとのファイル交換 | 第2回PDF pp.4–5 | X11アプリの導入・起動、`explorer.exe .`。 |
| `wsl_env_check` 課題 | 第2回PDF pp.5–6 | KU-LMS archiveの取得、WSLへコピー、展開、実行、TEXT/GUIコードの提出。2026教材では原則廃止し、役割ごとに代替する（§7）。コード実値は本報告書では秘匿。 |
| Linux / Unixの背景 | 第2回PDF pp.7–9 | Unix/Linux、macOS、Cygwin/MSYS2、WSL、工学での利用についての説明。 |
| WSLの日本語化・UBX用Python環境 | 第4回PDF pp.1–2 | locale、`python3-venv`、venv作成・有効化。 |
| UBXを通したCLI練習 | 第4回PDF pp.2–8 | UBX紹介、登録、クラス参加、CLI導入・設定、演習、進捗確認、課題。 |
| 再起動後の操作・代替環境・補足 | 第4回PDF pp.9–10、およびDOCX補足 | venv再有効化、WSL以外のUnix系環境、shell/editor、コマンド補足。DOCXのみの画像・記述あり。 |

第2回PDFは9ページ、第4回PDFは10ページ。DOCXはこれら二つの授業単元を統合し、配布版にない補足を含む。公開本文の主ソースはDOCX、PDFはページ・図配置の照合用とするのがよい。年度表示、コマンド画面、アプリ画面は2025年時点のものとして扱い、2026版へそのまま転記しない。

## 3. Image / media inventory

DOCXには `word/media/image1.png`–`image19.png` の19件がある。独立した原本PNG 9件は、対応する `image1.png`–`image9.png` とバイト単位で一致した。つまり独立PNGは別の内容ではなく、DOCX内画像の再利用コピーである。ここに挙げる画像はいずれもまだMySTへ移行していない。

| DOCX media | PDF page | 内容・本文中の役割 | 推定出所 / 公開判断候補 |
| --- | --- | --- | --- |
| `image1.png` | 第2回 p.2 | Task Managerで仮想化状態を確認する画面。 | 教材作成用PCの画面と推定。CPU・メモリ等の固有情報があるため、一般化した説明または撮り直し。 |
| `image2.png` | 第2回 p.3 | Ubuntu/WSL初回terminal。 | 2025年の実機画面と推定。ユーザー/ホスト・ネットワーク等の情報を含むため現状のまま掲載しない。 |
| `image3.png` | 第2回 p.5 | `xlogo` のウィンドウ。 | X11アプリ画面。由来・撮影者は原資料だけでは独立確認できない。現行環境で撮り直すかコマンド表示に置換。 |
| `image4.png` | 第2回 p.5 | `xeyes` のウィンドウ。 | 同上。アプリ表示自体は簡単な動作確認例。 |
| `image5.png` | 第2回 p.5 | `xclock` のウィンドウ。 | 同上。 |
| `image6.png` | 第2回 p.5 | `oclock` のウィンドウ。 | 同上。対象Ubuntuでパッケージ提供・起動可能か要再確認。 |
| `image7.png` | 第2回 p.6 | `wsl_env_check.sh` の出力例。 | 参加者固有の確認値を含む画面。withhold。文章で確認手順の目的のみ説明する。 |
| `image8.png` | 第2回 p.6 | archive/実行に関するterminalエラー例。 | 実機画面と推定。ユーザー/環境固有表示を含む可能性。必要性があれば情報を除いた新しい例を撮る。 |
| `image9.png` | 第4回 p.2 | venv有効化前後のprompt。 | 実機画面と推定。ユーザー/ホスト名を含む。コードブロックで説明可能で、公開用には再撮影不要。 |
| `image10.png` | 第4回 p.3 | UBXサイトの入口画面。 | UBX Webアプリの画面。スクリーンショットより公式アプリへのリンクと操作説明を推奨。 |
| `image11.png` | 第4回 p.3 | 未ログイン時のUBXページ。 | UBX UIの画面。2025年のUIでありGoogleログイン要素を含む。必要なら最新版を撮り直す。 |
| `image12.png` | 第4回 p.4 | UBX画面のテーマ表示例。 | UBX UI。ライト/ダーク表示の説明は本文で十分。最新画面が必要な場合のみ撮り直す。 |
| `image13.png` | 第4回 p.4 | クラス参加・認証情報を入力する画面。 | 実アカウント/クラス参加に結びつく欄・情報を含む。画像全体を公開せず、汎用テキスト手順にする。 |
| `image14.png` | 第4回 p.5 | ログイン後のクラス/アカウント画面。 | アカウント・授業年度・クラス情報を含む。withhold。後で必要なら合成データのデモ画面を作る。 |
| `image15.png` | 第4回 p.7 | UBXのステージ/演習進捗画面。 | 利用者・授業固有の進捗表示を含む。現状はwithhold。合成データで再作成する場合は明示する。 |
| `image16.png` | 第4回 p.8 | 別ステージの進捗・ストーリー画面。 | 同上。 |
| `image17.png` | PDF未収録（DOCX補足） | `nano`でテキストを編集する画面。 | 非配付補足のterminal screenshot。ユーザー/環境情報があり、コマンド例だけで代替可能。 |
| `image18.png` | PDF未収録（DOCX補足） | ユーザー/ホスト表示のあるshell prompt画面。 | 非配付資料内の補助例。固有環境表示があり、公開版では本文コードブロックを優先。 |
| `image19.png` | PDF未収録（DOCX補足） | 別のユーザー/ホスト表示のあるshell prompt画面。 | 非配付資料内の補助例。固有環境表示があり、公開版では本文コードブロックを優先。 |

原本PNGの対応: `タスクマネージャー・パフォーマンス画面.png`→image1、`WSL-terminal.png`→image2、`xlogo.png`→image3、`xeyes.png`→image4、`xclock.png`→image5、`oclock.png`→image6、`wsl_env_check.png`→image7、`wsl_error.png`→image8、`wsl_venv.png`→image9。

**著作者について:** 原資料への収録は撮影者・著作者の独立証明ではない。システム画面やUBX UIに含まれる第三者ソフトウェア/サービスのロゴや画面要素も、公開可否を別途検討する。機微情報を含む画面は、著作者の確認とは別に公開しない。

## 4. Educational content inventory

| Category | Source content | Phase 2での扱い候補 |
| --- | --- | --- |
| A. WSL導入 | WSLの役割とWindows上でLinuxを使う目的、仮想化確認、WSL/Ubuntuの導入案内、Ubuntu起動、終了/ログアウト、導入時の注意。 | 残す。導入の主手順は2026年のMicrosoft公式手順へ差し替え、仮想化・再起動・既存WSLの分岐を整理。 |
| B. Linux/Unix基本操作 | shell/terminal/prompt、CLIとGUI、`date`、`cal`、`echo`、`yes`、Ctrl-C、`ls`、directory/file、Windowsとのファイル移動、`explorer.exe .`。 | 残す。短い安全な操作列と、どの環境（PowerShellかUbuntu shellか）に入力するかを明記。 |
| C. WSL GUI / WSLg | `x11-apps` / `x11-utils`、`xlogo` / `xeyes` / `xclock` / `oclock`。旧scriptはDISPLAY等の存在とX11接続を部分確認し、GUIコードを別窓へ表示。 | 採点・提出ではなく学生本人のself-checkとして扱う。例として `xeyes` 等を起動しウィンドウ表示を確認する。UBX checkpointとは別であり、パッケージとアプリ選定は選択したUbuntuで確認する。 |
| D. Python環境 | `python3-venv`、`python -m venv ~/venv`、`source ~/venv/bin/activate`。起動のたびにvenvを有効化する説明。 | UBX用のLinux環境として残す。Python教材のWindows/conda環境とは別物であることを強調し、`python3`/`python`を2026対象で確認。 |
| E. UBX | UBXの目的、ユーザー登録、クラス参加、CLI導入、旧短縮形 `ubx -c` / `ubx -s`、課題実行・進捗確認。 | 2026教材では `ubx --config` / `ubx --status` / `ubx --help` / `ubx --version` を標準表記とする。UBXの最初の課題を最低1問正解することを導入checkpoint候補とし、教員側はUBX/Firestore記録を確認する。年度依存の参加情報はKU-LMSへ分離。 |
| F. 授業運用 | KU-LMS配布archive、授業年度・クラス参加情報、認証値、提出フォーム/期限、提出用コード、課題の到達段階。 | `wsl_env_check`用archive・TEXT/GUIコード・LMS提出フォームは原則廃止。公開教材に実値を移さず、年度固有の値・提出先・締切はKU-LMSに限定する。 |

## 5. Year-specific / KU-LMS-specific content

原資料には以下の種類の情報がある。識別子やコードの実値は、本文・画像のいずれについても本レポートでは再掲しない。

| Information type | Source location | Public-safe handling recommendation |
| --- | --- | --- |
| 2025年度・授業回・クラス名称 | PDF表紙、UBX画面/本文 | 年度表示を除くか「授業で指定されたクラス」と一般化。公開ページに年度固定の案内を置かない。 |
| クラスコード、クラスパスコード、ワンタイム値 | DOCX本文とUBX画面 | `[REDACTED]`相当。教材・画像・repository履歴へ移さない。履修者へKU-LMSで個別案内。 |
| 学生/テスト用アカウント識別子、メール、学籍番号に見える値 | 画面・実行例 | 全てマスクまたは画像自体を不採用。架空例を使う場合も、現実の値と誤解されないサンプルだと明記。 |
| KU-LMS内の資料・`wsl_env_check` archive | 第2回PDFの課題 | 公開版では特定LMSの未公開ファイルを必須依存にしない。授業年度の配布物がある場合はKU-LMSから案内。 |
| 提出フォーム、提出期限、課題達成段階 | 両資料の課題 | 公開版は課題の学習目的・一般的な完了条件まで。提出先・締切・今年度の閾値はKU-LMS。 |
| Microsoft Learn等の公開リンク | WSL導入 | 公式の最新案内へリンク。LMS資料は公開URLに置換できる内容か確認する。 |
| UBX公開アプリ | UBX導入 | 公開アプリへのリンクは可能。授業参加に必要な値は別チャネルのまま。 |

外部参照として確認したhostには、`learn.microsoft.com`（PDF内参照）、`unix-basics-test.firebaseapp.com`、`test.pypi.org`、`pypi.org`、Cygwin/MSYS2関連、VirtualBox、複数のLinux/Unix解説・教科書サイトがある。旧リンクは公開前に到達性、現在の内容、公式性を個別確認し、古い二次解説は公式資料へ置換する。

## 6. UBX old-vs-current compatibility table

**Verified source:** `kEduApps/apps/UBX/tester` の `github/main` / commit `33fe7d269df072935cef4fe11086900300dd5dcc`。この確認はsource code/README上の仕様であり、TestPyPIからの実インストールや授業用サーバーの稼働試験ではない。

| 項目 | 2025教材 | 2026-09時点のmain source | 差異 | 2026公開教材への推奨 |
| --- | --- | --- | --- | --- |
| Install | `pip install requests` の後、TestPyPIをindex指定して `ubx`。 | READMEはTestPyPIを指定し、PyPIを `--extra-index-url` で加える方式を説明。 | READMEはTestPyPIにない依存をPyPIから解決する意図だが、pipはindex間の優先順位を保証しない。 | 教材ではindexを混在させず、`requests`をPyPIから、UBX本体のみTestPyPIから `--no-deps` で入れる。 |
| Dependency | `requests`を先に別途install。 | `pyproject.toml`に `requests>=2.31` が依存として宣言。 | metadata上の依存を、index混在を避けるため教材側で明示的に先行installする設計。 | venv内で次の分離手順を基本案とする。実registryからのfresh installはPhase 2で確認する。 |
| Index security | TestPyPIのみを指定した旧install例。 | READMEはTestPyPIとPyPIの複数indexを同時指定。 | pip公式文書は複数indexに優先順位がなく、dependency-confusion riskを伴うと警告。 | 学生向け教材では `--extra-index-url` を採用しない。 |
| Configure | `ubx -c`。 | `ubx --config` と `-c`の双方が有効。 | 短形式はdeprecatedでないが、長形式のREADME/CLI仕様がある。 | `ubx --config` を標準表記。クラス値等はKU-LMSから取得。 |
| Status | `ubx -s`。 | `ubx --status` と `-s`の双方が有効。 | 短形式はbackward compatibilityとして有効。 | `ubx --status` を標準表記。 |
| Help/version | 旧資料には独立のversion確認手順がない。 | `ubx --help`、`ubx --version`を実装。READMEのversion historyは2026-09の1.0.1。 | `--version`は新機能。 | 起動確認に `ubx --version` を加える候補。1.0.1は確認したsource versionであり、indexからの取得成功は未確認。 |
| Bare `ubx` / first run | 先に `ubx -c` を実行し、その後 `ubx`。 | `ubx`は通常セッションを開始。READMEの1.0.1 noteはfresh install時の二重config prompt修正を記載。 | 旧手順の概念は残るが、初回フローは修正されている。 | 長形式設定後に通常実行する。新規venvで初回導線を教員がスモークテスト。 |
| Python compatibility | WSL venvを利用する説明。 | `pyproject.toml`: Python `>=3.9`、entry point `ubx`、依存 `requests>=2.31`。 | package要件は明文化。 | 対象UbuntuのPython版と `python3-venv` を合わせて確認。 |

2026教材のinstall案は次の通りとする。TestPyPIとPyPIを同一pip resolutionへ混在させない。

```sh
python -m pip install requests
python -m pip install --no-deps -i https://test.pypi.org/simple/ ubx
```

upgrade時も同じ分離方針を用いる。

```sh
python -m pip install --upgrade requests
python -m pip install --no-deps -i https://test.pypi.org/simple/ --upgrade ubx
```

これは教材設計として確定した方針であり、現行READMEの `--extra-index-url` は学生向け本文で採用しない。実際のTestPyPI wheel取得とfresh venvでの導入動作は未実施なので、Phase 2でスモークテストする。kEduAppsは変更しない。

## 7. `wsl_env_check` retirement / replacement analysis

旧教材はKU-LMS archiveをWSLへコピーし、`tar`で展開、`chmod +x`後にstudent IDを引数にしてscriptを実行し、生成されたTEXT/GUI確認値をLMSへ提出する構成だった。今回、原本の `wsl_env_check.tgz` をTempへコピーしSHA-256一致を確認。archiveには `wsl_env_check.sh` 1件（4,601 bytes、archive内mtime 2025-09-22 21:47:33 UTC）が含まれていた。scriptは実行していない。

### `wsl_env_check.sh` の静的確認

- **引数・実行環境:** positional argumentとしてstudent IDを1つ必須とする。未指定ならusageを表示して終了。冒頭で `set -euo pipefail` を有効にし、`sudo`で実行しないよう明記する。コメントではWSL/native Linux/VMを対象としている。
- **環境収集:** `/etc/os-release`からdistribution/version、`uname`からkernel/architecture、`hostname`からhostnameを読む。`/proc/version`中のMicrosoft文字列でWSLを判定し、存在すれば `systemd-detect-virt` でvirtualization種別も調べる。
- **Windows/WSL情報:** WSL判定時に固定pathの `powershell.exe` からWindows OS versionを、`wsl.exe --version`からWSL versionを取得しようとする。distro名も環境変数から取得する。これらは失敗時に空欄を許容する書き方だが、WSL version行には `$((...` と読める不正な算術展開/command substitutionの疑いがある。
- **GUI判定:** `DISPLAY` / `WAYLAND_DISPLAY` の有無でmodeを決める。`DISPLAY`がある場合のみ `xdpyinfo`を最大6秒実行し、結果をok/failed/detectedに分ける。Wayland接続自体はprobeしていない。GUI code表示には `xmessage`を優先し、なければ `zenity`を使う。実際の描画や学生による視認を待たず、GUIアプリをbackground起動できた時点で表示成功扱いにするため、可視性の厳密な判定ではない。GUI codeはstudent ID・course salt・display環境変数から生成され、GUI windowにだけ表示し、terminal/reportには出さない。
- **TEXT code:** student IDとscript内のcourse saltからSHA-1 digestの先頭6桁を大文字化して生成し、terminalに表示するとともにreportへ保存する。saltはscript内の定数として埋め込まれ、授業ごとに教員が変更する想定で、学生に見えることを許容するコメントがある。実値はこのinventoryへ記載しない。これは短い照合値であり、強固な認証手段ではない。
- **Report:** `report_<student_id>.txt`を実行した作業directoryへ生成。student ID、timestamp、環境種別、distribution/kernel/architecture/hostname、graphics modeとDISPLAY/WAYLAND値、X11 status、WSL時のWindows/WSL version情報、TEXT codeを記録する。GUI codeは含めない。script自体からLMSやFirestoreへの送信は行わず、学生がreportのTEXT codeを手動でフォームへ転記する設計。
- **依存・error handling:** `grep`, `uname`, `hostname`, `date`, `systemd-detect-virt`（任意）, `timeout`, `xdpyinfo`（任意）, `tr`, `powershell.exe`, `wsl.exe`, `sha1sum`, `awk`, および `xmessage`または`zenity`（GUI code表示用）に依存する。archive展開の `tar` はscript内ではなく教材側の事前手順で使用する。optional commandの一部はfallbackするが、必須command不足やreport書込失敗では `set -e` により失敗し得る。引数のstudent IDをreport名へ直接使うため、入力形式の検証・filename sanitizationは見当たらない。
- **構文検証の制約:** scriptは実行していない。利用可能なbash parserの起動はWindows access deniedで失敗したため `bash -n` による確認も完了していない。静的に読める `wsl.exe --version` 取得行は `$((wsl.exe ...` の形で、bashの算術展開として不正に見える。修正・配布・実行をせず、Phase 2で原本コピー上の構文確認が必要。

### 2026教材での確定方針

`wsl_env_check.tgz` / `wsl_env_check.sh`は、原則としてそのまま公開教材へ移植せず廃止する。旧課題の役割を次のように分離する。

| 旧課題の役割 | 2026教材での代替 | 扱い |
| --- | --- | --- |
| WSL/Linux terminalを開始できたか | WSL起動後にPython venvを準備しUBX CLIを使う | 独立したTEXT code提出は廃止。checkpointの進行で実作業を確認するが、UBX記録だけではOSがWSLであることを暗号学的に証明しない。 |
| 教員側の履修者到達確認 | UBX/Firestore上の初回課題結果を教員が確認 | old reportのLMS提出を置換。Phase 2では教員アカウントから対象recordが見えることを運用確認する。 |
| GUIが表示できるか | 学生が `xeyes` 等を起動しwindowを確認 | 採点・提出なしのlocal self-check。UBX checkpointとは別。これだけでWSLg全体の診断を保証するものではない。 |
| TEXT Confirm Code | 代替なし | 廃止。コード生成値は公開せず、提出もしない。 |
| GUI Verify Code | GUI applicationの表示確認 | code提出を廃止し、学生自身のself-checkへ変更。 |
| KU-LMSフォームへのコード提出 | UBX/Firestore progress check | 廃止。年度固有の授業連絡・締切等は引き続きKU-LMS。 |
| `tar`による展開 | Linux/UBXの別演習 | 学習目標として必要なら別課題へ移管。wsl_env_checkを残す理由にはしない。 |
| shell script実行 | Linux/UBXの別演習 | 必要なら無害な別課題へ移管。旧scriptはそのまま実行させない。 |
| WSL単元終了checkpoint | WSL → venv → UBX install/config → UBX初回問題を最低1問正解 | 新しい導入checkpointに統合。教員はUBX/Firestore記録を確認する。 |

新checkpointが確認する意図は、WSL terminal、Python/venv、pip、UBX install/config、network access、UBX exercise executionまで進んだこと。これは授業上の到達チェックであり、機械的に実行環境を証明する仕組みではない。GUIは別のself-checkとする。

### Residual functionality / caveats

旧scriptはOS/distribution、kernel、architecture、hostname、仮想化判定、WSL/Windows version取得の試行、graphics environmentの部分診断、local report生成を一つにまとめていた。新checkpointはこの詳細な環境情報の採取を引き継がない。後続授業でこれらの診断値を教員が必ず必要とする場合は、個人確認コードとは切り離した安全な診断方法を別途設計する。また、UBX初回課題だけではGUI動作もWSLで実行したことも保証しない。

## 8. Potentially outdated WSL instructions

以下は現行公式資料との照合によるPhase 1の分類。原資料の技術内容をここで修正するものではない。

| Topic | Classification | Phase 2前の確認 |
| --- | --- | --- |
| `wsl --install` | probably current | Microsoft公式はWindows 10 2004/build 19041以降またはWindows 11での標準導入コマンドとして案内。既にWSLがある場合、distribution指定や更新など分岐を最新案内に合わせる。 |
| Ubuntu version | needs verification | 資料画面は2025年時点のUbuntu。2026授業で実際に揃えるdistribution/releaseを決め、コマンドとパッケージをそこで試す。 |
| BIOS/UEFI virtualization | needs verification | 機種/firmware依存。特定Task Manager画像やメーカー操作を一般手順として掲載せず、現行Windows確認方法とOEM案内へ誘導。 |
| WSL1/WSL2の比較・WSLの歴史 | needs verification | 基礎背景は残せるが、性能・軽さ等の断定は用途依存。導入対象がWSL2なら必要な範囲に圧縮。 |
| WSLg / X11 | probably obsolete as worded | 現行Microsoft資料はWSL2でX11/Wayland GUIアプリを統合実行するWSLgを案内。古い「X11だけ」の説明を改め、WSLgと従来X server方式を混同しない。 |
| `x11-apps`, `x11-utils`, `oclock` | needs verification | Microsoft資料は `x11-apps`と`xclock`/`xeyes`等を例示し、Ubuntu package searchはUbuntu 24.04向け`x11-apps`の存在を示す。`x11-utils`、`oclock`、対象releaseでの同梱は実機確認。 |
| `explorer.exe .` | probably current | MicrosoftのWSL filesystem guideに現行例として掲載。どの方向のファイル操作か、Linux filesystemとWindows mounted filesystemの使い分けも併記。 |
| locale設定 | needs verification | `language-pack-ja`と`update-locale`を2026年に指定するUbuntu releaseで試す。必須化せず、UBX日本語表示との関係を確認。 |
| Python / venv | needs verification | Python公式は `python -m venv` を説明。Ubuntuでは `python3`名、`python3-venv` package、既存Python版を対象imageで確認。 |
| `date`、`echo`、`yes`、`ls` | probably current | 基本コマンドとして残せる。中断方法・大量出力への注意を追加し、初学者向けに副作用を明示。 |
| `cal` / `oclock`の可用性 | needs verification | command/packageがUbuntuのminimal installにあると決めつけず、対象releaseで確認。 |
| Cygwin/MSYS2/VirtualBoxの比較 | needs verification | 歴史紹介に限定するか削る。現行の第一選択を説明する場所ではない。 |
| 「WSLはVMより軽い」等の一般化 | probably obsolete / revise | 現在のWSL実装や用途に関わらず断定しない。必要ならWSL2の構成・運用上の違いを公式資料に基づき簡潔に説明。 |

確認したMicrosoft資料: [Install WSL](https://learn.microsoft.com/en-us/windows/wsl/install)、[Linux GUI apps with WSL](https://learn.microsoft.com/en-us/windows/wsl/tutorials/gui-apps)、[Working across Windows and Linux file systems](https://learn.microsoft.com/en-us/windows/wsl/filesystems)。Python/パッケージ参照: [Python `venv`](https://docs.python.org/3.12/library/venv.html)、[Ubuntu `x11-apps` package search](https://packages.ubuntu.com/noble/x11-apps)、[pip install index options and security warning](https://pip.pypa.io/en/stable/cli/pip_install/)。閲覧日はいずれも2026-09-23。

## 9. Public/private separation recommendations

### Public textbook candidate

- WSL/Linuxの概念、一般化した導入案内、shellの基本操作、公開公式資料へのリンク。
- UBXの公開アプリへのリンク、install/config/status/help/versionの一般手順。公開前に安全なpackage取得方法を確定。
- GUI動作確認は任意のself-checkとして記述し、必要以上の提出を求めない。
- 画像は固有情報を含まないものに限定。ログイン画面・実クラス・アカウント情報・実進捗は公開しない。

### KU-LMS / restricted course channel

- 今年度のクラス参加コード、パスコード、ワンタイム値、具体的ログイン情報。
- 課題配布archive、提出フォーム、締切、今年度の達成stage、授業固有のお知らせ、限定動画。
- 授業用の一時的な設定値・サンプルアカウントなど、公開すべきでない情報。

実クラスコードや学生固有値は、public repositoryのMarkdown、画像、release、git履歴へ含めない。公開画像が必要なら、合成アカウント・架空授業で作ったことを明記した専用demoを作る。

## 10. Proposed MyST page structure

推奨トップレベル表示名: **Linux / UNIX操作**。資料の語彙と合い、WSLが提供するLinux環境と、そこで学ぶUnix系CLI操作の両方を示せる。「Linux環境とUNIX操作」は説明的だが長く、「Linuxコマンドライン」はWSL導入・GUI・UBX登録まで含む範囲を狭く見せる。

教育の流れは4章よりも5章が自然。導入、コマンド基礎、Windows/GUI統合、UBX環境準備、UBX演習を分け、GUIはCLI導入から独立した任意項目にできる。

```text
textbook/linux/
  wsl-install.md       # WSL/Ubuntu導入、初回起動、logout、初回確認
  linux-basics.md      # shell/prompt、date/cal/echo/yes、ls、file/directory
  wsl-files-and-gui.md # Windowsとのファイル交換、explorer.exe、任意のWSLg確認
  ubx-setup.md         # venv、UBX取得、登録/config（年度値はKU-LMS）
  ubx-exercises.md     # UBXの起動、課題、status、checkpoint
```

この案は作成済みの教材構造ではなく、Phase 2設計案に限る。TOCや教材本文は変更していない。

## 11. Existing textbook overlap / cross-link opportunities

- `textbook/python/miniforge.md` はWindows側のconda環境を段階的に作る教材。UBXのLinux venvとは別環境であり、同じpackage環境やactivate手順だと誤認させない。必要なら「Python環境を分ける考え方」の参照先としてリンクするだけにする。
- `textbook/python/jupyterlab.md` / `pygame1.md` はMiniforge Prompt・Windows側の実行例が中心。Linux shellの導入を重複掲載せず、shell種別（PowerShell/Bash）と入力先を見分ける案内からLinux教材へリンクする。
- Python教材の `cd` / `dir` 説明はWindows側の作業ディレクトリの文脈。Linux教材の `cd` / `ls` と同じコマンド体系と見せない。共通概念を再説明せず比較リンクにする。
- `textbook/cfd/bluecfd-install.md` はWindows上のblueCFD-Coreを主経路とし、WSL/Linuxは別の代替環境と述べる。将来WSL環境でCFDを行う読者へLinux教材を案内できるが、OpenFOAMの導入をこのWSL/UBX単元の範囲へ混在させない。
- CFDの`explorer.exe .`はblueCFD shellの文脈で使われる。Linux教材のWSL interop例との類似点はリンク可能だが、同じ実行環境だとは説明しない。

## 12. Open questions / human decisions required

以下は教材本文作成前、またはPhase 2の検証で決める事項。旧 `wsl_env_check` の継続可否、code提出、install index混在、UBX短縮optionの標準化は決定済みであり、open questionには含めない。

1. 2026授業のWindows/Ubuntu targetをどこまで固定するか。Microsoft標準 `wsl --install` に任せるか、同一Ubuntu LTSを明示するか。
2. GUI self-checkに `xlogo` / `xeyes` / `xclock` / `oclock` のどれを残すか。選択したUbuntu上でpackage availabilityも確認する。
3. WSL、venv、UBX、ParaView等の画面画像をどこまで2026環境で撮り直すか。アカウント・授業データ入り画像は公開しない。
4. `tar`展開・shell script実行を別のLinux/UBX演習へ移管するか。移管するなら具体的な学習目標と安全な課題を定義する。
5. 5ページ案（WSL導入、Linux基本、Windows/GUI連携、UBX設定、UBX演習）をPhase 2の本文構成として採用するか。
6. DOCX補足のどの部分を公開本文へ残すか。`image17`–`image19`はPDF配布版に見当たらず、Word原稿のみの補足。
7. 旧外部リンクを残す範囲。書籍/解説サイトを公式Microsoft/Ubuntu/Python資料へ集約するか。

**Phase 2での運用確認:** 分離install commandをfresh venvで試し、UBX設定・初回問題・Firestore上の教員確認が成立することを検証する。これは方針を再審議する項目ではなく、実装前の動作確認。

## Verification notes / links

- UBX source: [kEduApps `apps/UBX/tester`](https://github.com/akonno/kEduApps/tree/main/apps/UBX/tester)。確認したsource commit: `33fe7d269df072935cef4fe11086900300dd5dcc`。
- CLI実装は `-c`/`--config`、`-s`/`--status`双方を受理し、`--version`を提供する。READMEは`--help`等の長形式を示す。
- 現行UBX source version `1.0.1` とCLI optionはsource上で確認した。TestPyPIからの分離install、初回課題記録、およびFirestoreの教員側可視性はPhase 2で動作確認する。
- `wsl_env_check.tgz`は原本外で一覧・展開し、scriptを静的確認した。script自体は実行しておらず、構文検証はWindows bash起動時のpermission errorにより完了していない。
