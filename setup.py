from setuptools import setup, find_packages

setup(
    name="gemini-chat",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "google-adk",
        "google-generativeai",
        "streamlit",
        "python-dotenv",
        "mcp",  # Model Context Protocol SDK
        "docker",  # MCPのDockerサポート用
    ],
    extras_require={
        "dev": [
            "black",
            "pytest",
        ]
    }
)