from datetime import datetime
import statistics

class Experimento:
    #Se establece metodo constructor
    def __init__(self, nombreExperimento, fechaRealización, tipoExperimento, resultado):
        self.nombreExperimento = nombreExperimento
        self.fechaRealización = fechaRealización
        self.tipoExperimento = tipoExperimento
        self.resultado = resultado

#Metodo para agregar expermento
def agregarExperimento(listaExperimento):
    print("\n--- Agregar nuevo experimento ---")
    nombreExperimento = input("Nombre del experimento: ").strip()
    fechaRealizaciónstr = input("Fecha de realización (DD/MM/AAAA): ").strip()
    try:
        fechaRealización = datetime.strptime (fechaRealizaciónstr, "%d/%m/%Y")
    except ValueError:
        print("Fecha no valida")
        return
    tipoExperimento = input("Tipo de experimento (Química, Biología, Física): ").strip().upper()
    if tipoExperimento not in ["QUIMICA", "BIOLOGIA", "FISICA"]:
        print("Error: Tipo de experimento no válido.")
        return
    resultado_str =input("Ingresar resultado (ej. 12.5, 14.3): ")
    try:
        resultado = list(map(float, resultado_str.split(',')))
    except ValueError:
        print("Error: Los resultados deben ser números separados por comas.")
        return

    experimento = Experimento(nombreExperimento, fechaRealización,  tipoExperimento, resultado)
    listaExperimento.append(experimento)
    print(f"¡Experimento '{nombreExperimento}' agregado con éxito!")

#Metodo que nos permite visualizar los experimentos registrados
def visualizarExperimento(listaExperimento):
    if not listaExperimento:
        print("No hay experimentos registrados")
        return

    for i, experimento in enumerate(listaExperimento, start=1):
        print(f"\nExperimento {i}")
        print(f"Nombre: {experimento.nombreExperimento}")
        print(f"Fecha de realizacion: {experimento.fechaRealización.strftime('%d/%m/%Y')}")
        print(f"Tipo de experimento: {experimento.tipoExperimento}")
        print(f"resultado: {experimento.resultado}")

#Analisis de resultados
def AnalisisResultado(listaExperimento):
    if not listaExperimento:
        print("No hay experimentos registardos")
        return

    for experimento in listaExperimento:
        promedio = statistics.mean(experimento.resultado)
        maximo = max(experimento.resultado)
        minimo = min(experimento.resultado)
        print(f"\nanalisis de experimento{experimento.nombreExperimento}")
        print(f"promedio de horas:{promedio}")
        print (f"resultado maximo:{maximo}")
        print(f"resultado minimo:{minimo}")

#Metodo que genere informe en formato txt
def InformeFinal(listaExperimento):
    if not listaExperimento:
        print("No hay experimentos registrados")
        return

    with open("informe_experimentos.txt", "w") as archivo:
        for experimento in listaExperimento:
            archivo.write(f"Nombre: {experimento.nombreExperimento}\n")
            archivo.write(f"Fecha de realizacion: {experimento.fechaRealización.strftime('%d/%m/%Y')}\n")
            archivo.write(f"Tipo de experimento: {experimento.tipoExperimento}\n")
            archivo.write(f"Resultado: {experimento.resultado}\n")
            archivo.write("\n")
    print("Informe generado como 'informe_tareas.txt' ")

def menu():

    listaExperimento = []
    while True:
        print("\n--- Proyecto de Investigación Científica ---")
        print("1. Ingresar datos experimentales")
        print("2. Visualizar experimentos registrados")
        print("3. Analizar datos")
        print("4. Generar informe")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregarExperimento(listaExperimento)
        elif opcion == "2":
            visualizarExperimento(listaExperimento)
        elif opcion == "3":
            AnalisisResultado(listaExperimento)
        elif opcion == "4":
            InformeFinal(listaExperimento)
        elif opcion == "5":
            print("saliendo del programa....")
            break
        else:
            print("opcion invalida")

if __name__ == "__main__":
    menu()