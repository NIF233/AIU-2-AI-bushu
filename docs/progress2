# 项目工程日志

## [2026-10-06 08:00-22:00] 任务一：本地大模型与智能体应用全链路打通

### 阶段性进展
- ✅ 完成本地 Ollama 的部署，成功运行 qwen2.5 模型。
- ✅ 完成 Dify 平台的 Docker 本地化部署（16个容器全部 Running）。
- ✅ 在 Dify 中成功接入本地 Ollama 作为 Model Provider。
- ✅ 创建 Chatflow 应用并获取 API 密钥。
- ✅ 编写 Python CLI 应用，成功调用 Dify API 实现流式对话。

### 踩坑与思考（核心实战记录）
1. **Docker 环境报错**：
   - 报错 Virtual Machine Platform not enabled 以及 WSL not installed。
   - **解决**：通过管理员 PowerShell 开启虚拟机平台和 WSL 功能，重启电脑后解决。
2. **镜像拉取极其缓慢（EOF/Interrupted）**：
   - **原因**：VPN 代理与国内镜像加速源冲突，导致连接被拒。
   - **解决**：在 Docker Desktop -> Settings -> Resources -> Proxies 中彻底关闭代理，并在 Docker Engine 中配置国内镜像源（1ms.run、xuanyuan.me 等）。
3. **接入 Ollama 模型报错 404 not found**：
   - **原因**：配置 Dify 模型名称时写了 `qwen2.5:7b`，但本地实际只下载了 `qwen2.5:latest`。
   - **解决**：通过 `ollama ls` 查看本地实际模型，修正 Dify 配置。
4. **运行 Python CLI 脚本报错找不到 pip 和 requests**：
   - **解决**：切换至 `D:\AIU-Project` 目录，并使用 `python -m pip install requests` 替代 `pip` 命令安装依赖。

### 下一步计划
- 开始准备 YOLO 的跑通与实时推理部署。
- 尝试将 YOLO 结果通过 API 接入到 Web 端。
