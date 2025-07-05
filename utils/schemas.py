from pydantic import BaseModel
from typing import Optional

class AccidentFeatures(BaseModel):
    Calculation1: str
    City: str
    Side: str
    State: str
    Wind_Direction: str
    Weather_Condition: str
    Sunrise_Sunset: str
    Start_Time: str  

    Temperature_F: float
    Visibility_mi: float
    Pressure_in: float
    Wind_Speed_mph: float
    Humidity: float

    Lat: float  
    Lng: float

    Amenity: bool = False
    Bump: bool = False
    Traffic_Calming: bool = False
    Crossing: bool = False
    Junction: bool = False
    Stop: bool = False
    Traffic_Signal: bool = False

    Give_Way: bool = False
    No_Exit: bool = False
    Railway: bool = False
    Roundabout: bool = False
    Station: bool = False

class PredictionResponse(BaseModel):
    severity: Optional[int] = None  
    error: Optional[str] = None     
    msg: Optional[str] = None      