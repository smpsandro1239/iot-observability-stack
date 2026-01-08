"""
Script auxiliar para simular métricas que viriam do Laravel.
Num cenário real, o Laravel exporia /metrics via laravel-prometheus-exporter.
Este script pode ser expandido para iniciar um servidor HTTP simples.
"""
import random
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT_NUMBER = 8000

class MetricsHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/metrics":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()

            # Gerar métricas simuladas formato Prometheus
            access_count = random.randint(100, 500)
            online_devices = random.randint(1, 5)

            metrics = f"""
# HELP iot_access_total Total de acessos registados
# TYPE iot_access_total counter
iot_access_total {access_count}

# HELP iot_devices_online Número de dispositivos online
# TYPE iot_devices_online gauge
iot_devices_online {online_devices}
"""
            self.wfile.write(metrics.encode())
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == "__main__":
    try:
        server = HTTPServer(('', PORT_NUMBER), MetricsHandler)
        print(f"Servidor de métricas a correr na porta {PORT_NUMBER}")
        server.serve_forever()
    except KeyboardInterrupt:
        print("^C recebido, a parar o servidor")
        server.socket.close()
