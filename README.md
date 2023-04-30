# SOA

## Запуск
```
docker-compose build
docker-compose up
```

## Запрос
```
echo "get_result ИМЯ ФОРМАТА" | nc -u 0.0.0.0 2000

ИМЯ ФОРМАТА:

1.PICKLE

2.JSON

3.XML

4.PROTOBUFF

5.AVRO

6.YAML

7.MSGPACK

```

## Ответ

```
Формата : ИМЯ ФОРМАТА - size - sirialization_time (ms) -  desirialization_time (ms)
```