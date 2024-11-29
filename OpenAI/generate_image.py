import openai
from dotenv import dotenv_values

config = dotenv_values()

openai.api_key = config["OPENAI_API_KEY"]


response = openai.images.generate(
    prompt="Monkey D luffy image with fire background, he looks very angry, activating gear 2",
    n=2,
    size="1024x1024"
)

print(response.data[0].url)