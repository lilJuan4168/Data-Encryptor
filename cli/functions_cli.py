from cryptography.fernet import Fernet
import pickle
import os
from datetime import datetime
from time import sleep

def create_key(my_password, path):
    key = Fernet.generate_key()
    file_key = open(f"{path}/password.pickle", "wb")
    pickle.dump(key, file_key)
    file_key.close()
    return key

def data_encrypt(key, path, file, pwd):
    my_key = Fernet(key + pwd.encode('utf-8'))
    with open(f"{path}/{file}", "rb") as v:
        video = v.read()
    video_encrypted = my_key.encrypt(video)
    file_name = str(datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
    foder_exist = os.path.exists(f"{path}/encrypted_files")
    if foder_exist:
        pass
    else:
       os.mkdir(f"{path}/encrypted_files")
    pkfile = open(f"{path}/encrypted_files/{file_name}.pickle", "wb")
    pickle.dump(video_encrypted, pkfile)
    pkfile.close()
    return True

def data_decrypt(key, path, file, pwd):
    my_key = Fernet(key + pwd.encode('utf-8'))
    filepk = open(f"{path}/{file}", "rb")
    videopk = pickle.load(filepk)
    filepk.close()
    video_decrypted = my_key.decrypt(videopk)
    foder_exist = os.path.exists(f"{path}/decrypted_files")
    if foder_exist:
        pass
    else:
       os.mkdir(f"{path}/decrypted_files")
    with open(f"{path}/decrypted_files/{file}.mp4", "wb") as dc:
        dc.write(video_decrypted)
    return video_decrypted