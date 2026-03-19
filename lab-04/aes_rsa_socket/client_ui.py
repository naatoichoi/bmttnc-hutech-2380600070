import sys
import threading

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer

from chat_ui import Ui_MainWindow
from client_core import ClientCore


class ChatClient(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.core = None

        # UI event
        self.ui.sendBtn.clicked.connect(self.send_message)
        self.ui.inputBox.returnPressed.connect(self.send_message)

        # delay connect (tránh đơ UI)
        QTimer.singleShot(100, self.init_connection)

    def init_connection(self):
        try:
            self.core = ClientCore()

            self.thread = threading.Thread(target=self.receive_messages)
            self.thread.daemon = True
            self.thread.start()

            self.ui.chatBox.append("Connected to server!")

        except:
            self.ui.chatBox.append("❌ Cannot connect to server")

    def send_message(self):
        if not self.core:
            return

        msg = self.ui.inputBox.text()
        if not msg:
            return

        encrypted = self.core.encrypt(msg)
        self.core.client_socket.send(encrypted)

        self.ui.chatBox.append(f"You: {msg}")
        self.ui.inputBox.clear()

    def receive_messages(self):
        while True:
            try:
                data = self.core.client_socket.recv(1024)
                if not data:
                    break

                msg = self.core.decrypt(data)
                self.ui.chatBox.append(f"Other: {msg}")

            except:
                break


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatClient()
    window.show()
    sys.exit(app.exec_())