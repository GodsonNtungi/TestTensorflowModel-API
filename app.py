import base64

import io

from PIL import Image
from flask import Flask, jsonify, request
import joblib
import sklearn

model = joblib.load('testmodel.pkl')
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return jsonify({'text': 'helloworld'})


@app.route('/testprediction', methods=['POST'])
def Picture_prediction():
    if request.method == 'POST':
        some_json = request.get_json()
        #image_bytes=some_json['body'].encode()
        #value = base64.b64decode( image_bytes)
        #image = Image.open(io.BytesIO(value))



        return jsonify({'value':1})


if __name__ == '__main__':
    app.run(debug=True)
