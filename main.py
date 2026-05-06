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

import nltk
from gtts import gTTS
from newspaper import Article

nltk.download("punkt_tab")


class ArticleAudioConverter:
    def __init__(self, language="es"):
        self.language = language

    def fetch_article(self, url):
        """Download and process the article from web"""
        article = Article(url)
        article.download()
        article.parse()
        if not article.text:
            raise ValueError("⚠️ Warning: No text content found in this URL")
        return article

    def save_to_mp3(self, text, filename="article_audio_mp3"):
        """Convert text to speech and save it"""
        tts = gTTS(text=text, lang=self.language)
        tts.save(filename)
        return filename


def main():
    # Set the URL of the article you want to convert
    url = input(
        "Enter the URL of the article that you want to convert to audio: "
    ).strip()

    # Basic validation of the URL
    if not url.startswith("https://"):
        print("⚠️ Invalid URL. Please make sure it starts with 'https://'")
        return

    converter = ArticleAudioConverter(language="es")

    try:
        # Download and parse the article
        print("Connecting with the article...")
        article = converter.fetch_article(url)
        print(f"🎧convertig '{article.title}' to audio...")
        output = converter.save_to_mp3(article.text)
        print(f"☑️ Success! Audio saved as: {output}")
    except Exception as e:
        print(f"🚨 An unexpected error ocurred: {e}")


if __name__ == "__main__":
    main()
