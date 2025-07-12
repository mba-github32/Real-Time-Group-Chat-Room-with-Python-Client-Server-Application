import socket
import threading

# Client settings
SERVER_HOST = '127.0.0.1'  # Localhost
SERVER_PORT = 12345        # Port to connect to

# Receive messages from the server
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print(message)
            else:
                break
        except:
            print("An error occurred.")
            client_socket.close()
            break

# Send messages to the server
def send_messages(client_socket):
    while True:
        message = input()
        client_socket.send(message.encode())

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    send_thread = threading.Thread(target=send_messages, args=(client_socket,))
    send_thread.start()

if __name__ == "__main__":
    start_client()
