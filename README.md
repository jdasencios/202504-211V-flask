<<<<<<< HEAD
202504-211V-flask

#2.1 Reestructuración completa del proyecto
#Instalación y ejecución

```bash
uv sync
uv run python scripts/init_db.py
uv run flask --app app.main run --debug
```


```

## Criterio de organización
- routes/: define las URLs, métodos HTTP y flujo de cada endpoint.
- views/: concentra las funciones que renderizan plantillas.
- models/: concentra las consultas y operaciones contra la base de datos.
- db/: administra conexión, cierre e inicialización de SQLite.
- utils/: contiene funciones auxiliares reutilizables, como validadores.
- templates/: mantiene la capa visual HTML/Jinja.
- static/: mantiene archivos estáticos como CSS.
>>>>>>> 4709d0a (commit reestructuración completa del proyecto)


# CRUD de usuarios





Ejemplo de creación de usuario:

```bash
curl -X POST http://127.0.0.1:5000/users \
  -H "Content-Type: application/json" \
  -d '{"username":"juan","email":"jdasencios@gmail.com","password":"123456"}'
```

Ejemplo de actualización:

```bash
curl -X PUT http://127.0.0.1:5000/users/1 ^
  -H "Content-Type: application/json" ^
  -d "{\"username\":\"juan_updated\",\"email\":\"juan.updated@example.com\",\"password\":\"654321\"}"
```

Códigos HTTP usados:

- `200`: operación exitosa.
- `201`: usuario creado correctamente.
- `400`: JSON inválido o campos obligatorios faltantes.
- `404`: usuario no encontrado.
- `409`: email duplicado.