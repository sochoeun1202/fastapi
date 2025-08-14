#!/usr/bin/env python3
"""
Test script to verify MySQL connection and basic functionality
"""
import asyncio
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.core.database import test_connection, create_tables
from app.core.config import settings

def main():
    print("=== FastAPI MySQL Connection Test ===")
    print(f"Database Host: {settings.database_host}")
    print(f"Database Port: {settings.database_port}")
    print(f"Database Name: {settings.database_name}")
    print(f"Database User: {settings.database_user}")
    
    print("\n1. Testing database connection...")
    if test_connection():
        print("✅ Database connection successful!")
    else:
        print("❌ Database connection failed!")
        return
    
    print("\n2. Creating database tables...")
    try:
        create_tables()
        print("✅ Database tables created successfully!")
    except Exception as e:
        print(f"❌ Failed to create tables: {e}")
        return
    
    print("\n✅ All tests passed! Your FastAPI MySQL setup is ready!")
    print("\nNext steps:")
    print("1. Run the application: uvicorn app.main:app --reload")
    print("2. Open http://localhost:8000/docs to view the API documentation")
    print("3. Test the endpoints using the interactive documentation")

if __name__ == "__main__":
    main()
