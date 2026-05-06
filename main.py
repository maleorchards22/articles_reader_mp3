"""
Articles Web Reader to audio MP3
--------------------------------
This program takes a URL of a web article and converts it into an audio MP3 file using 'newspaper3k' 
to extract the article's text  and 'gTTS' (Google Text-to-Speech) to convert the text into speech. The
resulting MP3 file is saved locally with the title of the article as its filename.
requiriments:
- newspaper3k
- gTTS
Author: @maleorchards22
date: 2026-02
"""
from newspaper import Article
from gtts import gTTS
import nltk
nltk.download('punkt_tab')

def main():
    #* 1. Set the URL of the article you want to convert
    url= input("Enter the URL of the article that you want to convert to audio: ").strip()

    #* 2. Basic validation of the URL
    if not url.startswith("https://"):
      print("⚠️ Invalid URL. Please make sure it starts with 'https://'")
      return
    
        
    
    try:
          
          #* 3. Download and parse the article
          print("Connecting with the article...")
          article= Article(url)
          article.download()
          article.parse()

          #* 4.Check if text was actually extracted
          if not article.text:
              print("⚠️ Warning: No text content found in this URL")
              return
          #* 5. Convert text to speech
          print(f"🎧convertig '{article.title}' to audio...")
          tts= gTTS(text=article.text, lang='es')
          #* 6. Save the final file
          output_file="article_audio.mp3"
          tts.save(output_file)
          print(f"☑️ Success! Audio saved as: {output_file}")
    except Exception as e:
        print(f"🚨 An unexpected error ocurred: {e}")

if __name__== "__main__":
    main()


      