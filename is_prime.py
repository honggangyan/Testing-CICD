def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        # If n is divisible by i, it's not prime
        if n % i == 0:
            return False
    # If no divisors found, n is prime
    return True

