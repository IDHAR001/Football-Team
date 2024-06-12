import pathlib
import google.generativeai as genai
import os
from dotenv import load_dotenv

GOOGLE_API_KEY=load_dotenv('./.env')
# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')

def chat(prompt):
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    return response.text