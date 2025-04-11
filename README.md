# Gemini Chat Client

Gemini 2.5 Pro を使用したシンプルなチャットクライアント。
Streamlit UIとGoogle ADK（Agent Development Kit）を使用して実装されています。

## 必要条件

- Python 3.10 以上
- Gemini API キー（[Google AI Studio](https://makersuite.google.com/) から取得可能）

## インストール手順

1. リポジトリのクローン
```bash
git clone <repository-url>
cd a2a-client
```

2. Python 仮想環境の作成と有効化

**Windows:**
```bash
# 仮想環境の作成
python -m venv venv

# 仮想環境の有効化
venv\Scripts\activate
```

**macOS/Linux:**
```bash
# 仮想環境の作成
python3 -m venv venv

# 仮想環境の有効化
source venv/bin/activate
```

3. 必要なパッケージのインストール
```bash
# pip のアップグレード
python -m pip install --upgrade pip

# 開発モードでのインストール
pip install -e .
```

これにより、以下のパッケージが自動的にインストールされます：
- google-adk
- google-generativeai
- streamlit
- python-dotenv

4. 環境変数の設定

`.env` ファイルをプロジェクトのルートディレクトリに作成し、Gemini API キーを設定します：

```plaintext
GOOGLE_API_KEY=your_api_key_here
```

## 実行方法

1. 仮想環境が有効化されていることを確認
```bash
# 仮想環境の状態確認（プロンプトに (venv) が表示されているはず）
```

2. Streamlit アプリケーションを起動
```bash
streamlit run ui/app.py
```

ブラウザが自動的に開き、チャットインターフェースが表示されます。

## プロジェクト構造

```
a2a-client/
├── agents/
│   ├── __init__.py
│   └── chat_agent/
│       ├── __init__.py
│       └── agent.py        # エージェントの定義
├── ui/
│   └── app.py             # Streamlit UI の実装
├── venv/                  # Python 仮想環境（git管理外）
├── .env                   # 環境変数（git管理外）
├── .gitignore
├── README.md
└── setup.py
```

## 開発

1. 開発用インストール：
```bash
pip install -e ".[dev]"
```

2. コードフォーマット：
```bash
black .
```

## 仮想環境の終了

作業が終わったら、仮想環境を終了します：

**Windows/macOS/Linux 共通:**
```bash
deactivate
```

## ライセンス

[ライセンス情報をここに記載]

## 注意事項

- API キーは `.env` ファイルで管理し、絶対にGitにコミットしないでください
- まだ開発中の機能があります
- 必ず仮想環境内で実行してください