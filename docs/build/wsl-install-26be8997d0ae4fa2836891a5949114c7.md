# WSLの導入とUbuntuの起動

Windows Subsystem for Linux（WSL）は、Windows上でLinuxディストリビューションやLinux用プログラムを使うための環境である。このページではWSLを導入し、Ubuntuを起動する。本授業ではWindows 11とWSL 2を使い、動作確認はUbuntu 24.04 LTSで行っている。

## WSLを導入する

すでにWSLを使っている場合は、PowerShellで状態を確認する。Ubuntuがすでにある場合は、重ねて導入する前に授業の指示を確認する。

```powershell
wsl --status
wsl -l -v
```

新規導入では、管理者として開いたPowerShellで次を実行する。

```powershell
wsl --install
```

再起動を求められた場合はWindowsを再起動し、スタートメニューからUbuntuを起動する。初回起動時にLinux用のユーザー名とパスワードを作成する。これはWindowsへのサインインに使うアカウントとは別であり、パスワード入力中は文字が画面に表示されない。

Ubuntu 24.04 LTSを明示するよう授業で指示された場合は、オンライン一覧に表示された名称を使って導入する。`wsl --install`と以下の指定導入は、どちらか一方を選ぶ。

```powershell
wsl --list --online
wsl --install -d Ubuntu-24.04
```

## WSLとUbuntuの状態を確認する

PowerShellで次を実行する。

```powershell
wsl --version
wsl --status
wsl -l -v
```

Ubuntuの一覧で`VERSION`が`2`であることを確認する。Ubuntuの名前は一覧に表示されたものを使う。たとえば名前が`Ubuntu-24.04`の場合、次のように起動できる。

```powershell
wsl -d Ubuntu-24.04
```

Ubuntuの端末で作業を終えるときは、次を実行する。

```bash
logout
```

## インストールに失敗した場合

通常は最初からBIOS/UEFIの設定を変更する必要はない。エラーが出た場合は内容を記録し、[MicrosoftのWSLトラブルシューティング](https://learn.microsoft.com/windows/wsl/troubleshooting)を確認する。仮想化やWindowsの機能に関する設定が必要な場合も、案内を確認してから対応する。

```{note}
WSL、Windows Terminal、Linuxの一般的な操作、GUI、Windowsとのファイル連携などの詳しい説明は、参考資料『[Windowsユーザーのための WSLで始めるLinux環境構築術](https://media.virtualtech.jp/wsl-book.pdf)』（VirtualTech Japan Inc., 2026年版）も参照できる。ディストリビューションの導入方法やUbuntuの版などは本授業の手順と異なる場合があるため、**本授業ではこの教材に記載した手順を優先する**。
```

## 次に読むページ

Ubuntuが起動したら、[Linux / UNIXコマンドラインの基本](linux-basics.md)へ進む。

## ライセンス

```{note}
教材本文は [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.ja)、コード例はMIT Licenseのもとで提供されています。
```
