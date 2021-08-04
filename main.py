import pandas as pd
from fastapi import FastAPI
from schemas import Diabetes,DiabetesResponse
import uvicorn

app = FastAPI()

@app.get('/')
def index():
    return {"detail":"please make a post request to /predict"}


@app.post('/predict/',response_model=DiabetesResponse)
def predict(request : Diabetes):
    
    data = dict(request)
    
    Pregnancies = request.Pregnancies
    Glucose = request.Glucose
    BloodPressure = request.BloodPressure
    SkinThickness = request.SkinThickness
    Insulin = request.Insulin
    BMI = request.BMI
    DiabetesPedigreeFunction = request. DiabetesPedigreeFunction
    Age = request.Age
    scale = pd.read_pickle('model/scale.pkl')
    temp = []
    columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin','BMI','DiabetesPedigreeFunction','Age']
    for i in columns:
        temp.append(data[i])
    x = [temp]
    new_data = scale.transform (x)
    #print(new_data)

    Pregnancies = new_data[0][0]
    Glucose= new_data[0][1]
    BloodPressure = new_data[0][2]
    SkinThickness = new_data[0][3]
    Insulin = new_data[0][4]
    BMI = new_data[0][5]
    DiabetesPedigreeFunction = new_data[0][6]
    Age = new_data[0][7]


    model = pd.read_pickle('model/model.pkl')
    
    Outcome = model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    classification = Outcome[0]
    #print(classification)
    data['Outcome'] = classification
    return data
    # return data


if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=9000)