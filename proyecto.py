## Christian Matias Alvarez
## COMP 315 C4
## Introducción a los fundamentos de Python
## 23 de mayo de 2025



#--------------------------------------------------------------------------#

class ConversorTemperatura:

  #Inicializando la clase
    def __init__(self):
        self.temperaturas = []
        self.escalas = []
        self.conversiones = []
        self.conversionesescalas = []

    def registrar_temperatura(self, temperatura, escala):
        
        if escala not in ["C", "F"]:
            print("Escala no válida. Usa C, F")
            return
        
        self.temperaturas.append(temperatura)
        self.escalas.append(escala)

    def conversion(self, temperatura, escala):
        

        for i in enumerate(self.escalas):

    

            if escala == "C":
                conversion = (temperatura * 9/5) + 32
                self.conversiones.append(conversion)
                self.conversionesescalas.append("F")
                
            elif escala =="F":
                conversion = (temperatura - 32) * 5/9
                self.conversiones.append(conversion)
                self.conversionesescalas.append("C")
            else: 
                print(f"Hubo un error al intentar convertir la temperatura {temperatura}: {escala}")

    def display(self):
        print(f"{"-" * 10} LISTA DE CONVERSIONES {"-" * 10}")
        for i, conversion in enumerate(self.temperaturas):
            print(f"#{i}: {self.temperaturas[i]}, escala: {self.escalas[i]} / {self.conversiones[i]}, escala: {self.conversionesescalas[i]}")

#--------------------------------------------------------------------------#

#Función Main

def main():
    #Inicializando la clase:

    conversion = ConversorTemperatura()

    print(f"{"=" * 20} Conversor De Temperaturas {"=" * 20}")
    #Ciclo para pedirle al usuario que entre la cantidad de temperaturas que quiera realizar:
    while True:
        try:
            cantidad = int(input("\n ¿Cuántas temperaturas quieres registrar?: "))

            for i in range(cantidad):
                temperatura = float(input("Introduce la temperatura: "))
                escala = input("Introduce la escala (C o F): ")
                escala = escala.upper()
                conversion.registrar_temperatura(temperatura, escala)
                print(f"La temperatura #{i + 1} {temperatura}: {escala} se ha añadido exitosamente")
               
            conversion.conversion(temperatura, escala)
            continuar = input("¿Quieres registrar otra temperatura? (s/n): ").lower()
            if continuar != "s":
                conversion.display()
                break
        except ValueError:
            print("Entrada inválida, introduce un número válido.")




#Llamando la función Main
main()