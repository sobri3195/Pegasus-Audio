# Importing Libraries
from gtts import gTTS
import PyPDF2
import os

def pegasus_audio(pdf_path, language='en'):
    """
    Convert text from a PDF file to an audio file using Google Text-to-Speech (gTTS).
    
    Parameters:
    pdf_path (str): Path to the PDF file.
    language (str): Language code for the audio conversion (default is 'en' for English).
    """
    # Check if the file exists
    if not os.path.isfile(pdf_path):
        print(f"The file {pdf_path} does not exist.")
        return

    # Open file
    try:
        pdf_File = open(pdf_path, 'rb')
    except Exception as e:
        print(f"Error opening file: {e}")
        return

    # Create PDF Reader Object
    try:
        pdf_Reader = PyPDF2.PdfFileReader(pdf_File)
    except Exception as e:
        print(f"Error reading PDF file: {e}")
        return

    count = pdf_Reader.numPages # Counts number of pages in pdf
    textList = []

    # Extracting text data from each page of the pdf file
    for i in range(count):
        try:
            page = pdf_Reader.getPage(i)
            textList.append(page.extractText())
        except Exception as e:
            print(f"Error extracting text from page {i}: {e}")

    # Close the PDF file
    pdf_File.close()

    # Converting multiline text to single line text
    textString = " ".join(textList)

    # Check if text extraction was successful
    if not textString.strip():
        print("No text could be extracted from the PDF.")
        return

    # Print the extracted text (optional)
    # print(textString)

    # Call GTTS
    try:
        myAudio = gTTS(text=textString, lang=language, slow=False)
    except Exception as e:
        print(f"Error during text-to-speech conversion: {e}")
        return

    # Save as mp3 file
    audio_file = "Audio.mp3"
    try:
        myAudio.save(audio_file)
        print(f"Audio saved as {audio_file}")
    except Exception as e:
        print(f"Error saving audio file: {e}")

# User input for PDF file name and language
pdf_path = input("Enter the path to the PDF file: ")
language = input("Enter the language code (default is 'en' for English): ")
if not language.strip():
    language = 'en'

pegasus_audio(pdf_path, language)
