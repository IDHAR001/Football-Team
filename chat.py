import os
from openai import OpenAI
from dotenv import load_dotenv
import google.generativeai as genai

def load_chat(llm, prompt):
    if llm == "Gemini":
        GOOGLE_API_KEY=load_dotenv('./.env')
        GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
        def chat(prompt):
            genai.configure(api_key=GOOGLE_API_KEY)
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(prompt)
            return response.text
        anwser = chat(prompt)
    
    elif llm == "Kimi" :
        MOONSHOT_API_KEY=load_dotenv('./.env')
        MOONSHOT_API_KEY=os.getenv('MOONSHOT_API_KEY')
        def chat(prompt):
            llm = OpenAI(
                api_key = MOONSHOT_API_KEY,
                base_url = "https://api.moonshot.cn/v1",
            )
            completion = llm.chat.completions.create(
                model = "moonshot-v1-8k",
                messages = [
                    {"role": "system", "content": "你是 idhar，一个提供足球阵容解决方案的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。"},
                    {"role": "user", "content": f"{prompt}"}
                ],
                temperature = 0.3,
            )
            return completion.choices[0].message.content
        anwser = chat(prompt)
        
    return anwser