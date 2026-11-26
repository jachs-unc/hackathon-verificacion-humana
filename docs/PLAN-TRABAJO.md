# Plan de trabajo inicial

## Objetivo

Crear una demostración local segura con backend, widget, modelo básico, administración y documentación.

## Tareas por área

| Responsable sugerido | Tarea | Criterio de terminado |
|---|---|---|
| José Chávez | Coordinación backend y contrato API | Endpoints documentados y probados |
| Backend | Crear estructura FastAPI y rutas v1 | Pruebas pasan y `/health` responde |
| Seguridad | Diseñar claves JWT RS256 y validación | `jti`, expiración y validación documentadas |
| IA | Definir dataset sintético y modelo ONNX | Modelo carga localmente y devuelve puntuación |
| Widget | Crear página JavaScript embebible | Captura señales anonimizadas sin CDN |
| Infraestructura | Ajustar Compose y proxy básico | `docker compose up --build` funciona |
| Administración | Crear consola mínima | Estado y políticas visibles |
| Pruebas | Añadir pytest e integración | Tests automatizados en CI |
| Documentación | Completar README y riesgos | Instalación y límites claros |

## Orden recomendado

1. Backend mínimo: salud, contrato y pruebas.
2. Seguridad: claves locales y emisión JWT.
3. IA: clasificador básico reemplazable.
4. Widget: llamada a la API y demostración.
5. Proxy, consola y observabilidad.
6. Documentación, pruebas finales y preparación de entrega.

## Convención de ramas

- `main`: versión estable.
- `avance`: integración revisada.
- `trabajo-NOMBRE`: trabajo individual.

Cada contribución debe llegar mediante Pull Request hacia `avance`.

## Primer paso técnico

```bash
cd /home/estudiante/Documentos/hackaton/hackathon-verificacion-humana
cp .env.example .env
docker compose up --build
```

Abrir `http://localhost:8000/health`.
