# from dotenv import load_dotenv
# load_dotenv()

from langchain.llms import OpenAI
#llm = OpenAI()
#result = llm.predict("내가 좋아하는 동물은 ")
print("호호")

import time
import streamlit as st

st.title("제목")

content = st.text_input("제목을 입력해주세요")
if st.button("Say hello"):
    with st.spinner('Wait for it...'):
        time.sleep(5)
        st.write("Why hello there")