import fitz

def extract_text_from_pdf(uploaded_file,file_type):
    try:
        doc = fitz.open(stream=uploaded_file.read(),filetype=file_type)
        text=""
        for page in doc:
            text += page.get_text()
        return text 
    except Exception as e:
        return f"Failed to read pdf:{str(e)}"
