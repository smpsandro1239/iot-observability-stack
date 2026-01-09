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
    # Usar a nova API v2 do Paho MQTT
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id=f"python-simulator-{random.randint(0, 1000)}")
    try:
        client.connect(BROKER, PORT)
        print(f"Ligado ao broker {BROKER}:{PORT}")
        return client
    except Exception as e:
        print(f"Erro ao ligar ao MQTT: {e}")
        return None

def simulate_device_data(device_id):
    """Gera dados falsos realistas para um dispositivo IoT."""
    return {
        "device_id": device_id,
        "rssi": random.randint(-95, -60),
        "battery": round(random.uniform(3.3, 4.2), 2),
        "status": "online",
        "uptime": int(time.time()),
        "temperature": round(random.uniform(20.0, 45.0), 1)
    }

def run():
    client = connect_mqtt()
    if not client:
        return

    print(f"Simulador iniciado. A enviar dados para o tópico '{TOPIC_TELEMETRY}'...")

    try:
        while True:
            for device in DEVICES:
                payload = simulate_device_data(device)
                result = client.publish(TOPIC_TELEMETRY, json.dumps(payload))

                # Verificar se o envio foi bem sucedido
                status = result.rc
                if status == 0:
                    print(f"[{device}] Dados enviados com sucesso!")
                else:
                    print(f"[{device}] Falha ao enviar dados (rc: {status})")

                time.sleep(1)

            time.sleep(5)
    except KeyboardInterrupt:
        print("\nSimulador parado pelo utilizador.")
    finally:
        client.disconnect()

if __name__ == "__main__":
    run()
