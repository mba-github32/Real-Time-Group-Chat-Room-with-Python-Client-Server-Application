import socket
import threading

# Server settings
HOST = '127.0.0.1'  # Localhost
PORT = 12345        # Port to listen on

# Data structures to manage chat rooms and clients
chat_rooms = {}
clients = {}

# Handle incoming messages from clients
def handle_client(client_socket, client_address):
    client_socket.send(b'Enter your username: ')
    username = client_socket.recv(1024).decode().strip()

    client_socket.send(b'Enter chat room name: ')
    chat_room_name = client_socket.recv(1024).decode().strip()

    if chat_room_name not in chat_rooms:
        chat_rooms[chat_room_name] = []

    chat_rooms[chat_room_name].append((client_socket, username))
    clients[client_socket] = (chat_room_name, username)

    # Notify the new client of existing members
    existing_members = [user for _, user in chat_rooms[chat_room_name]]
    client_socket.send(f'Welcome to {chat_room_name} chat room, {username}! Members in the room: {", ".join(existing_members)}'.encode())

    # Notify all members about the new client
    broadcast("welcome", chat_room_name, username, client_socket, welcome=1)

    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break

            broadcast(message, chat_room_name, username, client_socket)
        except:
            break

    client_socket.close()
    chat_rooms[chat_room_name].remove((client_socket, username))
    del clients[client_socket]


def broadcast(message, chat_room_name, username, sender_socket, welcome=0):
    for client_socket, user in chat_rooms[chat_room_name]:
        if client_socket != sender_socket:
            try:
                if welcome == 1:
                    client_socket.send(f'{username} has joined the chat room!'.encode())
                else:
                    client_socket.send(f'{username}: {message.decode()}'.encode())
            except:
                client_socket.close()
                chat_rooms[chat_room_name].remove((client_socket, user))

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f'Server started on {HOST}:{PORT}')

    while True:
        client_socket, client_address = server_socket.accept()
        print(f'Connection from {client_address}')
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()

if __name__ == "__main__":
    start_server()
