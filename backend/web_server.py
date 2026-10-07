import io
import base64
import cv2
import numpy as np
from flask import Flask, request, jsonify, send_from_directory
from ultralytics import YOLO

app = Flask(__name__)
# 加载官方模型，为了测试方便，用轻量的
model = YOLO("yolo11n.pt")

@app.route('/')
def index():
    # 返回前端页面
    return send_from_directory('../frontend', 'index.html')

@app.route('/detect', methods=['POST'])
def detect():
    file = request.files.get('image')
    if not file:
        return jsonify({"error": "未上传图片"}), 400

    # 1. 读取图片
    img_bytes = file.read()
    nparr = np.frombuffer(img_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # 2. YOLO 推理
    results = model(img)
    
    # 3. 将识别结果绘制在图像上
    annotated_img = results[0].plot()
    
    # 4. 将图片转换为 base64 编码返回前端
    _, buffer = cv2.imencode('.jpg', annotated_img)
    img_base64 = base64.b64encode(buffer).decode('utf-8')
    
    return jsonify({"image": f"data:image/jpeg;base64,{img_base64}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)