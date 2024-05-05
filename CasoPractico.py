class Tarea:
    def __init__(self, descripcion):
        # Inicializa una nueva tarea con una descripción y la marca como no completada
        self.descripcion = descripcion
        self.completada = False

    def marcar_completada(self):
        # Marca la tarea como completada
        self.completada = True

    def __str__(self):
        # Devuelve una representación de cadena de la tarea, incluyendo su descripción y estado
        estado = "completada" if self.completada else "pendiente"
        return f"Tarea: {self.descripcion} ({estado})"


class GestorTareas:
    def __init__(self):
        # Inicializa el gestor de tareas con una lista vacía de tareas
        self.lista_tareas = []

    def agregar_tarea(self, descripcion):
        # Agrega una nueva tarea a la lista de tareas
        tarea = Tarea(descripcion)
        self.lista_tareas.append(tarea)
        print("Tarea agregada correctamente.")

    def marcar_tarea_como_completada(self, posicion):
        try:
            # Marca una tarea específica como completada, dado su índice en la lista
            tarea = self.lista_tareas[posicion]
            tarea.marcar_completada()
            print("Tarea marcada como completada correctamente.")
        except IndexError:
            print("La posición especificada no existe.")

    def mostrar_todas_tareas(self):
        # Muestra todas las tareas en la lista de tareas, numeradas y con su estado
        if self.lista_tareas:
            print("Lista de tareas:")
            for i, tarea in enumerate(self.lista_tareas):
                print(f"{i + 1}. {tarea}")
        else:
            print("No hay tareas pendientes.")

    def eliminar_tarea(self, posicion):
        try:
            # Elimina una tarea específica de la lista de tareas, dado su índice
            tarea_eliminada = self.lista_tareas.pop(posicion)
            print(f"Tarea '{tarea_eliminada.descripcion}' eliminada correctamente.")
        except IndexError:
            print("La posición especificada no existe.")


def main():
    # Función principal del programa
    gestor = GestorTareas()
    
    while True:
        # Menú de opciones para el usuario
        print("\n1. Agregar tarea")
        print("2. Marcar tarea como completada")
        print("3. Mostrar todas las tareas")
        print("4. Eliminar tarea")
        print("5. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            # Opción para agregar una nueva tarea
            descripcion = input("Ingrese la descripción de la tarea: ")
            gestor.agregar_tarea(descripcion)
        elif opcion == "2":
            # Opción para marcar una tarea como completada
            try:
                posicion = int(input("Ingrese la posición de la tarea a marcar como completada: "))
                gestor.marcar_tarea_como_completada(posicion)
            except ValueError:
                print("Error: Por favor, ingrese un número entero válido para la posición.")
        elif opcion == "3":
            # Opción para mostrar todas las tareas
            gestor.mostrar_todas_tareas()
        elif opcion == "4":
            # Opción para eliminar una tarea
            try:
                posicion = int(input("Ingrese la posición de la tarea a eliminar: "))
                gestor.eliminar_tarea(posicion)
            except ValueError:
                print("Error: Por favor, ingrese un número entero válido para la posición.")
        elif opcion == "5":
            # Opción para salir del programa
            print("Saliendo del programa...")
            break
        else:
            # Mensaje de error para opciones no válidas
            print("Opción no válida")


if __name__ == "__main__":
    # Llamada a la función principal cuando se ejecuta el script
    main()
