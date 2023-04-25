from opcional import opcional


def test_contar_vocales():
    cadena = opcional("Vamos a comprobar que funciona la clase opcional.py")
    assert cadena.contarVocales() == 19


def test_contar_palabras():
    cadena = opcional(
        "Ahora, vamos a comprobar que funciona la clase opcional, así que venga, cuantas palabras tiene esta oracion campeón")
    assert cadena.contarPalabras() == 18
