vlr = int(input())

cem =  vlr // 100
cem_resto = vlr / 100
resto = cem - cem_resto

print(f'{cem} nota(s) de R$ 100,00')
print(f'{resto} notas(s) de R$ 50,00')


