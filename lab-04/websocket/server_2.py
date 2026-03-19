import tornado.ioloop
import tornado.web
import tornado.websocket
import base64
import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.backends import default_backend

# KEY cố định (16 bytes = AES-128)
AES_KEY = b'1234567890abcdef'


def encrypt_aes(message: str) -> str:
    iv = os.urandom(16)

    # padding
    padder = PKCS7(128).padder()
    padded_data = padder.update(message.encode()) + padder.finalize()

    cipher = Cipher(algorithms.AES(AES_KEY), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    # gửi iv + ciphertext (encode base64)
    return base64.b64encode(iv + ciphertext).decode()


class WebSocketServer(tornado.websocket.WebSocketHandler):
    clients = set()

    def open(self):
        print("Client connected")
        WebSocketServer.clients.add(self)

    def on_close(self):
        print("Client disconnected")
        WebSocketServer.clients.remove(self)

    def on_message(self, message):
        print(f"Received from client: {message}")

        encrypted = encrypt_aes(message)
        print(f"Encrypted: {encrypted}")

        self.write_message(encrypted)


def make_app():
    return tornado.web.Application([
        (r"/websocket/", WebSocketServer),
    ])


def main():
    app = make_app()
    app.listen(8888)
    print("Server running at ws://localhost:8888/websocket/")
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()