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

    # Dicionário de conversões com base em metro
    unidades = {
        "ym"    : 1e-24,         # yoctômetro
        "zm"    : 1e-21,         # zeptômetro
        "am"    : 1e-18,         # attômetro
        "fm"    : 1e-15,         # fentômetro
        "pm"    : 1e-12,         # picômetro
        "nm"    : 1e-9,          # nanômetro
        "µm"    : 1e-6,          # micrômetro
        "mm"    : 1e-3,          # milímetro
        "cm"    : 1e-2,          # centímetro
        "dm"    : 1e-1,          # decímetro
        "m"     : 1,             # metro
        "dam"   : 1e1,           # decâmetro
        "hm"    : 1e2,           # hectômetro
        "km"    : 1e3,           # quilômetro
        "Mm"    : 1e6,           # megâmetro
        "Gm"    : 1e9,           # gigâmetro
        "Tm"    : 1e12,          # terâmetro
        "Pm"    : 1e15,          # petâmetro
        "Em"    : 1e18,          # exametro
        "Zm"    : 1e21,          # zettâmetro
        "Ym"    : 1e24,          # yottâmetro
        "milha" : 1609.344,      # milha
        "jarda" : 0.9144,        # jarda
        "foot"  : 0.3048,        # pé
        "inch"  : 0.0254,        # polegada
        "UA"    : 1.496e11,      # unidade astronômica
        "ly"    : 9.461e15,      # ano-luz
        "pc"    : 3.086e16       # parsec
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

    valor_convertido = None

    if unidade_original.lower() == "kelvin" and unidade_final.lower() == "celsius":

        valor_convertido = valor - 273

    elif unidade_original.lower() == "kelvin" and unidade_final.lower() == "fahrenheit":

        valor_convertido = (valor - 273) * 1.8 + 32

    elif unidade_original.lower() == "celsius" and unidade_final.lower() == "kelvin":

        valor_convertido = valor + 273

    elif unidade_original.lower() == "celsius" and unidade_final.lower() == "fahrenheit":

        valor_convertido = valor * 1.8 + 32

    elif unidade_original.lower() == "fahrenheit" and unidade_final.lower() == "celsius":

        valor_convertido = (valor - 32) / 1.8

    elif unidade_original.lower() == "fahrenheit" and unidade_final() == "kelvin":

        valor_convertido = (valor - 32) * (5/9) + 273

    return valor_convertido