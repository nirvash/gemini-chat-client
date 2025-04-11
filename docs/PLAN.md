# Gemini チャットクライアント開発計画

## 概要

`adk-python` ライブラリと Streamlit を使用して、Gemini 2.5 (利用可能な最新モデル) と 1:1 でチャットできるシンプルな Web アプリケーションの基礎部分を作成します。

## 計画

1.  **環境設定:**
    *   Python 開発環境を準備します。
    *   必要なライブラリをインストールします。
        ```bash
        pip install google-adk streamlit
        ```
    *   Gemini API キーを環境変数 `GOOGLE_API_KEY` に設定します。

2.  **プロジェクト構造の作成:**
    *   ワークスペース (`c:/Work/a2a-client`) 直下に以下のディレクトリ構造を作成します。
        ```
        c:/Work/a2a-client/
        ├── agents/
        │   ├── chat_agent/
        │   │   ├── agent.py
        │   │   └── __init__.py
        │   └── __init__.py
        └── ui/
            └── app.py
        ```
    *   Mermaid ダイアグラム:
        ```mermaid
        graph TD
            A[c:/Work/a2a-client] --> B(agents);
            B --> C(chat_agent);
            C --> C1(agent.py);
            C --> C2(__init__.py);
            B --> D(__init__.py);
            A --> E(ui);
            E --> F(app.py);
        ```

3.  **エージェント (バックエンド) の定義:**
    *   `agents/chat_agent/agent.py` に `google.adk.agents.Agent` を使用してチャットエージェントを定義します。
        *   `name`: `"gemini_chatter"`
        *   `model`: `"gemini-1.5-flash-latest"` (または利用可能な最新モデル)
        *   `instruction`: `"あなたはユーザーと会話するフレンドリーなチャットボットです。"`
        *   `description`: `"Gemini と 1:1 でチャットするエージェント"`
        *   `tools`: `[]`
    *   `agents/chat_agent/__init__.py` で上記エージェントをインポートします。
    *   `agents/__init__.py` は空ファイルとして作成します。

4.  **UI (フロントエンド) の作成 (Streamlit):**
    *   `ui/app.py` に Streamlit アプリケーションを実装します。
    *   基本的なチャットインターフェース (入力欄、送信ボタン、会話履歴表示) を作成します。
    *   ユーザー入力時に `google.adk.run_agent` (または関連関数) を使用して `agents.chat_agent` を呼び出し、応答を取得・表示します。

5.  **実行と確認:**
    *   ターミナルで `streamlit run ui/app.py` を実行し、Web ブラウザでチャット UI が表示され、Gemini との対話が可能であることを確認します。