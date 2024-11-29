import openai

response = openai.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role":"system",
            "content": [
                {
                    "type":"text",
                    "text":"You are a helpful assistant that answers programming questions in the indian style."
      
                }
            ]
        },
        {
            "role": "user",
            "content": [
                {
                "type":"text",
                "text":"Are semicolons optioanl in javascript?"
                }
            ]
        }
    ]
)

print(response.choices[0].message)
   