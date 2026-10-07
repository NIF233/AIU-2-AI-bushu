 ## [2026-10-07 13:44] 任务四：Harness 智能体框架搭建完毕。
 
 **进展**：从零实现了包含 Agent Loop、工具注册（read_file/write_file/bash）、Ollama LLM 封装、对话历史管理的完整 Harness。
 
 **踩坑与解决**：
 1. 跨盘符切换路径失败。解决：使用 `cd /d D:\AIU-Project` 强制切换。
  <img width="1706" height="1279" alt="4425115e83b1d84f598d8d8d065d5131" src="https://github.com/user-attachments/assets/e19cf5fe-54dd-4fd3-a7d5-83fd48072d06" />
 2. 文件名拼写错误（将字母 `l` 敲成数字 `1`，导致 `llm.py` 变成 `11m.py`）。解决：重命名文件并清理 `__pycache__`。
  
3. 调用工具报错 `TypeError: the JSON object must be str, bytes or bytearray, not dict`。原因：Ollama 返回的 arguments 是 dict，而 OpenAI 是字符串。解决：在 `agent.py` 中增加 `isinstance` 类型判断，兼容两种格式。
  <img width="1706" height="1279" alt="56e1d2ff226cc65fc2506136798e2171" src="https://github.com/user-attachments/assets/d6624405-a5df-44e7-9f50-1644f420a415" />
 4. 读取文件报错 `FileNotFoundError`。原因：本地目录确实没有该文件。解决：在本地补建文件，验证了 Agent 的异常捕获与反馈机制。

---

### 📊 当前我的面试任务完成度：
*   **任务一（大模型+智能体应用）** ✅ 已完成（Ollama + Dify + CLI）
*   **任务二（YOLO跑通与接入）** ✅ 已完成（训练 + 实时推理 + Web接入）
*   **任务三（硬件结合）** ⏳ 进阶选做。没有单片机，**跳过**。
*   **任务四（Harness搭建）** ✅ 已完成（从零实现Agent框架）
*   <img width="1280" height="800" alt="屏幕截图 2026-10-07 142319" src="https://github.com/user-attachments/assets/3731aca0-de5a-4bad-ad50-6973e7ed10f4" />
*   **任务五（创意作品）** ⏳ 自由发挥。
