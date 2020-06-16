def formata_cnpj(cnpj):
    cnpj = cnpj.replace('.', '')
    cnpj = cnpj.replace('-', '')
    cnpj = cnpj.replace('/', '')
    return cnpj


def verifica_qtd(cnpj):
    if len(cnpj) != 14:
        print('Quantidade incorreta de números. Favor inserir 14 caracteres.')
        return True
    else:
        return False


def verifica_char(cnpj):
    try:
        float(cnpj)
        return False
    except ValueError as error_value:
        print('Caracteres inválidos. Favor inserir apenas números.')
        with open('Erro_CNPJ.txt', 'a') as file:
            file.write(str(error_value))
            file.write('\n')
            file.close()
        return True
    except Exception as general_error:
        print('Erro inesperado.')
        with open('Erro_CNPJ.txt', 'a') as file:
            file.write(str(general_error))
            file.write('\n')
            file.close()
        return True


def transforma_int(cnpj):
    cnpj = list(cnpj)
    for i in range(0, len(cnpj)):
        cnpj[i] = int(cnpj[i])
    return cnpj


def multiplica_primeiro(cnpj):
    prod = 0
    vec = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    for i in range(0, 12):
        prod += vec[i] * cnpj[i]
    return prod


def multiplica_segundo(cnpj, primeiro_d):
    prod = 0
    vec = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    for i in range(0, 12):
        prod += vec[i] * cnpj[i]
    prod += vec[12] * primeiro_d
    return prod


def primeiro_digito(cnpj):
    cnpj = transforma_int(cnpj)
    prod = multiplica_primeiro(cnpj)
    char1 = 11 - (prod % 11)
    if char1 > 9:
        char1 = 0
    else:
        pass
    return char1


def segundo_digito(cnpj, p_d):
    cnpj = transforma_int(cnpj)
    prod = multiplica_segundo(cnpj, p_d)
    char1 = 11 - (prod % 11)
    if char1 > 9:
        char1 = 0
    else:
        pass
    return char1


def compara_cnpj(cnpj, p_d, s_d):
    cnpj = transforma_int(cnpj)
    if cnpj[12] == p_d and cnpj[13] == s_d:
        print('CNPJ válido.')
    else:
        print('CNPJ inválido.')
