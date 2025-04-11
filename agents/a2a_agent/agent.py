"""A2Aエージェントの定義"""

from google.adk.agents import Agent
from google.adk.tools import ToolRegistry
from mcp import Client as McpClient
from agents.mcp_config import MCP_CONFIG

# MCPクライアントの初期化
mcp_client = McpClient(MCP_CONFIG)

# MCPツールの登録
tool_registry = ToolRegistry()
tool_registry.register_tool(
    "github",
    "GitHubファイルの操作",
    {
        "get_file_contents": {
            "description": "GitHubのリポジトリからファイルの内容を取得します",
            "parameters": {
                "owner": "string",
                "repo": "string",
                "path": "string",
                "branch": "string"
            }
        }
    }
)

# A2Aエージェントの定義
a2a_agent = Agent(
    name="a2a_executor",
    model="models/gemini-2.5-pro-preview-03-25",
    instruction="""あなたはA2A（Agent-to-Agent）タスクを実行するエージェントです。
    他のエージェントからの要求に応じて、MCPツールを使用してタスクを実行します。
    GitHubのファイル操作などのツールを使って、効率的にタスクを遂行してください。""",
    description="A2Aタスクを実行し、MCPツールを使用して作業を行うエージェント",
    tools=tool_registry.tools,
)

# エージェントにMCPクライアントを関連付け
setattr(a2a_agent, "mcp_client", mcp_client)