from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import List, Optional
from passlib.context import CryptContext
from app.core.models.user import User
from app.schemas.user import UserCreate, UserUpdate
import logging

logger = logging.getLogger(__name__)

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserService:
    @staticmethod
    def hash_password(password: str) -> str:
        """Hash a password"""
        return pwd_context.hash(password)
    
    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """Verify a password against its hash"""
        return pwd_context.verify(plain_password, hashed_password)
    
    @staticmethod
    def create_user(db: Session, user_data: UserCreate) -> Optional[User]:
        """Create a new user"""
        try:
            # Hash the password
            hashed_password = UserService.hash_password(user_data.password)
            
            # Create user object
            db_user = User(
                username=user_data.username,
                email=user_data.email,
                full_name=user_data.full_name,
                bio=user_data.bio,
                hashed_password=hashed_password,
                is_active=user_data.is_active,
                is_admin=user_data.is_admin
            )
            
            db.add(db_user)
            db.commit()
            db.refresh(db_user)
            
            logger.info(f"User created successfully: {user_data.username}")
            return db_user
            
        except IntegrityError as e:
            db.rollback()
            logger.error(f"User creation failed - duplicate entry: {e}")
            return None
        except Exception as e:
            db.rollback()
            logger.error(f"User creation failed: {e}")
            return None
    
    @staticmethod
    def get_user_by_id(db: Session, user_id: int) -> Optional[User]:
        """Get user by ID"""
        return db.query(User).filter(User.id == user_id).first()
    
    @staticmethod
    def get_user_by_username(db: Session, username: str) -> Optional[User]:
        """Get user by username"""
        return db.query(User).filter(User.username == username).first()
    
    @staticmethod
    def get_user_by_email(db: Session, email: str) -> Optional[User]:
        """Get user by email"""
        return db.query(User).filter(User.email == email).first()
    
    @staticmethod
    def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[User]:
        """Get list of users"""
        return db.query(User).offset(skip).limit(limit).all()
    
    @staticmethod
    def update_user(db: Session, user_id: int, user_data: UserUpdate) -> Optional[User]:
        """Update user"""
        try:
            db_user = db.query(User).filter(User.id == user_id).first()
            if not db_user:
                return None
            
            # Update fields if provided
            update_data = user_data.dict(exclude_unset=True)
            
            # Handle password hashing if password is being updated
            if 'password' in update_data:
                update_data['hashed_password'] = UserService.hash_password(update_data.pop('password'))
            
            for field, value in update_data.items():
                setattr(db_user, field, value)
            
            db.commit()
            db.refresh(db_user)
            
            logger.info(f"User updated successfully: {user_id}")
            return db_user
            
        except IntegrityError as e:
            db.rollback()
            logger.error(f"User update failed - duplicate entry: {e}")
            return None
        except Exception as e:
            db.rollback()
            logger.error(f"User update failed: {e}")
            return None
    
    @staticmethod
    def delete_user(db: Session, user_id: int) -> bool:
        """Delete user"""
        try:
            db_user = db.query(User).filter(User.id == user_id).first()
            if not db_user:
                return False
            
            db.delete(db_user)
            db.commit()
            
            logger.info(f"User deleted successfully: {user_id}")
            return True
            
        except Exception as e:
            db.rollback()
            logger.error(f"User deletion failed: {e}")
            return False
    
    @staticmethod
    def authenticate_user(db: Session, username: str, password: str) -> Optional[User]:
        """Authenticate user"""
        user = UserService.get_user_by_username(db, username)
        if not user:
            return None
        
        if not UserService.verify_password(password, user.hashed_password):
            return None
        
        return user
