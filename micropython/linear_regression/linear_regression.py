# Simple linear regression
# David Therincourt - 2020
# MIT License

def moy(x,n):
    somme = 0
    for val in x:
        somme += val
    return somme/n

def sum_xy(x,y,n):
    somme = 0
    for i in range(n):
        somme += x[i]*y[i]
    return somme

def linear_reg(x,y):
    n = len(x)
    m_x = moy(x,n)
    m_y = moy(y,n)
    print(m_x, m_y)
    SS_xy = sum_xy(x,y,n) - n*m_x*m_y
    SS_xx = sum_xy(x,x,n) - n*m_x**2
    a = SS_xy/SS_xx
    b = m_y - a*m_x
    return a, b