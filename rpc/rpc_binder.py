import socket
import threading

class Binder:
    def __init__(self, host='localhost', port=5000):
        self.host = host
        self.port = port
        self.services = {}

    def start_binder(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.host, self.port))
        server.listen()
        print(f"Binder iniciado em {self.host}:{self.port}")

        while True:
            client_socket, _ = server.accept()
            threading.Thread(target=self.handle_client, args=(client_socket,), daemon=True).start()

    def handle_client(self, client_socket):
        try:
            request = client_socket.recv(1024).decode()
            parts = request.split('|')
            command = parts[0]

            if command == "REGISTER":
                _, service_name, ip, port = parts
                self.services[service_name] = (ip, int(port))
                client_socket.send(b"OK")

            elif command == "LOOKUP":
                _, service_name = parts
                if service_name in self.services:
                    ip, port = self.services[service_name]
                    client_socket.send(f"{ip}|{port}".encode())
                else:
                    client_socket.send(b"NOT_FOUND")

        finally:
            client_socket.close()

if __name__ == "__main__":
    binder = Binder()
    binder.start_binder()
