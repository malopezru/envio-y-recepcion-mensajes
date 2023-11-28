from sha256 import calcular_sha256

def digital_signature(message, module, privateKey):
  message = bytes(message, 'utf-8')
  hash = int.from_bytes(bytes(calcular_sha256(message), "utf-8"), byteorder = 'big')
  signature = pow(hash, privateKey, module)
  return signature

