import os
import pdfplumber
from gtts import gTTS
import argparse

print("This may take a while")

parser = argparse.ArgumentParser(description='Convert a book or text file into a text to speech audiobook')
group = parser.add_mutually_exclusive_group()
group.add_argument('-f', '--file', metavar='', help='file to be converted to audio')
group.add_argument('-t', '--text', metavar='', help='text to be converted to audio')
args = parser.parse_args()

if args.text:
	text = args.text
elif args.file:
	ext = os.path.splitext(args.file)[1]
	if ext == '.txt':
		with open(args.file, 'r') as book_file:
			text = book_file.read()
	elif ext == '.pdf':
		pdf = pdfplumber.open(args.file)
		text = ''
		for i in range(len(pdf.pages)):
			page = pdf.pages[i]
			text += page.extract_text()


language = 'en'
print("Text extracted!")
gtts_transformer = gTTS(text=text, lang=language)
gtts_transformer.save("test.wav")
print("File converted!")