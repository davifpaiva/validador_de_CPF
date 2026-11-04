import os
os.system('cls')  


def calcular_digito(digitos, peso):
    soma = 0  
    for digito in digitos:
        soma += int(digito) * peso  
        peso -= 1  
    resto = (soma * 10) % 11  
    return 0 if resto > 9 else resto  

def validar_cpf(CPF):

    if CPF == CPF[0] * 11:
        return 'invalido'
    
    elif len(CPF) < 11:
        return 'Invalido precisa de 11 digitos'

    else:

        primeiro = calcular_digito(CPF[:9], 10)
        segundo = calcular_digito(CPF[:9] + str(primeiro), 11)

        print('Primeiro dígito:', primeiro)
        print('Segundo dígito:', segundo)

        
        CPF_validado = f'{CPF[:9]}{primeiro}{segundo}'

        if CPF_validado == CPF:
            return 'Valido!'
        else:
            return 'Invalido ;( '


CPF = input('Escreva seu CPF: ') 
print(f'O seu cpf {CPF} está {validar_cpf(CPF)}')
print('Fim do Programa.')