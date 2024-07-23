'''
Este código é para as funções de conversões de valores
'''

def converter_tempo(valor, unidade_original, unidade_final):
    '''
    Conversão de unidades de medidas de tempo

    :param valor: Valor a ser convertido
    :param unidade_original: Unidade original
    :param unidade_final: Unidade à ser convertida
    :return: Valor convertido
    '''

    # Dicionário de conversões com base em segundos
    unidades = {
        "ms": 10e-3,           # Milissegundo
        "s": 1,                # Segundo
        "min": 60,             # Minuto
        "h": 3600,             # Hora
        "dia": 86400,          # Dia
        "semana": 604800,      # Semana
        "mes": 2628000,        # Mês (média de 30.44 dias)
        "ano": 31536000,       # Ano (média de 365.25 dias)
        "decada": 315360000,   # Década
        "seculo": 3153600000   # Século
    }
    
    valor_em_segundos = valor * unidades[unidade_original] # Convertendo o valor de entrada em segundos
    valor_convertido = valor_em_segundos / unidades[unidade_final] # Convertendo o valor em segundos para o valor de saída
    
    return valor_convertido

def converter_distancia(valor, unidade_original, unidade_final):
    '''
    Conversão de unidades de medidas de distância

    :param valor: Valor a ser convertido
    :param unidade_original: Unidade original
    :param unidade_final: Unidade à ser convertida
    :return: Valor convertido
    '''

    # Dicionário de conversões com base em metros
    unidades = {
        "ym" : 10e-24,
        "zm" : 10e-21,
        "am" : 10e-18,
        "fm" : 10e-15,
        "pm" : 10e-12,
        "nm" : 10e-9,
        "µm" : 10e-6,
        "mm" : 10e-3,
        "cm" : 10e-2,
        "dm" : 10e-1,
        "m" : 1,
        "dam" : 10,
        "hm" : 100,
        "km" : 1000,
        "Mm" : 10e6,
        "Gm" : 10e9,
        "Tm" : 10e12,
        "Pm" : 10e15,
        "Em" : 10e18,
        "Zm" : 10e21,
        "Ym" : 10e24
    }

    valor_em_metros = valor * unidades[unidade_original]
    valor_convertido = valor_em_metros / unidades[unidade_final]

    return valor_convertido

def converter_temperatura(valor, unidade_original, unidade_final):
    '''
    Conversão de unidades de medidas de temperatura

    :param valor: Valor a ser convertido
    :param unidade_original: Unidade original
    :param unidade_final: Unidade à ser convertida
    :return: Valor convertido
    '''

