from rpc.rpc_server import RPCServer
from interface.math_service import MathService

if __name__ == "__main__":
    service = MathService()
    server = RPCServer(service, service_label='math_service')
    server.start()
