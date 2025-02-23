import math


## criando as order de faixas

order_belt = {
    "branca": 0,
    "azul": 1,
    "roxa": 2,
    "marrom": 3,
    "preta": 4
}

def calculate_lesson_to_graduate(n):

    d = 1.47 # constante de decaimento
    k = 30/ math.log(d) # constante de crescimento

    aulas = k * math.log(n + d)
    return round(aulas) # arredonda para o inteiro mais próximo