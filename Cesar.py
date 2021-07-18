#import nltk as nltk
import operator

ESPDICT = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
ENDICT = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
DICT64 = ENDICT + ENDICT.lower() + '0123456789/.'
CHARSREMOVE = [' ', '.', ',', '(', ')']


# Funcion para encriptar y desencriptar cifrado Cesar
def caesarEncrypt(plainText, key, alphabet = ESPDICT):
    mod = len(alphabet)

    plainText = plainText \
    .upper() \
    .replace('Á','A') \
    .replace('É','E') \
    .replace('Í','I') \
    .replace('Ó','O') \
    .replace('Ú','U') \
    .replace(' ','')

    result = ''
    for n in plainText:
        result += alphabet[(alphabet.index(n) + key)%mod]

    print(result)
    
    

# Funcion para encriptar y desencriptar cifrado Cesar
def caesarDecrypt(cyphredText, key, alphabet = ESPDICT):
    mod = len(alphabet)

    result = ''
    for n in cyphredText:
        result += alphabet[(alphabet.index(n) - key)%mod]

    return result
    


#Vignere Encrypt
def vignereEncrypt(cyphredText, key, alphabet = ESPDICT):

    cyphredText = cyphredText \
    .upper() \
    .replace('Á','A') \
    .replace('É','E') \
    .replace('Í','I') \
    .replace('Ó','O') \
    .replace('Ú','U') \
    .replace(' ','') \
    .replace('.','') \
    .replace('(','') \
    .replace(')','') \
    .replace(',','')

    keyCount = 0
    result = ''
    mod = len(alphabet)
    for n in cyphredText:
        result += alphabet[(alphabet.index(n)+ alphabet.index(key[keyCount]))%mod]
        keyCount = (keyCount + 1) %len(key)
    return result


#Vignere Decrypt
def vignereDencrypt(cyphredText, key, alphabet = ESPDICT):
    keyCount = 0
    result = ''
    mod = len(alphabet)
    for n in cyphredText:
        result += alphabet[(alphabet.index(n)- alphabet.index(key[keyCount]))%mod]
        keyCount = (keyCount + 1) %len(key)
    return result


frecuencias = {'A': 11.525, 'B': 2.215, 'C': 4.019, 'D': 5.01, 'E': 12.181, 'F': 0.692, 'G': 1.768, 'H': 0.703, 'I': 6.247, 'J': 0.493, 'K': 0.011, 'L': 4.967, 'M': 3.157, 'N': 6.712, 'O': 8.683, 'P': 2.51,
              'Q': 0.877, 'R': 6.871, 'S': 7.977, 'T': 4.632, 'U': 2.927, 'V': 1.138, 'W': 0.017, 'X': 0.215, 'Y': 1.008, 'Z': 0.467, 'á': 0.502, 'é': 0.433, 'í': 0.725, 'Ñ': 0.311, 'ó': 0.827, 'ú': 0.168, 'ü': 0.012}


# Desencriptar por fuerza Bruta el cifrado de Cesar
def desencryptarFuerzaBruta(mensaje):
    x = 0
    resultado = {}
    while x < 27:
        x = x + 1
        ciphershift = int(x)
        stringdecrypted = ""
        for character in mensaje:
            position = ESPDICT.find(character)
            newposition = position-ciphershift
            if character in ESPDICT:
                stringdecrypted = stringdecrypted + ESPDICT[newposition]
            else:
                stringdecrypted = stringdecrypted + character
        ciphershift = str(ciphershift)
        #print("Key: " + ciphershift)
        frecuenciaDecrypted = calcDist(stringdecrypted)
        diccionario = {}
        total = 0
        for letra in ESPDICT:
            probabilidad = abs(int(frecuenciaDecrypted[letra]*100) - frecuencias[letra])
            diccionario[letra] = probabilidad
            total += probabilidad
        resultado[x] = total
    resultadoOrdenado = sorted(resultado.items(), key=operator.itemgetter(1), reverse = False)
    return resultadoOrdenado
        




        
    
    

############## Parte de probabilidades


def calcDist(text: str) -> dict:
    letras = {}
    totalLetras = len(text)
    upperText = text.upper()

    ## agregar cantidad de letras
    for x in upperText:
        if x not in letras:
            letras[x] = 0
        letras[x] += 1

    ## asignar probabilidad
    for key in letras:
        letras[key] = letras[key] / totalLetras

    ## agregar letras que no estaban en el texto y asignarles probabilidad 0
    for char in frecuencias:
        c = char.upper()
        if c not in letras:
            letras[c] = 0.0 

    return letras


#utilizando NLTK
# def calcDist2( texto, alphabet = ESPDICT ):
#     distribution = dict(nltk.FreqDist(texto))

#     for i in distribution.keys():
# ...     distribution[i] = distribution[i]/len(texto)

#     if (len(distribution) == len(alphabet)):
        
#         return distribution
#     else:
#         absentChars = set(alphabet) - set(distribution.keys())

#         for n in absentChars:
#             distribution[n] = 0
        
#         return distribution




def most_common(letrasDict: dict, limit: int) -> dict:
    return dict(sorted(letrasDict.items(), key=lambda item: item[1], reverse=True)[0:limit])