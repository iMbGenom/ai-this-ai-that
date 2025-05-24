# Import FastAPI Framework
from fastapi import FastAPI
# Import BaseModel for data validation
from pydantic import BaseModel

# Init FastAPI instance
app = FastAPI()

# Define the structure of the incoming request body using Pydantic
class Input(BaseModel):
    text: str # expects JSON body like {"text": "bakayaro konoyaro"}

# Define Endpoint
@app.post("/predict")
# function predict with params input (type data Input)
async def predict(input: Input):
    # Return a back the f input
    return {"prediction": f"Received: {input.text}"}