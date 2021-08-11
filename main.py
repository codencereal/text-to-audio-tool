import pdfplumber
from gtts import gTTS
import argparse

parser = argparse.ArgumentParser(description='Convert a book or text file into a text to speech audiobook')
parser.add_argument('-t', '--text', metavar='', help='text to be converted to audio')
args = parser.parse_args()

text = args.text
print("Text extracted!")

language = 'en'
gtts_transformer = gTTS(text=text, lang=language)
gtts_transformer.save("test.mp3")
print("File converted!")