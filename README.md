# 🪪 Proyecto de Carnetización Digital

---

### Transformando la identificación en una experiencia digital segura y moderna

**Carnetización Digital** es un sistema integral diseñado para optimizar la gestión de **identificación, acceso y asistencia** en instituciones, empresas y centros educativos.  
La plataforma permite **registrar organizaciones y usuarios**, **generar carnets digitales con código QR**, **controlar la asistencia mediante escaneo** y **administrar roles y permisos** de manera segura y eficiente.

El sistema se centra en la **automatización y digitalización de procesos**, eliminando el uso de documentación física y garantizando la **seguridad, disponibilidad y respaldo de la información**.  
Además, incorpora funciones de **personalización de carnets**, **carga masiva de usuarios**, **respaldo automático de datos** y **autenticación de doble factor**, asegurando un entorno confiable y adaptable a distintos contextos tecnológicos.

Su arquitectura está diseñada para ofrecer **rendimiento, compatibilidad y usabilidad**, permitiendo el acceso desde cualquier dispositivo o navegador, con una experiencia intuitiva para administradores, supervisores y usuarios finales.

---

## Repositorios del Proyecto

| Módulo | Repositorio | Descripción |
|:--|:--|:--|
| **Backend (.NET 8 / API REST)** | [CARNETIZACION-DIGITAL-BACK](https://github.com/IsabelTovar08/CARNETIZACION-DIGITAL-BACK.git) | Lógica del servidor, entidades, autenticación y conexión a base de datos. |
| **Frontend (Angular / Web)** | [CARNETIZACION-DIGITAL-FRONT](https://github.com/IsabelTovar08/CARNETIZACION-DIGITAL-FRONT.git) | Panel administrativo, gestión de usuarios y generación visual de carnets. |
| **Móvil (React Native / Expo)** | [CARNETIZACION-DIGITAL-MOVIL](https://github.com/IsabelTovar08/CARNETIZACION-DIGITAL-MOVIL.git) | Aplicación móvil para escaneo de QR y registro de asistencia. |

# Configuración de Puertos y URLs por Entorno

## **Backend (.NET / API)**

| Entorno   | Puerto | URL Swagger                                   |
|------------|---------|----------------------------------------------|
| **Develop** | 5100 | [http://localhost:5100/swagger/index.html](http://localhost:5100/swagger/index.html) |
| **QA**      | 5101 | [http://localhost:5101/swagger/index.html](http://localhost:5101/swagger/index.html) |
| **Staging** | 5105 | [http://localhost:5105/swagger/index.html](http://localhost:5105/swagger/index.html) |
| **Production** | 5103 | [http://localhost:5103/swagger/index.html](http://localhost:5103/swagger/index.html) |

---

## **Frontend (Angular)**

| Entorno   | Puerto | URL de acceso local |
|------------|---------|---------------------|
| **Develop** | 4300 | [http://localhost:4300/](http://localhost:4300/) |
| **QA**      | 4400 | [http://localhost:4400/](http://localhost:4400/) |
| **Staging** | 4500 | [http://localhost:4500/](http://localhost:4500/) |
| **Production** | 4600 | [http://localhost:4600/](http://localhost:4600/) |
