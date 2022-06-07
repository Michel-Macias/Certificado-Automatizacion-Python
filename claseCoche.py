'''Clase Car con atributos definidos por el metodo __init__
   Contiene otros metodos que iremos documentando a posteriori
   '''


class Car:
    __potencia = 0
    stock = {}
    def __init__(self, largochasis, anchochasis, puertas, marca, nombre):
        self.largochasis = largochasis
        self.anchochasis = anchochasis
        self.puertas = puertas
        self.marca = marca
        self.nombre = nombre
        
        
    def __str__(self) :
        cadena =  "El coche creado es un " + self.marca + " y su nombre comercial es " +  self.nombre + "." + " \nTiene un chasis de " + str(self.anchochasis) + "cm de ancho y " + str(self.largochasis) + "cm de largo y tiene " + str(self.puertas) + " puertas.\nSu potencia es de " + str(self.__potencia)+"\n"
        return cadena
 
    
    def modif_potencia(self, potencia):
        self.__potencia = potencia
        
    
          
car1 = Car(350, 160, 3,"Audi", "A4")
car1.modif_potencia(180)
car2 = Car(420 ,150, 5, "BMW", "M5 Sedan")
car2.modif_potencia(360)
print(car1, car2)