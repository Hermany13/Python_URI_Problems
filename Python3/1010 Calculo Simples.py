prod_1 = [str(input()).split()]
prod_2 = [str(input()).split()]
pagar = (int(prod_1[0][1]) * float(prod_1[0][2]))+(int(prod_2[0][1]) * float(prod_2[0][2]))
print("VALOR A PAGAR: R$ {:.2f}".format(pagar))
