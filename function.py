population = ["A","B","C","D","E","F"]
fitness = [30,22,45,53,21,109]

def spinRoulette(value):
    cont = 0
    roulette = fitness[cont]
    for i in fitness:
        if(roulette >= value):
            return population[cont]
        cont += 1
        roulette += fitness[cont]
