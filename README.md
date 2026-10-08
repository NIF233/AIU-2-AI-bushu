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
- **任务一：本地大模型与智能体应用**
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
任务二：YOLO 跑通与 Web 部署

1. 安装依赖：pip install ultralytics opencv-python flask
2. 训练模型（可选）：python 后端/train.py
3. 启动 Web 后端：python 后端/web_server.py
4. 浏览器访问 http://localhost:5000，上传图片即可查看检测结果。

### 任务四：Harness 搭建（进阶）
1. 确保 Ollama 已启动，本地已下载 `qwen2.5` 模型。
2. 在项目根目录运行：
   ```bash
   python -m harness.cli

- **任务五：创意作品 - 2D转3D场景生成（进阶）**
  - 结合 YOLO 与前端 Three.js，实现“上传图片 -> 识别物体 -> 前端渲染 3D 场景”。
  - **工程决策**：放弃不稳定的 LLM 代码生成，改用“数据驱动渲染”架构，实现了高稳定性。
   
🤖 AI 使用说明

本项目在开发过程中使用了 AI 辅助（如生成 CLI 测试代码、排查 Docker 网络配置问题、检查 HTML 语法错误），所有系统环境配置、Dify 平台接入和调试均由本人独立完成。

📝 踩坑记录（详见 docs/progress1.md）

· Windows 下安装 Docker 遇到“虚拟机平台未开启”、“WSL 未安装”等连环报错，通过手动开启系统功能并安装内核更新包解决。
· Docker 镜像拉取遇到网络限制，通过在 Docker Engine 配置国内镜像源解决。
· Dify 接入 Ollama 时，基础 URL 必须使用 host.docker.internal，因为容器内的 localhost 指向容器自身。

## 📂 项目结构
```text
AIU-2-AI-bushu/
├── README.md
├── .gitignore
├── backend/                     # 所有 Python 后端服务与脚本
│   ├── cli_app.py            # 任务一：Dify CLI 客户端
│   ├── train.py              # 任务二：YOLO 训练脚本
│   ├── yolo_cam.py           # 任务二：摄像头实时推理
│   ├── web_server.py         # 任务二：纯 YOLO Web 后端
│   └── web_server_task5.py   # 任务五：2D转3D Web 后端
├── frontend/                     # 网页前端资源
│   ├── index.html            # 任务二：纯 YOLO 前端
│   ├── index_task5.html      # 任务五：2D转3D 前端
│   ├── three.min.js          # 任务五：本地 Three.js 库
│   └── OrbitControls.js      # 任务五：轨道控制器
├── hardness/                   # 任务四：极简智能体运行框架 (Harness)
│   ├── agent.py
│   ├── tools.py
│   ├── llm.py
│   ├── memory.py
│   └── cli.py
└── docs/                   # 工程日志
    ├── progress1.md
    ├── progress2.md
    ├── progress3.md
    ├── progress4.md
    └── progress5.md          # 后续补充
