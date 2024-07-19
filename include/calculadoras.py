from math import sqrt, sin, cos

def delta(f,i):
    '''
    Função que calcula o delta (variação) de alguma variável final e inicial

    :param f: Variável final de delta
    :param i: Variável inicial de delta
    '''

    delta_calc = f - i

    return delta_calc

def velocidade_media(velocidade_media=None, deltaX=None, deltaT=None, x_inicial=None, x_final=None, t_inicial=None, t_final=None):
    '''Utiliza da fórmula de velocidade média para encontrar algum valor específico'''

    # Caso 1: Calculando velocidade média usando deltaX e deltaT
    if (velocidade_media is None) and (deltaX is not None) and (deltaT is not None) and (x_inicial is None) and (x_final is None) and (t_inicial is None) and (t_final is None):

        velocidade_media = deltaX / deltaT

        return velocidade_media, deltaX, deltaT

    # Caso 2: Calculando deltaX usando velocidade média e deltaT
    elif (velocidade_media is not None) and (deltaX is None) and (deltaT is not None) and (x_inicial is None) and (x_final is None) and (t_inicial is None) and (t_final is None):

        deltaX = velocidade_media * deltaT

        return deltaX, velocidade_media, deltaT

    # Caso 3: Calculando deltaT usando deltaX e velocidade média
    elif (velocidade_media is not None) and (deltaX is not None) and (deltaT is None) and (x_inicial is None) and (x_final is None) and (t_inicial is None) and (t_final is None):

        deltaT = deltaX / velocidade_media

        return deltaT, deltaX, velocidade_media

    # Caso 4: Calculando velocidade média usando x_inicial, x_final, t_inicial, t_final
    elif (velocidade_media is None) and (deltaX is None) and (deltaT is None) and (x_inicial is not None) and (x_final is not None) and (t_inicial is not None) and (t_final is not None):

        deltaX = x_final - x_inicial
        deltaT = t_final - t_inicial
        velocidade_media = deltaX / deltaT

        return velocidade_media, deltaX, deltaT, x_inicial, x_final, t_inicial, t_final

    # Caso 5: Calculando x_final usando x_inicial, velocidade média e deltaT
    elif (velocidade_media is not None) and (deltaX is None) and (deltaT is not None) and (x_inicial is not None) and (x_final is None) and (t_inicial is None) and (t_final is None):

        x_final = x_inicial + velocidade_media * deltaT

        return x_final, x_inicial, velocidade_media, deltaT

    # Caso 6: Calculando x_inicial usando x_final, velocidade média e deltaT
    elif (velocidade_media is not None) and (deltaX is None) and (deltaT is not None) and (x_inicial is None) and (x_final is not None) and (t_inicial is None) and (t_final is None):

        x_inicial = x_final - velocidade_media * deltaT

        return x_inicial, x_final, velocidade_media, deltaT

    # Caso 7: Calculando t_final usando t_inicial, deltaX e velocidade média
    elif (velocidade_media is not None) and (deltaX is not None) and (deltaT is None) and (x_inicial is None) and (x_final is None) and (t_inicial is not None) and (t_final is None):

        deltaT = deltaX / velocidade_media
        t_final = t_inicial + deltaT

        return t_final, t_inicial, deltaX, velocidade_media, deltaT

    # Caso 8: Calculando t_inicial usando t_final, deltaX e velocidade média
    elif (velocidade_media is not None) and (deltaX is not None) and (deltaT is None) and (x_inicial is None) and (x_final is None) and (t_inicial is None) and (t_final is not None):

        deltaT = deltaX / velocidade_media
        t_inicial = t_final - deltaT

        return t_inicial, t_final, deltaX, velocidade_media, deltaT

    else:

        return "Parâmetros insuficientes ou inválidos"
    

def torricelli(vf, v0, a, deltax):

    vf = sqrt((v0**2) + (2 * a * deltax))

def funcao_horaria_posicao_mu(s, s0, v, t):

    s = s0 + (v * t)

def funcao_horaria_posicao_muv(s, s0, v0, t, a):

    s = s0 + (v0 * t) + ((a * (t**2)) / (2))

def funcao_horaria_velocidade_muv(v, v0, a, t):

    v = v0 + (a * t)

def velocidade_media_muv(vm, v0, vf):

    vm = (v0 * vf) / 2

def altura_max_lancamento_vertical(hmax, s0, v0, g):

    hmax = s0 + ((v0**2) / (2 * g))

def lancamento_horizontal(sx, s0x, vx, t, sy, s0y, v0y, g):

    sx = s0x + vx * t

    sy = s0y + v0y * t - ((g * (t**2)) / 2)

def segunda_lei_newton(fr, m, a):

    fr = m * a


