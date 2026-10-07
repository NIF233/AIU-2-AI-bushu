from ultralytics import YOLO

# 加载官方轻量模型
model = YOLO("yolo11n.pt")

# 开始训练（用官方迷你数据集跑通流程）
model.train(data="coco8.yaml", epochs=10, imgsz=640)