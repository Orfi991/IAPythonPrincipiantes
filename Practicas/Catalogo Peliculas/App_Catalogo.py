from Pelicula import Pelicula
from Servicios_Pelicula import Servicio_Peliculas

class AppCatalogo:
    def __init__(self):
        self.servicio = Servicio_Peliculas()

    def menu(self):
        print("*** Bienvenido al Catálogo de Películas ***\n")

        while True:
            try:
                print(f"=== MENU ===\n"
                      f"1. Agregar película\n"
                      f"2. Listar películas\n"
                      f"3. Eliminar archivo de catálogo\n"
                      f"4. Salir\n")

                opcion = int(input("Seleccione una opción (1-4): "))
                if opcion == 1:
                    nombre_pelicula = input("Ingrese el nombre de la película: ")
                    pelicula = Pelicula(nombre_pelicula)
                    self.servicio.agregar_pelicula(pelicula)
                elif opcion == 2:
                    self.servicio.listar_peliculas()
                elif opcion == 3:
                    self.servicio.eliminar_archivo()
                    print("Catálogo de películas eliminado.\n")
                elif opcion == 4:
                    print("Saliendo del catálogo...")
                    break
                else:
                    print("Opción no válida. Intente de nuevo.\n")
            except ValueError:
                print("Por favor, ingrese un número válido.\n")
            except Exception as e:
                print(f"Error al mostrar el menú: {e}\n")

if __name__ == "__main__":
    app = AppCatalogo()
    app.menu()