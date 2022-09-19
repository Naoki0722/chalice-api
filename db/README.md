# DynamoDBのセットアップ方法

## 前提

- aws-cliコマンドがインストール済みであること
- awsのクレデンシャル情報が設定済みであること


## 作業手順

### テーブルの作成

```
./01-create-table.sh
```

標準出力のTableArnを後で使うので、控えておくこと。

### テーブルへの初期データ登録

```
./02-post-initial-data.sh
```

### Cleanup(テーブルの削除)

```
aws dynamodb delete-table --table-name Records
```
