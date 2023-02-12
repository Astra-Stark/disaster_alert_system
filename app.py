from flask import Flask, request, url_for, redirect, render_template
import pickle
import numpy as np
app = Flask(__name__, template_folder='template')
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def hello():
        return render_template("index1.html")
@app.route('/hailstorm', methods=['POST','GET'])
def hailstorm():
        return render_template('hailstorm.html')
@app.route('/pre', methods=['POST', 'GET'])
def predct():
        model = pickle.load(open('model1.pkl', 'rb'))
        int_features = [float(x) for x in request.form.values()]
        final = [np.array(int_features)]
        prediction = model.predict(final)
        if prediction >= 10:
            return render_template('hailstorm.html', pred='Risky')
        else:
            return render_template('hailstorm.html', pred="Safe")

@app.route('/flood', methods=['POST','GET'])
def floods():
        return render_template('floodprediction.html')
@app.route('/predicts', methods=['POST', 'GET'])
def predicts():
        model = pickle.load(open('model2.pkl', 'rb'))
        int_features = [float(x) for x in request.form.values()]
        final = [np.array(int_features)]
        prediction = model.predict(final)
        if prediction == 1:
            return render_template('floodprediction.html', pred='Risky')
        else:
            return render_template('floodprediction.html', pred='safe')
@app.route('/earthquake', methods=['POST','GET'])
def earthquake():
        return render_template('index.html')
@app.route('/predict', methods=['POST', 'GET'])
def predict():
        model = pickle.load(open('model.pkl', 'rb'))
        int_features = [float(x) for x in request.form.values()]
        final = [np.array(int_features)]
        prediction = model.predict(final)
        if prediction >= 3:
            return render_template('index.html', pred='Risky')
        else:
            return render_template('index.html', pred='safe')

if __name__ == "__main__":
        app.run(host='localhost', port=5000)
