from dotenv import dotenv_values
import openai

config = dotenv_values()

openai.api_key = config["OPENAI_API_KEY"]

completion = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Tell me about yourself in detail."
        }
    ]
)

print(completion.choices[0].message)
