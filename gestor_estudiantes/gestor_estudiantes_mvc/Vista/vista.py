from gestor_estudiantes_mvc.Controlador.gestor import GestorEstudiantes

class Vista:
    def __init__(self):
        self.gestor = GestorEstudiantes()

    def mostrar_menu(self):
            print("\n      Menú      ")
            print("1. Agregar estudiante")
            print("2. Listar estudiantes")
            print("3. Actualizar nota")
            print("4. Eliminar registro por nombre")
            print("5. Eliminar registro por nota")
            print("6. Buscar por nombre")
            print("7. Listar por nota descendente")
            print("8. Consultar estudiantes por nota")
            print("9. Salir")

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción:")
            if opcion == "1":
                nombre = input("Nombre: ")
                correo = input("Correo: ")
                nota = float(input("Nota: "))
                print(self.gestor.agregar_estudiante(nombre, correo, nota))

            elif opcion == "2":
                print(self.gestor.listar_estudiantes())

            elif opcion == "3":
                nombre = input("Nombre del estudiante a actualizar: ")
                nota = float(input("Nota nueva: "))
                print(self.gestor.actualizar_nota(nombre, nota))

            elif opcion == "4":
                nombre = input("Nombre del estudiante a eliminar: ")
                print(self.gestor.eliminar_registro_nombre(nombre))

            elif opcion == "5":
                nota = input("Eliminar estudiantes con nota menor a: ")
                print(self.gestor.eliminar_registro_nota(nota))

            elif opcion == "6":
                texto = input("Buscar nombre que contenga: ")
                print(self.gestor.buscar_estudiantes(texto))

            elif opcion == "7":
                print(self.gestor.listar_por_nota())

            elif opcion == "8":
                nota = input("Ingrese la nota a consultar")
                print(self.gestor.consultar_estudiantes(nota))
                
            elif opcion == "9":
                print("Saliendo del programa...")
                break

            else:
                print("Opción inválida. Intente nuevamente")

