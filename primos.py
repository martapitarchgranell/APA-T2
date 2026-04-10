"""
TASCA 2: APA CURS 2025-2026 Marta Pitarch Granell 

Primos.py: Mòdul de gestió de nombres primers

Tests unitaris:
>>> [ numero for numero in range(2, 50) if esPrimer(numero) ]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

>>> Primers(50)
(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)

>>> descompon(36 * 175 * 143)
(2, 2, 3, 3, 5, 5, 7, 11, 13)

>>> mcm(90, 14)
630

>>> mcd(924, 780)
12

>>> mcm(42, 60, 70, 63)
1260

>>> mcd(840, 630, 1050, 1470)
210
"""

def esPrimer(numero):
    """
    Retorna True si el nombre és primer i False si no ho és.
    Llança TypeError si l'argument no és un enter major que 1.
    """
    if type(numero) is not int or numero <= 1:
        raise TypeError("El nombre ha de ser enter i > 1")
    
    for prova in range(2, int(numero**0.5) + 1):
        if numero % prova == 0:
            return False
    return True

def Primers(numero):
    """
    Retorna una tupla amb els numeros primers menors que el seu argument.
    """
    nombres_primers = []
    for i in range(2, numero):
        if esPrimer(i):
            nombres_primers.append(i)
    return tuple(nombres_primers)

def descompon(numero):
    """
    Retorna una tupla amb la descomposició en factors primers del seu argument.
    """
    descomposicio_factors = []
    divisor = 2
    numero_reduit = numero
    
    while numero_reduit > 1:
        while numero_reduit % divisor == 0:
            descomposicio_factors.append(divisor)
            numero_reduit //= divisor
        divisor += 1
    return tuple(descomposicio_factors)

def mcm(*numeros):
    """
    Retorna el MCM dels seus arguments (accepta 2 o més números).
    """
    llista_de_nums_descomposats = []
    factors_totals = []

    for numero in numeros:
        num_descomposat = descompon(numero)
        llista_de_nums_descomposats.append(num_descomposat)
        for factor in num_descomposat:
            if factor not in factors_totals:
                factors_totals.append(factor)

    mcm_res = 1
    for factor in factors_totals:
        exp_max = 0
        for num_descomposat in llista_de_nums_descomposats:
            comptador = num_descomposat.count(factor)
            if comptador > exp_max:
                exp_max = comptador
        mcm_res *= (factor ** exp_max)

    return mcm_res

def mcd(*numeros):
    """
    Retorna el MCD dels seus arguments (accepta 2 o més números).
    """
    llista_de_nums_descomposats = [descompon(n) for n in numeros]
    
    # Busquem factors comuns a tots
    primer_num = llista_de_nums_descomposats[0]
    factors_comuns = []
    
    # Creem un conjunt de factors únics del primer número per provar
    for factor in set(primer_num):
        es_comu = True
        for i in range(1, len(llista_de_nums_descomposats)):
            if factor not in llista_de_nums_descomposats[i]:
                es_comu = False
                break
        if es_comu:
            factors_comuns.append(factor)

    mcd_res = 1
    for factor in factors_comuns:
        # Busquem l'exponent mínim entre tots els números
        exp_min = llista_de_nums_descomposats[0].count(factor)
        for i in range(1, len(llista_de_nums_descomposats)):
            comptador = llista_de_nums_descomposats[i].count(factor)
            if comptador < exp_min:
                exp_min = comptador
        mcd_res *= (factor ** exp_min)
        
    return mcd_res

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)