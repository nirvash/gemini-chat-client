"""Gemini チャットエージェントの定義"""

from google.adk.agents import Agent

# Geminiチャットエージェントの定義
chat_agent = Agent(
    name="gemini_chatter",
    model="models/gemini-2.5-pro-preview-03-25",  # Gemini 2.5 Pro Preview モデル
    instruction="""あなたはユーザーと会話するフレンドリーなチャットボットです。
    ユーザーからの質問や相談に対して、親切で分かりやすい応答をお願いします。
    また、技術的な質問に対しては具体的な例を交えながら説明してください。""",
    description="Gemini 2.5 Pro Preview と 1:1 でチャットするエージェント",
    tools=[],  # 今回はツールを使用しない
)