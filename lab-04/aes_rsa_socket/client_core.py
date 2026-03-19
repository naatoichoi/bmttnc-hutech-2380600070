import socket
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad, unpad


class ClientCore:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('localhost', 12345))

        self.client_key = RSA.generate(2048)

        server_pub = RSA.import_key(self.client_socket.recv(2048))
        self.client_socket.send(self.client_key.publickey().export_key())

        encrypted_key = self.client_socket.recv(2048)
        cipher_rsa = PKCS1_OAEP.new(self.client_key)
        self.aes_key = cipher_rsa.decrypt(encrypted_key)

    def encrypt(self, msg):
        cipher = AES.new(self.aes_key, AES.MODE_CBC)
        return cipher.iv + cipher.encrypt(pad(msg.encode(), AES.block_size))

    def decrypt(self, data):
        iv = data[:AES.block_size]
        ciphertext = data[AES.block_size:]
        cipher = AES.new(self.aes_key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(ciphertext), AES.block_size).decode()