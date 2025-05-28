import socket
import random

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('localhost', 3004))
server_socket.listen()

print("Server is running on localhost:3003")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")

    request = client_socket.recv(1024).decode()

    if (not request) or ('favicon.ico' in request):
        client_socket.close()
        continue

    request_line = request.splitlines()[0]
    request_list = request_line.split()
    http_method = request_list[0]
    path = request_list[1][0]
    params = {}
    for query in request_list[1][2:].split("&"):
        param = query.split("=")
        params[param[0]] = param[1]

    
    response_body = (f"{request_line}\nHTTP Method: {http_method}\n"
                    f"Path: {path}\nParameters: {params}\n")
    

    for _ in range(int(params["rolls"])):
        roll = random.randint(1, 6)
        response_body += f'Roll: {roll}\n'
    

    response = ("HTTP/1.1 200 OK\r\n"
            "Content-Type: text/plain\r\n"
            f"Content-Length: {len(response_body)}\r\n"
            "\r\n"
            f"{response_body}\n")
    
    client_socket.sendall(response.encode())
    client_socket.close()



