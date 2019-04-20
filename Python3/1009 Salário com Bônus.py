name = str(input())
fixo = float(input())
vendas = float(input())
comicao = (vendas*15)/100
total = (fixo+comicao)
print('TOTAL = R$ {:.2f}'.format(total))
