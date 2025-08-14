from fastapi import APIRouter
from app.api.endpoint import users

# Create the main API router
api_router = APIRouter()

# Include user routes
api_router.include_router(
    users.router,
    prefix="/users",
    tags=["users"]
)

# Health check endpoint
@api_router.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "message": "API is running"}
