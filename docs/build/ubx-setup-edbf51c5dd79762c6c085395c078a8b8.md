# UBXを使う準備

UBXは、Unix / Linuxのコマンドライン操作を練習するための教育用システムである。このページではUbuntu上でUBXを使う準備をする。

## UBXのWebアプリ

[UBXのWebアプリ](https://unix-basics-test.firebaseapp.com/)を開き、授業で案内された方法で利用登録を行う。クラス参加に必要なコードや一時的な認証情報は、公開ページには掲載しない。これらの値はKU-LMSで確認する。

## Python仮想環境を作る

Ubuntuの端末で、venv作成に必要なパッケージを導入する。

```bash
sudo apt update
sudo apt install python3-venv
```

次に、UBX用の仮想環境を作成して有効化する。

```bash
python3 -m venv ~/venv-ubx
source ~/venv-ubx/bin/activate
```

有効化すると、端末のプロンプトの先頭に`(venv-ubx)`のような表示が加わる。仮想環境の中では`python`と`python -m pip`を使う。

## UBXをインストールする

仮想環境を有効にし、次のコマンドでインストールする。

```bash
python -m pip install requests
python -m pip install --no-deps -i https://test.pypi.org/simple/ ubx
```

UBX本体は現在TestPyPIから配布されている。公開版やバージョンは更新されることがあるため、番号は固定せず、表示された結果を確認する。

```bash
ubx --version
ubx --help
```

本教材は2026年9月時点でUBX 1.0.1を使って動作確認している。異なる版が表示された場合は、授業の案内に従う。

## UBXを設定する

Web登録後、クラス参加に必要な情報をKU-LMSで確認してから初回設定を行う。

```bash
ubx --config
```

対話形式の質問に、案内された利用者情報、クラス情報、一時的な認証情報を入力する。これらの値を公開ページや共有画面へ書き込まない。

既存設定がある場合は、再設定の確認が表示されることがある。設定を変更する場合は、新しいクラス情報を手元に用意してから続行する。

設定が終わった後で、状態を確認する。

```bash
ubx --status
```

初回設定前に`--status`を実行すると設定入力へ進むことがあるため、必ず先に`--config`を実行する。状態表示にはアカウントやクラスの情報が含まれる場合があるので、不用意に共有しない。

## 次回の起動

Ubuntuを終了して起動し直した後は、UBXを実行する前に仮想環境を再度有効化する。

```bash
source ~/venv-ubx/bin/activate
```

次は[UBXを使ったコマンド練習](ubx-exercises.md)へ進む。

## ライセンス

```{note}
教材本文は [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.ja)、コード例はMIT Licenseのもとで提供されています。
```
