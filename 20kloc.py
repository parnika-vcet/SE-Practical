#Python code

# Basic COCOMO: Q5
kloc = 20
a, b, c, d = 2.4, 1.05, 2.5, 0.38
cost_per_person_month = 30000
 
effort = a * (kloc ** b)
time_months = c * (effort ** d)
total_cost = effort * cost_per_person_month
 
print(f"Effort: {effort:.2f} person-months")
print(f"Development time: {time_months:.2f} months")
print(f"Estimated cost: Rs. {total_cost:,.2f}")
