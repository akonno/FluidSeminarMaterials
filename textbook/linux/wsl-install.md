# WSLの導入とUbuntuの起動

このページでは、Windows上でLinux環境を使うためのWSLを導入し、Ubuntuを起動するまでを説明する。主な対象はWindows 11とWSL 2で、LinuxディストリビューションはUbuntu 24.04 LTS系を想定する。

## WSLとは

Windows Subsystem for Linux（WSL）は、Windows上でLinuxディストリビューションとLinux用のプログラムを使うための環境である。Windowsを使い続けながら、Linuxで広く使われるコマンドや開発・解析用ソフトウェアを実行できる。

WSL 2はLinuxカーネルを使う方式であり、この教材ではWSL 2を前提とする。WSL 1とWSL 2は内部の仕組みが異なるため、導入後に使用中のバージョンを確認する。

## 新しくWSLを導入する

すでにWSLを使っている場合は、まずPowerShellで状態を確認する。既存のUbuntuが見つかったときは、新しい環境を重ねて導入する前に授業の指示を確認する。

```powershell
wsl --status
wsl -l -v
```

新規導入の標準経路では、管理者としてPowerShellを開き、次のコマンドを実行する。既定のUbuntuを導入する。

```powershell
wsl --install
```

インストール後に再起動を求められた場合は、Windowsを再起動する。再起動後、スタートメニューからUbuntuを起動する。初回起動ではLinux用のユーザー名とパスワードを作成する。

Linuxのユーザー名とパスワードは、Windowsへのサインインに使うアカウントとは別のものである。パスワード入力中は画面に文字が表示されないことがある。入力後にEnterを押す。

授業でUbuntu 24.04 LTSを明示するよう指示された場合は、既定のUbuntuを入れる代わりに、利用可能なディストリビューション名を確認して指定する。以下の2つの導入方法はどちらか一方を選び、両方を続けて実行しない。

```powershell
wsl --list --online
wsl --install -d Ubuntu-24.04
```

一覧に表示される名前は、実行時の案内に従う。導入済みの環境がある場合は、重複してインストールする前に状態を確認する。

## 導入状態を確認する

次のコマンドはWindowsのPowerShellで実行する。

```powershell
wsl --version
wsl --status
wsl -l -v
```

`wsl -l -v`の一覧で、Ubuntuの`VERSION`が`2`であることを確認する。表示されるディストリビューション名は、後でWSLを起動するときにも使う。

## Ubuntuを起動する

Ubuntuはスタートメニューから起動できる。PowerShellから起動する場合は、実際のディストリビューション名を指定する。

```powershell
wsl -d Ubuntu-24.04
```

Ubuntuのウィンドウ内に、ユーザー名やディレクトリを含むプロンプトが表示される。プロンプトは入力待ちを示す部分であり、コマンドはその後ろに入力してEnterを押す。

```text
user@computer:~$
```

上の表示は形式の例である。ユーザー名やコンピューター名はそれぞれの環境で異なる。

Linuxの作業を終えるときは、Ubuntuのプロンプトで次を実行する。

```bash
logout
```

## インストールに失敗したとき

通常は、最初からBIOS/UEFIの設定を変更する必要はない。WSLのインストールでエラーが出た場合は、エラーメッセージを記録し、[MicrosoftのWSLトラブルシューティング](https://learn.microsoft.com/windows/wsl/troubleshooting)を確認する。仮想化やWindowsの機能に関する確認が必要な場合も、PCの説明書や授業で案内された方法に従い、不明な設定を自己判断で変更しない。

## 次に読むページ

Ubuntuが起動したら、[Linux / UNIXコマンドラインの基本](linux-basics.md)へ進む。

## ライセンス

```{note}
教材本文は [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.ja)、コード例はMIT Licenseのもとで提供されています。
```
