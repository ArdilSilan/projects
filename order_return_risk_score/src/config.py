import os
from dotenv import load_dotenv

load_dotenv()


DB_CONFIG = {
    "host": os.getenv("DB_HOST","localhost"),
    "port": os.getenv("DB_PORT","5432"),
    "user": os.getenv("DB_USER","your_user_name"),
    "password": os.getenv("DB_PASSWORD","your_password"),
    "dbname": os.getenv("DB_NAME","your_db_name")
}

MODEL_CONFIG = {
    "test_size": 0.2,
    "random_state": 42,
    "epochs": 100,
    
}

FEATURE_CONFIG ={
    'high_discount_threshold': 0.75,
    'low_amount_threshold': 0.25
}








