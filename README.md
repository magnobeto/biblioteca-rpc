# Biblioteca RPC

Esta biblioteca implementa um sistema simples de RPC (Remote Procedure Call) em Python, permitindo que métodos de serviços sejam chamados remotamente como se fossem locais. O sistema é composto por três principais componentes:

- **Binder:** Responsável por registrar e localizar serviços disponíveis na rede.
- **Servidor RPC:** Expõe métodos de uma classe de serviço para serem chamados remotamente.
- **Cliente RPC:** Descobre e consome serviços remotos de forma transparente.

A comunicação entre cliente e servidor é feita via sockets TCP, e os dados são serializados para facilitar a troca de informações.

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
Resultado de 34 + 8: 42
Resultado de 55 - 11: 44
Resultado de 5 * 5: 25
Resultado de 33 / 11: 3.0
```
