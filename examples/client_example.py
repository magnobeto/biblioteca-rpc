from rpc.rpc_client import RPCClient
from rpc.rpc_stub_generator import MathServiceStub

if __name__ == "__main__":
    client = RPCClient()
    math_stub = MathServiceStub(client)

    print("Operação 34 + 8 = ", math_stub.add(34, 8))
    print("Operação 55 - 11 = ", math_stub.sub(55, 11))
    print("Operação 5 * 5 = ", math_stub.multiply(5, 5))
    print("Operação 33 / 11 = ", math_stub.divide(33, 11))
