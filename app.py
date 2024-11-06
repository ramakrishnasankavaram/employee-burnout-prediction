import pickle
from flask import Flask,request,jsonify,render_template
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


app=Flask(__name__)

##import ridge regressor and standard scaler pickle
linear_model=pickle.load(open('models/lr.pkl','rb'))
standard_scaler=pickle.load(open('models/scaler.pkl','rb'))


@app.route('/',methods=['GET','POST'])
def predict():
     if request.method=='POST':
          Gender=request.form.get('Gender')
          Company_Type=request.form.get('Company Type')
          WFH_Setup_Available=request.form.get('WFH Setup Available')
          Designation=request.form.get('Designation')
          Resource_Allocation=request.form.get('Resource Allocation')
          Mental_Fatigue_Score=request.form.get('Mental Fatigue Score')
          Tenure=request.form.get('Tenure')


          new_data_scaled=standard_scaler.transform([[Gender,Company_Type,WFH_Setup_Available,Designation,Resource_Allocation,Mental_Fatigue_Score,Tenure]])
          result=linear_model.predict(new_data_scaled)

          return render_template('home.html',results=result[0])
     else:
          return render_template('home.html')


if __name__=="__main__":
     app.run(debug=True,host="0.0.0.0",port=5000)