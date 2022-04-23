import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result',methods=['POST'])
def predict():

        features = [float(x) for x in request.form.values()]
        final_features = [np.array(features)]
        
        prediction = model.predict(final_features)
        
        output = prediction

        if output==0:
                return render_template('index.html', prediction='THE PATIENT IS NOT LIKELY TO HAVE A HEART FAILURE')
        else:
                return render_template('index.html', prediction='THE PATIENT IS LIKELY TO HAVE A HEART FAILURE')


if __name__ == '__main__':
#Run the application
    app.run(debug=True)
           