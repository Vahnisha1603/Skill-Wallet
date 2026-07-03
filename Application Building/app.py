import numpy as np
# pyrefly: ignore [missing-import]
from flask import Flask, request, render_template, redirect, url_for
import pickle
import json
import datetime
import os

app = Flask(__name__)

# Load the trained machine learning model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = pickle.load(open(os.path.join(BASE_DIR, "model.pkl"), 'rb'))
label_encoder = pickle.load(open(os.path.join(BASE_DIR, "label_encoder.pkl"), 'rb'))

HISTORY_FILE = os.path.join(BASE_DIR, 'predictions_history.json')

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r') as f:
            return json.load(f)
    return []

def save_history(history):
    with open(HISTORY_FILE, 'w') as f:
        json.dump(history, f, indent=4)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/findyourcrop')
def findyourcrop():
    return render_template('findyourcrop.html')

@app.route('/previous_crops')
def previous_crops():
    history = load_history()
    return render_template('previous_crops.html', history=history)

@app.route('/delete_prediction/<int:index>')
def delete_prediction(index):
    history = load_history()
    if 0 <= index < len(history):
        history.pop(index)
        save_history(history)
    return redirect(url_for('previous_crops'))


@app.route('/predict', methods=['POST'])
def predict():
    int_features = [float(x) for x in request.form.values()]
    features = [np.array(int_features)]
    prediction = model.predict(features)

    output = label_encoder.inverse_transform(prediction)[0]
    
    # Save to history
    history = load_history()
    now = datetime.datetime.now().strftime("%b %d, %Y %H:%M")
    
    # Format conditions string nicely
    N, P, K, temp, hum, ph, rain = int_features
    conditions = f"N:{int(N)}, P:{int(P)}, K:{int(K)}, Temp:{temp:.1f}°C, Hum:{hum:.1f}%, pH:{ph:.1f}, Rain:{rain:.1f}mm"
    
    history.insert(0, {
        'date': now,
        'conditions': conditions,
        'crop': output.capitalize()
    })
    save_history(history)
    
    return render_template('findyourcrop.html', prediction_text='Best crop for given conditions is: {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)
