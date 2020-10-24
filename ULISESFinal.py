class Automovil():

    def __init__(self, color, llantas):
        self.color = color
        self.llantas = llantas

    def __str__(self):
        return "color {}, {} llantas".format( self.color, self.llantas )


class Carro(Automovil):

    def __init__(self, color, llantas, velocidad, cilindrada):
        super().__init__(color, llantas)  
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(
            self.velocidad, self.cilindrada)


# Parte 1 #

class Camioneta(Carro):

    def __init__(self, color, llantas, velocidad, cilindrada, carga):
        super().__init__(color, llantas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return super().__str__() + ", {} kg de carga".format(self.carga)


class Bicicleta(Automovil):

    def __init__(self, color, llantas, tipo):
        super().__init__(color, llantas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + ", {}".format(self.tipo)


class Motocicleta(Bicicleta):

    def __init__(self, color, llantas, tipo, velocidad, cilindrada):
        super().__init__(color, llantas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(
            self.velocidad, self.cilindrada) 


# Parte 2 #

def catalogar(Automovil, llantas=None):
    if llantas != None:
        contador = 0
        for v in Automovil:
            if v.llantas == llantas: 
                contador += 1
        print("\nSe han encontrado {} Automovil con {} llantas:".format(
            contador, llantas))

    # Parte 3 #
    for v in Automovil:
        if llantas == None:
            print(type(v).__name__, v)
        else:
            if v.llantas == llantas:
                print(type(v).__name__, v)

# Parte 4 #
lista = [
    Carro("azul", 4, 150, 1200),
    Camioneta("blanco", 4, 100, 1300, 1500),
    Bicicleta("verde", 2, "urbana"),
    Motocicleta("negro", 2, "deportiva", 180, 900)
]

catalogar(lista,   )
catalogar(lista, 0)
catalogar(lista, 2)
catalogar(lista, 4)