from Crypto.PublicKey import RSA

def digitalSignature(message):
  message = bytes(message, 'utf-8')
  keyPair = RSA.generate(1024)
  nModule = keyPair.n
  publicKey = keyPair.e
  privateKey = keyPair.d

  #return publicKey, privateKey

  hash = int.from_bytes(bytes(calcular_sha256(message), "utf-8"), byteorder = 'big')
  #print(hash)

  # hashFromSignature = pow(signature, publicKey, nModule)
  # print(hashFromSignature)

  signature = pow(hash, privateKey, nModule)
  return signature

