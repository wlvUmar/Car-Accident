import logging
import pandas as pd

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

async def preprocess_input(data: dict):
    df = pd.DataFrame([data])

    df.rename(columns={
        'Lat': 'Start_Lat',
        'Lng': 'Start_Lng',
        'Temperature_F': 'Temperature(F)',
        'Visibility_mi': 'Visibility(mi)',
        'Pressure_in': 'Pressure(in)',
        'Wind_Speed_mph': 'Wind_Speed(mph)',
        'Humidity': 'Humidity(%)'
    }, inplace=True)

    return df



async def predict_severity(features, model):
    if model:
        df = await preprocess_input(features.dict())
        logger.debug(df)
        try:
            pred = model.predict(df)
            return int(pred[0])
        except Exception as e:
            logger.error(f"Prediction error: {e}", exc_info=True)
            raise RuntimeError("Model prediction failed:", {"msg": e})
    else:
        logger.warning("Model not loaded")
        return None