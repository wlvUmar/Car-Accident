import logging
from fastapi import FastAPI, Request
from utils import *
import cloudpickle


setup_logging()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

app = FastAPI()

@app.on_event("startup")
async def startup_event():
	logger.info("Loading the model...")
	try:
		with open("utils/xgb_full_pipeline.pkl", "rb") as f:
			app.state.model = cloudpickle.load(f)
			logger.info("Model Loaded!")

	except Exception as e:
		logger.error(f"Failed To load the model:\n {e}", exc_info=True)

@app.post('/predict', response_model=PredictionResponse)
async def predict(request:Request, features: AccidentFeatures):
    model = request.app.state.model
    try:
        prediction = await predict_severity(features, model)
    except RuntimeError as e:
        prediction = None
        return PredictionResponse(error=str(e), msg="Failed to predict")    
    return PredictionResponse(severity=prediction) 
    
