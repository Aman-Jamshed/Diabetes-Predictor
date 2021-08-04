from pydantic import BaseModel
from typing import Optional

class Diabetes(BaseModel):
    Pregnancies: float
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI : float
    DiabetesPedigreeFunction: float	
    Age: float

    
class DiabetesResponse(BaseModel):
    Outcome : float
    Pregnancies: float
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float	
    Age: float