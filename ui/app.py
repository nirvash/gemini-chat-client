"""
Gemini チャットクライアント UI
Streamlit を使用したシンプルなチャットインターフェース
"""

import os
import logging
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
from agents.chat_agent import chat_agent

# ログ設定
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# .env ファイルから環境変数を読み込む
load_dotenv()

# API キーが設定されているか確認
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("APIキーが設定されていません。.envファイルにGOOGLE_API_KEYを設定してください。")
    st.code("""
# .env ファイルに以下の形式で API キーを設定してください
GOOGLE_API_KEY=your_api_key_here
    """)
    st.stop()
else:
    logger.info(f"APIキーが設定されています: {api_key[:4]}...")
    st.sidebar.success("APIキーが設定されています")

# Gemini の設定
genai.configure(api_key=api_key)

try:
    # エージェントの設定に基づいてGeminiモデルを初期化
    model = genai.GenerativeModel(chat_agent.model)
    
    # システムプロンプトを含むチャットを開始
    chat = model.start_chat(history=[])
    
    # システムプロンプトを送信
    logger.debug(f"システムプロンプト:\n{chat_agent.instruction}")
    logger.debug("システムプロンプトを送信...")
    chat.send_message(f"システム: {chat_agent.instruction}")
    
    st.sidebar.success(f"使用モデル: {chat_agent.model}")
    st.sidebar.info(f"システムプロンプト:\n{chat_agent.instruction}")
except Exception as e:
    logger.error(f"モデルの初期化エラー: {e}")
    st.error(f"モデルの初期化エラー: {e}")
    st.stop()

def initialize_session_state():
    """セッションステートの初期化"""
    if "messages" not in st.session_state:
        st.session_state.messages = []
        logger.debug("セッションステートを初期化しました")

def display_chat_history():
    """チャット履歴の表示"""
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
            logger.debug(f"表示: [{message['role']}] {message['content'][:100]}...")

def process_user_input(user_input: str):
    """ユーザー入力の処理とエージェントからの応答取得"""
    if user_input:
        logger.info(f"ユーザー入力を受信 ({len(user_input)} 文字): {user_input}")
        print(f"[ユーザー] {user_input}")
        
        # ユーザーメッセージの保存
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        try:
            logger.debug("Gemini に問い合わせを開始...")
            print("Gemini に問い合わせを開始...")
            
            # Gemini からの応答を取得
            response = chat.send_message(user_input)
            response_text = response.text
            
            logger.info(f"Gemini からの応答 ({len(response_text)} 文字): {response_text}")
            print(f"[Gemini] {response_text}")
            
            # エージェントの応答を保存
            st.session_state.messages.append({"role": "assistant", "content": response_text})
        except Exception as e:
            error_msg = f"エラーが発生しました: {str(e)}"
            logger.error(error_msg)
            logger.exception(e)
            print(f"[エラー] {error_msg}")
            st.error(error_msg)
            st.sidebar.error(f"エラー詳細: {repr(e)}")

def main():
    """メインアプリケーション"""
    st.title("Gemini 2.5 Pro チャット")
    st.caption("Gemini 2.5 と 1:1 でチャットができます")
    
    # エージェント情報の表示
    st.sidebar.info(chat_agent.description)
    
    # セッションステートの初期化
    initialize_session_state()
    
    # チャット履歴の表示
    display_chat_history()
    
    # ユーザー入力の処理
    user_input = st.chat_input("メッセージを入力してください...")
    if user_input:
        process_user_input(user_input)
        st.rerun()  # UIを更新

if __name__ == "__main__":
    logger.info("アプリケーションを起動")
    print("アプリケーションを起動")
    main()