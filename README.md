#  Fastapi + Docker

This project is a simple example of how to use Fastapi with Docker.

## Run

```bash
docker build -t fastapi .
```

```bash
docker run --env-file .env -d --name fastapi_container -p 8002:8080 fastapi
```

## Test

```bash
curl http://localhost:8002
```

Bash output:

```bash
{"message":"Hello World"}
```

Go to url: http://localhost:8002

## Stop

```bash
docker stop fastapi
```

## Remove

```bash
docker rm fastapi
```

## Remove image

```bash
docker rmi fastapi
```

## Documentation

Go to url: http://localhost:8002/docs

## Install local

- Create a virtual environment

```bash
python3 -m venv venv
```

- Activate the virtual environment in linux or mac

```bash
source venv/bin/activate
```

- Activate the virtual environment in windows

```bash
venv\Scripts\activate
```

- Install the dependencies

```bash
pip install -r requirements.txt
```

- Run the application

```bash
uvicorn main:app --reload
```