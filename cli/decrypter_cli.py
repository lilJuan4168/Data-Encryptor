from functions_cli import *
from tqdm import tqdm

wh_status = True
while wh_status == True:
    print("\n---Data Decrypter---\n")
    path = str(input("Write your path: "))
    pwd = str(input("Write your password: "))
    os.system("clear")
    if len(path) != 0 and len(pwd) != 0:
        file = open(f"{path}/password.pickle", "rb")
        key = pickle.load(file)
        file.close()
        files = os.listdir(path)
        files.remove("password.pickle")
        n_files = len(files)
        print(f"You are about to decrypt {n_files}")
        feedback = input("Continue? [Y/n]: ")
        if feedback.upper() == "Y":
            for file in tqdm(files):
                vid_path = path+"/"+file
                data_decrypt(key, path, file, pwd)
                sleep(1)
            os.system("clear")
            print("Completed")
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