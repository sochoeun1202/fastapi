from pydantic_settings import BaseSettings
from pydantic import ConfigDict
from typing import Optional

class Settings(BaseSettings):
    model_config = ConfigDict(
        env_file=".env",
        case_sensitive=False,
        extra='allow'
    )
    
    # Database settings
    database_host: str
    database_port: int = 3306
    database_user: str
    database_password: str
    database_name: str
    
    # Application settings
    app_name: str = "FastAPI MySQL Demo"
    app_version: str = "1.0.0"
    debug: bool = True
    
    # Security settings
    secret_key: str = "your-secret-key-change-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    @property
    def database_url(self) -> str:
        """Construct database URL from components"""
        return f"mysql+pymysql://{self.database_user}:{self.database_password}@{self.database_host}:{self.database_port}/{self.database_name}"

# Create global settings instance
settings = Settings()
