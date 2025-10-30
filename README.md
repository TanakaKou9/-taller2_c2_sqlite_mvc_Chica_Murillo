# 🎓 Gestor de Estudiantes MVC

## 🧩 Descripción general
**Gestor de Estudiantes MVC** es una aplicación desarrollada en **Python** que implementa el patrón de arquitectura **Modelo–Vista–Controlador (MVC)**.  
Su propósito es gestionar la información académica de los estudiantes a través de operaciones **CRUD** (crear, leer, actualizar y eliminar), garantizando una separación clara entre la lógica de negocio, la persistencia de datos y la interfaz con el usuario.  

El proyecto aplica los **principios SOLID**, promoviendo un código modular, escalable y fácil de mantener.  
Fue desarrollado como parte de una práctica académica orientada al diseño limpio y la aplicación del patrón MVC en proyectos reales.

---


## 🧩 **Estructura del proyecto**

```bash
gestor_estudiantes_mvc/
│
├── modelo/
│   ├── estudiante.py          # Persistencia y consultas SQL
│
├── controlador/
│   └── gestor.py              # Lógica de negocio (controlador principal)
│
├── vista/
│   └── vista.py               # Interfaz de usuario por consola
│
├── main.py 
│                           
└── README.md                 
```

## ⚙️ Funcionalidades principales

✅ Crear registros de estudiantes.  
✅ Listar todos los estudiantes registrados.  
✅ Actualizar la nota de un estudiante.  
✅ Eliminar registros según criterios definidos.  
✅ Buscar estudiantes por coincidencia parcial de nombre (usando `LIKE`).  
✅ Mostrar registros ordenados por nota descendente (`ORDER BY`).  
✅ Persistencia de datos mediante **SQLite**.  

---

## 🧠 Arquitectura aplicada

### 🧱 Modelo (M)
Encargado de la **persistencia de datos** y la ejecución de las sentencias SQL.  
Cumple el **principio de Responsabilidad Única (S)**, ya que se ocupa exclusivamente de manejar la base de datos.

### 🧭 Controlador (C)
Gestiona la **lógica de negocio** y coordina las acciones entre modelo y vista.  
Aplica los principios de **Inversión de Dependencia (D)** y **Abierto/Cerrado (O)**, facilitando la extensión del sistema sin modificar las clases existentes.

### 💬 Vista (V)
Proporciona una **interfaz de usuario por consola**, mostrando menús, mensajes y resultados.  
Respeta el **principio de Segregación de Interfaces (I)**, al no depender directamente del modelo.

---

## 🧩 Comandos SQL implementados

| Comando | Descripción |
|----------|--------------|
| `INSERT INTO` | Inserta nuevos registros en la base de datos |
| `SELECT * FROM` | Lista todos los registros disponibles |
| `UPDATE` | Permite modificar la nota de un estudiante |
| `DELETE` | Elimina registros con una condición (por ejemplo, nota < 3.0) |
| `ORDER BY nota DESC` | Muestra los estudiantes ordenados por nota descendente |
| `LIKE '%cadena%'` | Busca nombres que contengan una palabra específica |

---

## 🧠 Reflexión sobre el desarrollo*
El documento **`reflexion_mvc.pdf`** responde a las siguientes preguntas:
- Ventajas del patrón MVC en el desarrollo del proyecto.  
- Dificultades al separar responsabilidades entre modelo, vista y controlador.  
- Aprendizajes sobre el uso de **SQL** y su relación con la estructura del código.  
- Posibles mejoras y ampliaciones del sistema en futuras versiones.

---
## **👨‍💻 Autores**

_Daniela Murillo Castañeda_
_Chica Becerra_

📅 2025
🎓 Proyecto académico — Aplicación del patrón MVC en Python

“Dividir para conquistar: la esencia del diseño modular.”