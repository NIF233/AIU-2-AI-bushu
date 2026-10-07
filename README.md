# AIU-2-AI-bushu
此为用于记录华南农业大学AIU二面人工智能大模型本地部署
# AIU 创智部二面实战项目

一句话说明：基于本地 Ollama 大模型 + YOLO 目标检测的 Web 应用。

## 这个项目能做什么
- 在本地运行大模型，无需联网即可对话
- 通过 API 将本地模型接入 Web 应用
- YOLO 实时目标检测

## 怎么跑起来
### 环境要求
- Python 3.10+
- 8GB 以上内存（跑 7B 模型）

### 步骤

🚀 快速开始（复现步骤）

1. 启动本地大模型
   前往 Ollama 官网 下载并安装，在终端执行：
   ```bash
   ollama run qwen2.5
   ```
2. 部署 Dify 平台
   在终端执行（需确保 Docker 已启动）：
   ```bash
   git clone https://github.com/langgenius/dify.git
   cd dify/docker
   cp .env.example .env
   docker compose up -d
   ```
   启动成功后，浏览器访问 http://localhost/install 完成初始化。
3. 配置本地模型
   在 Dify 后台 -> 设置 -> 模型供应商中，添加 Ollama：
   · 基础 URL：http://host.docker.internal:11434
   · 模型名称：qwen2.5
4. 运行 CLI 应用
   创建一个聊天应用，生成 API 密钥后，执行：
   ```bash
   pip install requests
   python cli_app.py
   ```

🤖 AI 使用说明

本项目在开发过程中使用了 AI 辅助（如生成 CLI 测试代码、排查 Docker 网络配置问题），所有系统环境配置、Dify 平台接入和调试均由本人独立完成。

📝 踩坑记录（详见 docs/progress.md）

· Windows 下安装 Docker 遇到“虚拟机平台未开启”、“WSL 未安装”等连环报错，通过手动开启系统功能并安装内核更新包解决。
· Docker 镜像拉取遇到网络限制，通过在 Docker Engine 配置国内镜像源解决。
· Dify 接入 Ollama 时，基础 URL 必须使用 host.docker.internal，因为容器内的 localhost 指向容器自身。

## 项目结构
```text
AIU-2-AI-bushu/
├── README.md           # 项目说明文档
├── cli_app.py          # 自建 CLI 应用，通过 API 调用 Dify
└── docs/
    └── progress.md     # 工程日志（记录踩坑与解决过程）
