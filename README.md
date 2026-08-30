# Estación Climática — Patrones de diseño con FastAPI

Material de la clase práctica de patrones de diseño (Especialización en Desarrollo de Software,
Universidad del Magdalena): una API real de estación climática IoT, reescrita para mostrar **6
patrones GoF** aplicados a problemas reales — cada uno con su **caso malo** (el problema tal cual
existía) y su **caso bueno** (el mismo problema resuelto).

## Estructura

- **`app/`** — la API completa y funcional (nodos + lecturas de sensores + usuarios), con las 6
  versiones "buenas" ya integradas.
- **`examples/`** — 12 mini-apps standalone, pareadas malo/bueno, una por patrón. Cada carpeta
  corre sola y tiene su propio `README.md` explicando el problema:

  | # | Patrón | Carpeta |
  |---|--------|---------|
  | 01 | Factory Method | [`examples/01_factory_malo`](examples/01_factory_malo) / [`bueno`](examples/01_factory_bueno) |
  | 02 | Adapter | [`examples/02_adapter_malo`](examples/02_adapter_malo) / [`bueno`](examples/02_adapter_bueno) |
  | 03 | Facade | [`examples/03_facade_malo`](examples/03_facade_malo) / [`bueno`](examples/03_facade_bueno) |
  | 04 | Strategy (+ Repository, bonus no-GoF) | [`examples/04_repository_strategy_malo`](examples/04_repository_strategy_malo) / [`bueno`](examples/04_repository_strategy_bueno) |
  | 05 | Observer | [`examples/05_observer_malo`](examples/05_observer_malo) / [`bueno`](examples/05_observer_bueno) |
  | 06 | Decorator | [`examples/06_decorator_malo`](examples/06_decorator_malo) / [`bueno`](examples/06_decorator_bueno) |

  Los 6 son patrones GoF (los 23 clásicos). Repository viaja junto con Strategy en el módulo 04
  porque en la práctica se usan juntos, pero por sí solo no es un patrón GoF — no lo cuentes como
  uno de los 5 obligatorios del proyecto final.

- **`.claude/skills/patrones-fastapi/`** — un skill de Claude Code para aplicar este mismo método
  (problema real → caso malo → caso bueno → justificación) a tu propio proyecto final.

## Correr la API integrada

Sin Docker, sin Postgres — SQLite por defecto:

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Documentación interactiva: http://localhost:8000/docs

### Endpoints

- `POST /nodes/` · `GET /nodes/` — crear/listar nodos (Factory Method).
- `POST /sensors/` — guardar una lectura (Facade: guarda + revisa batería + notifica).
- `GET /sensors/?node_id=1&start_date=...&end_date=...&format=total|hour` — consultar lecturas
  (Repository + Strategy, con logging y caché vía Decorator).
- `POST /users/signup` · `POST /users/login` — registro/login con JWT.

### Cambiar de SQLite a Postgres (demuestra el Adapter)

```bash
docker compose up -d
DB_BACKEND=postgres DATABASE_URL=postgresql://postgres:postgres@localhost:5432/estacion_clima \
  uvicorn app.main:app --reload
```

Ningún endpoint cambia entre un modo y otro — esa es la demostración.

## Correr un ejemplo malo/bueno

```bash
cd examples/01_factory_malo
uvicorn main:app --reload --port 8001
```

Cada carpeta sugiere su propio puerto en su `README.md`, así puedes tener el malo y el bueno del
mismo patrón corriendo al mismo tiempo y compararlos con `curl` o `/docs`.

## Con Docker (la API integrada)

```bash
docker build -t estacion-clima .
docker run --env-file .env -p 8080:8080 estacion-clima
```

## Origen

Este repo era el backend real de una estación climática IoT propia, antes desplegado en Fly.io.
Se reescribió por completo para esta clase — ver `git log` para la versión anterior si hace
falta.
