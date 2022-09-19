# chalice-api

[![Language: Python3.9](https://img.shields.io/badge/Language-Python3.9-blue)](https://github.com/python)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Code style linter: flake8](https://img.shields.io/badge/Code%20style%20linter-flake8-lightgrey)](https://github.com/PyCQA/flake8)
[![Check: Pylance](https://img.shields.io/badge/Check-Pylance-red)](https://github.com/microsoft/pylance-release)

勉強会用で作成したテストアプリケーションです。

## 技術スタック

- Language：Python3.9.6
- Framework : Chalice
- Linter：flake8
- Formatter：black
- 解析ツール：Pylance

### 外部ライブラリ

VSCode などを利用している場合は、拡張機能として、下記を入れておくと便利です。

- Python
- Pylance

Python のバージョンは`pyenv`などを用いて切り替えてください。

## 環境構築方法(Local)

開発環境は仮想環境を用いて実行します。

### 仮想環境の構築

```
python3.9 -m venv .venv
```

### 仮想環境にログイン

```
source .venv/bin/activate
```

※抜ける時は、`deactivate`コマンドを実行

### requirements.txt のパッケージリストをインストール

```
pip install -r requirements.txt
```

### ローカルサーバーの起動

```
$ chalice local
```

## デプロイ

AWSへのデプロイは下記コマンドで対応可能

```
$ chalice deploy
```

IAMとLambdaとAPIGatewayが自動で作成される。

## dynamoDBへの接続

`db/README.md` を参照して下さい。

## リソースの削除

```
$ chalice delete
```


## その他

### Black によるフォーマットを無効化

fmt で囲む

```python
# fmt: off
matrix = {
    0,  1,  2,
    3,  4,  5,
    6,  7,  8,
}
# fmt: on
```
