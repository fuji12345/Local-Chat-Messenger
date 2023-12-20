from client import Client
from sever import Server


def print_description():
    print(
        """
        You can create fake content.
        For example, if you type name, you can get a fake name.
        name -> fake name, address -> fake address, email -> fake email, text -> fake text, exit -> Exit Program
        """
    )


def main():
    server = Server()
    client = Client()

    client.connect_server()
    server.accept_client()

    print_description()

    while True:
        user_input = input("-----Which one will you create-----: ")
        if user_input == "exit":
            break

        client.send_input(user_input)
        server.receive_and_send_fake()

        fake_content = client.receive_from_server()
        print("\n" + fake_content + "\n")

    client.close()
    server.close()


if __name__ == "__main__":
    main()
