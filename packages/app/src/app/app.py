from io import StringIO
from math import isclose

import pandas as pd
from animal_shelter.model.predict import predict as predict_model
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, model_validator

app = FastAPI()


@app.get("/")
def read_root():
    return "Welcome to the Animal Shelter API!"


@app.get("/ping/")
def ping():
    return "pong"


class Prediction(BaseModel):
    name: str
    adoption: float
    died: float
    euthanasia: float
    return_to_owner: float
    transfer: float

    @model_validator(mode="after")
    def prediction_adds_to_1(self):
        assert isclose(
            sum(
                [
                    self.adoption,
                    self.died,
                    self.euthanasia,
                    self.return_to_owner,
                    self.transfer,
                ]
            ),
            1,
        )
        return self


@app.post("/predict/")
def predict(input: UploadFile = File()) -> list[Prediction]:
    """
    Endpoint definition to showcase how to generate a JSON response validated by Pydantic.
    """
    # In this case the input data is uploaded via the API
    # Alternatively, the data could be a reference to version-controlled data somewhere
    input_data = input.file

    # The model could be specified as env variable in the server (or as an API parameter)
    model_path = "./output/model.pkl"

    # Create predictions.
    predictions = predict_model(input_data, model_path).to_dict(orient="records")

    print(len(predictions))

    return predictions


@app.post("/predict_streaming/")
def predict_streaming(input: UploadFile = File()) -> StreamingResponse:
    """
    Endpoint definition to showcase how to stream output as .csv files.
    """

    input_data = input.file
    model_path = "./output/model.pkl"
    predictions = predict_model(input_data, model_path)
    response = _convert_df_to_response(predictions)
    return response


def _convert_df_to_response(df: pd.DataFrame) -> StreamingResponse:
    """Convert a DataFrame to CSV response."""
    stream = StringIO()
    df.to_csv(stream, index=False)
    response = StreamingResponse(iter([stream.getvalue()]), media_type="text/csv")
    return response
