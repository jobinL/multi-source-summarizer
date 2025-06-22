import os
os.environ["TRANSFORMERS_NO_TF"] = "1"

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer,pipeline

def load_summarizer():
    model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")
    tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
    
    # Explicitly move model to CPU
    model = model.to("cpu")
    
    return pipeline(
        "summarization",
        model=model,
        tokenizer=tokenizer,
        framework="pt",
        device="cpu"
    )