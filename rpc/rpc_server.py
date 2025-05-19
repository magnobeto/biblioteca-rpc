import socket
import threading
from .serializer import serialize, deserialize

class RPCServer:
    def __init__(self, service, binder_host='localhost', binder_port=5000, service_name='service', server_host='localhost', server_port=0):
        self.service = service
        self.binder_host = binder_host
        self.binder_port = binder_port
        self.service_name = service_name
        self.server_host = server_host
        self.server_port = server_port

    def start(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.server_host, self.server_port))
        self.server_port = server.getsockname()[1]
        self.register_service()
        server.listen()
        print(f"Servidor RPC escutando em {self.server_host}:{self.server_port}")

        while True:
            client_socket, _ = server.accept()
            threading.Thread(target=self.handle_client, args=(client_socket,), daemon=True).start()

    def register_service(self):
        binder = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        binder.connect((self.binder_host, self.binder_port))
        message = f"REGISTER|{self.service_name}|{self.server_host}|{self.server_port}"
        binder.send(message.encode())
        binder.close()

    def handle_client(self, client_socket):
        try:
            data = client_socket.recv(4096)
            func_name, args, kwargs = deserialize(data)

            if hasattr(self.service, func_name):
                result = getattr(self.service, func_name)(*args, **kwargs)
                client_socket.send(serialize(result))
            else:
                client_socket.send(serialize(Exception("Function not found")))

        except Exception as e:
            client_socket.send(serialize(e))
        finally:
            client_socket.close()
