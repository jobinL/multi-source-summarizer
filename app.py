import streamlit as st
from utils.model_loader import load_summarizer
from summarizer_app.news import extract_text_from_url 
from summarizer_app.pdf import extract_text_from_pdf


def chunk_text(text,chunk_size=600):
    words = text.split()
    for i in range(0,len(words),chunk_size):
        yield " ".join(words[i:i+chunk_size])

def summarize_long_text(text):
    summaries =[]
    for i,chunk in enumerate(chunk_text(text)):
        try:
            result = summarizer(chunk,max_length =100,min_length=30,do_sample=False)
            if result and isinstance(result,list) and 'summary_text' in result[0]:
                summaries.append(result[0]['summary_text'])
            else:
                summaries.append(f"Skipped chunk{i+1} due to bad output")
        except Exception as e:
            summaries.append(f"Error on chunk {i+1}:{e}") 
    return "\n\,".join(summaries)
# 🎨 Page settings
st.set_page_config(
    page_title="Multi-Source Summarizer",
    page_icon="📚",
    layout="centered",
)

# 📚 Title and Description
st.markdown("""
# 📚 Multi-Source Summarizer  
Summarize long content from text, news articles, or documents in seconds.  
Select an input type and click **Summarize** to get a concise result powered by AI.
""")

# ✨ Load the model
summarizer = load_summarizer()

# 🔘 Selection
st.markdown("### 🔍 Select Input Type:")
option = st.radio(
    "", ["📝 Paste Text", "📰 News Article URL","📄 Upload PDF"],
    horizontal=True
)

text = ""

# ✍️ Text input
if option == "📝 Paste Text":
    text = st.text_area("Paste your content below 👇", height=200, placeholder="Enter any long text, essay, blog post...")

# 🌐 URL input
elif option == "📰 News Article URL":
    url = st.text_input("Paste a news article URL 🌐", placeholder="https://...")
    if url:
        with st.spinner("🔄 Extracting article content..."):
            text = extract_text_from_url(url)
        st.text_area("📰 Extracted Article:", value=text, height=200, disabled=True) 

elif option == "📄 Upload PDF":
    uploaded_file = st.file_uploader("Upload a PDF",type=["pdf"])
    if uploaded_file:
        with st.spinner("Extracting text from pdf"):
            text = extract_text_from_pdf(uploaded_file)
        st.text_area("Extracted PDF content:",value=text,height=250,disabled = True)
    else:
        text=""

# 🚀Summarize button

if text.strip():
    if st.button("✂️ Summarize"):
        with st.spinner("⚙️ Generating summary..."):
            try:
                summary = summarize_long_text(text)

                if summary.strip():
                    st.markdown("### ✅ Summary:")
                    st.success(summary)
                else:
                    st.warning("⚠️ Summary is empty. Try different input.")

            except Exception as e:
                st.error(f"Something went wrong: {e}")
else:
    st.info("Please provide some text or a URL above to enable summarization.")
