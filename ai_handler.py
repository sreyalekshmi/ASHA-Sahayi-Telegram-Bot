
from groq import Groq
from deep_translator import GoogleTranslator
from langdetect import detect

client = Groq(api_key=GROQ_API_KEY)

SYSTEM_PROMPT = """
You are a healthcare assistant supporting ASHA workers in India.

Rules:
- Provide only general health guidance
- Do NOT prescribe medicines or dosages
- Avoid diagnosis
- Use simple, safe explanations
- Encourage consulting a doctor when symptoms persist
"""

def translate_to_english(text):
    return GoogleTranslator(source="auto", target="en").translate(text)

def translate_to_malayalam(text):
    return GoogleTranslator(source="en", target="ml").translate(text)

def get_ai_reply(user_input):
    try:
        lang = detect(user_input)

        # Malayalam → English
        if lang == "ml":
            user_input_en = translate_to_english(user_input)
        else:
            user_input_en = user_input

        # GenAI reasoning
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input_en}
            ],
            temperature=0.3
        )

        answer_en = response.choices[0].message.content.strip()

        # English → Malayalam
        if lang == "ml":
            return translate_to_malayalam(answer_en)

        return answer_en

    except Exception as e:
        print("AI ERROR:", e)
        return "ക്ഷമിക്കണം, ഇപ്പോൾ മറുപടി നൽകാൻ കഴിയുന്നില്ല."




