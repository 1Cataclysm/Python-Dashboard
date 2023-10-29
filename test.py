import caracteristique as c

data = c.get_data(1)

print(data["22"])
print(data["96"])
cles = [cle for cle in data]
print(cles)
print(len(cles))