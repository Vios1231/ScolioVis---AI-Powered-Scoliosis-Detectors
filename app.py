# app.py

import os
from flask import Flask, request, render_template, jsonify, url_for
from werkzeug.utils import secure_filename

import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
import io

app = Flask(__name__)
app.secret_key = 'your_secure_secret_key'  

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

MODEL_PATH = os.path.join('static', 'scoliosis_detection_model_fixed.keras')  
model = tf.keras.models.load_model(MODEL_PATH)

def load_and_preprocess_image(file_stream):
    try:
        img = Image.open(file_stream)

        if img.mode != 'RGB':
            img = img.convert('RGB')

        img = img.resize((224, 224))

        img_array = image.img_to_array(img)

        img_array = img_array / 255.0
       
        img_array = np.expand_dims(img_array, axis=0)
        return img_array, img
    except Exception as e:
        print(f"Error in image preprocessing: {e}")
        return None, None

def predict_image(model, img_array):
    try:
        prediction = model.predict(img_array)
        threshold = 0.6
        if prediction[0] < threshold:
            return "Normal Detected"
        else:
            return "Scoliosis Detected"
    except Exception as e:
        print(f"Error in prediction: {e}")
        return "Error in prediction"

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        if 'file' not in request.files:
            return jsonify({'result': 'No file part in the request'}), 400
        file = request.files['file']
   
        if file.filename == '':
            return jsonify({'result': 'No file selected for uploading'}), 400
        if file and allowed_file(file.filename):
            try:
        
                filename = secure_filename(file.filename)
                
                img_array, img = load_and_preprocess_image(file.stream)
                if img_array is None:
                    return jsonify({'result': 'Invalid image format or corrupted image'}), 400
                
                result = predict_image(model, img_array)
                
                return jsonify({
                    'result': result
                })
            except Exception as e:
                print(f'Error processing image: {e}')
                return jsonify({'result': 'An error occurred during processing'}), 500
        else:
            return jsonify({'result': 'Allowed file types are png, jpg, jpeg, gif'}), 400

    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/paper')
def paper():
    return render_template('paper.html')

if __name__ == '__main__':
    app.run(debug=True)
