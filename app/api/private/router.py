from fastapi import APIRouter, Depends
from app.dependencies import verify_token

router = APIRouter()

@router.get("/private")
async def get_private_data(current_user: str = Depends(verify_token)):
    return {"message": f"Hello {current_user}, this is private data!"}
