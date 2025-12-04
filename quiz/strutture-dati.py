#liste
"""stringhe: list[str] = ["Pippo"]

stringhe.append("Pluto")

for x in stringhe:

    print(x)

stringhe.append("Minnie")
stringhe.append("Paperino")

value_to_check_and_delete: str = "Pluto"

deleted_values: list[str] = []

is_value_in_the_list : bool = value_to_check_and_delete in stringhe

if is_value_in_the_list == True:

    index_value_to_delete = stringhe.index(value_to_check_and_delete.capitalize())
    deleted_value = stringhe.pop(index_value_to_delete)

    deleted_values.append(deleted_value)

else: 
    print(f"{value_to_check_and_delete}Non esiste nella lista  {stringhe}")

print("*"*30)
print(stringhe)
print(deleted_values)
"""

#dizionari 
"""

personaggio1: dict[ str | int] = {

    "nome": "Pippo",
    "tipo": "cane",
    "email": "pippo@disney.com"
}

personaggio1["Telefono"] = "1234567890"

#print(personaggio1.get("Telefono"))
#print(personaggio1.get("nome"))

personaggio1["nome"] = "Pluto"

for chiave, valore in personaggio1.items():

    print(f"{chiave} : {valore}")
    """

personaggio1: dict[ str | int] = {

    "nome": "Pippo",
    "tipo": "cane",
    "email": "pippo@disney.com"
}

personaggio2: dict[ str | int] = {

    "nome": "Minnie",
    "tipo": "topo",
    "email": "minnieo@disney.com"
}
personaggi: list[ dict[ str | int]] = []
print(personaggi[1].get("tipo"))

del personaggio1["tipo"]

#print(personaggio1.get("Telefono"))
#print(personaggio1.get("nome"))

personaggio1["nome"] = "Pluto"

for x in personaggi:
    if x.get("tipo") == "topo":
        x("tipo")