import sys
from models.todo_list import TodoList

def main():
    todo = TodoList()

    while True:
        print("\n" + "="*30)
        print("   MENÚ TO-DO LIST MANAGER")
        print("="*30)
        print("1. Agregar una tarea")
        print("2. Listar todas las tareas")
        print("3. Marcar tarea como completada")
        print("4. Eliminar una tarea")
        print("5. Limpiar toda la lista")
        print("6. Salir")
        print("="*30)

        opcion = input("Seleccione una opción (1-6): ")

        if opcion == '1':
            tarea = input("\nIngrese el nombre de la nueva tarea: ")
            if tarea.strip():
                todo.add_task(tarea)
                print(f"Tarea '{tarea}' agregada exitosamente.")
            else:
                print("El nombre de la tarea no puede estar vacío.")

        elif opcion == '2':
            print("\n--- Lista Actual de Tareas ---")
            tasks = todo.all_tasks()
            if not tasks:
                print("(La lista está vacía)")

        elif opcion == '3':
            tarea = input("\nIngrese el nombre de la tarea a completar: ")
            if todo.mark_task_completed(tarea):
                print(f"Tarea '{tarea}' marcada como completada.")
            else:
                print(f"Error: La tarea '{tarea}' no se encuentra en la lista.")

        elif opcion == '4':
            tarea = input("\nIngrese el nombre de la tarea a eliminar: ")
            if todo.delete_task(tarea):
                print(f"Tarea '{tarea}' eliminada.")
            else:
                print(f"Error: La tarea '{tarea}' no existe.")

        elif opcion == '5':
            confirmacion = input("\n¿Está seguro de borrar TODAS las tareas? (s/n): ")
            if confirmacion.lower() == 's':
                todo.clear_list()
                print("La lista ha sido limpiada completamente.")
            else:
                print("Operación cancelada.")

        elif opcion == '6':
            print("\nSaliendo del sistema. ¡Hasta luego!")
            sys.exit()

        else:
            print("\nOpción no válida. Por favor intente de nuevo.")

if __name__ == "__main__":
    main()