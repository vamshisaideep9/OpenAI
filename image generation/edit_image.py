from openai import OpenAI

client = OpenAI()

response = client.images.generate(
    model="dall-e-3",
    image=open("sunlit_lounge.png", "rb"),
    mask=open("mask.png", "rb"),
    prompt="A sunlit indoor lounge area with a pool containing a flamingo.",
    n=1,
    size="1024x1024"
)

image_url = response.data[0].url

print(image_url)