# Secrets

Secret stores like Vault provide an accessible API with audit trails and policy based access to provide an overall zero trust security solution for secret access.

## Standing up Vault

```sh
docker-compose up -d vault
```

> Visit [http://127.0.0.1:8200](http://127.0.0.1:8200) - log in with the token `root`

Using the secret store also grants you the abilit to utilize the API to pull down secrets, meaning its easily accessed by services and servers across your network.

*PUT* a secret into the secret store

```sh
curl -XGET http://127.0.0.1:8200/v1/secret/data/test --header "X-Vault-Token: root" --header "Content-Type: application/json" -XPOST -d '{"data":{"foo":"bar"}}'
```

*GET* a secret out of the secret store

```sh
curl -XGET http://127.0.0.1:8200/v1/secret/data/test --header "X-Vault-Token: root"
```

## Shutting down Vault

```sh
docker-compose stop consul
docker-compose rm -v # this removes the volume of the container - which will delete all test data
```
