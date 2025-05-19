# Biblioteca RPC

## Como executar

### 1. Iniciar o Binder
```bash
python3 -m rpc.rpc_binder
```

### 2. Iniciar o servidor
```bash
python3 -m examples.server_example
```

### 3. Iniciar o cliente
```bash
python3 -m examples.client_example
```

## Como adicionar novos serviços

- Crie uma nova classe de serviço dentro de `interface/`.
- Atualize ou gere um novo stub em `rpc_stub_generator.py`.
- Registre o novo serviço no Binder.

## Exemplo de execução
```
Operação 34 + 8 = 42
Operação 55 - 11 = 44
Operação 5 * 5 = 25
Operação 33 / 11 = 3
```
