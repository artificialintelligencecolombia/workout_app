import os
import requests
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

APP_ID = os.environ.get('APP_ID')
API_KEY=os.environ.get('API_KEY')
BASE_URL = os.environ.get('BASE_NUTRITIONIX_URL')

# 
exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

nlp_excercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

params = {
    "query": exercise_text,
    "weight_kg": 55,
    "height_cm": 179,
    "age": 33
}