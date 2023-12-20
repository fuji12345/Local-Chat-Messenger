import os
import socket

from faker import Faker


class Server:
    def __init__(self) -> None:
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.server_address = "./socket_file"
        try:
            os.unlink(self.server_address)
        except FileNotFoundError:
            pass

        print(f"Starting up on {self.server_address}")

        self.sock.bind(self.server_address)
        self.sock.listen(1)

    def accept_client(self):
        self.connection, self.client_address = self.sock.accept()
        print(f"connect address: {self.client_address}")

    def receive_and_send_fake(self):
        user_input = self.connection.recv(16).decode("utf-8")

        fake_content = self.make_fake_content(user_input)
        self.connection.sendall(fake_content.encode("utf-8"))

    def make_fake_content(self, user_input):
        fake = Faker()

        fake_content = ""
        if user_input == "name":
            fake_content = fake.name()
        elif user_input == "address":
            fake_content = fake.address()
        elif user_input == "email":
            fake_content = fake.email()
        elif user_input == "text":
            fake_content = fake.text()
        else:
            fake_content = "no content"

        return fake_content

    def close(self):
        self.connection.close()
