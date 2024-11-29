import openai

repsonse = openai.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role":"user",
            "content": [
                {
                    "type":"text",
                    "text": "Knock Knock."
                }
            ]
        },
        {
            "role": "assistant",
            "content": [
                {
                    "type":"text",
                    "text": "Who's There?"
                }
            ]
        },
        {
            "role":"user",
            "content": [
                {
                    "type":"text",
                    "text": "orange. "
                }
            ]
        }
    ]

)

print(repsonse.choices[0].message)