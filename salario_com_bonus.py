nome = input()
slr = float(input())
venda = float(input())

comissao = ((15*venda)/100)

slr_bruto = comissao + slr

print(f'TOTAL = R$ {slr_bruto:.2f}')