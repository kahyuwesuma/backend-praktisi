from fastapi import FastAPI as FAPI
from app.api.auth.router import router as auth_router
from app.api.private.router import router as private_router

app = FAPI()

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(private_router, prefix="/private", tags=["private"])
