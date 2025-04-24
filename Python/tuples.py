perfect_day = ("Wake up", "Breakfast", "Explore", "Relax", "Sleep")
print(f"My perfect day is {perfect_day}")
print(perfect_day[0])
print(perfect_day[-1])
print(perfect_day[1:4])

(a, b, c, d, e) = perfect_day
print(a)
print(b)
print(c)
print(d)
print(e)

# Wont work de to tuples being unchangable
# perfect_day[1] = Shower

perfect_day2 = ("Read", "Eat a Snack")

full_day = perfect_day + perfect_day2
print(full_day)

x = full_day.count("Sleep")
print (f"Sleep appears {x} time(s)")

y = full_day.index("Explore")
print(f"Explore is found at index {y}")

print(len(full_day))

z = list(full_day)
z[1] = "Ice Cream"

full_day = tuple(z)
print(full_day)