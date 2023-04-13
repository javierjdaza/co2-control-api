# co2-control-api

API REST para la gestion de la base de datos

## API Reference

#### Home

```python
  GET /
```

#### Documentation

```python
  GET /docs
```

#### Get todas las mediciones

```python
  GET /fetch/all
```

#### POST medicion

```python
  POST /load/data
```

| Parameter | Type   | Description                  |
| :-------- | :----- | :--------------------------- |
| `body`    | `json` | **Required**. Json with data |

#### Estructura de la medicion

```python
    body = {
        "key" : "1", # String
        "aula" : "aula 2", # String
        "nivel_co2" : 1100, # Integer
        "datetime" : "02-06-2022 12:34:23", # String datetime -> %d/%m/%Y%H:%M:%S
        "sensor" : "aula 2_sensor", # String
        "edificio" : "camilo torres", # String
        "piso" : 2, # Integer
    }
```

## Authors

- Ivan Daniel Maestre Muza

## Tech Stack

**DataBase:** SQL Deta

**Server:** FastApi, Uvicorn

## Proximos Pasos

- Conectar los dispositivos IOT al API, con el objetivo de almacenar en la base de datos relacional los datos de medicion.
- Agregar nuevos metodos para la extraccion filtrada de las mediciones.
