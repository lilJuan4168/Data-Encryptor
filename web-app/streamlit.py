import streamlit as st

st.title("Data Encrypt")

with st.expander("Create key"):
    pwd = st.text_input("Wrtite you password: ")
    st.write(pwd)