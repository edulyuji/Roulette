from function import spinRoulette

values = [1,61,82,21,279,6,26]

for x in values:
    returnRoulette = spinRoulette(x)
    print(f"Valor Sorteado: {x} - Resultado Individuo: {returnRoulette}")