from openai import OpenAI
import base64
import copykitten
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv
import os

system_prompt = '''
Please answer question in this image. Response shouldn't be like an AI assistant; just answer is enough.
DO NOT use markdown format while answering, use - for lists only if needed.
Just leave space after headings, DON'T USE #,*,_,"," for formating.
Write answer accouding to the marks of the question.
'''


load_dotenv(dotenv_path='.env', override=True)

# Code of your application, which uses environment variables (e.g. from `os.environ` or
# `os.getenv`) as if they came from the actual environment.

API_KEY = os.getenv("OPENAI_API_KEY")



# Function to get image from clipboard and encode it as a base64 string
def get_image_from_clipboard():
    pixels, width, height = copykitten.paste_image()
    image = Image.frombytes(mode="RGBA", size=(width, height), data=pixels)
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode('utf-8')

# Function to get response from OpenAI Vision API for an image
def openai_image_response(api_key):
    # Get the base64-encoded image from clipboard
    base64_image = get_image_from_clipboard()

    # Initialize OpenAI client
    client = OpenAI(api_key=api_key)

    # Send image and prompt to OpenAI's Vision model
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": system_prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{base64_image}",
                        },
                    },
                ],
            }
        ],
        max_tokens=300,
    )

    # Extract and copy the response
    result = response.choices[0].message.content
    if result is None:
        result = "Oops, something went wrong."
    
    # Copy the result to the clipboard
    copykitten.copy(result)
    print("Response copied to clipboard:", result)

if __name__ == "__main__":
    # Get and process the image response
    openai_image_response(API_KEY)
