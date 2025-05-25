# Import FastAPI Framework
from fastapi import FastAPI
# Import BaseModel for data validation
from pydantic import BaseModel
# Import model
from model.model import predict_sentiment

# Init FastAPI instance
app = FastAPI()

# Define the structure of the incoming request body using Pydantic
class Input(BaseModel):
    text: str # expects JSON body like {"text": "bakayaro konoyaro"}

# Define Endpoint
@app.post("/predict")
# function predict with params input (type data Input)
async def predict(input: Input):
    sentiment = predict_sentiment(input.text)
    # Return back the input
    return {"prediction": sentiment}
    # return {"prediction": f"Received: {input.text}"}