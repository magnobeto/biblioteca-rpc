import socket
import threading
from .serializer import serialize, deserialize

class RPCServer:
    def __init__(self, service_object, registry_host='localhost', registry_port=5050, service_label='service', host='localhost', port=0):
        self.service_object = service_object
        self.registry_host = registry_host
        self.registry_port = registry_port
        self.service_label = service_label
        self.host = host
        self.port = port

    def start(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        self.port = server_socket.getsockname()[1]
        self.register_service()
        server_socket.listen()
        print(f"Servidor RPC escutando em {self.host}:{self.port}")

        while True:
            client_conn, _ = server_socket.accept()
            threading.Thread(target=self.handle_client, args=(client_conn,), daemon=True).start()

    def register_service(self):
        registry_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        registry_socket.connect((self.registry_host, self.registry_port))
        message = f"REGISTER|{self.service_label}|{self.host}|{self.port}"
        registry_socket.send(message.encode())
        registry_socket.close()

    def handle_client(self, client_conn):
        try:
            data = client_conn.recv(4096)
            func_name, args, kwargs = deserialize(data)

            if hasattr(self.service_object, func_name):
                result = getattr(self.service_object, func_name)(*args, **kwargs)
                client_conn.send(serialize(result))
            else:
                client_conn.send(serialize(Exception("Function not found")))

        except Exception as e:
            client_conn.send(serialize(e))
        finally:
            client_conn.close()
