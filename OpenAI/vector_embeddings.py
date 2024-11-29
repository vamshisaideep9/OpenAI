import openai
from dotenv import dotenv_values
config = dotenv_values()
openai.api_key = config["OPENAI_API_KEY"]

response = openai.embeddings.create(
    model="text-embedding-3-large",
    input="The food was delicious and the waiter..."
)

print(response)