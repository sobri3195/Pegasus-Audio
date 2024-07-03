# Pegasus Audio

Pegasus Audio is a Python script that converts text from a PDF file into an audio file using Google Text-to-Speech (gTTS). This tool is useful for creating audiobooks or listening to documents on the go.

## Features

- Converts PDF text to speech.
- Supports multiple languages via language codes.
- Provides error handling for file operations and text extraction.

## Requirements

- Python 3.x
- gTTS library
- PyPDF2 library

## Installation

1. Clone the repository or download the script.
2. Install the required libraries using pip:
   ```sh
   pip install gtts pypdf2

## Usage
Run the script:
sh
python pegasus_audio.py
Enter the path to the PDF file when prompted.
Enter the language code for the text-to-speech conversion (default is 'en' for English).
The script will generate an audio file named Audio.mp3 in the same directory.

## Example
sh
Enter the path to the PDF file: example.pdf
Enter the language code (default is 'en' for English): en
Audio saved as Audio.mp3

## Notes
Ensure that the PDF file is not encrypted or password-protected.
The text extraction quality depends on the PDF's formatting.

## License
This project is licensed under the MIT License 
