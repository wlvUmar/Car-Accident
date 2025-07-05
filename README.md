# Car Accident Severity Prediction API

## Setup

1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

2. Train the model:
   - Use the provided notebook to preprocess data and train an XGBoost model.
   - Save the model as `xgb_model.pkl` in the project root:
     ```python
     import joblib
     joblib.dump(model, 'xgb_model.pkl')
     ```

3. Run the FastAPI server:
   ```bash
   uvicorn main:app 
   ```

## API Usage

- **POST** `/predict`
  - Request body: JSON with required features
  - Response: `{ "severity": int }`

Example request:
```json
{
  "Calculation1": "value",
  "City": "value",
  "Side": "value",
  "State": "value",
  "Sunrise_Sunset": "value",
  "Weather_Condition": "value",
  "Wind_Direction": "value",
  "Start_Time": "2023-01-01 12:00:00",
  "Temperature_F": 70.0,
  "Visibility_mi": 10.0,
  "Humidity": 50.0,
  "Pressure_in": 30.0,
  "Wind_Speed_mph": 5.0,
  "Lat": 34.0,
  "Lng": -118.0
}
``` 