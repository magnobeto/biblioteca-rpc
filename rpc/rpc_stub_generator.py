from .rpc_client import RPCClient

class MathServiceStub:
    def __init__(self, client):
        self.client = client

    def add(self, a, b):
        return self.client.call('math_service', 'add', a, b)

    def multiply(self, a, b):
        return self.client.call('math_service', 'multiply', a, b)

    def sub(self, a, b):
        return self.client.call('math_service', 'sub', a, b)

    def divide(self, a, b):
        return self.client.call('math_service', 'divide', a, b)
