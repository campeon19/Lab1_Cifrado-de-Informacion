
ESPDICT = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
ENDICT = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
DICT64 = ENDICT + ENDICT.lower() + '0123456789/.'
CHARSREMOVE = [' ', '.', ',', '(', ')']
import nltk as nltk
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


frecuencias = {'A': 0.12027, 'B': 0.02215, 'C': 0.040190000000000003, 'D': 0.0501, 'E': 0.12613999999999997, 'F': 0.006919999999999999, 'G': 0.01768, 'H': 0.00703, 'I': 0.06972, 'J': 0.00493, 'K': 0.00010999999999999999, 'L': 0.04967, 'M': 0.03157, 'N': 0.06712, 'O': 0.0951, 'P': 0.025099999999999997, 'Q': 0.00877, 'R': 0.06871000000000001, 'S': 0.07977000000000001, 'T': 0.04632, 'U': 0.03107, 'V': 0.01138, 'W': 0.00017, 'X': 0.00215, 'Y': 0.01008, 'Z': 0.0046700000000000005, 'Ñ': 0.00311}


def calcDist2( texto, alphabet = ESPDICT ):
    distribution = dict(nltk.FreqDist(texto))

    for i in distribution.keys():
        distribution[i] = distribution[i]/len(texto)

    if (len(distribution) == len(alphabet)):
        
        return distribution
    else:
        absentChars = set(alphabet) - set(distribution.keys())

        for n in absentChars:
            distribution[n] = 0
        
        return distribution

def calculateDistError(experimental, theoretical = frecuencias):
    error = 0
    for n in theoretical:
        error += abs(experimental[n] - theoretical[n])
    return error




def calculateProbableKeys(cipherText, alphabet = ESPDICT):
    keys = []
    tent = ''
    for y in alphabet:
        tent = y
        err = calculateDistError(calcDist2(vignereDencrypt(cipherText,tent)))
        if(len(keys) <=10):
            keys.append((tent,err))
        else:
            for w in range(len(keys)):
                if(err < keys[w][1]):
                    keys[w] = (tent,err)
                    break
                
    for x in alphabet:
        for y in alphabet:
            tent = x+y
            err = calculateDistError(calcDist2(vignereDencrypt(cipherText,tent)))
            for w in range(len(keys)):
                if(err < keys[w][1]):
                    keys[w] = (tent,err)
                    break

    for n in alphabet:
        for x in alphabet:
            for y in alphabet:
                tent = n+x+y
                err = calculateDistError(calcDist2(vignereDencrypt(cipherText,tent)))
                for w in range(len(keys)):
                    if(err < keys[w][1]):
                        keys[w] = (tent,err)
                        break

    for m in alphabet:
        for n in alphabet:
            for x in alphabet:
                for y in alphabet:
                    tent = m+n+x+y
                    err = calculateDistError(calcDist2(vignereDencrypt(cipherText,tent)))
                    for w in range(len(keys)):
                        if(err < keys[w][1]):
                            keys[w] = (tent,err)
                            break
    
    return keys


