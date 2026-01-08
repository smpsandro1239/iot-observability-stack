# IoT Observability Stack

Este repositório contém a infraestrutura de observabilidade para o projeto **IOT Access Control**.
A stack é baseada em Docker e inclui Prometheus, Grafana e Mosquitto.

## Estrutura

- `mosquitto/`: Broker MQTT.
- `prometheus/`: Configuração de recolha de métricas.
- `grafana/`: Dashboards e visualização.
- `simulators/`: Scripts Python para testar a stack sem hardware real.

## Como Executar

1. Certifique-se de que tem o Docker e Docker Compose instalados.
2. Na raiz deste projeto, execute:

```bash
docker-compose up -d
```

3. Aceda aos serviços:
   - **Grafana**: http://localhost:3000 (admin/admin)
   - **Prometheus**: http://localhost:9090
   - **Mosquitto**: Porta 1883

## Simulação

Para gerar dados de teste:

```bash
pip install paho-mqtt
python simulators/esp32-mock.py
```
