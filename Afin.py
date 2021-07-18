ESPDICT = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
ENDICT = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def getFactores(num):
    divisores = []
    for n in range(1, num + 1):
        div = (num / n) % 1
        if (not 0 > div) and (not 0 < div):
            divisores.append(n)
    return divisores

def relativePrimes(div1, div2):
    commonDivisores = [value for value in div1 if value in div2]
    if len(commonDivisores) > 1:
        return False
    return True

def egcd(a, b):
    x,y, u,v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y
 
def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None
    else:
        return x % m


def cifrar(texto, a=1, k=1, alphabet=ESPDICT):
    mod = len(alphabet)
    div1 = getFactores(mod)
    div2 = getFactores(a)
    textoCifrado = ''
    
    if relativePrimes(div1, div2):
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


def descifrar(texto,  a=1, k=1, alphabet=ESPDICT):
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