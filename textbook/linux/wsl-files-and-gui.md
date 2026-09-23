# Windowsとのファイル連携とWSLg

Linuxのコマンドラインで使う課題やプロジェクトのファイルは、原則としてWSL内のLinux filesystem（たとえばホームディレクトリ`/home/...`）に置く。Windows側のfilesystem上では、多数のファイルを扱うLinux toolsの処理が遅くなる場合がある。

WSLやWindows Terminalの一般的な説明は、[WSLの導入とUbuntuの起動](wsl-install.md)で紹介した参考資料も参照できる。

## Windows Explorerで現在の場所を開く

Ubuntuの端末で次を実行すると、現在のディレクトリをWindows Explorerで開ける。

```bash
explorer.exe .
```

`.`は現在のディレクトリを表す。Linux側で作業するファイルはWSL内に置いたまま、Explorerで閲覧できる。

## WindowsのファイルをWSLから見る

WindowsのC:ドライブは、WSLから通常`/mnt/c/`以下で参照できる。Windows側のファイルを一時的に使うときなどに利用する。

```text
/mnt/c/
```

```{note}
Explorerのアドレス欄からWSL内を直接開く場合は、`\\wsl.localhost\<DistroName>`を使える。`<DistroName>`は`wsl -l -v`で確認する。環境によっては互換表記`\\wsl$\<DistroName>`も利用できる。
```

## WSLgでGUIアプリを確認する

WSLgを使うと、一部のLinux GUIアプリをWindowsデスクトップ上に表示できる。GUI確認は任意のself-checkで、提出課題でもUBX課題の実行条件でもない。

`x11-apps`がまだインストールされていない場合は、Ubuntuの端末で一度だけ次を実行する。

```bash
sudo apt update
sudo apt install x11-apps
```

次に`xeyes`を起動する。

```bash
xeyes
```

ウィンドウが表示され、ウィンドウ内でポインターを動かすと目が反応すれば、GUI表示を確認できる。ウィンドウを閉じるか、起動した端末でCtrl+Cを押すと終了する。

```{figure} ./images/wsl/xeyes-wslg-2026.png
:alt: WSLg上で表示されたxeyesのウィンドウ
:align: center

教材作成者がWindows 11のWSLg上で撮影した`xeyes`の表示例（2026年9月）。
```

## 次に読むページ

UBXを使う場合は、[UBXを使う準備](ubx-setup.md)へ進む。

## ライセンス

```{note}
教材本文は [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.ja)、コード例はMIT Licenseのもとで提供されています。
```
