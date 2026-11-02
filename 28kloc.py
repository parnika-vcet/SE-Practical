# Q19: COCOMO and LOC method
kloc = 28
a, b, c, d = 2.4, 1.05, 2.5, 0.38
productivity_loc_per_pm = 600
 
cocomo_effort = a * (kloc ** b)
development_time = c * (cocomo_effort ** d)
loc_effort = (kloc * 1000) / productivity_loc_per_pm
 
print(f"COCOMO effort: {cocomo_effort:.2f} person-months")
print(f"Development time: {development_time:.2f} months")
print(f"LOC-method effort: {loc_effort:.2f} person-months")
