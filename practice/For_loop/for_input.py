size_input = input("Mekkora legyen a lista?")
if size_input.isnumeric():
    size = int(size_input)
else:
    print("Számot adj meg!")

lista=[]
for n in range(0,size):
    input_lista = input(f"Add meg a lista {n}. tagját")
    lista.append(input_lista)

print(lista)