import io
import base64
import cv2
import numpy as np
from flask import Flask, request, jsonify, send_from_directory
from ultralytics import YOLO

app = Flask(__name__)
# 加载 YOLO 模型
model = YOLO("yolo11n.pt")

@app.route('/')
def index():
    # 返回任务五的前端页面
    return send_from_directory('../frontend', 'index_task5.html')

@app.route('/<path:filename>')
def static_files(filename):
    # 提供本地 three.min.js 和 OrbitControls.js 等静态文件
    return send_from_directory('../frontend', filename)

@app.route('/detect', methods=['POST'])
def detect():
    file = request.files.get('image')
    if not file:
        return jsonify({"error": "未上传图片"}), 400

    # 1. 读取图片并进行 YOLO 推理
    img_bytes = file.read()
    nparr = np.frombuffer(img_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    results = model(img)
    
    img_h, img_w = img.shape[:2]
    
    # 2. 遍历所有识别到的物体，并提取坐标映射
    objects_data = []
    for box in results[0].boxes:
        cls_name = model.names[int(box.cls)]
        x_center, y_center, w, h = box.xywh[0].tolist()
        
        # 将 2D 像素坐标映射到 3D 场景坐标 (-3 到 3 之间)
        pos_x = round(((x_center / img_w) - 0.5) * 6, 2)
        # 将 Y 轴翻转（图像坐标原点在左上角，3D场景原点在左下角）
        pos_y = round((1 - y_center / img_h) * 3, 2)
        # 用宽度映射为深度 Z 轴
        pos_z = round(((w / img_w) - 0.5) * 4, 2)
        
        # 确保物体不会沉入地下
        if pos_y < 0.3:
            pos_y = 0.3
            
        objects_data.append({
            "name": cls_name,
            "x": pos_x,
            "y": pos_y,
            "z": pos_z
        })
        
    # 如果一个物体都没识别到，给一个默认数据
    if not objects_data:
        objects_data = [{"name": "default", "x": 0, "y": 0.5, "z": 0}]

    # 3. 将识别框画在图像上，并转为 Base64 返回给前端展示
    annotated_img = results[0].plot()
    _, buffer = cv2.imencode('.jpg', annotated_img)
    img_base64 = base64.b64encode(buffer).decode('utf-8')

    # 4. 返回最终结果
    return jsonify({
        "image": f"data:image/jpeg;base64,{img_base64}",
        "objects": list(set(model.names[int(box.cls)] for box in results[0].boxes)),
        "objects_data": objects_data
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)