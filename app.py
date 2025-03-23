from flask import Flask,request,render_template
import numpy as np
import pandas as pd
from src.pipeline.predict_pipeline import *

application=Flask(__name__)

app=application


@app.route('/',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        age = int(request.form.get('age', 0))
        sex = int(request.form.get('sex', 0))
        cp = int(request.form.get('cp', 0))
        trestbps=int(request.form.get('trestbps', 0))
        chol = int(request.form.get('chol', 0))
        fbs = int(request.form.get('fbs', 0))
        restecg = float(request.form.get('restecg', 0.0))
        thalach = float(request.form.get('thalach', 0.0))
        exang = float(request.form.get('exang', 0.0))
        oldpeak = float(request.form.get('oldpeak', 0.0))
        ca = int(request.form.get('ca', 0))
        slope = int(request.form.get('slope', 0))
        thal = int(request.form.get('thal', 0))

        # Create a DataFrame directly from the form data
        pred_df = pd.DataFrame([[age, sex, cp,trestbps, chol, fbs, restecg, thalach, exang, oldpeak, ca, slope, thal]], 
                                columns=['age', 'sex', 'cp','trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'ca', 'slope', 'thal'])
        
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=predict_pip()
        print("Mid Prediction")
        results=predict_pipeline.predict1(pred_df)
        print("after Prediction")
        d = {0:"no heart disease",1:"heart disease"}
        return render_template('home.html',results=d[results[0]])
    

if __name__=="__main__":
    app.run(debug = True,host="0.0.0.0",port = 5000)        