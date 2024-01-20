from cryptography.fernet import Fernet
import pickle
import socket

def create_key(my_password):
    gen_key = Fernet.generate_key() + my_password.encode('utf-8')
    return gen_key

def data_encrypt(gen_key, video):
    key = Fernet(gen_key)
    with open("../vid/mediapipe.mp4", "rb") as v:
        video = v.read()
    video_encripted = key.encrypt(video)
    return video_encripted

def data_decrypt():
    pass

def obtener_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception as e:
        print(f"No se pudo obtener la dirección IP: {e}")
        ip = None
    finally:
        s.close()
    return ip
