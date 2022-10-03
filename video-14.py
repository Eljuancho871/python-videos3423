conjunto = {1,2,3,4,5}
conjunto.add(6)
print(conjunto)

conjunto.remove(5)

for elem in conjunto:
    print(elem)



d = {
    "nombre": "messi",
    "edad": 35
}

d["apellido"] = "Lionel"

print(d["edad"])
print(d["nombre"])
print(d)

for k,v in list(d.items()):
    print(k,v)