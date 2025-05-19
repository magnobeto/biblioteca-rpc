import socket
import threading

class ServiceRegistryBinder:
    def __init__(self, host='localhost', port=5050):
        self.binder_host = host
        self.binder_port = port
        self._services = {}

    def start(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.binder_host, self.binder_port))
        sock.listen()
        print(f"ServiceRegistryBinder ativo em {self.binder_host}:{self.binder_port}")

        while True:
            conn, _ = sock.accept()
            threading.Thread(target=self._handle_request, args=(conn,), daemon=True).start()

    def _handle_request(self, conn):
        try:
            data = conn.recv(1024).decode()
            tokens = data.split('|')
            action = tokens[0]

            if action == "REGISTER":
                _, service_name, service_ip, service_port = tokens
                self._services[service_name] = (service_ip, int(service_port))
                conn.sendall(b"REGISTERED")

            elif action == "LOOKUP":
                _, service_name = tokens
                if service_name in self._services:
                    service_ip, service_port = self._services[service_name]
                    conn.sendall(f"{service_ip}|{service_port}".encode())
                else:
                    conn.sendall(b"NOT_FOUND")

        finally:
            conn.close()

if __name__ == "__main__":
    binder = ServiceRegistryBinder()
    binder.start()
