

tupla=(1,2,3)
print(tupla)
print(type(tupla))
tupla2=(7,"Bernardo",True,23.8,16+7j)

print(tupla2)

print(tupla2[1])

print(tupla2[4])
print(tupla2[-1])
print(tupla2[0:3])
print(tupla2[3:])

a,b,c=tupla

print(a)
print(c)
tuplan=tupla+tupla2
print(tuplan)
print(tupla.count(2))

tupla[2]=23
