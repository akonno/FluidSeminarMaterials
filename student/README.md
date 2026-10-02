# 履修者向け配布資材

このディレクトリには、Python/JupyterLab演習で使う環境定義、Notebook、データ、PyGame演習用ファイルをまとめています。

## Conda環境

`environment.yml`はPython/JupyterLab演習用のConda環境です。リポジトリのrootから作成する場合は、次を実行します。

```bash
conda env create -f student/environment.yml
```

この`student/`ディレクトリ内で実行する場合は、次の指定でも作成できます。

```bash
conda env create -f environment.yml
```

## Notebook

`notebooks/`には演習で使うJupyter Notebookとデータが入っています。Notebookが`sample_data/`を参照するため、Notebookと同じ階層にある`sample_data/`を含め、ディレクトリ構造を保って使用してください。

## PyGame

`pygame/`にはPyGame演習用ファイルがあります。`bouncingballs.py`と`bb-sample.py`は同じディレクトリに置いたまま使用してください。
