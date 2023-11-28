def calcular_sha256(datos):
    h0 = 0x6a09e667
    h1 = 0xbb67ae85
    h2 = 0x3c6ef372
    h3 = 0xa54ff53a
    h4 = 0x510e527f
    h5 = 0x9b05688c
    h6 = 0x1f83d9ab
    h7 = 0x5be0cd19
    k = [
        0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
        0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
        0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
        0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
        0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
        0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
        0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
        0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
    ]

    # Funciones auxiliares
    def rotr(n, x):
        return ((x >> n) | (x << (32 - n))) & 0xFFFFFFFF

    def ch(x, y, z):
        return (x & y) ^ (~x & z)

    def maj(x, y, z):
        return (x & y) ^ (x & z) ^ (y & z)

    def sigma0(x):
        return rotr(2, x) ^ rotr(13, x) ^ rotr(22, x)

    def sigma1(x):
        return rotr(6, x) ^ rotr(11, x) ^ rotr(25, x)

    def gamma0(x):
        return rotr(7, x) ^ rotr(18, x) ^ (x >> 3)

    def gamma1(x):
        return rotr(17, x) ^ rotr(19, x) ^ (x >> 10)

    longitud_bits = len(datos) * 8
    datos += b'\x80'

    while (len(datos) % 64) != 56:
        datos += b'\x00'

    datos += longitud_bits.to_bytes(8, byteorder='big')

    # Procesamiento del mensaje en bloques de 512 bits
    # Procesamiento del mensaje en bloques de 512 bits
    for i in range(0, len(datos), 64):
        bloque = datos[i:i + 64]

        palabras = [int.from_bytes(bloque[j:j + 4], byteorder='big') for j in range(0, 64, 4)]

        # Asegúrate de que la lista 'palabras' tenga al menos 64 elementos
        if len(palabras) < 64:
            palabras.extend([0] * (64 - len(palabras)))

        for j in range(16, 64):
            palabras[j] = (gamma1(palabras[j - 2]) + palabras[j - 7] + gamma0(palabras[j - 15]) + palabras[j - 16]) & 0xFFFFFFFF

        # Resto del código...


        a, b, c, d, e, f, g, h = h0, h1, h2, h3, h4, h5, h6, h7

        for j in range(64):
            temp1 = h + sigma1(e) + ch(e, f, g) + k[j] + palabras[j]
            temp2 = sigma0(a) + maj(a, b, c)
            h, g, f, e, d, c, b, a = (g + temp1) & 0xFFFFFFFF, f, e, (d + temp1) & 0xFFFFFFFF, (c + temp1) & 0xFFFFFFFF, b, a, (temp1 + temp2) & 0xFFFFFFFF

        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF
        h4 = (h4 + e) & 0xFFFFFFFF
        h5 = (h5 + f) & 0xFFFFFFFF
        h6 = (h6 + g) & 0xFFFFFFFF
        h7 = (h7 + h) & 0xFFFFFFFF

    hash_resultado = f"{h0:08x}{h1:08x}{h2:08x}{h3:08x}{h4:08x}{h5:08x}{h6:08x}{h7:08x}"

    return hash_resultado

# Tu texto o datos para los que deseas calcular el SHA
datos = "todos gays"

# Calcular el hash SHA-256
hash_resultado = calcular_sha256(datos.encode('utf-8'))

print("El hash SHA-256 es:", hash_resultado)