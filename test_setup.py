import os
import sys
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

print("Python version:", sys.version)
print("OPENAI_API_KEY is set:", "OPENAI_API_KEY" in os.environ)
