#from app import app
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.app import app

def test_home_page():
    tester = app.test_client()
    response = tester.get("/")
    assert response.status_code == 200