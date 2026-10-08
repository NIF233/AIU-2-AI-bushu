### 阶段一：本地大模型部署与 Dify 接入（任务一）

 - 1. AI 协助的内容

· 提供了 Ollama 和 Dify 的部署指导。

<img width="1080" height="2400" alt="80c9c746b9402f7b829ab3bd708afbd7" src="https://github.com/user-attachments/assets/d4c71353-5da4-4d84-999e-88de1fa2da1c" />

<img width="1080" height="2400" alt="b110f59246c4531906469aebc1686e4a" src="https://github.com/user-attachments/assets/5e04808f-968f-4498-81e4-879c5fd0b133" />

· 排查了 Docker 的安装报错（Virtual Machine Platform、WSL）。
· 协助解决了拉取镜像时的网络问题（配置 registry-mirrors 和代理）。

 - 2. AI 翻车与我的解决（高价值经验）

· AI 的局限：AI 给出的 localhost:11434 作为 Dify 的 Base URL，导致连接失败。
· 我的解决：我意识到 Dify 运行在 Docker 容器内，容器内的 localhost 指向容器自身。通过查阅资料，我主动将 Base URL 改为了 http://host.docker.internal:11434，成功连通。
· AI 的局限：AI 提供的 Dify 镜像拉取命令在国内网络下频繁出现 EOF 报错。AI 推荐的 docker pull 依然卡死。
· 我的解决：我通过不断排查，发现是 VPN 代理与国内镜像源冲突。在 Docker Desktop 中关闭代理，并仅保留国内加速源后，问题得以解决。

### 阶段二：YOLO 跑通与 Web 接入（任务二）

 - 1. AI 协助的内容
   
 <img width="1080" height="2400" alt="b79d2b34276891331580339291dd7c12" src="https://github.com/user-attachments/assets/691c25fc-d22a-4842-ab51-184e1ab7c4f6" />

 <img width="1080" height="2400" alt="34f4c807db36bb688906a1c3ac505976" src="https://github.com/user-attachments/assets/e4594d21-83db-4acc-87ff-6f48969e2974" />


· 提供了 Ultralytics 的极简训练脚本和 Flask 后端代码。

 - 2. AI 翻车与我的解决（高价值经验）

· AI 的局限：AI 给的命令 yolo detect train ... 在终端报错“不是内部或外部命令”，因为 Python Scripts 目录未加入系统 PATH。AI 建议的 python -m ultralytics 依然报错。
· 我的解决：我果断放弃了命令行调用，要求 AI 提供 Python 脚本版本，通过 model.train() 方式成功启动训练，彻底绕过了环境变量问题。
· AI 的局限：前端 HTML 中 JS 报错 Cannot set properties of null。AI 给出的代码里，<img> 标签内部多了一个肉眼难以察觉的空格（< img），导致浏览器将其渲染为纯文本。
· 我的解决：我按下 F12 查看控制台，并逐行检查代码，发现了这个空格并修正。这让我明白了前端工程中“严格语法”的重要性。

### 阶段三：Harness 智能体框架搭建（任务四）

 - 1. AI 协助的内容

· 提供了基于 Python 从零实现 Agent Loop（包含工具注册、LLM 调用、对话记忆）的代码骨架。

<img width="1080" height="2400" alt="6bec277186f07279728629ee4d03fe06" src="https://github.com/user-attachments/assets/c0754158-22bd-4cca-967f-35cbf42916eb" />

<img width="1080" height="2400" alt="c4fa575537bbf1a3aa89308184a9a6f5" src="https://github.com/user-attachments/assets/a52b08a0-b1a4-44e7-a3cd-bef57193b877" />

 - 2. AI 翻车与我的解决（高价值经验）

· AI 的局限：AI 在 tools.py 中生成的文件名为 11m.py（数字1），而代码里 from .llm import 用的是字母 l。AI 拼写错误导致 ModuleNotFoundError。
· 我的解决：我通过仔细比对文件名和导入路径，发现了这个“拼写错觉”，重命名文件并清理 __pycache__ 后解决。
· AI 的局限：调用工具时出现 TypeError: the JSON object must be str, bytes or bytearray, not dict。
· 我的解决：我排查发现，标准 OpenAI 接口返回的 arguments 是字符串，而本地 Ollama 返回的是已经解析好的字典。我修改了 agent.py 代码，加入了 isinstance 类型判断，成功兼容了两种 API 格式。

### 阶段四：创意作品 - 2D 转 3D 场景生成（任务五）

 - 1. AI 协助的内容
 
<img width="1080" height="2400" alt="6bec277186f07279728629ee4d03fe06" src="https://github.com/user-attachments/assets/b8a1d7fc-b3f6-4d5a-a57b-79b596eefbfc" />

· 提供了 Three.js 渲染基础几何体的前端模板。

<img width="1080" height="2400" alt="75bfdf14d796a37469a1d309c7eee46b" src="https://github.com/user-attachments/assets/4195982e-af54-4a54-8670-5ceae5e3366d" />

· 协助设计了 YOLO 2D 坐标映射到 3D 空间的算法。

<img width="1080" height="2400" alt="d10d93989acf516a4cb39844fa9e3ba0" src="https://github.com/user-attachments/assets/73a14b88-138c-4d6e-81e5-f1c5295cb6c8" />

 - 2. AI 翻车与我的解决（高价值经验）

· AI 的局限：本地小模型（qwen2.5）在生成 Three.js 代码和严格 JSON 时极其不稳定，容易出现幻觉。
· 我的解决：我将架构从“让大模型生成代码”重构为“数据驱动渲染”。后端只负责 YOLO 识图和坐标计算，前端写死一个“物体-几何体映射字典”。这个工程决策彻底解决了黑屏和崩溃问题，保证了系统的健壮性。
· AI 的局限：AI 生成的 CDN 链接（cdnjs）在国内被拦截，导致 Three.js 加载失败。
· 我的解决：我放弃了外网 CDN，下载 three.min.js 和 OrbitControls.js 到本地，并在 Flask 后端添加了静态文件路由，彻底摆脱了网络依赖。
