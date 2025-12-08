# redash-mcp

Redash API連携用のMCP (Model Context Protocol) サーバー

[English](README.md)

## 必要要件

- Python 3.10+
- [uv](https://docs.astral.sh/uv/)

## インストール

```bash
# リポジトリをクローン
git clone https://github.com/eiji-hb/redash-mcp.git
cd redash-mcp

# 依存関係をインストール
uv sync
```

## 設定

以下の環境変数を設定してください：

| 変数名 | 必須 | デフォルト | 説明 |
|--------|------|-----------|------|
| `REDASH_URL` | Yes | - | RedashインスタンスのURL |
| `REDASH_API_KEY` | Yes | - | Redash APIキー |
| `REDASH_TIMEOUT` | No | 30000 | リクエストタイムアウト（ミリ秒） |

## 使い方

### Claude Desktopで使用する場合

Claude Desktopの設定ファイル（`~/Library/Application Support/Claude/claude_desktop_config.json`）に以下を追加：

```json
{
  "mcpServers": {
    "redash": {
      "command": "uv",
      "args": ["--directory", "/path/to/redash-mcp", "run", "redash-mcp"],
      "env": {
        "REDASH_URL": "https://your-redash-instance.example.com",
        "REDASH_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

> **注意**: 環境変数は設定ファイルの`env`セクションに記述する必要があります。Claude Desktopから起動する場合、`.env`ファイルは読み込まれません。

### 単体で実行する場合

```bash
# 環境変数を設定
export REDASH_URL=https://your-redash-instance.example.com
export REDASH_API_KEY=your-api-key-here

# または.envファイルを作成して実行
uv run redash-mcp
```

## 利用可能なツール

### クエリ
- `list_queries` - Redashに保存されているSQLクエリの一覧を取得
- `get_query` - 指定したIDのクエリ詳細を取得
- `create_query` - 新しいSQLクエリを作成
- `update_query` - 既存のクエリを更新
- `archive_query` - クエリをアーカイブ（ソフト削除）
- `get_query_result` - クエリのキャッシュ結果を取得（パラメータなしクエリのみ）
- `execute_query` - クエリを実行（パラメータ付きクエリ・キャッシュ制御対応）
- `get_query_result_by_id` - 結果IDでクエリ結果を取得

### ジョブ
- `get_job` - ジョブのステータスを取得（1=PENDING, 2=STARTED, 3=SUCCESS, 4=FAILURE, 5=CANCELLED）

### ダッシュボード
- `list_dashboards` - Redashのダッシュボード一覧を取得
- `get_dashboard` - スラッグでダッシュボードを取得
- `create_dashboard` - 新しいダッシュボードを作成
- `update_dashboard` - 既存のダッシュボードを更新
- `archive_dashboard` - ダッシュボードをアーカイブ（ソフト削除）

### データソース
- `list_data_sources` - Redashのデータソース一覧を取得
- `get_data_source` - IDでデータソースを取得
- `create_data_source` - 新しいデータソースを作成
- `update_data_source` - 既存のデータソースを更新
- `delete_data_source` - データソースを削除

## ライセンス

MIT
