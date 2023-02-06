import random

nove_digitos=''
for i in range(9):
    nove_digitos+= str(random.randint(0,9))


cpf_usuario=nove_digitos \
    .replace('.','')\
    .replace('-','')\
    .replace(' ','')

nove_digitos_1=cpf_usuario[:9]
contador_regressivo_1=10
resultado_1=0

for digito in nove_digitos_1:
     resultado_1+=int(digito)* contador_regressivo_1
     contador_regressivo_1-=1

digito=(resultado_1 *10) %11
digito=digito if digito<=9 else 0


dez_digitos_2=cpf_usuario[:9]+str(digito)
contador_regressivo_2=11
resultado_2=0

for digito_2 in dez_digitos_2:
    resultado_2+=int(digito_2)*contador_regressivo_2
    contador_regressivo_2-=1

digito_2=(resultado_2*10)%11
digito_2=digito_2 if digito_2 <=9 else 0
cpf_gerado=f'{nove_digitos_1}{digito}{digito_2}'

print(cpf_gerado)
