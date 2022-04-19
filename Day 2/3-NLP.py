import spacy_streamlit

models = ["en_core_web_sm", "en_core_web_md"]
default_text = "Sundar Pichai is the CEO of Google."
spacy_streamlit.visualize(models, default_text)

# pip install spacy_streamlit
# python -m spacy download en_core_web_sm
# streamlit run 3-NLP.py

# pip install spacy-transformers # If Needed