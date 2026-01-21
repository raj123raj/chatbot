import streamlit as st
import google.generativeai as genai
import pathlib
import textwrap
from IPython.display import display
from IPython.display import Markdown
import PIL.Image
import urllib.request 
from PIL import Image

GOOGLE_API_KEY = "AIzaSyB0s4jeiEXu1CgxNuyiosibCB2mJxgd8sk"
genai.configure(api_key=GOOGLE_API_KEY)

## function to load Gemini Pro model and get repsonses
model = genai.GenerativeModel('gemini-pro-vision')

image = PIL.Image.open('friendscast.jpg')
image
def to_markdown(text):
    text = text.replace("•", "  *")
    print(text)
    return Markdown(textwrap.indent(text, "> ", predicate=lambda _: True))
# response = model.generate_content(image)
# to_markdown(response.text)

response = model.generate_content(
    ["Write an explanation based on the image", image],
    stream=True
)
#print("before printing")
#print(response)
response.resolve()
#print("after resolving")
to_markdown(response.text)
  

# cookie_picture = {
#     'mime_type': 'image/jpg',
#     'data': pathlib.Path('marie.jpg').read_bytes(),
# }
# prompt = "Give me the required information:"

# response = model.generate_content(
#     contents=[prompt, cookie_picture],
# )
# print(response.text)