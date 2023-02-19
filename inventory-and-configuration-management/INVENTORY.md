# Inventory (Service Discovery)

Though embedded in many solutions today, Consul can provide an easy accessible API and UI around service discovery and inventory management for services and resources alike.  Consul also has many other potential uses - but these uses are not utilized in this demo.

## Standing up Consul

```sh
docker-compose up -d consul
```

*PUT*

An example for registering a node and service

```sh
curl -XPUT --data @register.json http://127.0.0.1:8500/v1/catalog/register
```
