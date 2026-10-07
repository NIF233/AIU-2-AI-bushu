import cv2
from ultralytics import YOLO

# 加载刚才训练好的模型（或者直接用官方模型 yolo11n.pt）
# 这里为了展示效果，我们用官方预训练模型（能识别80种类别，比刚才只识别4张图的模型效果好）
model = YOLO("yolo11n.pt") 

# 打开摄像头，0代表默认摄像头
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("无法打开摄像头，请检查设备。")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 进行推理
    results = model(frame)
    
    # 在画面上绘制检测框
    annotated_frame = results[0].plot()
    
    # 显示画面
    cv2.imshow("YOLO Real-time Detection", annotated_frame)

    # 按 'q' 键退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()