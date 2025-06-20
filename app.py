import streamlit as st
from utils.model_loader import load_summarizer
from summarizer_app.news import extract_text_from_url



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
    "", ["📝 Paste Text", "📰 News Article URL"],
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

# 🚀 Summarize button
if text.strip():
    if st.button("✂️ Summarize"):
        with st.spinner("⚙️ Generating summary..."):
            try:
                summary = summarizer(text, max_length=100, min_length=30, do_sample=False)[0]['summary_text']
                st.markdown("### ✅ Summary:")
                st.success(summary)
            except Exception as e:
                st.error(f"Something went wrong: {e}")
else:
    st.info("Please provide some text or a URL above to enable summarization.")
