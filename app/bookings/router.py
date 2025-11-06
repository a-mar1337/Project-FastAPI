from fastapi import APIRouter, Depends
from sqlalchemy import select
from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBookings
from app.database import async_session_maker
from app.bookings.schemas import SBookings
from app.users.dependencies import get_current_user
from app.users.models import Users


router = APIRouter(
    prefix = "/bookings",
    tags = ["бронирования"]
)

@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)): #-> list[SBookings]:
    return await BookingDAO.find_all(user_id=1)

    
 

