# Car Accident Severity Prediction API

## Setup

1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

2. Train the model:
   - Use the provided notebook to preprocess data and train an XGBoost model.

3. Run the FastAPI server:
   ```bash
   uvicorn main:app 
   ```

## API Usage

- **POST** `/predict`
  - Request body: JSON with required features
  - Response: `{ "severity": int, "error": str, "msg" : str }`

Example request:
```json
{
  "Calculation1": "Remaining",
  "City": "New York",
  "Side": "R",
  "State": "NY",
  "Wind_Direction": "SE",
  "Weather_Condition": "Heavy Snow",
  "Sunrise_Sunset": "Night",
  "Start_Time": "01/05/2022 06:45:00 AM",
  "Temperature_F": 20.0,
  "Visibility_mi": 0.5,
  "Pressure_in": 28.8,
  "Wind_Speed_mph": 15.0,
  "Humidity": 95.0,
  "Lat": 40.7128,
  "Lng": -74.0060,
  "Amenity": true,
  "Bump": true,
  "Traffic_Calming": true,
  "Crossing": true,
  "Junction": true,
  "Stop": true,
  "Traffic_Signal": true,
  "Give_Way": true,
  "No_Exit": true,
  "Railway": true,
  "Roundabout": true,
  "Station": true
}

``` 
