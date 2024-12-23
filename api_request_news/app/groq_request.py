import os
from groq import Groq

GROQ_API_KEY = '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'

def get_type_of_event(text: str):
    client = Groq(
        api_key=GROQ_API_KEY,
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"Answer with one of three words: terrorism,"
                           f" historical, current. What type of event does the following text describe?\n{text}",
            }
        ],
        model="llama3-8b-8192",
    )

    return chat_completion.choices[0].message.content

def get_city_and_country(text: str):
    client = Groq(
        api_key=GROQ_API_KEY,
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"Answer me in the following format: City, Country, Lat, Lng\n"
                           f"In which city and country is it likely that the main story in the article took place?\n{text}",
            }

        ],
        model="llama3-8b-8192",
    )

    return chat_completion.choices[0].message.content