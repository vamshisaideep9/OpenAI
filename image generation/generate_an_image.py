from openai import OpenAI
client = OpenAI()

response = client.images.generate(
    model="dall-e-3", #dall-e-2
    prompt="a white indian cat. I NEED to test how the tool works with extremely simple prompts. DO NOT add any detail, just use it AS-IS:",
    size="1024x1024", #1024x1792,  1792x1024
    quality="hd", #standard
    n=1,
)

image_url = response.data[0].url

print(image_url)