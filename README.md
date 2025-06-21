# 📚 Multi-Source Summarizer

Summarize long content from text, news articles, or PDF documents in seconds using powerful NLP models.

![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![HuggingFace](https://img.shields.io/badge/Powered%20by-Hugging%20Face-yellow?logo=huggingface&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)

---

## ✨ Features

- 📝 **Paste Text**: Input long text and get a short, clean summary.
- 📰 **News Article URL**: Paste a link to extract and summarize the article.
- 📄 **Upload PDF**: Upload a PDF and get a summary of its content (supports long PDFs by chunking).
- ⚙️ **Hugging Face Transformers**: Uses `facebook/bart-large-cnn` or `sshleifer/distilbart-cnn-12-6` for state-of-the-art summarization.
- ✅ **Streamlit UI**: Clean, fast, and interactive frontend.

---


## 🛠️ Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/jobinL/multi-source-summarizer.git
   cd multi-source-summarizer
2. **Create a virtual environment and install dependencies**
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

3. **Run the app**
streamlit run app.py
