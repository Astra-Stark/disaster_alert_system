from flask import Flask, request, url_for, redirect, render_template
import pickle
import numpy as np
app = Flask(__name__, template_folder='template')
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def hello():
        return render_template("index1.html")
@app.route('/hailstrom', methods=['POST','GET'])
def hailstorm():
        return render_template('hailstrom.html')
@app.route('/pre', methods=['POST', 'GET'])
def predicts():
        int_features = [float(x) for x in request.form.values()]
        final = [np.array(int_features)]
        prediction = model.predict(final)
        if prediction == 1:
            return render_template('hailstrom.html', pred='Risky')
        else:
            return render_template('hailstrom.html', pred='safe')
        
@app.route('/flood', methods=['POST','GET'])
def floods():
        return render_template('floodprediction.html')
@app.route('/predicts', methods=['POST', 'GET'])
def predicts():
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
        int_features = [float(x) for x in request.form.values()]
        final = [np.array(int_features)]
        prediction = model.predict(final)
        if prediction >= 3:
            return render_template('index.html', pred='Risky')
        else:
            return render_template('index.html', pred='safe')

if __name__ == "__main__":
        app.run(host='localhost', port=5000)
