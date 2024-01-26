import streamlit as st
from api.functions import *
from datetime import datetime
#st.title("Data Encrypt")

with st.sidebar:
    st.title("Data Encrypt")

with st.expander("Create key"):
    pwd = st.text_input("Wrtite you password: ")
    my_key = create_key(pwd)
    status = len(pwd) == 0
    st.download_button(label='Download Password', data=my_key, file_name="password.pickle", disabled=status)

with st.expander("Data Encryptation"):
    key_file = st.file_uploader("Choose the key file")
    video = st.file_uploader("Choose a file")
    if key_file is not None and video is not None:
        st.success('Key File Loaded!', icon="✅")
        key_file = key_file.read()
        videord = video.read()
        video_encrypted = data_encrypt(key_file, videord)
        status = video_encrypted is None
        file_name = str(datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
        st.download_button(label='Download Encrypted File', data=video_encrypted, file_name=f"{file_name}.pickle", disabled=status)

