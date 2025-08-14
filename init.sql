-- Initialize the database with required tables and sample data

USE testdb;

-- Create users table
CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    full_name VARCHAR(100),
    hashed_password VARCHAR(255) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    is_admin BOOLEAN DEFAULT FALSE,
    bio TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Create indexes for better performance
CREATE INDEX idx_users_username ON users(username);
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_active ON users(is_active);
CREATE INDEX idx_users_created_at ON users(created_at);

-- Insert sample admin user (password is 'admin123!')
-- Hash generated with: python -c "from passlib.context import CryptContext; pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto'); print(pwd_context.hash('admin123!'))"
INSERT IGNORE INTO users (username, email, full_name, hashed_password, is_active, is_admin, bio) VALUES 
(
    'admin',
    'admin@example.com',
    'System Administrator',
    '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LeblT17NdV/dKy2XK',
    TRUE,
    TRUE,
    'Default system administrator account'
);

-- Insert sample regular user (password is 'user123!')
-- Hash generated with the same method as above
INSERT IGNORE INTO users (username, email, full_name, hashed_password, is_active, is_admin, bio) VALUES 
(
    'testuser',
    'test@example.com',
    'Test User',
    '$2b$12$8k3H9D4MvQW6YjJ5JcG8E.rN1yZ2QKpL7vX8F9MnP4Q6R5S3T7U1V',
    TRUE,
    FALSE,
    'Sample test user account'
);

-- Display the created tables
SHOW TABLES;
