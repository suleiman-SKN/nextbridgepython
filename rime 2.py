def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
        i = i + 2

    return True

is_prime(7)

def prime_generator():
    n =3
    while True:
        n += 1
        if is_prime(n):
            yield n
generator = prime_generator()

for i in range(2, 10):
    print(i, next(generator))

#__________________________________________________________
#prime function
"""For all numbers True, unless stated otherwise"""
def isprime():
    if n == 1:
        return False
    else:
        for d in range(2, n):
            if n%d==0:
                return False
    return True

for n in range(1,21):
    print(n, isprime())