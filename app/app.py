from io import StringIO

import pandas as pd
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse

from animal_shelter.model.predict import predict as predict_model

app = FastAPI()

@app.get("/ping/")
def ping():
    return "pong"

@app.post("/predict/")
def predict(input: UploadFile = File()) -> StreamingResponse:
    """
    Endpoint definition to showcase how to stream output as .csv files.
    """

    # In this case the input data is uploaded via the API
    # Alternatively, the data could be a reference to version-controlled data somewhere
    input_data = input.file

    # The model could be specified as env variable in the server (or as an API parameter)
    model_path = "../output/model.pickle"

    # Create predictions.
    predictions = predict_model(input_data, model_path)

    response = _convert_df_to_response(predictions)
    return response


def _convert_df_to_response(df: pd.DataFrame) -> StreamingResponse:
    """Convert a DataFrame to CSV response."""
    stream = StringIO()
    df.to_csv(stream, index=False)
    response = StreamingResponse(iter([stream.getvalue()]), media_type="text/csv")
    return response
