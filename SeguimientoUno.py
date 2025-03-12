
import os


def cargar_notas():
    """
    Carga las notas desde un archivo llamado 'notas.txt'.
    Si el archivo existe, devuelve una lista de notas.
    Si no existe, devuelve una lista vacía.
    """
    if os.path.exists("notas.txt"):
        with open("notas.txt", "r") as archivo:
            return [line.strip() for line in archivo.readlines()]
    return []


def guardar_notas(notas):
    """
    Guarda las notas en un archivo llamado 'notas.txt'.
    Cada nota se almacena en una línea separada.
    """
    with open("notas.txt", "w") as archivo:
        for nota in notas:
            archivo.write(nota + "\n")


def ver_notas(notas):
    """
    Muestra todas las notas guardadas.
    Si no hay notas, informa al usuario.
    """
    if notas:
        print("\n--- Notas ---")
        for i, nota in enumerate(notas, 1):
            print(f"{i}. {nota}")
    else:
        print("\nNo hay notas disponibles.")


def agregar_nota(notas):
    """
    Permite al usuario ingresar una nueva nota y la agrega a la lista.
    """
    nueva_nota = input("Ingrese la nueva nota: ")
    notas.append(nota=nueva_nota)
    print("Nota agregada correctamente.")


def eliminar_nota(notas):
    """
    Permite al usuario eliminar una nota específica.
    Valida que el índice ingresado sea correcto.
    """
    ver_notas(notas)
    if notas:
        try:
            indice = int(input("Ingrese el número de la nota que desea eliminar: ")) - 1
            if 0 <= indice < len(notas):
                nota_eliminada = notas.pop(indice)
                print(f"Nota eliminada: {nota_eliminada}")
            else:
                print("Índice inválido.")
        except ValueError:
            print("Por favor, ingrese un número válido.")


def actualizar_nota(notas):
    """
    Permite al usuario actualizar el contenido de una nota específica.
    Valida que el índice ingresado sea correcto.
    """
    ver_notas(notas)
    if notas:
        try:
            indice = int(input("Ingrese el número de la nota que desea actualizar: ")) - 1
            if 0 <= indice < len(notas):
                nueva_nota = input("Ingrese el nuevo contenido de la nota: ")
                notas[indice] = nueva_nota
                print("Nota actualizada correctamente.")
            else:
                print("Índice inválido.")
        except ValueError:
            print("Por favor, ingrese un número válido.")


def main():
    """
    Función principal del programa.
    Coordina el flujo del programa y presenta un menú interactivo.
    """
    # Cargar notas existentes
    notas = cargar_notas()

    while True:
        print("\n--- Gestión de Notas ---")
        print("1. Ver todas las notas")
        print("2. Agregar una nueva nota")
        print("3. Eliminar una nota")
        print("4. Actualizar una nota")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ver_notas(notas)
        elif opcion == "2":
            agregar_nota(notas)
        elif opcion == "3":
            eliminar_nota(notas)
        elif opcion == "4":
            actualizar_nota(notas)
        elif opcion == "5":
            guardar_notas(notas)
            print("Notas guardadas. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()
