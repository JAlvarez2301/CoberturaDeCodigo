class par_Impar:

    numeros: int = []

    def __init__(self, lista):
        self.numeros = lista

    def add(self, n: int):
        self.numeros.append(n)

    def suma_impares(self) -> int:
        suma_impares: int = 0
        for x in self.numeros:
            if x % 2 != 0:
                suma_impares += x
        return suma_impares

    def sumar_par(self) -> int:
        sumar_par: int = 0
        for x in self.numeros:
            if x % 2 == 0:
                sumar_par += x
        return sumar_par


    def cuadrado_lista(self):
        numeros_cuadrado: int = []
        for x in self.numeros:
            numeros_cuadrado.append(x*x)
        return numeros_cuadrado
