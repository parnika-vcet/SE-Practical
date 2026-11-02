a = int(input("Enter a: "))
b = int(input("Enter b: "))

if a > b:
    max_value = a
else:
    max_value = b

if max_value > 0:
    print("Positive")
else:
    print("Non-positive")



# Enter a: 5
# Enter b: 3
# Positive

# Enter a: 2
# Enter b: 7
# Positive

# Enter a: -1
# Enter b: -5
# Non-positive