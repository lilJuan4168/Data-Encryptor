from functions_cli import *
from tqdm import tqdm

wh_status = True
while wh_status == True:
    print("\n---Data Encrypter---\n")
    path = str(input("Write your path: "))
    pwd = str(input("Write your password: "))
    os.system("clear")
    if len(path) != 0 and len(pwd) != 0:
        key = create_key(pwd, path)
        files = os.listdir(path)
        files.remove("password.pickle")
        n_files = len(files)
        print(f"You are about to encrypt {n_files}")
        feedback = input("Continue? [Y/n]: ")
        if feedback.upper() == "Y":
            for file in tqdm(files):
                vid_path = path+"/"+file
                data_encrypt(key, path, file, pwd)
                sleep(1)
            os.system("clear")
            print("Completed, Save your password.pickle file and do not forget your password")
            input("Press enter to exit")
            wh_status = False
            break
        else:
            wh_status = False
            break
    else:
        print("Empty path or password")
        sleep(4)
        os.system("clear")