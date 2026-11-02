n = int(input("Enter n: "))

if n > 0:
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")
else:
    print("Invalid")


# Enter n: -1
# Invalid

# Enter n: 2
# Even

# Enter n: 7
# Odd