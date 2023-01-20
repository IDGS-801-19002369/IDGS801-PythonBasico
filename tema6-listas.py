
nombres=["juan",",mario","laura"]
numeros=[1,2,3,4,5]

datos=[1,2,5,"mario",True]

nombres[0]="Bernardo"

print(nombres[1])
print(nombres[2])
print(nombres[:3])
print(nombres[1:])

nombres.append("dario")
print(nombres)

nombres.insert(2,"maria")
print(nombres)

nombres.extend(["checha",2,23,5])
print(nombres)

nombres.remove("checha")
print(nombres)

nombres.pop()
print(nombres)

n=["juan"]
n2=n*5
print(n2)
print(nombres)

del nombres[0]
print(nombres)