# post-slack-sample
Slackに投稿するサンプルコード

## プロジェクトインストール

```bash
poetry install
```

## credentialファイル作成

```bash
cp post_slack_sample/.env.sample post_slack_sample/.env
```

## プログラム実行

```bash
poetry run python post_slack_sample/main.py
```

or 

```bash
make main
```

## フォーマット

```bash
make format
```

## テスト実行

```bash
make test
```

## 型チェック

```bash
make type-check
```

## 全てまとめてチェック

```bash
make format test type-check
```
