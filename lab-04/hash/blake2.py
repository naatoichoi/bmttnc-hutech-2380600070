import hashlib

def blake2(message):
    blake_hash = hashlib.blake2b()
    blake_hash.update(message)
    return blake_hash.digest()  

def main():
    text = input("Nhập chuỗi cần băm: ").encode('utf-8')
    hashed_text = blake2(text)
    
    print("Chuoi nhap vao: {}".format(text.decode('utf-8')))
    print("BLAKE2 hash: ", hashed_text.hex())

if __name__ == "__main__":
    main()