import sqlite3

class Estudiante:
    """Clase que maneja los metodos relacionados a la persistencia
    """
    def __init__(self, nombre_bd: str = "estudiantes.db"):
        self.nombre_bd = nombre_bd
        self._crear_base()

    def _crear_base(self) -> None:
        """Crea la base de datos y la tabla si no existen."""
        with sqlite3.connect(self.nombre_bd) as conn:
            cur = conn.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS estudiantes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    correo TEXT NOT NULL UNIQUE,
                    nota REAL
                )
            """)
            conn.commit()

    def agregar_estudiante(self, nombre, correo, nota):
        """Agrega un nuevo estudiante a la base de datos

        Args:
            nombre (str): Nombre del estudiante a insertar
            correo (str): Correo del estudiante a insertar
            nota (float): Nota del estudiante a insertar
        """
        with sqlite3.connect(self.nombre_bd) as conn:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO estudiantes (nombre, correo, nota) VALUES (?, ?, ?)",
                (nombre, correo, nota)
            )
            conn.commit()

    def listar_estudiantes(self):
        """Lista todos los estudiantes ordenados por nombre.

        Returns:
            str: lista de estudiantes en la base
        """
        
        with sqlite3.connect(self.nombre_bd) as conn:
            cur = conn.cursor()
            cur.execute("SELECT nombre, correo, nota FROM estudiantes ORDER BY nombre ASC")
            resultados = cur.fetchall()

        mensajeListar = ""
        for nombre, correo, nota in resultados:
            mensajeListar += f"{nombre:15s} | {correo:25s} | {nota:.2f}\n"
        return mensajeListar if mensajeListar else "No hay estudiantes registrados."

    def actualizar_nota(self, nombre, nota):
        """Actualiza la nota de un estudiante mediante su nombre
        
        Args:
            nombre (str): Nombre del estudiante a actualizar
            nota (float): Nota nueva del estudiante a actualizar
        """
    def actualizar_nota(self, nombre, nota):
        """Actualiza la nota de un estudiante mediante su nombre"""
        with sqlite3.connect(self.nombre_bd) as conn:
            cur = conn.cursor()
            cur.execute("""
                    UPDATE estudiantes
                    SET nota = ?
                    WHERE nombre = ? COLLATE NOCASE
                """, (nota, nombre))
            conn.commit()
            filas = cur.rowcount

            if filas > 0:
                return f"Nota del estudiante '{nombre}' actualizada correctamente."
            else:
                return f"No se encontró ningún estudiante llamado '{nombre}'."

    def eliminar_registro_nombre(self, nombre):
        """Elimina un estudiante por su nombre
        
        Args:
            nombre (str): Nombre del estudiante a eliminar
        
        Verifica que el nombre sea válido y confirma la cantidad de filas afectadas."""
        if not nombre.strip():
            print("[ERROR] El nombre no puede estar vacío.")
            return

        with sqlite3.connect(self.nombre_bd) as conn:
            cur = conn.cursor()
            cur.execute("DELETE FROM estudiantes WHERE nombre = ?", (nombre,))
            conn.commit()
            filas = cur.rowcount

        if filas > 0:
            print(f"[OK] Se eliminó {filas} registro(s) con el nombre '{nombre}'.")
        else:
            print(f"[INFO] No se encontró ningún estudiante llamado '{nombre}'.")


    def eliminar_registro_nota(self, umbral):
        """Elimina todos los estudiantes con nota menor al umbral.
        
        Args:
            umbral (float): Nota limite para eliminar los estudiantes
        """
        with sqlite3.connect(self.nombre_bd) as conn:
            cur = conn.cursor()
            cur.execute("DELETE FROM estudiantes WHERE nota < ?", (umbral,))
            conn.commit()
            return cur.rowcount

    def buscar_estudiante(self, texto):
        """Busca estudiantes cuyo nombre contenga el texto indicado.
        
        Args:
            texto (str): Caracter o cadena clave para realizar la busqueda
        """
        with sqlite3.connect(self.nombre_bd) as conn:
            cur = conn.cursor()
            cur.execute("SELECT nombre, correo, nota FROM estudiantes WHERE nombre LIKE ?", (f"%{texto}%",))
            resultados = cur.fetchall()

        mensajeBuscar = ""
        for nombre, correo, nota in resultados:
            mensajeBuscar += f"{nombre:15s} | {correo:25s} | {nota:.2f}\n"
        return mensajeBuscar if mensajeBuscar else "No se encontraron coincidencias."

    def listar_estudiantes_nota(self):
        """Lista los estudiantes ordenados por nota descendente.

        Returns:
            str: lista de estudiantes en la base ordenada en forma descendente de las notas
        """
        with sqlite3.connect(self.nombre_bd) as conn:
            cur = conn.cursor()
            cur.execute("SELECT nombre, nota FROM estudiantes ORDER BY nota DESC")
            resultados = cur.fetchall()

        mensajeListarN = ""
        for nombre, nota in resultados:
            mensajeListarN += f"{nombre:15s} | {nota:.2f}\n"
        return mensajeListarN if mensajeListarN else "No hay registros disponibles."

    def consultar_estudiantes(self, umbral):
        """Consulta estudiantes con nota mayor o igual al umbral.
        
        Args:
            umbral (float): Nota limite para consultar los estudiantes
        """
        with sqlite3.connect(self.nombre_bd) as conn:
            cur = conn.cursor()
            cur.execute("SELECT nombre, nota FROM estudiantes WHERE nota >= ?", (umbral,))
            resultados = cur.fetchall()

        mensajeConsultar = ""
        for nombre, nota in resultados:
            mensajeConsultar += f"{nombre:15s} | {nota:.2f}\n"
        return mensajeConsultar if mensajeConsultar else "No hay estudiantes con nota en ese rango."

    def existe_correo(self, correo):
        """Verifica si ya existe un estudiante con el correo dado.
        
        Args:
            correo (str): Correo del estudiante
        """
        with sqlite3.connect(self.nombre_bd) as conn:
            cur = conn.cursor()
            cur.execute("SELECT 1 FROM estudiantes WHERE correo = ?", (correo,))
            existe = cur.fetchone() is not None
        return existe
