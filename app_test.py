from pandasai.llm.local_llm import LocalLLM
import streamlit as st
import pandas as pd
from pandasai import SmartDataframe

model = LocalLLM(
    api_base="http://localhost:11434/v1",
    model="llama3.2"
)

st.title("Data Analysis With PandasAI")

uploaded_file = st.file_uploader("Upload a CSV file", type=['csv'])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data.head(5))

    df = SmartDataframe(data, config={"llm":model})
    prompt = st.text_area("Enter your prompt:")

    if st.button("Generate"):
        if prompt:
            with st.spinner("Generating Response ..."):
                st.write(df.chat(prompt))