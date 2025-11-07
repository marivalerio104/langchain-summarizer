import streamlit as st
from summarizer import summarize_text


st.markdown("""
  <style>
  h1 {
    text-align: center;
  }
  .stVerticalBlock  {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .stForm {
    box-shadow: 2px 5px 15px rgba(0, 0, 0, 0.15);
  }
  button {
    box-shadow: 2px 3px 5px rgba(0, 0, 0, 0.15);
  }
  </style>
""", unsafe_allow_html=True)


st.set_page_config(page_title="Text Summarizer", page_icon="✏️")

st.title('Text Summarizer')

with st.form("form"):
  text = st.text_area(
    "Text",
    height=400,
    placeholder="Enter the text here...",
    max_chars=6000,
    help="Type or paste the text to summarize."
  )

  option = st.selectbox(
    "Choose an option for the summary:",
    ["Detailed", "Brief", "Bullet points"]
  )

  summarize = st.form_submit_button("Summarize!")

if summarize:
  if text.strip():
    with st.spinner("Summarizing..."):
      summary = summarize_text(text, option)
      st.subheader("Summary:")
      st.write(summary)
  else:
    st.warning("Please enter some text first.")
