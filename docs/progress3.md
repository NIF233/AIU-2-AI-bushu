## [2026-10-07 10:56] 任务二：YOLO 跑通与 Web 接入完成

**进展**：
- ✅ 使用 `coco8.yaml` 数据集完成 `yolo11n.pt` 的 10 轮训练，mAP50 达 0.85。
- <img width="1706" height="1279" alt="b7b2394177569a71ff5d62cf2254a0dc" src="https://github.com/user-attachments/assets/ed267caf-6544-4b65-8f46-48e49bcd1352" />
- ✅ 编写 Python 脚本调用摄像头，实现 YOLO 实时推理检测。
- <img width="1706" height="1279" alt="3f7836cba05ec7a57125fc67b4a4e13e" src="https://github.com/user-attachments/assets/bdd7f9aa-478c-44fb-9bb4-3f904bfc6b02" />
- ✅ 编写 Flask 后端接口与 HTML 前端页面，实现“网页上传图片 -> 后端推理 -> 展示画框结果”全链路。
- <img width="1706" height="1279" alt="405cc8d041bf359b7ed7da535ed81f49" src="https://github.com/user-attachments/assets/df932d82-1127-42b3-9e71-fc6ce8d2c861" />

**踩坑与思考**：
- `yolo` 命令报错“不是内部或外部命令” -> 原因是 Python Scripts 目录未加入系统 PATH。解决：在 `train.py` 中通过 `model.train()` 方式调用，绕过命令行执行。
- 前端页面点“上传”无反应，报错 `Cannot set properties of null` -> 原因是 `<img>` 标签内部多了一个空格，导致浏览器将其渲染为文本，JS 找不到该元素。解决：手动删除空格并强制刷新浏览器。
- <img width="1706" height="1279" alt="19fc0b10d42c5dcca0f1f8ea6068eb01" src="https://github.com/user-attachments/assets/130a7165-74c7-49a1-bbdb-3e3fda869de9" />

**下一步**：
- 尝试进阶任务（如硬件结合或 Harness 搭建）。
