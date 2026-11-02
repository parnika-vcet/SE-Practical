# Q18 calculations using coefficients supplied in the question
kloc = 32
a, b, c, d = 2.4, 1.05, 2.5, 0.38
counts = {"EI": 18, "EO": 14, "EQ": 10, "ILF": 8, "EIF": 5}
weights = {"EI": 4, "EO": 5, "EQ": 4, "ILF": 10, "EIF": 7}
ufp = sum(counts[k] * weights[k] for k in counts)
vaf = 1.05
afp = ufp * vaf
effort = a * (kloc ** b)
time_months = c * (effort ** d)
print("UFP:", ufp)
print("AFP:", afp)
print(f"Effort: {effort:.2f} person-months")
print(f"Development time: {time_months:.2f} months")