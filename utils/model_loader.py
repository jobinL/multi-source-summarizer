import os
os.environ["TRANSFORMERS_NO_TF"] = "1"

from transformers import pipeline 



def load_summarizer():
    return pipeline("summarization",model ="facebook/bart-large-cnn",framework="pt")
