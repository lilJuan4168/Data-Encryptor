import streamlit as st
from api.functions import *

st.title("Data Encrypt")

with st.expander("Create key"):
    pwd = st.text_input("Wrtite you password: ")
    my_key = create_key(pwd)
    st.download_button(label='Download Password', data=my_key, file_name="password.pickle")