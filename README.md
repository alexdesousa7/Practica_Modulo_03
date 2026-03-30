Esta es la actividad del Modulo 03 de Contenedores y Virtualizacion

# fastapi-students-crud

## Requisitos
- Docker Desktop (WSL2 recomendado)
- PowerShell o Windows Terminal

## Levantar el proyecto
1. Clonar repo
2. Copiar `.env.example` a `.env` y ajustar si es necesario
3. Ejecutar:
   docker compose up --build

La API quedará disponible en http://localhost:8080


Donde nos piden realizar lo siguiente:

Descripcion

Crea un docker compose funcional que incluya una aplicación con API CRUD accesible mediante HTTP en el puerto 8080 y una base de datos con persistencia de datos. La aplicación debe implementar endpoints REST con manejo de errores y logging, mientras que ambos contenedores deben comunicarse a través de una red personalizada.

Requisitos

- Crear un archivo docker-compose.yml que defina los servicios necesarios.
- La aplicación debe escuchar peticiones HTTP y ser accesible desde el huésped en el puerto 8080.
- Implementar una API CRUD con los siguientes endpoints: GET para listar todas las entidades, GET para recuperar una entidad específica, POST para crear entidades y DELETE para borrar entidades.
- Implementar control de errores que devuelva códigos HTTP 404 (Not Found) cuando una entidad no exista y HTTP 400 (Bad Request) cuando los datos de entrada no sean válidos.
- Incluir logging con un mínimo de trazabilidad en la aplicación.
- Los datos deben persistirse en una base de datos a elegir (PostgreSQL, MySQL, MongoDB, etc.).
- La imagen de la aplicación debe construirse automáticamente al ejecutar docker compose.
- La base de datos debe utilizar un volumen con nombre personalizado para persistir los datos.
- Ambos contenedores deben estar en una red personalizada y comunicarse entre ellos utilizando los nombres de los contenedores.

Instrucciones

Crear un docker compose funcional que cumpla las siguientes características:

Un contenedor con una aplicación que escuche peticiones HTTP y que se pueda acceder a esta por medio del huésped y en el puerto 8080.

Esta API puede ser cualquier tipo de CRUD hecho en FastAPI Python, tendréis que escoger vosotros de qué la queréis hacer por ejemplo, un CRUD de "estudiantes de un master" hecho en FastAPI. Debe tener los siguientes métodos:

GET /<entidad> Lista todas las entidades existentes
GET /<entidad>/<id> Recupera una entidad en específico.
POST /<entidad> Crea una entidad
DELETE /<entidad>/<id> Borra una entidad

Es importante que estos endpoints tengan control de errores, devolviendo códigos HTTP tales como:

HTTP 404 Not Found: Entidad no encontrada
HTTP 400 Bad Request: Si alguno de los campos para crear no cumple con su característica deseada (por ejemplo, pasar un número en un campo tipo "string")

El logging también será considerado, por lo que es importante tener un mínimo de trazabilidad.

Todos los objetos deben ser guardados en una base de datos de vuestra preferencia.

Esta imagen debe ser construida en el momento de ejecutar el docker compose.

Una imagen con la base de datos que vayáis a usar. Esta imagen debe tener un volumen con el nombre que preferías y persistir allí todos los datos de la base de datos.

Estos dos contenedores deben coexistir en una misma red creada por vosotros y deben comunicarse entre ellos por el nombre que le asignéis al contenedor.

Criterios de Calificacion

Configuración de Docker Compose y red personalizada
Debe existir un archivo docker-compose.yml válido que defina al menos dos servicios: la aplicación y la base de datos. Ambos servicios deben estar configurados en una red personalizada creada explícitamente. Los contenedores deben poder comunicarse entre sí utilizando los nombres de servicio como nombres de host. El servicio de la aplicación debe exponer el puerto 8080 al huésped.
Peso: 25%
Construcción de imagen y persistencia de datos
La imagen de la aplicación debe configurarse para construirse automáticamente cuando se ejecute docker compose, utilizando un Dockerfile en el contexto de construcción. El servicio de base de datos debe tener un volumen con nombre personalizado configurado para persistir los datos. El volumen debe estar correctamente montado en el contenedor de la base de datos.
Peso: 25%
Implementación de endpoints CRUD con manejo de errores
La API debe implementar los cuatro endpoints requeridos: GET para listar todas las entidades, GET para recuperar una entidad por ID, POST para crear una entidad y DELETE para eliminar una entidad por ID. Los endpoints deben devolver código HTTP 404 cuando se intente acceder a una entidad que no existe. Los endpoints POST deben devolver código HTTP 400 cuando los datos proporcionados no sean válidos (por ejemplo, tipos de datos incorrectos o campos requeridos faltantes).
Peso: 25%
Logging y conectividad con base de datos
La aplicación debe implementar logging que registre al menos las operaciones principales (creación, lectura, eliminación de entidades) y errores que ocurran. Los logs deben ser visibles al ejecutar docker compose logs. La aplicación debe conectarse correctamente a la base de datos utilizando el nombre del servicio como hostname. Los datos creados mediante POST deben persistirse en la base de datos y ser recuperables mediante GET.
Peso: 25%

Tecnologia a utilizar
FastrAPI
Docker