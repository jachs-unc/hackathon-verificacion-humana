# Verificación Humana Soberana

## Estado actual

La base inicial incluye FastAPI, Docker Compose y una prueba básica de salud. Aún faltan los endpoints de desafío, el modelo local, el widget, JWT y la consola administrativa.

## Arranque rápido

```bash
cd /home/estudiante/Documentos/hackaton/hackathon-verificacion-humana
cp .env.example .env
docker compose up --build
```

Comprueba el servicio en `http://localhost:8000/health`.

## 1. Nombre del proyecto

**Verificación Humana Soberana**

Servicio local de verificación humana y mitigación de bots con infraestructura soberana, modular y auditable.

## 2. Participantes

| Nombre completo | Rol en el equipo | Área principal |
|---|---|---|
| Valentin <Apellido> | Líder de ciberseguridad y criptografía | Seguridad, JWT, OWASP, auditoría, SBOM |
| Guillermo <Apellido> | Líder de infraestructura, borde y despliegue | Docker, reverse proxy, rate limiting, CI |
| Joci <Apellido> | Líder de IA conductual y observabilidad | Dataset, modelo local, métricas, dashboards |
| José Chávez | Líder de backend, integración y widget | API central, widget SDK, README, demo |

## 3. Descripción del proyecto

<Explicar en 1 o 2 párrafos:

- Problema que resuelve: dependencia de captchas privativos extranjeros, ataques automatizados y falta de soberanía tecnológica.
- Propósito: ofrecer un servicio de verificación humana soberano, seguro, modular y de código abierto.
- Funcionamiento general: el widget captura señales conductuales anonimizadas, el backend las evalúa con un modelo de IA local, emite un token JWT firmado si el riesgo es aceptable y las aplicaciones protegidas validan ese token.>

## 4. Alcance

### Funcionalidades cubiertas en esta versión

- [ ] Widget/SDK web embebible sin dependencias externas no auditadas.
- [ ] Endpoint `POST /api/v1/challenge/init` para iniciar el desafío.
- [ ] Endpoint `POST /api/v1/challenge/verify` para evaluar señales y emitir token.
- [ ] Endpoint `POST /api/v1/token/validate` para validar tokens.
- [ ] Endpoint `GET /api/v1/policies/{site_id}` para consultar políticas.
- [ ] Módulo de IA local para clasificación humana/bot.
- [ ] Firma y validación de JWT con claves asimétricas, expiración corta y `jti`.
- [ ] Capa de borde con reverse proxy y rate limiting básico.
- [ ] Consola administrativa mínima y observabilidad básica.
- [ ] Documentación de seguridad y SBOM.

### Límites de la entrega

- <Indicar qué no se implementó o quedó como trabajo futuro: por ejemplo, MFA/TOTP completo, dashboards avanzados, integración con Prometheus/Grafana, modelo entrenado con datos reales, alta disponibilidad, etc.>
- La solución se ejecuta en entorno local mediante Docker Compose.
- No se almacenan datos biométricos identificables ni se envía telemetría a servicios externos.

## 5. Requerimientos del sistema

### Lenguajes y runtimes

- Python 3.11+
- JavaScript moderno para el widget, sin CDN externos
- Docker y Docker Compose

### Dependencias principales

- FastAPI / Uvicorn
- PyJWT y cryptography
- scikit-learn / LightGBM / ONNX Runtime, según el modelo implementado
- Nginx o Traefik como reverse proxy
- pytest para pruebas

### Servicios y puertos

| Servicio | Puerto sugerido | Descripción |
|---|---:|---|
| Backend FastAPI | 8000 | API central de verificación |
| Reverse proxy / edge | 8080 | Punto de entrada protegido |
| Admin / observabilidad | 8080/admin | Consola administrativa mínima |

### Variables de entorno

Copiar `.env.example` a `.env` y completar:

```env
APP_ENV=local
APP_PORT=8000
EDGE_PORT=8080
JWT_PRIVATE_KEY_PATH=./secrets/private.pem
JWT_PUBLIC_KEY_PATH=./secrets/public.pem
JWT_TTL_SECONDS=120
AI_MODEL_PATH=./ai/model/model.onnx
RISK_THRESHOLD=0.65
RATE_LIMIT_REQUESTS=60
RATE_LIMIT_WINDOW_SECONDS=60
ADMIN_USER=<usuario_admin>
ADMIN_PASSWORD_HASH=<hash_seguro>
```
