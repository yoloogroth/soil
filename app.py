from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from joblib import load
import pathlib
from fastapi.middleware.cors import CORSMiddleware


origins = ["*"]

app = FastAPI(title = 'Soil Prediction')

app.add_middleware(
   CORSMiddleware,
   allow_origins=origins,
   allow_credentials=True,
   allow_methods=["*"],
   allow_headers=["*"]
)
model = load(pathlib.Path('model/soil_data-v1.joblib'))

class InputData(BaseModel):
    fips:float=1001
    lat:float=32.536382
    lon:float=-86.64449
    slope1:float=0.0419
    slope2:float=0.2788
   
    
  

class OutputData(BaseModel):
    score:float=0.80318881046519

@app.post('/score', response_model = OutputData)
def score(data:InputData):
    model_input = np.array([v for k,v in data.dict().items()]).reshape(1,-1)
    result = model.predict(model_input)

    return {'score':result}

