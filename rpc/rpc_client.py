import socket
from .serializer import serialize, deserialize

class RPCClient:
    def __init__(self, binder_host='localhost', binder_port=5050):
        self.binder_host = binder_host
        self.binder_port = binder_port

    def lookup_service(self, service_name):
        binder = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        binder.connect((self.binder_host, self.binder_port))
        message = f"LOOKUP|{service_name}"
        binder.send(message.encode())
        response = binder.recv(1024).decode()
        binder.close()

        if response == "NOT_FOUND":
            raise Exception("Service not found")
        ip, port = response.split('|')
        return ip, int(port)

    def call(self, service_name, func_name, *args, **kwargs):
        ip, port = self.lookup_service(service_name)
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((ip, port))
        client.send(serialize((func_name, args, kwargs)))
        data = client.recv(4096)
        result = deserialize(data)
        client.close()

        if isinstance(result, Exception):
            raise result
        return result
