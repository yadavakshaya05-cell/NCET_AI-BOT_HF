# import streamlit as st
# from transformers import pipeline


# @st.cache_resource
# def load_summarizer():
#   return pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
# summarizer = load_summarizer()

# st.title(" AI text Summarizer")
# st.write("Enter a long text below, and get a concise summary!")
# long_text = st.text_area("Enter text to summarizer:",height=200)
# max_length = st.slider("Max Summary Length",min_value=50,max_value=300,value=150)
# min_length = st.slider("Min Summary Length", min_value=20,max_value=100,value=30)

# if st.button("Summarize"):
#   if long_text.strip():
#     with st.spinner("Generating summary... "):
#       summary = summarizer(long_text, max_length=max_length,
#                       min_length=min_length, do_sample=False)
#       st.subheader(" Summary:")
#       st.success(summary[0]['summary_text'])
# else:
#     st.warning(" Please enter some text to summarize.")
import streamlit as st
from transformers import pipeline

# 1. Use st.cache_resource to load the model only once
@st.cache_resource
def load_summarizer():
    # Explicitly using the correct model path and task name
    # We use 'summarization' and the specific distilbart model
    return pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

# 2. Page Configuration
st.set_page_config(page_title="AI Text Summarizer", page_icon="📝")

# 3. Load the model
try:
    summarizer = load_summarizer()
except Exception as e:
    st.error(f"Failed to load model: {e}")
    st.stop()

# 4. App UI
st.title("📝 AI Text Summarizer")
st.write("Enter a long text below, and get a concise summary!")

# Input area
input_text = st.text_area("Input Text", height=300, placeholder="Paste your article or long text here...")

# Settings for the summary
with st.expander("Summary Settings"):
    min_length = st.slider("Minimum Summary Length", 10, 50, 30)
    max_length = st.slider("Maximum Summary Length", 50, 300, 130)

# Action button
if st.button("Summarize"):
    if input_text.strip():
        with st.spinner("Generating summary..."):
            try:
                # Perform summarization
                summary = summarizer(
                    input_text, 
                    max_length=max_length, 
                    min_length=min_length, 
                    do_sample=False
                )
                
                # Display Result
                st.subheader("Summary")
                st.success(summary[0]['summary_text'])
            except Exception as e:
                st.error(f"An error occurred during summarization: {e}")
    else:
        st.warning("Please enter some text first!")

# Footer
st.markdown("---")
st.caption("Powered by Hugging Face Transformers & Streamlit")
