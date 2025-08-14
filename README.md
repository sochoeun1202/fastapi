# FastAPI MySQL Project

A complete FastAPI application with MySQL database integration, featuring user management, authentication, and CRUD operations.

## Features

- 🚀 **FastAPI** - Modern, fast web framework for building APIs
- 🐬 **MySQL** - Robust relational database with PyMySQL driver
- 🔐 **Environment Variables** - Secure configuration management
- 📊 **SQLAlchemy ORM** - Powerful database toolkit and ORM
- 🔒 **Password Hashing** - Secure password storage with bcrypt
- 📝 **Pydantic Validation** - Data validation and serialization
- 📚 **API Documentation** - Auto-generated interactive docs
- 🧪 **Connection Testing** - Database connectivity verification

## Project Structure

```
D:\python\fastapi/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application entry point
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routers.py       # Main API router configuration
│   │   └── endpoint/
│   │       ├── __init__.py
│   │       └── users.py     # User-related endpoints
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py        # Application configuration
│   │   ├── database.py      # Database connection and setup
│   │   └── models/
│   │       ├── __init__.py
│   │       └── user.py      # User database model
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── user.py          # Pydantic schemas for API
│   └── services/
│       ├── __init__.py
│       └── user_service.py  # Business logic for users
├── venv/                    # Virtual environment
├── .env                     # Environment variables (not in git)
├── .env.example            # Environment variables template
├── .gitignore              # Git ignore rules
├── requirements.txt        # Python dependencies
├── test_connection.py      # Database connection test
└── README.md              # This file
```

## Quick Start

### Option 1: Docker (Recommended)

#### Prerequisites
- Docker and Docker Compose
- Git (optional)

#### Installation
```bash
# Clone or navigate to the project directory
cd D:\python\fastapi

# Start all services with Docker
docker-compose up -d

# Or use the management script (Windows)
.\docker-manage.ps1 up
```

The application will be available at:
- **FastAPI**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **phpMyAdmin**: http://localhost:8080 (admin tools)

#### Docker Management
```bash
# Build the image
docker-compose build

# Start services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Access database
docker-compose exec mysql mysql -u dev -pdev123! testdb

# Access app container
docker-compose exec web bash
```

### Option 2: Local Development

#### Prerequisites
- Python 3.8+
- MySQL Server
- Virtual Environment (recommended)

#### Installation

```bash
# Clone or navigate to the project directory
git clone https://github.com/sochoeun1202/fastapi.git ; cd fastapi

# Activate virtual environment
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

### 3. Database Configuration

Create a `.env` file with your MySQL database credentials:

```env
DATABASE_HOST=your_mysql_host
DATABASE_PORT=3306
DATABASE_USER=your_username
DATABASE_PASSWORD=your_password
DATABASE_NAME=your_database_name
DEBUG=true
```

> **Note**: Use the provided `.env.example` as a template. Never commit your actual `.env` file to version control.

### 4. Test Database Connection

```bash
python test_connection.py
```

This will verify:

- ✅ Database connection is working
- ✅ Database tables are created
- ✅ Configuration is loaded correctly

### 5. Run the Application

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The application will be available at:

- **API**: http://localhost:8000
- **Interactive Docs**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## API Endpoints

### Core Endpoints

- `GET /` - Welcome message and API info
- `GET /info` - Application information
- `GET /api/v1/health` - Health check

### User Management

- `POST /api/v1/users/` - Create a new user
- `GET /api/v1/users/` - Get list of users (with pagination)
- `GET /api/v1/users/{user_id}` - Get user by ID
- `PUT /api/v1/users/{user_id}` - Update user
- `DELETE /api/v1/users/{user_id}` - Delete user
- `POST /api/v1/users/login` - User authentication
- `GET /api/v1/users/username/{username}` - Get user by username

## Environment Variables

| Variable            | Description              | Required | Default |
| ------------------- | ------------------------ | -------- | ------- |
| `DATABASE_HOST`     | MySQL server hostname/IP | Yes      | -       |
| `DATABASE_PORT`     | MySQL server port        | No       | 3306    |
| `DATABASE_USER`     | MySQL username           | Yes      | -       |
| `DATABASE_PASSWORD` | MySQL password           | Yes      | -       |
| `DATABASE_NAME`     | MySQL database name      | Yes      | -       |
| `DEBUG`             | Enable debug mode        | No       | true    |

## Database Schema

### Users Table

```sql
CREATE TABLE users (
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
```

## Example Usage

### Create a User

```bash
curl -X POST "http://localhost:8000/api/v1/users/" \
     -H "Content-Type: application/json" \
     -d '{
       "username": "johndoe",
       "email": "john@example.com",
       "full_name": "John Doe",
       "password": "securepassword123"
     }'
```

### Get Users List

```bash
curl "http://localhost:8000/api/v1/users/?skip=0&limit=10"
```

### User Login

```bash
curl -X POST "http://localhost:8000/api/v1/users/login" \
     -H "Content-Type: application/json" \
     -d '{
       "username": "johndoe",
       "password": "securepassword123"
     }'
```

### Get User by ID

```bash
curl "http://localhost:8000/api/v1/users/1"
```

## Development

### Running Tests

```bash
python test_connection.py
```

### Code Style

The project follows Python best practices and uses:

- Type hints for better code documentation
- Pydantic for data validation
- SQLAlchemy for database operations
- Secure password hashing with bcrypt

### Project Dependencies

Key dependencies from `requirements.txt`:

- `fastapi` - Web framework
- `uvicorn` - ASGI server
- `sqlalchemy` - Database ORM
- `pymysql` - MySQL driver
- `pydantic` - Data validation
- `python-dotenv` - Environment variables
- `passlib[bcrypt]` - Password hashing
- `email-validator` - Email validation

## Security Features

- 🔐 **Password Hashing**: Passwords are securely hashed using bcrypt
- 🔒 **Environment Variables**: Sensitive data stored securely
- 🛡️ **SQL Injection Protection**: SQLAlchemy ORM prevents SQL injection
- 📋 **Input Validation**: Pydantic schemas validate all input data
- 🚫 **CORS Configuration**: Configurable CORS settings

## Troubleshooting

### Database Connection Issues

1. **Verify MySQL server is running**

   ```bash
   # Check if MySQL service is running
   net start mysql  # Windows
   ```

2. **Check database credentials in `.env` file**

   - Ensure all required variables are set
   - Verify credentials are correct

3. **Ensure database exists and user has proper permissions**

   ```sql
   -- Create database if it doesn't exist
   CREATE DATABASE IF NOT EXISTS testdb;

   -- Grant permissions to user
   GRANT ALL PRIVILEGES ON testdb.* TO 'dev'@'%';
   FLUSH PRIVILEGES;
   ```

4. **Test connection**
   ```bash
   python test_connection.py
   ```

### Common Errors

| Error                   | Cause                                                   | Solution                                                |
| ----------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `"Unknown column"`      | Database table doesn't exist or has different structure | Run `python test_connection.py` to create tables        |
| `"Access denied"`       | Wrong database credentials                              | Check `.env` file credentials                           |
| `"Connection refused"`  | MySQL server not running                                | Start MySQL server                                      |
| `"ValidationError"`     | Missing environment variables                           | Check `.env` file exists and has all required variables |
| `"ModuleNotFoundError"` | Missing dependencies                                    | Run `pip install -r requirements.txt`                   |

### Debug Mode

To enable detailed logging, set `DEBUG=true` in your `.env` file. This will:

- Show SQL queries in console
- Enable detailed error messages
- Provide request/response logging

## Production Deployment

For production deployment:

1. **Environment Configuration**

   ```env
   DEBUG=false
   DATABASE_HOST=production-mysql-host
   SECRET_KEY=your-production-secret-key
   ```

2. **Security Settings**

   - Use strong, unique passwords
   - Enable HTTPS
   - Configure proper CORS settings
   - Set up firewall rules

3. **Performance**

   - Use a production ASGI server (e.g., Gunicorn with Uvicorn workers)
   - Configure database connection pooling
   - Enable caching where appropriate

4. **Monitoring**
   - Set up application logging
   - Monitor database performance
   - Configure health check endpoints

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test your changes thoroughly
5. Commit your changes (`git commit -m 'Add some amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## License

This project is for demonstration purposes. Feel free to modify and use it according to your needs.

## Support

If you encounter any issues or have questions:

1. Check the troubleshooting section above
2. Review the error logs
3. Test database connection with `python test_connection.py`
4. Verify all environment variables are correctly set

---

**Built with ❤️ using FastAPI and MySQL**
