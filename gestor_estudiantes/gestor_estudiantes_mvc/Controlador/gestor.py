from gestor_estudiantes_mvc.Modelo.estudiante import Estudiante

class GestorEstudiantes:
    repo = Estudiante()   
    
    def agregar_estudiante(self, nombre, correo, nota):
        try:
            if not nombre or not correo:
                return "los datos no pueden ser casillas vacias"
            if not (0.0 <= nota <= 5.0):
                return "La nota debe estar entre 0.0 y 5.0."
        except Exception as e:
            return f"Datos invalidos: {e}"
        
        try:
            self.repo.agregar_estudiante(nombre, correo, nota)
            return "El estudiante fue añadido correctamente"
        except Exception as e:
            return f"No se pudo agregar el estudiante: {e}"
        
    def listar_estudiantes(self):
        return self.repo.listar_estudiantes()
    
    def actualizar_nota(self, nombre, nota):
        try:
            # Validar rango
            if not (0.0 <= nota <= 5.0):
                return "La nota debe estar entre 0.0 y 5.0."
            
            # Ejecutar actualización
            mensaje = self.repo.actualizar_nota(nombre, nota)
            return mensaje

        except Exception as e:
            return f"Error al actualizar la nota: {e}"

    def eliminar_registro_nombre(self, nombre):
        try:
            self.repo.eliminar_registro_nombre(nombre)
            return f"Estudiante {nombre} eliminado correctamente"
        except Exception as e:
            return f"No se pudo eliminar el estudiante: {e}"
        
    def eliminar_registro_nota(self, nota):
        try:
            self.repo.eliminar_registro_nota(umbral=nota)
            return f"Los estudiantes con notas inferiores a {nota} fueron eliminados."
        except Exception as e:
            return f"No se pudo eliminar el estudiante: {e}"
    
    def buscar_estudiantes(self, texto):
        try:
            return "Coincidencias: " + self.repo.buscar_estudiante(texto)
        except Exception as e:
            return f"No se pudo realizar la busqueda: {e}"
        
    def listar_por_nota(self):
            return "Listado por nota descendente\n " + self.repo.listar_estudiantes_nota()
        
    def consultar_estudiantes(self, nota):
        try:
            mensaje = f"\n[ INFO ] Estudiantes con nota >= {nota}"
            "\n--------------------------------------"
            return mensaje + self.repo.consultar_estudiantes(umbral=nota)
        except Exception as e:
            return f"No se pudo realizar la consulta: {e}"
        
    

        
