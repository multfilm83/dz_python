a = "Andrey"
print(type(a), a)

b = 10
print(type(b), b)

c = 1.5
print(type(c), c)

d = bytes([12, 13, 14])
print(type(d), d)

f = [a, b, c, d, "Dog"]
print(type(f), f)

e = (1, 2, 3)
print(type(e), e)

g = {1, 2, 3}
print(type(g), g)

h = frozenset([1, 2, 3])
print(type(h), h)

j = dict({1: "cat", 2: "dog"})
print(type(j), j)

a = "Andrey"
b = "Zverev"
c = a + b
print(c)

print("Andrey", 38)

print("Andrey " + str(38))

number = 38
print(f"Andrey {number}")