# blueCFD-Coreの導入

この章では、Windows上でOpenFOAMを実行するためのblueCFD-Core環境を準備する。原資料pp.1--4の内容を、2026年版の対象環境に合わせて整理している。

## 対象環境

2026年版で主に確認した環境は次のとおりである。

| 項目 | 対象 |
| --- | --- |
| OS | Windows 10/11 64-bit |
| blueCFD-Core | 2024-1 |
| OpenFOAM | 12相当 |
| ParaView | bundled版 5.11.2 |

blueCFD-Coreは、OpenFOAMをWindowsから利用するための環境をまとめて提供する。実際の計算はblueCFD-Core terminalから実行する。

## インストール

インストーラーは[blueCFD-Core Project](https://bluecfd.github.io/)の公式情報を確認して入手する。インストール時は、空白を含まないパスを選ぶ。授業で例として使うパスは次のとおりである。

```text
C:\blueCFD-Core\2024
```

実際のインストール先は、使用するインストーラーの案内に従う。固定パスを暗記することよりも、後でblueCFD-Core terminalが正しいOpenFOAM環境を読み込んでいることを確認することが重要である。

```{figure} ./images/bluecfd-install/bluecfd-terminal-first-run.png
:alt: blueCFD-Core terminalの初回起動画面
:align: center

blueCFD-Core terminalの初回起動画面の例。画面表示はバージョンやインストール状況によって異なる。
```

## blueCFD-Core terminalの起動

スタートメニューからblueCFD-Core terminalを起動する。通常のWindows PowerShellやコマンドプロンプトではなく、このterminalを使うことで、OpenFOAM用の環境変数や実行ファイルが設定される。

起動後、次のように環境を確認できる。

```sh
echo $WM_PROJECT_VERSION
echo $FOAM_RUN
echo $FOAM_TUTORIALS
which blockMesh
which foamRun
```

この教材で使用する2026年版のcaseでは、主に`blockMesh`、`foamRun`、`paraFoam`を使う。

## OpenFOAMの作業ディレクトリ

OpenFOAMでは、計算caseを作業ディレクトリにコピーしてから実行する。`$FOAM_RUN`は、そのための作業場所を表す環境変数である。

```sh
mkdir -p $FOAM_RUN
cd $FOAM_RUN
```

`$FOAM_RUN`は文字通り`$FOAM_RUN`という名前のフォルダーを作る指定ではない。terminalに設定された環境変数の値へ展開される。

## 別のOpenFOAM環境を使う場合

この教材の主対象はblueCFD-Coreだが、OpenFOAMはLinuxやWSLなどでも利用できる。別の環境を使う場合は、インストール方法、solver名、tutorialの配置が異なることがある。

- WindowsではWSL上のOpenFOAMを利用する方法がある。
- LinuxではOpenFOAM Foundationの配布方法を確認する。
- macOSでは、使用するOpenFOAMの公式または推奨されるコンテナ環境を確認する。

以降の手順でコマンドが見つからない場合は、まず使用している環境と`$WM_PROJECT_VERSION`を確認する。

## 次に読む章

次章では、配布済みのcavity caseを使って、メッシュ生成、計算、可視化を一通り実行する。

## ライセンス

```{note}
このページの本文と自作図版は [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.ja) のもとで提供されています。
コードやノートブックの例は MIT License に従います。
第三者の著作物を含む一部のスクリーンショット等は、CC BY-NC-SA 4.0の適用対象外です。詳細は [LICENSE-docs.md](https://github.com/akonno/FluidSeminarMaterials/blob/main/LICENSE-docs.md) を参照してください。
```
