import hashlib
import os
import sys


def main():
    if len(sys.argv == 2):
        passw = sys.argv[1]
        print(salted_password(passw, os.urandom(32).hex()))
    else:
        print("Invalid number of arguments")
                          
def salted_password (password, salt):    
    salted_pass = password+salt
    salted_pass = salted_pass.encode()
    return hashlib.sha256(salted_pass)

if __name__ == "__main__":
    main()

          