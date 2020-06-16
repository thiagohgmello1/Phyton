soma = 0
while True:
    CPF = input('Insert your CPF in the default formula (99999999999): ')
    if not (CPF.isnumeric() and CPF.__len__()==11):
        print('Wrong CPF.')
        continue
    else:
        break
for index, value in enumerate(range(CPF.__len__()-1, 1, -1)):
    soma += value*int(CPF[index])
if 11-(soma % 11)>9:
    dig1 = 0
else:
    dig1 = 1
soma = 0
for index, value in enumerate(range(CPF.__len__(), 1, -1)):
    soma += value*int(CPF[index])
dig2 = 11-(soma % 11)
if dig1 == int(CPF[-2]) and dig2 == int(CPF[-1]):
    print('Valid CPF.')
else:
    print('Invalid CPF.')
    print(dig1,dig2)


