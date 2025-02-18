from fastapi import APIRouter

router = APIRouter(prefix = "/start_center")

@router.get("/")
async def get_start_center():
    return {"message": "Start Center"}
