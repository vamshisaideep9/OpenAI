from io import BytesIO
from openai import OpenAI
client = OpenAI()

with open("image generation/cat_and_dog (1).png", "rb") as image_file:
    byte_stream = BytesIO(image_file.read())  #create a byteIO object
    byte_array = byte_stream.getvalue() #Get the binary data as a byte array
    #print(image_data)

# byte_stream: BytesIO = [image_data]
#byte_array = byte_stream.getvalue()
response = client.images.create_variation(
    image=byte_array,
    n=1,
    model="dall-e-2",
    size="1024x1024"
)

print(response.data[0].url)