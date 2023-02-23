from dotenv import load_dotenv
import os

# Load the environment variables from the .env file
load_dotenv()


FRONTEND = os.getenv('FRONTEND_URL')
BACKEND = os.getenv('BACKEND_URL')

