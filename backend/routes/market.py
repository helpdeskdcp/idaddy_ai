from fastapi import APIRouter
from backend.market.live_service import ws

router = APIRouter(
    prefix="/market",
    tags=["Market"],
)



@router.get("/live")
def live_market():

    return {
        "NIFTY": ws.get_tick("NIFTY"),
        "BANKNIFTY": ws.get_tick("BANKNIFTY"),
        "FINNIFTY": ws.get_tick("FINNIFTY"),
        "SENSEX": ws.get_tick("SENSEX"),
    }
