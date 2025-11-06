from pydantic import BaseModel
import datetime
class Rooms(BaseModel):
    room_id: int
    date_from: datetime
    date_to: datetime
    online: bool