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

    #Método para registrar la temperatura
    def registrar_temperatura(self, temperatura, escala):
        self.temperaturas.append(temperatura)
        self.escalas.append(escala)
       
       
    #Método para hacer la conversion
    def conversion(self, temperatura, escala):
        
        #Ciclo for para los cálculos de conversion
        for i, escala in enumerate(self.escalas):

            temperatura = self.temperaturas[i]

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

    #Método para el display
    def display(self):
        print(f"{"-" * 10} LISTA DE CONVERSIONES {"-" * 10}")
        print(f"Original {" " * 16} Convertido")
        for i, conversion in enumerate(self.temperaturas):
            #Display que permite desplegar las conversiones y temperatura, estas temperaturas tendrán un despliegue de tan solo 2 números decimales después del punto
            print(f"#{i + 1}: {self.temperaturas[i]:.2f}, escala: {self.escalas[i]} -> {self.conversiones[i]:.2f}, escala: {self.conversionesescalas[i]}")

#--------------------------------------------------------------------------#

#Función Main
#--------------------------------------------------------------------------#
def main():
    #Inicializando el objeto que utiliza la clase
    conversion = ConversorTemperatura()

    print(f"{"=" * 20} Conversor De Temperaturas {"=" * 20}")
    cantidad = int(input("\n ¿Cuántas temperaturas quieres registrar?: "))
    #Ciclo para pedirle al usuario que entre la cantidad de temperaturas que quiera realizar:
    while True:
        try:
        

            for i in range(cantidad):
                temperatura = float(input(f"Introduce la temperatura #{i + 1}: "))
                
                while True:
                    escala = input("Introduce la escala (C o F): ")
                    escala = escala.upper()
                    if escala in ["C", "F"]:
                        conversion.registrar_temperatura(temperatura, escala)
                        print(f"La temperatura #{i + 1} {temperatura}: {escala} se ha añadido exitosamente")
                        break
                    else:
                        print("Escala no válida. Usa C, F")
           
        
               
            conversion.conversion(temperatura, escala)
            conversion.display()
            break
        except ValueError:
            print("Entrada inválida, introduce un número válido.")


#--------------------------------------------------------------------------#

#Llamando la función Main
main()