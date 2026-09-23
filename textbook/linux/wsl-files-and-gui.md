# Windowsとのファイル連携とWSLg

WSLではLinuxのコマンドを使いながら、Windowsのファイルやアプリケーションとも連携できる。ここでは、作業ファイルを置く場所と、UbuntuからWindows Explorerを開く方法を確認する。

## Linuxの作業ファイルはWSL内に置く

Linuxのコマンドラインで使う課題やプロジェクトのファイルは、原則としてWSLのLinux filesystem、たとえばホームディレクトリの中に置く。Linux用ツールを使う作業は、Linux側のファイルシステム上で行う。

WindowsのC:ドライブは、WSLから通常`/mnt/c/`以下で参照できる。Windows側にあるファイルを一時的に利用するときなどに使えるが、Linuxで継続して作業するプロジェクトの主な保存先にはしない。

```text
/mnt/c/
```

## Windows Explorerで現在の場所を開く

Ubuntuの端末で、次のコマンドを実行する。

```bash
explorer.exe .
```

末尾の`.`は「現在のディレクトリ」を表す。Windows Explorerが開き、端末で作業している場所のファイルを確認できる。

Windows Explorerのアドレス欄からWSLのファイルを見る場合は、次の形式を使える。`<DistroName>`の部分は、`wsl -l -v`に表示される実際のディストリビューション名に置き換える。

```text
\\wsl.localhost\<DistroName>
```

互換性のため、次の形式が使える環境もある。

```text
\\wsl$\<DistroName>
```

Linuxの作業ファイルはWSL内に置いたまま、Explorerから閲覧・コピーできる。Windows側のファイルをLinuxから参照する方法と、Linux側のプロジェクトをWSL内で扱う方法を使い分けよう。

## WSLgでGUIアプリを確認する

WSL 2では、WSLgを通して一部のLinux GUIアプリをWindowsデスクトップに表示できる。コマンドラインの演習にはGUI確認は必要ないが、環境を試す場合は次のself-checkを行える。

`x11-apps`がまだインストールされていない場合、Ubuntuの端末で次を実行する。

```bash
sudo apt update
sudo apt install x11-apps
```

続いて、GUIアプリを起動する。

```bash
xeyes
```

小さな`xeyes`ウィンドウが表示され、ウィンドウ内でポインターを動かすと目が反応すれば、GUI表示を確認できる。ウィンドウを閉じるか、起動した端末でCtrl+Cを押すと終了する。

これは自分の環境を確認するためのself-checkであり、提出課題やUBXのcheckpointではない。必要なアプリだけを確認すればよく、GUI表示はコマンドライン課題の実行条件ではない。

## 次に読むページ

コマンドラインの練習システムUBXを使う場合は、[UBXを使う準備](ubx-setup.md)へ進む。

## ライセンス

```{note}
教材本文は [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.ja)、コード例はMIT Licenseのもとで提供されています。
```
