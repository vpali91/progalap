f = open("lotto.txt","r")

het=[]
szam1=[]
szam2=[]
szam3=[]
szam4=[]
szam5=[]
lines = f.read().splitlines()


for item in lines:
    sorsolas = item.split(';')
    het.append(sorsolas[0])
    szam1.append(sorsolas[1])
    szam2.append(sorsolas[2])
    szam3.append(sorsolas[3])
    szam4.append(sorsolas[4])
    szam5.append(sorsolas[5])

lista = []
for item in lines:
    sorsolas = item.split(';')
    dict = {
        "hét":sorsolas[0],
        "szám1":sorsolas[1],
        "szám2":sorsolas[2],
        "szám3":sorsolas[3],
        "szám4":sorsolas[4],
        "szám5":sorsolas[5],
    }
    lista.append(dict)

print(lista[0])

