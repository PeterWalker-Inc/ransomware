from cryptography.fernet import Fernet
import os

def load_key():
    file = open('key.key', 'rb')
    key_ = file.read()
    file.close()
    return key_

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
 
        ransom_extension_removed_filepath = filepath.replace(".lock", "")
        os.rename(filepath, ransom_extension_removed_filepath)

        print(ransom_extension_removed_filepath)

        with open(ransom_extension_removed_filepath, 'wb') as f:
            f.write(algo.decrypt(data))