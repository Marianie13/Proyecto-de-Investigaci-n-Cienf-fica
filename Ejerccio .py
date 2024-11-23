
# Ejemplo de un menú básico
def mostrar_menu():
    print("\n--- Proyecto de Investigación Científica ---")
    print("1. Ingresar datos experimentales")
    print("2. Analizar datos")
    print("3. Generar informe")
    print("4. Salir")
    opcion = input("Elige una opción: ")
    return opcion

#Función Adregar datos exprimentales
def agregar_experimento(experimentos):
    print("\n--- Agregar nuevo experimento ---")
    nombre = input("Nombre del experimento: ").strip()
    fecha = input("Fecha de realización (DD/MM/AAAA): ").strip()
    tipo = input("Tipo de experimento (Química, Biología, Física): ").strip()
    
    # Validar tipo de experimento
    if tipo not in ["Química", "Biología", "Física"]:
        print("Error: Tipo de experimento no válido.")
        return

    # Capturar resultados como lista de números
    try:
        resultados = list(map(float, input("Resultados separados por coma (ej. 12.5, 14.3): ").split(',')))
    except ValueError:
        print("Error: Los resultados deben ser números separados por comas.")
        return

    # Agregar el experimento a la lista
    experimentos.append({
        "nombre": nombre,
        "fecha": fecha,
        "tipo": tipo,
        "resultados": resultados
    })
    print(f"¡Experimento '{nombre}' agregado con éxito!")

def main():
    experimentos = []  # Lista para almacenar los datos
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            # Lógica para ingresar datos
            pass
        elif opcion == "2":
            # Lógica para analizar datos
            pass
        elif opcion == "3":
            # Lógica para generar informe
            pass
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()