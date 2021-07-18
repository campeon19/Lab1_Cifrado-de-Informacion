
ESPDICT = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
ENDICT = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
DICT64 = ENDICT + ENDICT.lower() + '0123456789/.'
CHARSREMOVE = [' ', '.', ',', '(', ')']

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



def getKeyLengths(cyphredData, alphabet = ESPDICT):
    mheight = 30 if len(cyphredData) > 30 else len(cyphredData)
    dataArray = []
    for m in range(mheight):
        for n in range(200):
            print('elpepe')

