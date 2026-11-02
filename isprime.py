n = int(input("Enter n: "))

i = 2
is_prime = True

while i <= n / 2:
    if n % i == 0:
        is_prime = False
        break
    i = i + 1

print(is_prime)

# Enter n: 3
# True

# Enter n: 8
# False

# Enter n: 7
# True