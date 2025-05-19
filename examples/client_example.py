from rpc.rpc_client import RPCClient
from rpc.rpc_stub_generator import MathServiceStub

if __name__ == "__main__":
    client = RPCClient()
    math_stub = MathServiceStub(client)

    print("Resultado de 34 + 8: ", math_stub.add(34, 8))
    print("Resultado de 55 - 11: ", math_stub.sub(55, 11))
    print("Resultado de 5 * 5:  ", math_stub.multiply(5, 5))
    print("Resultado de 33 / 11:  ", math_stub.divide(33, 11))
