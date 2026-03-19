from Crypto.Hash import SHA3_256

def sha3(message):
    sha_hash = SHA3_256.new()
    sha_hash.update(message)
    return sha_hash.hexdigest()

def main():
    text = input("Nhập chuỗi cần băm: ").encode('utf-8')
    hashed_text = sha3(text)
    
    print("Chuoi nhap vao: {}".format(text.decode('utf-8')))
    print("SHA3-256 hash: ", hashed_text)  
if __name__ == "__main__":
    main()