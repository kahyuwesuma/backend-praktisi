from fastapi import APIRouter
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies import get_db, verify_token
from app.models import User
from app.security import create_access_token

router = APIRouter()

@router.post("/token")
async def login_for_access_token(form_data: dict = Depends()):
    db = Session()
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not user.verify_password(form_data.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_access_token(data={"sub": form_data.username})
    return {"access_token": token, "token_type": "bearer"}
