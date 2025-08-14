from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.api.routers import api_router
from app.core.database import create_tables, test_connection
from app.core.config import settings
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="FastAPI application with MySQL integration",
    debug=settings.debug
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure this for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(api_router, prefix="/api/v1")

@app.on_event("startup")
async def startup_event():
    """Initialize database on startup"""
    logger.info("Starting up...")
    
    # Test database connection
    if not test_connection():
        logger.error("Failed to connect to database")
        raise HTTPException(status_code=500, detail="Database connection failed")
    
    # Create database tables
    try:
        create_tables()
        logger.info("Database tables created/verified")
    except Exception as e:
        logger.error(f"Failed to create tables: {e}")
        raise HTTPException(status_code=500, detail="Failed to initialize database")

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to the FastAPI MySQL project!",
        "app_name": settings.app_name,
        "version": settings.app_version,
        "docs_url": "/docs",
        "health_check": "/api/v1/health"
    }

@app.get("/info")
async def app_info():
    """Application information"""
    return {
        "app_name": settings.app_name,
        "version": settings.app_version,
        "database_host": settings.database_host,
        "database_port": settings.database_port,
        "database_name": settings.database_name
    }
