from fastapi import FastAPI

app = FastAPI(
    title="Verificación Humana",
    version="0.1.0",
)


@app.get("/")
def root():
    return {"service": "verificacion-humana", "status": "online"}


@app.get("/health")
def health():
    return {"status": "ok"}
