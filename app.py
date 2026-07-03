from fastapi import FastAPI

from schemas.input_schema import InternshipInput

from utils.model_loader import model
from utils.input_processor import prepare_input
from utils.predictor import predict_internship
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request



app = FastAPI(
    title="Internship Scam Detector"
)
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.get("/model-info")
def model_info():

    return {
        "total_features": len(model.feature_names_in_),
        "features": list(model.feature_names_in_)
    }


@app.post("/test")
def test(data: InternshipInput):

    df = prepare_input(data)

    return {
        "shape": df.shape,
        "columns": list(df.columns)
    }


@app.post("/predict")
def predict(data: InternshipInput):

    return predict_internship(data)