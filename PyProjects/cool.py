import pickle
try:
    with open(r"cred.dat", "rb") as f:
        credentials = pickle.load(f)
except IOError:
    with open(r"cred.dat", "wb") as f:
        username = raw_input("Please enter username: ")
        password = raw_input("Please enter password: ")
        credentials = {username: password}
        pickle.dump(credentials, f)
        
if credentials:
    print credentials