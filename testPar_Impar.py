from par_Impar import par_Impar

def test_add():
    listaNum = par_Impar([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
    listaNum.add(17)
    assert len(listaNum.numeros) == 17

def test_sumar_par():
    listaNum = par_Impar([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
    assert listaNum.sumarPar() == 72

def test_suma_ompares():
    listaNum = par_Impar([1,2,3,4,5,6,7,8,9,10,12,13,14,15,16])
    assert listaNum.sumaImpares() == 53

def test_cuadrado_lista():
    listaNum = par_Impar([1,2,3,4,5,6,7,8,9,10])
    assert listaNum.cuadradoLista() == [1,4,9,16,25,36,49,64,81,100]