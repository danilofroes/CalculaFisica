'''
Código específico para a função de calcular deltas da física.
'''

from calculadoras import delta
from math import radians, degrees

def calcdelta(parametro, f, i, unidade_original=None, unidade_desejada=None):
    '''
    Calculadora de deltas da física

    :param parametro: Definirá qual delta está sendo calculado
    :param f: É o valor final do delta
    :param i: É o valor inicial do delta
    :param unidade_original: É a unidade dos valores f e i
    :param unidade_desejada: É a unidade que o usuário deseja chegar no resultado do delta
    :return: String com o resultado do delta calculado na unidade desejada
    '''

    unidade_final = None
    f_final = None
    i_final = None

    # Δt (Tempo)
    if parametro.lower() == "tempo":

        if (unidade_original.lower() == "s" and unidade_desejada.lower() == "s") or (unidade_original.lower() == "h" and unidade_desejada.lower() == "h"):
            f_final = f
            i_final = i

        elif unidade_original.lower() == "min" and unidade_desejada.lower() == "s":     #converte a unidade de minuto para segundo
            unidade_final = unidade_desejada
            f_final = f * 60
            i_final = i * 60

        elif unidade_original.lower() == "h" and unidade_desejada.lower() == "s":       #converte horas em segundos
            unidade_final = unidade_desejada
            f_final = f * 3600
            i_final = i * 3600

        elif unidade_original.lower() == "min" and unidade_desejada.lower() == "h":
            unidade_final = unidade_desejada
            f_final = f / 60
            i_final = i / 60

        elif unidade_original.lower() == "s" and unidade_desejada.lower() == "h":
            unidade_final = unidade_desejada
            f_final = f / 3600
            i_final = i / 3600

        deltat = delta(f_final, i_final)
        return f"O valor de Δt com tempo inicial de {i}{unidade_original} e de tempo final de {f}{unidade_original} é {deltat}{unidade_final}"
    
    # Δx (Distância)
    if parametro.lower() == "distancia":
        if (unidade_original.lower() == "m" and unidade_desejada.lower() == "m") or (unidade_original.lower() == "km" and unidade_desejada.lower() == "km"):
            unidade_final = unidade_desejada
            f_final = f
            i_final = i

        elif unidade_original.lower() == "km" and unidade_desejada.lower() == "m":
            unidade_final = unidade_desejada
            f_final = f * 1000
            i_final = i * 1000

        elif unidade_original.lower() == "m" and unidade_desejada.lower() == "km":
            unidade_final = unidade_desejada
            f_final = f / 1000
            i_final = i / 1000

        deltax = delta(f_final, i_final)
        return f"O valor de Δx com distância inicial de {i}{unidade_original} e de distância final de {f}{unidade_original} é {deltax}{unidade_final}"
    
    # Δv (Velocidade)
    if parametro.lower() == "velocidade":

        if (unidade_original.lower() == "m/s" and unidade_desejada.lower() == "m/s") or (unidade_original.lower() == "km/h" and unidade_desejada.lower() == "km/h"):
            unidade_final = unidade_desejada
            f_final = f
            i_final = i

        elif unidade_original.lower() == "km/h" and unidade_desejada.lower() == "m/s":
            unidade_final = unidade_desejada
            f_final = f / 3.6
            i_final = i / 3.6

        elif unidade_original.lower() == "m/s" and unidade_desejada.lower() == "km/h":
            unidade_final = unidade_desejada
            f_final = f * 3.6
            i_final = i * 3.6

        deltav = delta(f_final, i_final)
        return f"O valor de Δv com velocidade inicial de {i}{unidade_original} e de velocidade final de {f}{unidade_original} é {deltav}{unidade_final}"

    # Δa (Aceleração)
    if parametro.lower() == "aceleracao":

        deltaa = delta(f, i)

        return f"O valor de Δa com aceleração inicial de {i}m/s² e de aceleração final de {f}m/s² é {deltaa}m/s²"

    # ΔE (Energia)
    if parametro.lower() == "energia":
        
        deltae = delta(f, i)

        return f"O valor de ΔE com energia inicial de {i}J e de energia final de {f}J é {deltae}J"
    
    # Δp (Momento linear)
    if parametro.lower() == "momento_linear":

        deltap = delta(f, i)

        return f"O valor de Δp com momento inicial de {i}kg.m/s e de momento final de {f}kg.m/s é {deltap}kg.m/s"
    
    # ΔP (Pressão)
    if parametro.lower() == "pressao":

        deltapressao = delta(f, i)

        return f"O valor de ΔP com pressão inicial de {i}pa e de pressão final de {f}pa é {deltapressao}pa"
    
    # Δθ (Ângulo)
    if parametro.lower() == "angulo":

        if (unidade_original.lower() == "rad" and unidade_desejada.lower() == "rad") or (unidade_original.lower() == "graus" and unidade_desejada.lower() == "graus"):
            unidade_final = unidade_desejada
            f_final = f
            i_final = i

        elif unidade_original.lower() == "graus" and unidade_desejada.lower() == "rad":
            unidade_final = unidade_desejada
            f_final = radians(f)
            i_final = radians(i)

        elif unidade_original.lower() == "rad" and unidade_desejada.lower() == "graus":
            unidade_final = unidade_desejada
            f_final = degrees(f)
            i_final = degrees(i)

        deltatheta = delta(f_final, i_final)
        return f"O valor de Δθ com ângulo inicial de {i}{unidade_original} e de ângulo final de {f}{unidade_original} é {deltatheta}{unidade_final}"
    
    # ΔT (Temperatura)
    if parametro.lower() == "temperatura":

        if (unidade_original.lower() == "c" and unidade_desejada.lower() == "c") or (unidade_original.lower() == "f" and unidade_desejada.lower() == "f") or (unidade_original.lower() == "k" and unidade_desejada.lower() == "k"):
            unidade_final = unidade_desejada
            f_final = f
            i_final = i

        elif unidade_original.lower() == "k" and unidade_desejada.lower() == "c":
            unidade_final = unidade_desejada
            f_final = f - 273.15
            i_final = i - 273.15
        
        elif unidade_original.lower() == "k" and unidade_desejada.lower() == "f":
            unidade_final = unidade_desejada
            f_final = (f - 273) * 1,8 + 32
            i_final = (i - 273) * 1,8 + 32

        elif unidade_original.lower() == "c" and unidade_desejada.lower() == "k":
            unidade_final = unidade_desejada
            f_final = f + 273.15
            i_final = i + 273.15

        elif unidade_original.lower() == "c" and unidade_desejada.lower() == "f":
            unidade_final = unidade_desejada
            f_final = f * 1,8 + 32
            i_final = i * 1,8 + 32

        elif unidade_original.lower() == "f" and unidade_desejada.lower() == "c":
            unidade_final = unidade_desejada
            f_final = (f - 32) / 1,8
            i_final = (i - 32) / 1,8

        elif unidade_original.lower() == "f" and unidade_desejada.lower() == "k":
            unidade_final = unidade_desejada
            f_final = (f - 32) * (5 / 9) + 273
            i_final = (i - 32) * (5 / 9) + 273

        deltaT = delta(f_final, i_final)

        return f"O valor de ΔT com temperatura inicial de {i}{unidade_original} e de temperatura final de {f}{unidade_original} é {deltaT}{unidade_final}"
    
    # Δf (Frequência)
    if parametro.lower() == "frequencia":

        deltaf = delta(f, i)

        return f"O valor de Δf com frequência inicial de {i}Hz e de frequência final de {f}Hz é {deltaf}Hz"
    
    # Δλ (Comprimento de onda)
    if parametro.lower() == "comprimento de onda":

        if (unidade_original.lower() == "m" and unidade_desejada.lower() == "m") or (unidade_original.lower() == "km" and unidade_desejada.lower() == "km"):
            unidade_final = unidade_desejada
            f_final = f
            i_final = i

        elif unidade_original.lower() == "km" and unidade_desejada.lower() == "m":
            unidade_final = unidade_desejada
            f_final = f * 1000
            i_final = i * 1000

        elif unidade_original.lower() == "m" and unidade_desejada.lower() == "km":
            unidade_final = unidade_desejada
            f_final = f / 1000
            i_final = i / 1000

        deltalambda = delta(f_final, i_final)
        return f"O valor de Δλ com comprimento de onda inicial de {i}{unidade_original} e de comprimento de onda final de {f}{unidade_original} é {deltalambda}{unidade_final}"
    
    # Δφ (Fluxo magnético)
    if parametro.lower() == "fluxo magnetico":

        deltafi = delta(f_final, i_final)

        return f"O valor de Δφ com fluxo magnético inicial de {i}wb e de fluxo magnético final de {f}wb é {deltafi}wb"
    
    # ΔU (Energia interna)
    if parametro.lower() == "energia interna":

        deltaU = delta(f_final, i_final)

        return f"O valor de ΔU com energia interna inicial de {i}J e de energia interna final de {f}J é {deltaU}J"
    
    # ΔG (Energia livre de Gibbs)
    if parametro.lower() == "energia livre de gibbs":

        deltaG = delta(f, i)
        return f"O valor de ΔG com energia livre de Gibbs inicial de {i}J e de energia livre de Gibbs final de {f}J é {deltaG}J"
    
    # ΔH (Entalpia)
    if parametro.lower() == "entalpia":

        deltaH = delta(f, i)

        return f"O valor de ΔH com entalpia inicial de {i}J e de entalpia final de {f}J é {deltaH}J"
    
    # ΔS (Entropia)
    if parametro.lower() == "entropia":

        deltaS = delta(f, i)

        return f"O valor de ΔS com entropia inicial de {i}J/K e de entropia final de {f}J/K é {deltaS}J/K"