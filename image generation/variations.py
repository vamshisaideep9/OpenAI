from openai import OpenAI

client = OpenAI()

response = client.images.create_variation(
    model="dall-e-2",
    image=open("image generation/cat_and_dog (1).png", "rb"),
    n=1,
    size="1024x1024"
)

print(response.data[0].url)