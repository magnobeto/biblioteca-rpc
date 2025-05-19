# Biblioteca RPC

## Como executar

### 1. Iniciar o Binder
```bash
python3 -m rpc.rpc_binder
```

### 2. Iniciar o servidor
```bash
python3 examples/server_example.py
```

### 3. Iniciar o cliente
```bash
python3 examples/client_example.py
```

## Como adicionar novos serviços

- Crie uma nova classe de serviço dentro de `interface/`.
- Atualize ou gere um novo stub em `rpc_stub_generator.py`.
- Registre o novo serviço no Binder.

## Exemplo de execução
```
Resultado de 5 + 3: 8
Resultado de 4 * 2: 8
Resultado de 5 - 3: 2
Resultado de 4 / 2: 2.0
```
