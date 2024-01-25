from cryptography.fernet import Fernet
import pickle
import socket
from io import BytesIO

def create_key(my_password):
    key = Fernet.generate_key() + my_password.encode('utf-8')
    file_key = pickle.dumps(key)
    file_key = BytesIO(file_key)
    return file_key

def data_encrypt(key, video):
    my_key = Fernet(key)
    with open("../vid/mediapipe.mp4", "rb") as v:
        video = v.read()
    video_encripted = my_key.encrypt(video)
    return video_encripted

def data_decrypt(key, video_pickle):
    my_key = Fernet(key)
    file = open("vid.pickle", "rb")
    videopk = pickle.load(file)
    file.close()
    video_decrypted = my_key.decrypt(videopk)
    with open("../vid/vid_decrypted.mp4", "wb") as dc:
        dc.write(video_decrypted)
    return True

def ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception as e:
        return (str(e))
        ip = None
    finally:
        s.close()
    return ip


print(create_key("juancho"))