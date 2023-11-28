#------------Envío de llaves--------------------

from sympy import primerange, mod_inverse

# Función para generar números primos
def generate_prime():
    primes = list(primerange(50, 200))
    return primes[0], primes[1]

# Función para calcular la clave pública
def calculate_public_key(base, private_key, prime):
    return pow(base, private_key, prime)

# Función para calcular la clave compartida
def calculate_shared_key(public_key, private_key, prime):
    return pow(public_key, private_key, prime)

# Generar números primos y bases
prime, base = generate_prime()

# Alice y Bob generan sus claves privadas
private_key_alice = 2  # Puede ser cualquier número secreto
private_key_bob = 10   # Puede ser cualquier número secreto

# Calcular las claves públicas de Alice y Bob
public_key_alice = calculate_public_key(base, private_key_alice, prime)
public_key_bob = calculate_public_key(base, private_key_bob, prime)

# Intercambio de claves públicas entre Alice y Bob
shared_key_alice = calculate_shared_key(public_key_bob, private_key_alice, prime)
shared_key_bob = calculate_shared_key(public_key_alice, private_key_bob, prime)

# Verificar que ambas partes obtienen la misma clave compartida
assert shared_key_alice == shared_key_bob

print(f"Clave compartida: {shared_key_alice}")