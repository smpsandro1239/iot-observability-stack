# Guia de Configuração e Integração

Este documento detalha como preparar o ambiente e integrar novas métricas.

## Requisitos
- Docker Desktop (Windows/Mac) ou Docker Engine (Linux)
- Python 3.9+ (para simuladores)

## Passo a Passo

1. **Clone do Repositório**
   ```bash
   git clone ...
   ```

2. **Início da Stack**
   ```bash
   docker-compose up -d
   ```

3. **Verificação de Saúde**
   - Verifique `docker ps` para garantir que `iot_prometheus`, `iot_grafana` e `iot_mosquitto` estão "Up".

## Integração com ESP32
(Detalhes sobre tópicos MQTT...)

## Integração com Laravel
(Detalhes sobre endpoint /metrics...)
