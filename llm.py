import os
from openai import OpenAI
from dotenv import load_dotenv

MOONSHOT_API_KEY = load_dotenv('./.env')


llm = OpenAI(
    api_key = os.environ[f'MOONSHOT_API_KEY'],
    base_url = "https://api.moonshot.cn/v1",
    temperature = 0.3
)