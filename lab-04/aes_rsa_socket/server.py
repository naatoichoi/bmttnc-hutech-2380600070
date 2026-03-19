from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)

print("Server listening...")

server_key = RSA.generate(2048)
clients = []


def encrypt_message(key, message):
    cipher = AES.new(key, AES.MODE_CBC)
    return cipher.iv + cipher.encrypt(pad(message.encode(), AES.block_size))


def decrypt_message(key, data):
    iv = data[:AES.block_size]
    ciphertext = data[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ciphertext), AES.block_size).decode()


def handle_client(client_socket, addr):
    print(f"Connected: {addr}")

    # gửi public key
    client_socket.send(server_key.publickey().export_key())

    # nhận public key client
    client_pub = RSA.import_key(client_socket.recv(2048))

    # tạo AES key
    aes_key = get_random_bytes(16)

    cipher_rsa = PKCS1_OAEP.new(client_pub)
    client_socket.send(cipher_rsa.encrypt(aes_key))

    clients.append((client_socket, aes_key))

    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break

            msg = decrypt_message(aes_key, data)
            print(f"{addr}: {msg}")

            # gửi cho client khác
            for c, k in clients:
                if c != client_socket:
                    c.send(encrypt_message(k, msg))

            if msg == "exit":
                break

        except:
            break

    clients.remove((client_socket, aes_key))
    client_socket.close()
    print(f"Disconnected: {addr}")


while True:
    client, addr = server_socket.accept()
    threading.Thread(target=handle_client, args=(client, addr)).start()