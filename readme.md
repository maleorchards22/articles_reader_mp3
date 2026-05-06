# 🔊 Web Article to Audio Converter

A python tool that extracts text from online articles and converts them into high-quality MP3 audio files.
This project demonstrates web scraping, natural language processing (NLP) basics, and speech synthesis.

## 🚀 Features

* **Smart Scraping:** Automatically extracts the main body of articles, filtering  out ads and menus using 'newspaper3k'.
* **Speech synthesis:** Converts text to natural-sounding speech using Google's TTS engine (`gTTS`).
* **Robust Error Handling:** Includes validation for URLs and exception management to prevent crashes.
* **Interactive CLI:** A user-friendly command-line interface with emojis for better status tracking

## 🛠 Technologies Used

* **Python 3.10+**
* **Newspaper3k:** For efficient web parsing.
* **gTTS (Google Text-to-Speech): **For audio generation.
* **NLTK:** For text tokenization and processing.

## 🖥 Installation & Setup

1.* **Clone the repository:**
 ```bash
 git clone https://github.com/@maleorchards22/article-to-audio.gitcdarticle-to-audio ```

2.* **Create and activate a virtual environment:**
```bash
python -m venv venv
# Windows:
.\venv\Scripts\activate
#Linux/Mac (WSL):
source venv/bin/activate

3.* ** Install dependencies:**
```bash
pip install -r requierements.txt

##🖥 How to Use
* **Run the main script:**
```bash
python main.py

* **Paste any article URL when prompted. The program will generate a file named article_audio.mp3 in the project directory.**

##📝 License

This project is open-source and available under MIT License.
