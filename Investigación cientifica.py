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
def agregarExperimento(listaExperimentos):
    print("\n--- Agregar nuevo experimento ---")
    nombreExperimento = input("Nombre del experimento: ").strip()
    fechaRealizaciónstr = input("Fecha de realización (DD/MM/AAAA): ").strip()
    try:
        fechaRealización = datetime.strptime (fechaRealizaciónstr, "%d/%m/%Y")
    except ValueError:
        print("Fecha no valida")
        return
    tipoExperimento = input("Tipo de experimento (Química, Biología, Física): ").strip()
    if tipoExperimento not in ["Química", "Biología", "Física"]:
        print("Error: Tipo de experimento no válido.")
        return
    resultado =input("Ingresar resultado (ej. 12.5, 14.3): ")
    try:
        resultados = list(map(float, input("Resultados separados por coma (ej. 12.5, 14.3): ").split(',')))
    except ValueError:
        print("Error: Los resultados deben ser números separados por comas.")
        return

    experimento = Experimento(nombreExperimento, fechaRealización,  tipoExperimento, resultado)
    listaExperimentos.append(experimento)
    print(f"¡Experimento '{nombreExperimento}' agregado con éxito!")

#Metodo que nos permite visualizar los experimentos registrados
def visualizarExperimento(listaExperimentos):
    if not listaExperimentos:
        print("No hay experimentos registrados")
        return

    for i, experimento in enumerate(listaExperimentos, start=1):
        print(f"\nTa {i}")
        print(f"Nombre: {experimento.nombreExperimento}")
        print(f"Fecha de realizacion: {experimento.fechaRealización.strftime('%d/%m/%Y')}")
        print(f"Tipo de experimento: {experimento.tipoExperimento}")
        print(f"resultado: {experimento.resultado}")
