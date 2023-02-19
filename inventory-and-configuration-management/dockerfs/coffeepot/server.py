import http.server, random
from prometheus_client import start_http_server
from prometheus_client import Counter,Gauge

SERVINGS = Counter('servings_of_coffee', 'Total number of coffees served')
TEMPERATURE = Gauge('coffee_temperature', 'Temp of Coffee Served')
MINUTES = Counter('coffee_minutes_to_prepare', 'Time in Minutes for Coffee Served')


class ServerHandler(http.server.BaseHTTPRequestHandler):
  def do_GET(self):
    SERVINGS.inc()
    self.send_response(200)
    self.end_headers()
    temp = random.randint(100,160)
    timer = random.randint(1,10)
    print(f"temperature registered at {temp}")
    print(f"minutes taken: {timer}")
    TEMPERATURE.set(temp)
    MINUTES.inc(timer)
    self.wfile.write(bytes(f"Customer served coffee at {temp} in {timer} minutes","utf-8"))
    self.wfile.close()

if __name__ == "__main__":
    start_http_server(8000)
    server = http.server.HTTPServer(('', 8001), ServerHandler)
    print("Prometheus metrics available on port 8000 /metrics")
    print("HTTP server available on port 8001")
    server.serve_forever()
