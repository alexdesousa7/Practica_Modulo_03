Esta es la actividad del **Modulo 03 de Contenedores y Virtualizacion**

# Students CRUD API – FastAPI + PostgreSQL + Docker

Este proyecto implementa una API REST sencilla utilizando **FastAPI**, **PostgreSQL** y **Docker Compose**.  
La API gestiona un CRUD básico de estudiantes de un máster.

---

## Funcionalidades

La API cumple los 4 requisitos obligatorios del ejercicio:

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/students` | Lista todos los estudiantes |
| GET | `/students/{id}` | Recupera un estudiante por ID |
| POST | `/students` | Crea un nuevo estudiante |
| DELETE | `/students/{id}` | Elimina un estudiante por ID |

---

## Tecnologías utilizadas

- Python 3.12  
- FastAPI  
- SQLAlchemy  
- PostgreSQL 16  
- Docker & Docker Compose  
- Pydantic  
- Uvicorn  

---

## Requisitos

- Docker Desktop (WSL2 recomendado)  
- PowerShell, Windows Terminal, Postman o navegador web  

---

## Cómo ejecutar el proyecto con Docker

1. Clonar el repositorio  
2. (Opcional) Copiar `.env.example` a `.env`  
3. Ejecutar en la raíz del proyecto:

```bash
docker compose up --build
Esto levantará:

FastAPI en: http://localhost:8080

PostgreSQL en el puerto 5432

Documentación automática
FastAPI genera documentación interactiva:

http://localhost:8080/docs

Cómo probar la API

Crear un estudiante

powershell
$body = @{ name="Ana"; email="ana@example.com"; master="DevOps" } | ConvertTo-Json
Invoke-RestMethod -Uri http://localhost:8080/students -Method Post -Body $body -ContentType "application/json"

Listar todos los estudiantes

powershell

Invoke-RestMethod -Uri http://localhost:8080/students -Method Get

Obtener un estudiante por ID

powershell

Invoke-RestMethod -Uri http://localhost:8080/students/1 -Method Get

Eliminar un estudiante por ID

powershell

Invoke-RestMethod -Uri http://localhost:8080/students/1 -Method Delete

Notas Final

La base de datos usa un volumen Docker para persistir datos.

Para reiniciar la base de datos desde cero:

bash
docker compose down -v

Autor

Práctica realizada por Jose Alexander De Sousa  
Módulo 03 – Contenedores y Virtualizacion
