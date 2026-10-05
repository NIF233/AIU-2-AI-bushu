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
1. 安装 Ollama：去 ollama.com 下载安装
2. 拉取模型：`ollama pull qwen2.5`
3. 安装依赖：`pip install -r requirements.txt`
4. 启动后端：`python app.py`
5. 打开浏览器访问 `http://localhost:5000`

## 项目结构
