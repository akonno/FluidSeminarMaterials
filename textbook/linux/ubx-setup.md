# UBXを使う準備

UBXは、Unix / Linuxのコマンドライン操作を練習・確認するための教育用システムである。このページでは、Ubuntu上に専用のPython仮想環境を作り、UBXを使えるようにする。

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

有効化すると、端末のpromptの先頭に`(venv-ubx)`のような表示が加わる。仮想環境の中では`python`と`python -m pip`を使う。

## UBXをインストールする

仮想環境を有効にした状態で、依存パッケージとUBX本体を順にインストールする。

```bash
python -m pip install requests
python -m pip install --no-deps -i https://test.pypi.org/simple/ ubx
```

現在、UBX本体はTestPyPIから配布されている。`requests`を先にインストールし、UBX本体は指定された手順で追加する。UBXの公開版やバージョンは更新されることがあるため、番号を固定せず、実際のインストール結果を確認する。

```bash
ubx --version
ubx --help
```

Phase 2AではUBX 1.0.1を確認した。表示されるバージョンが異なる場合も、授業で指定された手順に従う。

## UBXを設定する

UBXのWebアプリで利用登録を済ませ、クラス参加に必要な情報をKU-LMSで確認してから、初回設定を行う。

```bash
ubx --config
```

対話形式の質問に、案内された利用者情報、クラス情報、一時的な認証情報を入力する。値を公開ページや共有画面に書き込まない。

すでにUBXの設定がある場合は、再設定の確認が表示されることがある。新しいクラス情報を手元に用意し、設定を変更する必要がある場合にだけ続行する。

設定が終わった後で、状態を確認する。

```bash
ubx --status
```

初回設定前に`--status`を実行すると、設定入力へ進むことがある。そのため、最初に`--config`を実行し、その後で`--status`を使う。状態表示にはアカウントやクラスを識別できる情報が含まれる場合があるため、画面共有や公開投稿をする前に内容を確認し、出力全体を不用意に共有しない。

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
