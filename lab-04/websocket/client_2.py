import tornado.ioloop
import tornado.websocket

class WebSocketClient:
    def __init__(self, io_loop):
        self.connection = None
        self.io_loop = io_loop

    def start(self):
        self.connect()

    def connect(self):
        print("Connecting...")
        tornado.websocket.websocket_connect(
            url="ws://localhost:8888/websocket/",
            callback=self.on_connect,
        )

    def on_connect(self, future):
        try:
            self.connection = future.result()
            print("Connected to server")

            # Gửi message đầu tiên
            self.send_message()

            # Bắt đầu nhận
            self.connection.read_message(callback=self.on_message)

        except Exception as e:
            print("Connection failed:", e)

    def send_message(self):
        msg = input("Enter message: ")
        self.connection.write_message(msg)

    def on_message(self, message):
        if message is None:
            print("Disconnected")
            return

        print(f"Encrypted from server: {message}")

        # gửi tiếp
        self.send_message()
        self.connection.read_message(callback=self.on_message)


def main():
    io_loop = tornado.ioloop.IOLoop.current()
    client = WebSocketClient(io_loop)
    io_loop.add_callback(client.start)
    io_loop.start()


if __name__ == "__main__":
    main()