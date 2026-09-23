# UBXを使ったコマンド練習

UBXではLinuxコマンドを実行し、その結果を使って課題に回答する。問題文を読み、端末で作業しよう。

## UBXを起動する

Ubuntuの端末でUBX用仮想環境を有効にし、UBXを起動する。

```bash
source ~/venv-ubx/bin/activate
ubx
```

すでに同じ端末で仮想環境が有効になっている場合は、`source`の行を繰り返す必要はない。

## 1問に取り組む

UBXは課題の指示を表示し、`ubx$` promptのshellを開始する。指示に従ってLinuxコマンドを実行し、作業が終わったら次を入力してUBXへ戻る。

```bash
exit
```

質問に作業結果を回答し、表示された判定を確認する。課題ごとに指示や質問は異なる。

## 初回の環境checkpoint

UBXを設定し、最低1問を正解することを、導入時の環境checkpointとする。これによりWSL上で仮想環境とUBXを使って課題に取り組めることを確認する。

正解後は、進捗を確認できる。

```bash
ubx --status
```

教員側でも正解状況をWeb UIから確認できるため、専用の確認コードをKU-LMSへ提出する必要はない。

このcheckpointはWSL / Python / UBXで課題に取り組めることを確認するもので、WSLgやGUIの動作は確認しない。GUIは[別ページのself-check](wsl-files-and-gui.md)で任意に確認できる。

## 続けて練習する

続けて練習する場合はUBXを再実行して別の問題に取り組む。正解にならなかったときは判定を確認し、作業を見直して再挑戦する。

提出物、締切、連絡事項はKU-LMSの案内に従う。UBXの進捗確認コードを別途提出する必要はない。

## ライセンス

```{note}
教材本文は [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.ja)、コード例はMIT Licenseのもとで提供されています。
```
