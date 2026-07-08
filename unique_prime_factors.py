def unique_prime_factors(n):
    factors = []

    # Check for factor 2
    if n % 2 == 0:
        factors.append(2)
        while n % 2 == 0:
            n //= 2

    # Check for odd factors
    i = 3
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            while n % i == 0:
                n //= i
        i += 2

    # If n is still greater than 2, it is a prime factor
    if n > 2:
        factors.append(n)

    return factors


# Input
n = int(input("Enter a number: "))

# Output
print("Unique Prime Factors:", unique_prime_factors(n))