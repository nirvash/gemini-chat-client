"""MCP設定の管理"""

import os
from dotenv import load_dotenv

# 環境変数の読み込み
load_dotenv()

# MCPツールの設定
MCP_CONFIG = {
    "github": {
        "disabled": False,
        "command": "docker",
        "args": [
            "run",
            "-i",
            "--rm",
            "-e",
            "GITHUB_PERSONAL_ACCESS_TOKEN",
            "ghcr.io/github/github-mcp-server"
        ],
        "env": {
            "GITHUB_PERSONAL_ACCESS_TOKEN": os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN")
        },
        "alwaysAllow": [
            "get_file_contents"
        ]
    }
}