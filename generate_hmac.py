from sha256 import calcular_sha256
import operator

def hmac(key, message):
  blockSize = 516
  key = bytes(key, 'utf-8')
  message = bytes(message, 'utf-8')

  if len(key) > blockSize:
    key = calcular_sha256(key)
  elif len(key) < blockSize:
    key = key.ljust(blockSize, b'\x00')

  outerKeyPadding = bytes(map(operator.xor, key, [0x5c] * blockSize))
  innerKeyPadding = bytes(map(operator.xor, key, [0x36] * blockSize))
  innerHash = bytes(calcular_sha256(innerKeyPadding + message), "utf-8")
  outerHash = calcular_sha256(outerKeyPadding + innerHash)

  return outerHash