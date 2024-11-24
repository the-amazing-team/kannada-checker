import base64
import cv2
import numpy as np
from flask import Flask, request, jsonify
from core.checker import KannadaChecker

app = Flask(__name__)
checker = KannadaChecker()

@app.route('/hello', methods=['GET'])
def hello():
  return "Hello, World!"

@app.route('/check_kannada', methods=['POST'])
def check_kannada():
    data = request.json
    image_base64 = data['image']
    
    # Decode the base64 image
    image_data = base64.b64decode(image_base64)
    np_arr = np.frombuffer(image_data, np.uint8)
    image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    
    # Annotate the image
    annotated_image = checker.add_annotation(image)
    
    # Encode the annotated image to base64
    _, buffer = cv2.imencode('.png', annotated_image)
    annotated_image_base64 = base64.b64encode(buffer).decode('utf-8')
    
    return jsonify({'annotated_image': annotated_image_base64})

if __name__ == '__main__':
    app.run(debug=True)
