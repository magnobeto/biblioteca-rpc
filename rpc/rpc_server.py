import socket
import threading
from .serializer import serialize, deserialize

class RPCServer:
    def __init__(self, service_instance, binder_host='localhost', binder_port=5050, service_name='service', server_host='localhost', server_port=0):
        self.service_instance = service_instance
        self.binder_host = binder_host
        self.binder_port = binder_port
        self.service_name = service_name
        self.server_host = server_host
        self.server_port = server_port

    def start(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.server_host, self.server_port))
        self.server_port = server_socket.getsockname()[1]
        self.register_service()
        server_socket.listen()
        print(f"Servidor RPC escutando em {self.server_host}:{self.server_port}")

        while True:
            client_conn, _ = server_socket.accept()
            threading.Thread(target=self.handle_client, args=(client_conn,), daemon=True).start()

    def register_service(self):
        binder_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        binder_socket.connect((self.binder_host, self.binder_port))
        message = f"REGISTER|{self.service_name}|{self.server_host}|{self.server_port}"
        binder_socket.send(message.encode())
        binder_socket.close()

    def handle_client(self, client_conn):
        try:
            data = client_conn.recv(4096)
            func_name, args, kwargs = deserialize(data)

            if hasattr(self.service_instance, func_name):
                result = getattr(self.service_instance, func_name)(*args, **kwargs)
                client_conn.send(serialize(result))
            else:
                client_conn.send(serialize(Exception("Function not found")))

        except Exception as e:
            client_conn.send(serialize(e))
        finally:
            client_conn.close()
