from Crypto.PublicKey import RSA

def generate_key_pair():
    keyPair = RSA.generate(1024)
    nModule = keyPair.n
    publicKey = keyPair.e
    privateKey = keyPair.d

    return nModule, publicKey, privateKey