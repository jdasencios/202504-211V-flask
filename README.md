<<<<<<< HEAD
# 202504-211V-flask
=======
## 2.1 Reestructuración completa del proyecto
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
