import os
from openai import OpenAI
from dotenv import load_dotenv

MOONSHOT_API_KEY = load_dotenv('./.env')


llm = OpenAI(
    api_key = os.environ[f'MOONSHOT_API_KEY'],
    base_url = "https://api.moonshot.cn/v1",
)

def chat(prompt):
    completion = llm.chat.completions.create(
        model = "moonshot-v1-8k",
        messages = [
            {"role": "system", "content": "你是 idhar，一个提供足球阵容解决方案的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。"},
            {"role": "user", "content": f"{prompt}"}
        ],
        temperature = 0.3,
    )
    return completion.choices[0].message.content