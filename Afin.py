import math as mt
ESPDICT = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
ENDICT = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

frecuencias = {'A': 11.525, 'B': 2.215, 'C': 4.019, 'D': 5.01, 'E': 12.181, 'F': 0.692, 'G': 1.768, 'H': 0.703, 'I': 6.247, 'J': 0.493, 'K': 0.011, 'L': 4.967, 'M': 3.157, 'N': 6.712, 'O': 8.683, 'P': 2.51,
               'Q': 0.877, 'R': 6.871, 'S': 7.977, 'T': 4.632, 'U': 2.927, 'V': 1.138, 'W': 0.017, 'X': 0.215, 'Y': 1.008, 'Z': 0.467, 'á': 0.502, 'é': 0.433, 'í': 0.725, 'Ñ': 0.311, 'ó': 0.827, 'ú': 0.168, 'ü': 0.012}


def calcDist(text: str) -> dict:
    letras = {}
    totalLetras = len(text)
    upperText = text.upper()

    # agregar cantidad de letras
    for x in upperText:
        if x not in letras:
            letras[x] = 0
        letras[x] += 1

    # asignar probabilidad
    for key in letras:
        letras[key] = (letras[key] / totalLetras) * 100

    # agregar letras que no estaban en el texto y asignarles probabilidad 0
    for char in frecuencias:
        c = char.upper()
        if c not in letras:
            letras[c] = 0.0

    return letras


def most_common(letrasDict: dict, limit: int) -> dict:
    return dict(sorted(letrasDict.items(), key=lambda item: item[1], reverse=True)[0:limit])


def gcd(a: int, b: int):
    while b != 0:
        a, b = b, a % b
    return a


def coprime(a: int, b: int):
    return gcd(a, b) == 1


def egcd(a: int, b: int):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y


def modinv(a: int, m: int):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None
    else:
        return x % m


def cifrar(texto: str, a: int = 1, k: int = 1, alphabet: dict = ESPDICT):
    mod = len(alphabet)
    textoCifrado = ''

    if coprime(a, mod):
        try:
            numEq = [alphabet.index(value) for value in texto.upper()]
            for i in range(len(numEq)):
                num = ((a * numEq[i]) + k) % mod
                textoCifrado += alphabet[num]
            return textoCifrado
        except ValueError:
            print('caracter no se encontro en el alfabeto asignado')
    else:
        print('El valor de \'a\' y el modulo del alfabeto no son coprimos')


def descifrar(texto: str,  a: int = 1, k: int = 1, alphabet: dict = ESPDICT):
    mod = len(alphabet)
    i = modinv(a, mod)
    textoDescifrado = ''

    if (i == None):
        print('No existe modulo inverso')
        return
    try:
        numEq = [alphabet.index(value) for value in texto.upper()]

        for n in numEq:
            num = (i * (n - k)) % mod
            textoDescifrado += alphabet[num]
        return textoDescifrado
    except ValueError:
        print('caracter no se encontro en el alfabeto asignado')


def descifrarFuerzaBruta(texto: str, alphabet: dict = ESPDICT, top: int = 20):
    mod = len(alphabet)
    desifrados = []
    frecAlpha = [(n[0].upper(), n[1]) for n in sorted(
        frecuencias.items(), key=lambda item: item[1], reverse=True)]

    for pA in range(mod):
        if (coprime(pA, mod)):
            for pK in range(mod):
                res = descifrar(texto, pA, pK, alphabet=alphabet)
                frecRes = dict(sorted(calcDist(res).items(),
                                      key=lambda item: item[1], reverse=True))
                pTotal = 0

                for n in frecAlpha:
                    probalibilidad = abs(frecRes[n[0]] - n[1])
                    pTotal += probalibilidad

                desifrados.append(
                    {'a': pA, 'k': pK, 'error': pTotal, 'descifrado': res})

    return sorted(desifrados, key=lambda item: item['error'])[0:top]
