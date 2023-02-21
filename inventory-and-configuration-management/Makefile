coffeepot:
	docker-compose up -d coffeepot prometheus grafana node-exporter

418:
	docker-compose stop coffeepot prometheus grafana node-exporter

hashicorp:
	docker-compose up -d vault consul

bye-hashicorp:
	docker-compose stop vault consul
	docker-compose rm -v

register:
	curl -XPUT --data @register.json http://127.0.0.1:8500/v1/catalog/register

get-services:
	curl -XGET http://127.0.0.1:8500/v1/catalog/services
	curl -XGET http://127.0.0.1:8500/v1/catalog/service/coffeepot

deregister:
	curl -XPUT --data @deregister.json http://127.0.0.1:8500/v1/catalog/deregister
	curl -XPUT --data @deregister-node.json http://127.0.0.1:8500/v1/catalog/deregister
