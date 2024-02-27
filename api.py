# NOT COMPLETED

from flask import Flask, request, jsonify
import tensorflow as tf
from PIL import Image
import numpy as np
import os

app = Flask(__name__)

working_dir = os.path.dirname(os.path.abspath(__file__))
model_path = f"{working_dir}/trained_fashion_mnist_model.h5"
# Load the pre-trained model
model = tf.keras.models.load_model(model_path)

# Define class labels for Fashion MNIST dataset
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# Function to preprocess the uploaded image
def preprocess_image(image):
    img = Image.open(image)
    img = img.resize((28, 28))
    img = img.convert('L')  # Convert to grayscale
    img_array = np.array(img) / 255.0
    img_array = img_array.reshape((1, 28, 28, 1))
    return img_array

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    if file:
        img_array = preprocess_image(file)

        # Make a prediction using the pre-trained model
        result = model.predict(img_array)
        predicted_class = np.argmax(result)
        prediction = class_names[predicted_class]

        return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
