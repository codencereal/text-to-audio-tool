import pdfplumber
from gtts import gTTS
import argparse

text = "This is just some test text to ensure that the gTTS package is working."

language = 'en'
gtts_transformer = gTTS(text=text, lang=language)
gtts_transformer.save("test.mp3")
print("File converted")