from opcional import practicaOpcional


def test_contar_vocales():
    cadena = practicaOpcional("Vamos a comprobar que funciona la clase opcional.py")
    assert cadena.contar_vocales() == 19


def test_contar_palabras():
    cadena = practicaOpcional(
        "Ahora, vamos a comprobar que funciona la clase opcional, así que venga, cuantas palabras tiene esta oracion campeón")
    assert cadena.contar_palabras() == 18
