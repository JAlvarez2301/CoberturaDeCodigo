
'''
Primero creamos la funcion contar_vocales() que devuelve el numero de vocales de nuestro string
Creamos un for que recorra el string letra por letra, y si contiene aeioy se sumará 1 al contador

Despues, con el metodo split separamos las palabras de nuestro strin para que devuelvo un array, y con len
devuelve el numero de valores
'''
class practicaOpcional:

    cadena = ""

    def __init__(self, cadena):
        self.cadena = cadena


    def contar_vocales(self) -> int:
        contador = 0
        for letra in self.cadena:
            if letra.lower() in "aeiou":
                contador += 1
        return contador

    def contar_palabras(self) -> int:
        resultado = len(self.cadena.split())
        return resultado
