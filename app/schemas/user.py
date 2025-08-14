from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

# Base schema
class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    full_name: Optional[str] = Field(None, max_length=100)
    bio: Optional[str] = None
    is_active: bool = True
    is_admin: bool = False

# Schema for creating a user
class UserCreate(UserBase):
    password: str = Field(..., min_length=6, max_length=100)

# Schema for updating a user
class UserUpdate(BaseModel):
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    email: Optional[EmailStr] = None
    full_name: Optional[str] = Field(None, max_length=100)
    bio: Optional[str] = None
    is_active: Optional[bool] = None
    is_admin: Optional[bool] = None
    password: Optional[str] = Field(None, min_length=6, max_length=100)

# Schema for user response (what gets returned to client)
class UserResponse(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

# Schema for user login
class UserLogin(BaseModel):
    username: str
    password: str

# Schema for user in database (includes password hash)
class UserInDB(UserBase):
    id: int
    hashed_password: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True
