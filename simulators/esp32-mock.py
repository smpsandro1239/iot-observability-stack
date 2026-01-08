import json
import random
import time

import paho.mqtt.client as mqtt

# Configuração do Broker
BROKER = "localhost"
PORT = 1883
TOPIC_TELEMETRY = "iot/telemetry"

# Lista de Dispositivos Simulados
DEVICES = ["ESP32_01", "ESP32_02", "ESP32_03"]

def connect_mqtt():
    client = mqtt.Client(client_id=f"python-simulator-{random.randint(0, 1000)}")
    try:
        client.connect(BROKER, PORT)
        return client
    except Exception as e:
        print(f"Erro ao ligar ao MQTT: {e}")
        return None

def simulate_device_data(device_id):
    """Gera dados falsos realistas para um dispositivo IoT."""
    return {
        "device_id": device_id,
        "rssi": random.randint(-95, -60),  # Sinal LoRa típico
        "battery": round(random.uniform(3.3, 4.2), 2),
        "status": "online",
        "uptime": int(time.time()),
        "temperature": round(random.uniform(20.0, 45.0), 1)
    }

def run():
    client = connect_mqtt()
    if not client:
        return

    print(f"Simulador iniciado. A enviar dados para {BROKER}...")

    while True:
        for device in DEVICES:
            payload = simulate_device_data(device)
            client.publish(TOPIC_TELEMETRY, json.dumps(payload))
            print(f"[{device}] Dados enviados: {payload}")
            time.sleep(1) # Pequeno atraso entre dispositivos

        time.sleep(5)  # Envia batch a cada 5 segundos

if __name__ == "__main__":
    run()
