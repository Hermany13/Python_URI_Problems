cont100 = 0
cont50 = 0
cont20 = 0
cont10 = 0
cont5 = 0
cont2 = 0
cont1 = 0

valor = int(input())
aux = valor
while aux > 99:
    aux = aux-100
    cont100 += 1

while aux > 49:
    aux = aux-50
    cont50 += 1

while aux > 19:
    aux = aux-20
    cont20 += 1

while aux > 9:
    aux = aux-10
    cont10 += 1

while aux > 4:
    aux = aux-5
    cont5 += 1

while aux > 1:
    aux = aux-2
    cont2 += 1

while aux > 0:
    aux = aux-1
    cont1 += 1


print(valor)
print("{} nota(s) de R$ 100,00".format(cont100))
print("{} nota(s) de R$ 50,00".format(cont50))
print("{} nota(s) de R$ 20,00".format(cont20))
print("{} nota(s) de R$ 10,00".format(cont10))
print("{} nota(s) de R$ 5,00".format(cont5))
print("{} nota(s) de R$ 2,00".format(cont2))
print("{} nota(s) de R$ 1,00".format(cont1))