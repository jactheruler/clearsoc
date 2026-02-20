from pydantic import BaseModel
from datetime import datetime

class SecurityEvent(BaseModel):
    timestamp: datetime
    source: str
    event_type: str
    severity: str
    message: str
