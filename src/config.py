from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
model_name = os.getenv("MODEL_NAME")
environment = os.getenv("ENVIRONMENT")