fastapi_project/
├── app/
│ ├── **init**.py
│ ├── main.py
│ ├── api/
│ │ ├── **init**.py
│ │ ├── v1/
│ │ │ ├── **init**.py
│ │ │ ├── endpoints/
│ │ │ │ ├── **init**.py
│ │ │ │ ├── users.py
│ │ │ │ ├── items.py
│ │ │ ├── routers.py
│ ├── core/
│ │ ├── **init**.py
│ │ ├── config.py
│ │ ├── database.py
│ │ ├── models/
│ │ │ ├── **init**.py
│ │ │ ├── user.py
│ │ │ ├── item.py
│ ├── schemas/
│ │ ├── **init**.py
│ │ ├── user.py
│ │ ├── item.py
│ ├── services/
│ │ ├── **init**.py
│ │ ├── user_service.py
│ │ ├── item_service.py
│ ├── dependencies/
│ │ ├── **init**.py
│ │ ├── auth.py
│ ├── middleware/
│ │ ├── **init**.py
│ │ ├── logging.py
│ ├── tests/
│ │ ├── **init**.py
│ │ ├── test_users.py
│ │ ├── test_items.py
├── .env
├── requirements.txt
├── README.md
├── Dockerfile
├── docker-compose.yml
