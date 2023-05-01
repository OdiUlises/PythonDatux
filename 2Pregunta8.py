'''.Genear una funcion rango hasta un numero maximo (10^5), con un step y agregar a una lista
los números que cumplan las siguientes opciones , que sean primos.'''
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def generar_primos(maximo, step):
    primos = []
    for i in range(2, maximo, step):
        if es_primo(i):
            primos.append(i)
    return primos

primos = generar_primos(10**5, 1)
print(primos)