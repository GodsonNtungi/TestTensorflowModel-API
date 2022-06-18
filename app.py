from flask import Flask,jsonify,request
import joblib
import sklearn
model = joblib.load('testmodel.pkl')
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return jsonify({'text':'helloworld'})

@app.route('/testprediction',methods =['POST'])
def Picture_prediction():
    if request.method == 'POST':
        some_json = request.get_json()
        value = model.predict([some_json['some json']])
        return jsonify({'value':int(value[0])})





if __name__ == '__main__':
    app.run()
