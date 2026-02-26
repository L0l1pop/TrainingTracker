from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from authx import AuthX, AuthXConfig
from passlib.context import CryptContext

from src.auth.models import User
from src.auth.schemas import UserRegister, UserLogin
from src.core.db import get_db
from src.core.security import security

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

@router.post("/signup")
async def register(
    data: UserRegister,
    db: AsyncSession = Depends(get_db),
):
    user = User(
        email = data.email,
        password=data.password,
        name = data.name,
    )

    db.add(user)
    await db.commit()
    
