from flask import Flask, render_template, request
from PIL import Image
import cv2
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    image = request.files['image']
    img = Image.open(image)
    img = np.array(img)  # Mengubah gambar menjadi array numpy
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Mengubah gambar menjadi grayscale
    gray_img = Image.fromarray(gray_img)  # Mengubah array numpy kembali menjadi gambar PIL
    gray_img.save('static/grayscale_image.jpg')  # Simpan gambar grayscale
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
