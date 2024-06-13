def load_llm(selected_llm):
    llm = None

    if selected_llm == "Gemini":
        llm = "Gemini"

    elif selected_llm == "Kimi":
        llm = "Kimi"
        
    return llm   