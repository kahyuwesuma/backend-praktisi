# app/dependencies/verify_token.py
from jose import JWTError, jwt
from fastapi import Depends, HTTPException
from app.core.config import SECRET_KEY, ALGORITHM

def verify_token(token: str = Depends()):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    return username
