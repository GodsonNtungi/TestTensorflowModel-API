import base64

import io

from PIL import Image
from flask import Flask, jsonify, request
import tensorflow as tf
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"


with tf.device('/CPU:0'):
    model1 = tf.keras.models.load_model('TheCatsDogsModel.h5')
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return jsonify({'text': 'testing json return'})


@app.route('/imageprediction', methods=['POST'])
def Picture_prediction():
    if request.method == 'POST':
        some_json = request.get_json()
        picture_list = some_json['body']
        i = 0
        for image_str in picture_list:
            # convert string into bytes
            image_bytes = image_str.encode()
            # decode the base 64 bytes to obtain  image bytes
            value = base64.b64decode(image_bytes)
            image = Image.open(io.BytesIO(value))
            image.save('obama.jpg')
            img = tf.io.read_file("obama.jpg")
            with tf.device('/CPU:0'):
                tensor = tf.io.decode_image(img, dtype=tf.dtypes.float32)
            tensor = tf.image.resize(tensor, [160, 160])
            tensor = tensor * 255
            input_tensor = tf.expand_dims(tensor, axis=0)
            with tf.device('/CPU:0'):
                pred = model1.predict(input_tensor)
                print(pred)
            result = 'unknown'

            if pred[0][0] < 0:
                result = 'cat'
            if pred[0][0] > 0:
                result = 'dog'

        return jsonify({'value': result})



if __name__ == '__main__':
    app.run(port=3000, debug=True)
