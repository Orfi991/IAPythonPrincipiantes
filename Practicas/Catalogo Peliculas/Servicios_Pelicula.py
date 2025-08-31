# Servicios de la clase Pelicula: agregar, listar, eliminar
# se trabaja con archivos
# usar clase Pelicula
import os

class Servicio_Peliculas:
    def __init__(self):
        self.nombre_archivo = 'peliculas.txt'

    def agregar_pelicula(self, pelicula):
        with open(self.nombre_archivo, 'a', encoding='utf-8') as archivo:
            archivo.write(str(pelicula) + '\n')


    def listar_peliculas(self):
        with open(self.nombre_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                print(linea.strip())


    def eliminar_pelicula(self, pelicula):
        with open(self.nombre_archivo, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
        with open(self.nombre_archivo, 'w', encoding='utf-8') as archivo:
            for linea in lineas:
                if linea.strip() != str(pelicula):
                    archivo.write(linea)
        print(f"Pelicula '{pelicula}' eliminada correctamente.")        