# django_api

Este repositorio contiene un ejemplo sencillo de una API monolítica
utilizando [Flask](https://flask.palletsprojects.com/). Expone un único
endpoint `/items` que permite realizar peticiones **GET** y **POST**.

## Instalación

```bash
pip install -r requirements.txt
```

## Uso

Inicie la aplicación con:

```bash
python app.py
```

La API quedará escuchando en `http://localhost:8000/items`.

- **GET** `/items` devuelve la lista de items en formato JSON.
- **POST** `/items` crea un nuevo item. Envíe un cuerpo JSON con la
  propiedad `name`.

## Licencia

Distribuido bajo los términos de la licencia MIT.
