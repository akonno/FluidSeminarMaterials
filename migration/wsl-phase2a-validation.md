# WSL / UBX 教材 Phase 2A: 2026環境 validation

検証日: 2026-09-24
目的: 2026年度向けに案内するWSL / Ubuntu / Python venv / UBX操作の実機確認。本文教材はまだ作成していない。

## 1. Test environment

### Verified — 実機

| 項目 | 確認結果 |
|---|---|
| Windows | Windows 11 Pro 25H2、build 26200.9457、64-bit |
| CPU / logical processors | AMD Ryzen 7 3700X、16 logical processors |
| RAM | 31.93 GiB |
| WSL | WSL 2.7.14.0、default version 2 |
| WSL kernel | 6.18.33.2-2 |
| WSLg | 1.0.73.2 |
| distribution | Ubuntu-24.04、WSL 2 |
| Ubuntu | 24.04.5 LTS |
| Linux kernel / architecture | 6.18.33.2-microsoft-standard-WSL2 / x86_64 |
| Python / pip | Python 3.12.3、pip 24.0 |

Ubuntu-24.04は既存distroを明示して利用した。WSLやUbuntuの新規install、既定distroの変更は行っていない。Windows edition/buildはWindows側のOS情報、WSL/distro/kernel/Python情報は各実機コマンドで確認した。

### Not verified

`wsl --install` をこの既存環境で実行するfresh-install試験は行っていない。既存Windows環境へのWSL再installやdistro追加を避けるためである。下記の導入評価はMicrosoft公式手順と現在の実機状態を照合したもの。

## 2. WSL install guidance review

### Verified — Microsoft公式資料（2026-09-24確認）

- Windows 10 version 2004 / build 19041以降またはWindows 11では、管理者PowerShellから `wsl --install` を実行し、必要な場合は再起動する単一コマンド導入が公式の基本経路。既定でUbuntuを導入し、初回起動時にLinuxユーザー名・パスワードを作成する。
- `wsl --install` が既存環境でhelpを表示する場合は、`wsl --list --online` でdistribution名を確認し、`wsl --install -d <DistroName>` を使う。
- 新しくinstallしたdistributionはWSL 2が既定。各distroの実際のversionは `wsl --list --verbose` / `wsl -l -v` で確認できる。
- WSL 2 GUI supportが必要で、WSLが古い場合は `wsl --update` の後、`wsl --shutdown` で再起動する案内がある。GUI appsはWSL 2が対象。
- 仮想化・Virtual Machine Platformの手動確認は、古いOSや導入失敗時のtroubleshooting/manual-install経路に寄せ、全受講者へ最初からBIOS画面操作を要求しない構成が簡潔。

Sources: [Install WSL](https://learn.microsoft.com/en-us/windows/wsl/install), [Basic commands for WSL](https://learn.microsoft.com/en-us/windows/wsl/basic-commands), [Run Linux GUI apps with WSL](https://learn.microsoft.com/en-us/windows/wsl/tutorials/gui-apps)（確認日: 2026-09-24）。

### 2025教材との差分と判断

| Topic | 判定 | Phase 2Bへの推奨 |
|---|---|---|
| `wsl --install` | current | 主経路として説明し、既存WSL時の分岐を併記する。 |
| Restart / Ubuntu初回起動 | current | 再起動後の初回展開とLinuxユーザー作成を明示。Windowsアカウントとは別のLinux資格情報であることを説明。 |
| WSL 2 | needs wording update | 現行新規installのdefaultだが、受講者PCで実際の状態を `wsl -l -v` で確認させる。 |
| Ubuntu version | fix target for reproducibility | 実機はUbuntu 24.04.5 LTS。教材はLTS releaseを明示する案が再現性に優れる。授業年度のtargetを教員が最終確定する。 |
| Virtualization check | troubleshooting path | install前の全員必須スクリーンショットではなく、install失敗時の確認・公式troubleshootingへ移す。 |
| WSLg / X11 | revise | WSL 2でX11/WaylandアプリをWindows desktopへ統合する現行経路を説明し、旧X server前提の説明と混ぜない。 |

## 3. Basic command validation

### Verified — Ubuntu-24.04

- `date`, `cal`, `echo Hello`, `yes` が利用可能。
- `yes` は出力を確認でき、GNU `timeout --signal=INT`からSIGINTを送る試験はtimeout終了コード124で終わった。実端末での手動Ctrl-C入力は行っていないため、教材の対話確認では学生自身がCtrl-Cで止める。
- `cal 10 2022`、`cal 2022`、`cal 10`、`cal 9 1752` はすべて終了コード0。`cal` はこの実機に存在する。
- `python` と `python3` は両方存在し、同じPython 3.12.3を指す。

### Recommendation

WSL上でvenvを最初に作る説明は `python3 -m venv ...` を標準にする。Ubuntuのsystem Pythonを起点にする意図が明確で、`python` aliasの有無に依存しない。venvを有効化した後は、提示コマンドを短くするため `python -m pip` / `python` を使う。

## 4. Windows ↔ WSL integration validation

### Verified

- `/mnt/c/Windows` が存在し、WSLからWindowsのC: filesystemを参照できる。
- Windows側から `\\wsl.localhost\Ubuntu-24.04\tmp\...` および互換形式の `\\wsl$\Ubuntu-24.04\tmp\...` にある専用test directoryを読み取れた。
- `explorer.exe` はWSLのPATHから見つかった。`explorer.exe .` を実行し、Windows Explorerで専用test directory `/tmp/wsl-ubx-phase2a-20260924` が開くことをユーザーが初回・再実行の両方で目視確認した。呼び出し元にはexit code 1が返ったが、実際の表示は成功しており、この終了コードはExplorer表示失敗の証拠ではない。

Microsoftの現行ガイドは `explorer.exe .` とWindows Explorerの `\\wsl$` 表示を案内している。またLinux CLIで作業するprojectはWSLのLinux filesystem内へ置く方が速いとしている。

Source: [Working across Windows and Linux file systems](https://learn.microsoft.com/en-us/windows/wsl/filesystems)（確認日: 2026-09-24）。

### Recommendation

Linux CLIで扱う課題ファイルはLinux filesystemに置き、Windows Explorerから見る場合は `\\wsl.localhost\<DistroName>`（互換表記 `\\wsl$\<DistroName>`）を使う説明を主にする。`/mnt/c/...` はWindows側のファイルをLinuxから扱うときの補助経路とする。`explorer.exe .` はMicrosoft推奨の簡易操作で、初回・再実行とも一時検証directoryの表示をユーザーが目視確認した。呼び出し元のexit codeは1だったが、終了コードだけで表示失敗とは判断しない。

## 5. Python / venv validation

### Verified

- 既存の `~/venv` は存在するため触れていない。
- 専用一時領域にfresh venvを `python3 -m venv <path>` で作成できた。
- venvの中では `python` がそのvenvのPython 3.12.3を実行し、pip 24.0もvenv内にある。
- systemの `python` / `python3` とactivated venvの `python` が利用できた。
- 検証用venvとpip cacheは一時領域に分離。既存venvを削除・更新していない。

### Recommendation

教材手順は `sudo apt install python3-venv`（未導入の場合）→ `python3 -m venv ~/venv-ubx` → `source ~/venv-ubx/bin/activate` → venv内で `python -m pip ...` とする。既存の `~/venv` と名前が衝突しない説明にする。

## 6. UBX install validation

### Verified — fresh venv

次の分離方式をfresh venvで実行し、両方成功した。

```sh
python -m pip install requests
python -m pip install --no-deps -i https://test.pypi.org/simple/ ubx
```

- `requests`とその依存はPyPIからinstallされた（requests 2.34.2）。
- `ubx`本体はTestPyPIからwheel `ubx-1.0.1-py3-none-any.whl` として取得・installされた。
- `--no-deps`によりTestPyPI側で依存解決を行わず、metadataは `Requires: requests`。dependency errorなし。
- `pip show ubx`、`pip show requests`の両方でfresh venv内のinstall先を確認。
- TestPyPI上で今回取得したversionは1.0.1で、Phase 1で想定したversionと一致。

upgrade commandも同じ環境で受け付けられた。

```sh
python -m pip install --upgrade requests
python -m pip install --no-deps -i https://test.pypi.org/simple/ --upgrade ubx
```

その時点で両packageは最新のまま（requests 2.34.2、ubx 1.0.1）で、upgradeはno-op。古いversionからの実更新は行っていない。

### Recommendation

教材ではPyPI/TestPyPIを同一resolutionへ混在させず、上記の二段階installを採用する。`--extra-index-url`方式は学生向け手順に使わない。

## 7. UBX CLI / configuration validation

### Verified

- `ubx --version` は `ubx 1.0.1`、exit 0。
- `ubx --help` はexit 0。実装は `-s/--status` と `-c/--config` を同じargumentとして登録している。短縮形は現在も有効だが、教材の標準は長形式とする。
- cleanなtest HOMEでの `ubx --status` はstatusを表示せず `ID:` を求め、stdinを閉じるとexit 1。configがない初回状態では、`--status`もuser info読込・初期設定へ進む挙動。
- `ubx --config`もcredential入力前の `ID:` promptまで進むことを確認した。stdinを閉じて終了させ、test HOMEにconfig fileが作られていないことを確認。
- その後、人間が通常のWSL端末で `ubx --config` を完了し、保存済み設定を使う `ubx --status` が進捗を返すことを確認した。credentialの値はこのreportに記録していない。

### Recommendation

初回は `ubx --config` を案内し、その後に `ubx --version` / `ubx --status` を使う。初回configなしの `--status` は純粋なread-only status checkではないため、教材で「未設定でも安全な確認」と表現しない。`-c` / `-s` はbackward-compatibleだが、公開教材では `--config` / `--status` を使用する。

**UBX source reviewed read-only:** local `kEduApps/apps/UBX/tester`, branch `main`, commit `33fe7d269df072935cef4fe11086900300dd5dcc`; `README.md`, `pyproject.toml`, `src/ubx/__main__.py`, version metadataを照合した。Python要件は `>=3.9`、依存は `requests>=2.31`、TestPyPIのREADMEは `--extra-index-url`方式を説明している。今回の教材側install方針とは異なるが、kEduAppsは変更していない。cloneには別件の既存変更・未追跡ファイルがあり、今回それらには触れていない。

## 8. Configuration → first exercise → Web progress E2E

| Stage | Result | Evidence / reason |
|---|---|---|
| WSL / Ubuntu startup | PASS | 既存Ubuntu-24.04をWSL 2で起動。 |
| Python / venv | PASS | fresh専用venvを作成・有効化。 |
| pip / UBX install | PASS | 指定のPyPI/TestPyPI分離install成功。 |
| CLI version / help | PASS | `ubx --version`、`ubx --help`成功。 |
| UBX configuration | PASS | 人間がWSL端末で対話設定を完了。credential値は記録していない。 |
| First question | PASS | UBXで課題を1問正解。 |
| UBX status progress update | PASS | 正解前の残り3問から、正解後に残り2問へ変化。 |
| Teacher-side Web progress | PASS | 教員側Web UIで進捗表示を確認。Firestoreを直接操作・確認していない。 |

### E2E result and propagation timing

学生側の `config` → 課題1問正解 → status進捗更新 → 教員側Web UI表示まで確認済み。正解後、Web UIを開いた時点ですでに進捗が表示されていた。観測上は5分以内だが、同期・反映に要した正確な時間は測定していない。即時反映や特定時間を保証するものではない。

## 9. GUI / WSLg validation

### Verified — process/protocol and user visual confirmation

- WSL 2上で `DISPLAY` と `WAYLAND_DISPLAY` が設定されていた。
- `xdpyinfo` はexit 0でX displayへ接続した。
- Ubuntu上で `x11-apps` 7.7+11build3、`x11-utils` 7.7+6build2が既に導入済み。今回apt install/updateは行っていない。
- `xeyes`、`xclock`、`xlogo`、`oclock`は全てcommandが存在し、各プロセスは2秒のtimeoutまで稼働した。起動時fatal errorはなかった。`xclock`のみfont charset warningをstderrへ出した。
- ユーザーが初回試験で `xeyes` と `xclock` のwindow表示を目視確認した。再試験では `xeyes -geometry 320x240+40+40` も表示された。今回の `xeyes` は枠付きで、目以外の領域は透明に見えた。マウスカーソルがwindow内にある間は目が追随し、window外では追随せず停止した。これは観察された挙動として記録し、window表示の失敗とは扱わない。
- `xlogo` と `oclock` はprocess起動まで確認したが、画面上の表示は目視確認していない。process起動とdisplay protocol接続だけでは、これらのwindow表示確認の代替にならない。

### Recommendation

2026教材のself-checkは `xeyes` 1つに絞る案がよい。Microsoft公式も `x11-apps` と `xeyes` / `xclock`を例示し、この実機ではxclockにfont warningが出た。`xeyes`のwindow表示は目視確認済み。枠外が透明に見えること、pointer追随がwindow内に限られることも観察事項として記録する。`x11-utils`は診断コマンド `xdpyinfo` 等向けで、学生のGUI self-checkに必須ではない。導入は必要な場合だけ `sudo apt install x11-apps`。GUI確認はUBX checkpointとは別の任意self-checkとする。

Source: [Run Linux GUI apps with WSL](https://learn.microsoft.com/en-us/windows/wsl/tutorials/gui-apps)（確認日: 2026-09-24）。

## 10. Locale validation

### Verified

- このdistroの `LANG` は `ja_JP.UTF-8`、`LC_ALL`は未設定。`locale`は日本語UTF-8 localeを表示。
- `ubx --help` は `ja_JP.UTF-8` と `C.UTF-8` の両方で成功し、出力は同一だった。
- `update-locale`等の永続設定変更は行っていない。

### Recommendation / limitation

UBX install、version、helpの動作に日本語localeは必須ではない。教材ではlocale変更を必須手順にせず任意・troubleshooting扱いにする。ただし、UBXの対話課題本文が `C.UTF-8` でどこまで日本語化されるかはfirst-exercise試験を行っていないので **Not verified**。

## 11. `tar` / shell script learning

### Recommendation

旧 `wsl_env_check`を残す理由として `tar` / script実行を温存する必要はない。まずUBX初回問題までを環境checkpointにし、基礎コマンドを先に教える。`tar`またはshell scriptが後続課題で具体的に必要になる場合だけ、目的と副作用の小さい独立演習として移管する。旧archiveの展開・script実行をUBX到達確認の必須条件にはしない。

## 12. Screenshot refresh plan

| 旧画像 / image group | Recommendation | 理由 |
|---|---|---|
| Task Manager virtualization | replace with text | PC固有CPU/メモリ情報。導入失敗時のみ公式troubleshootingへ。 |
| WSL terminal | retake if it materially helps | 2026のUbuntu/Windows UIで撮り直し、username/hostnameを含めない。本文はcommand中心で代替可能。 |
| `xlogo`, `xeyes`, `xclock`, `oclock` | remove old images; optional single fresh `xeyes` | 古い画像の代わりにself-check commandを掲載。画像が教育上必要なら本人が2026環境で撮り直す。 |
| `wsl_env_check` output / confirm-code screen | remove | 旧仕組み廃止、個別情報とコードを含む。 |
| WSL error example | replace with text or retake sanitized case | 特定環境のerror screenshotは再現条件が不明。実在する頻出errorが特定できた場合のみ撮り直す。 |
| venv prompt screenshot | replace with text/code | path・user/host表示を避け、activate前後のcommandで説明可能。 |
| UBX website/UI/account/progress | replace with link/text; retake only with synthetic data | 実アカウント、class、進捗を含む旧画面は公開しない。必要なら架空データで撮り直す。 |
| UBX CLI | code block preferred | `--config`、`--status`、`--version`を本文コードで示し、画面画像を必須にしない。 |

画像撮影・差し替えは今回行っていない。

## 13. Proposed five-page structure

Phase 1案の5ページ分割を維持する。

```text
textbook/linux/
  wsl-install.md       # WSL/Ubuntu導入、初回起動、logout、確認
  linux-basics.md      # shell/prompt、date/cal/echo/yes、file/directory
  wsl-files-and-gui.md # Windows連携、explorer.exe、任意のWSLg self-check
  ubx-setup.md         # venv、install、登録/config（年度値はKU-LMS）
  ubx-exercises.md     # 課題session、status、初回checkpoint、続きの練習
```

WSL導入・基本操作・Windows連携・package設定・演習の境界が明確で、GUI確認も採点なしの独立self-checkとして扱える。本文作成・TOC変更は未実施。

## 14. Issues found

1. `explorer.exe .` は初回・再実行とも一時検証フォルダー `wsl-ubx-phase2a-20260924` を開いたことをユーザーが目視確認。両回とも呼び出し元のexit codeは1だったが、実際の表示成功を確認済み。
2. `xeyes` と `xclock` のwindow表示はユーザーが目視確認済み。`xlogo` / `oclock`はprocess起動のみ確認し、視認は未確認。`xclock`にfont charset warning。
3. `ubx --status`はclean configなしでID入力へ進む。未設定時の安全なread-only確認手順ではない。
4. UBX configuration、課題1問正解、status進捗更新、教員側Web UI表示は人間による手作業で確認済み。正解後の残り問題数は3から2へ変化した。
5. 既存環境での観察であり、fresh Windows/Ubuntu installの再現試験ではない。`xlogo` / `oclock`の目視とUBX対話課題の`C.UTF-8`表示は未確認だが、いずれもPhase 2B blockerではない。

## 15. Recommendations for Phase 2B

- Windows 11向け導入はMicrosoft公式 `wsl --install`を中心にし、既存WSL時の分岐と再起動・Ubuntu初回ユーザー作成を含める。対象案はUbuntu 24.04 LTS系とする。
- Ubuntu 24.04系のsystem Pythonでは `python3 -m venv`、venv内では `python -m pip` を使う。
- UBXはPyPIから `requests`、TestPyPIから `ubx`を `--no-deps` で分けてinstall。教材では `ubx --config`、`ubx --status`、`ubx --help`、`ubx --version`の長形式を標準にする。
- UBXの対話設定から最低1問正解し、statusで進捗を確かめ、教員側Web UIで表示を確認する環境checkpointを採用候補とする。年度固有のクラス参加情報はKU-LMSで案内する。
- GUI self-checkは `xeyes` を第一候補とする。WSLgでのwindow表示はこの実機で目視確認済み。`xclock`も表示確認済みだがfont warningがあったため、教材例は `xeyes` に絞る。
- 作業ファイルはWSL Linux filesystemを主とし、Windows Explorer連携は `\\wsl.localhost` / `\\wsl$`を案内。`explorer.exe .`も表示成功を実機確認した操作例として使える。
- Locale変更は必須にしない。UBX対話課題の`C.UTF-8`表示は未確認だが、これはPhase 2B blockerではない。

### Phase 2B readiness

**ready for Phase 2B.** UBXの対話設定、1問正解、statusの残り問題数3→2、教員側Web UIでの進捗表示まで確認済み。GUIの`xeyes` / `xclock`表示と`explorer.exe .`も目視確認済み。

### Non-blocking limitations

- fresh Windows環境で `wsl --install` を再実施していない。
- Web progressは確認時点ですでに表示済みだったため、正確な反映時間は未測定（観測上5分以内）。
- `xlogo` / `oclock`の画面表示、およびUBX対話課題の`C.UTF-8`表示は未確認。

## 16. Git / artifact status

Phase 1 inventory commitは `origin/main` 上へrebaseしてpush済み。GitHub Actionsによる `Auto-build Jupyter Book` commitも確認し、local `main` をfast-forwardで同期した。Phase 2作業branch `migrate-wsl-ubx-myst` は同期済みmain HEADから作成した。教材本文、TOC、images、kEduApps sourceは変更していない。既存の未追跡source資料・notebook・contact sheet類はvalidation reportの管理対象外。
