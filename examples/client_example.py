from rpc.rpc_client import RPCClient
from rpc.rpc_stub_generator import MathServiceStub

if __name__ == "__main__":
    client = RPCClient()
    math_stub = MathServiceStub(client)

    print("Resultado de 5 + 3:", math_stub.add(5, 3))
    print("Resultado de 4 * 2:", math_stub.multiply(4, 2))
    print("Resultado de 5 - 3:", math_stub.sub(5, 3))
    print("Resultado de 4 / 2:", math_stub.divide(4, 2))
