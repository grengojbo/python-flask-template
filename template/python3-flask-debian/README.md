# wifi-clickhouse

OpenFaas функция

один раз на компьютере

Для Gitlab
зарегистрировать Add a personal access token [Личные токены доступа](https://<GITLAB URL>/profile/personal_access_tokens)
docker login <REGISTRY HOST> -u <Name> -p <Your new personal access token>

```shell
PASSWORD=$(kubectl -n openfaas get secret basic-auth -o jsonpath="{.data.basic-auth-password}" | base64 --decode)
echo $PASSWORD | faas-cli login -s  --gateway <OPENFAAS GATEWAY URL> -u admin
```

```shell
faas-cli template pull https://github.com/grengojbo/python-flask-template
faas-cli new --lang python3-flask-debian <FUNCTION NAME> -g <OPENFAAS GATEWAY URL> --cpu-request 100m --memory-request 20Mi
```

## Добавление секрета

```shell
faas-cli secret create secret-<NAME> -g <OPENFAAS GATEWAY URL> --from-literal <SECRET>
```