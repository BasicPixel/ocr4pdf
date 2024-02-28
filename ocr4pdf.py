import pytesseract
import sys
from pdf2image import convert_from_path

# Use Homebrew to locate Tesseract automatically (if installed)
import os

if os.path.exists("/usr/local/Cellar/tesseract-ocr/"):
    tesseract_cmd = "/usr/local/Cellar/tesseract-ocr/latest/bin/tesseract"
else:
    # Provide a custom path if Tesseract isn't installed using Homebrew
    # Replace with your path
    pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

# Get PDF filename from command line arguments
if len(sys.argv) < 2:
    print("Error: Please provide the PDF filename as a command-line argument.")
    exit(1)
pdf_path = sys.argv[1]

# Name of the output text file
# Dynamically create output filename
output_filename = os.path.splitext(pdf_path)[0] + '.txt'

# Convert PDF pages to images (one image per page)
images = convert_from_path(pdf_path, dpi=200)

# Extract text from each image and append it to the output string
text = ""
for image in images:
    text += pytesseract.image_to_string(image, lang='ara') + "\n"

# Write the extracted text to the output file
with open(output_filename, 'w') as f:
    f.write(text)

print(f"Text extracted and saved to {output_filename}.")
