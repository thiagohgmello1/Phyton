import functions as fc

ans = 'S'
while ans == 'S':
    cnpj = input('Digite o CNPJ: ')
    cnpj = fc.formata_cnpj(cnpj)
    flag1 = fc.verifica_qtd(cnpj)
    flag2 = fc.verifica_char(cnpj)
    if flag1 or flag2:
        ans = input('Deseja verificar outro CNPJ? [S][N] \n')
    else:
        p_d = fc.primeiro_digito(cnpj)
        s_d = fc.segundo_digito(cnpj, p_d)
        fc.compara_cnpj(cnpj, p_d, s_d)
        ans = input('Deseja verificar outro CNPJ? [S][N] \n')
