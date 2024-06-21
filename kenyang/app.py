from flask import Flask, request, jsonify
import tensorflow as tf
from PIL import Image
import io 
import numpy as np

app = Flask(__name__)
model = tf.keras.models.load_model('modelmobilenetv2.h5')

@app.route('/predict', methods=['POST'])
def upload(): 
    if 'file' not in request.files:
        return jsonify({'error': 'no file'})
    file= request.files['file']
    if file.filename == '': 
        return jsonify({'error': 'no selected file'})
    if file: 
        image = Image.open(io.BytesIO(file.read()))
        image = image.resize((150, 150))
        image = np.array(image)
        image = image / 255.0  # Normalisasi gambar
        image = np.expand_dims(image, axis=0)
        

    
        # Prediksi dengan model
        prediction = model.predict(image)

        predicted_class_index = np.argmax(prediction)

        # Daftar label yang sesuai dengan kelas
        class_labels = [
            'Fresh Bread', 'Fresh Apples', 'Fresh Banana',
            'Fresh Cucumber', 'Fresh Oranges',
            'Moldy Bread', 'Rotten Apples', 'Rotten Banana',
            'Rotten Cucumber', 'Rotten Oranges'
        ]
        # Menentukan label
        predicted_label = class_labels[predicted_class_index]

        return jsonify({'predict':predicted_label})

if __name__ == '__main__':
    app.run(host= '0.0.0.0', port= 5000)
    
    