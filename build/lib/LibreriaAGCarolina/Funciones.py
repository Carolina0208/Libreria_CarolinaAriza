import random
# SELECCIÓN
def seleccion_torneo(poblacion, fitnesses, k=3):
    seleccionados = []
    for _ in range(len(poblacion)):
        aspirantes = random.sample(list(zip(poblacion, fitnesses)), k)
        ganador = max(aspirantes, key=lambda x: x[1])[0]
        seleccionados.append(ganador)
    return seleccionados
def seleccion_aleatoria(poblacion, fitnesses, n=None):
    if n is None:
        n = len(poblacion)
    return random.choices(poblacion, k=n)
def seleccion_ruleta(poblacion, fitnesses):
    total_fit = sum(fitnesses)
    if total_fit == 0:
        return random.choices(poblacion, k=len(poblacion))  # evitar división por cero
    probabilidades = [f / total_fit for f in fitnesses]
    return random.choices(poblacion, weights=probabilidades, k=len(poblacion))
def seleccion_ranking(poblacion, fitnesses):
    ordenados = sorted(zip(poblacion, fitnesses), key=lambda x: x[1])
    ranks = list(range(1, len(poblacion) + 1))
    total_ranks = sum(ranks)
    probabilidades = [r / total_ranks for r in ranks]
    return random.choices([ind for ind, _ in ordenados], weights=probabilidades, k=len(poblacion))
def seleccion_elitista(poblacion, fitnesses, n_elite):
    ordenados = sorted(zip(poblacion, fitnesses), key=lambda x: x[1], reverse=True)
    elite = [ind for ind, _ in ordenados[:n_elite]]
    resto = seleccion_ruleta(poblacion, fitnesses)
    return elite + resto[:len(poblacion) - n_elite]
# CRUCE
def cruce_un_punto(padre1, padre2):
    punto = random.randint(1, len(padre1) - 1)
    return padre1[:punto] + padre2[punto:], padre2[:punto] + padre1[punto:]
def cruce_dos_puntos(padre1, padre2):
    p1, p2 = sorted(random.sample(range(1, len(padre1)), 2))
    hijo1 = padre1[:p1] + padre2[p1:p2] + padre1[p2:]
    hijo2 = padre2[:p1] + padre1[p1:p2] + padre2[p2:]
    return hijo1, hijo2
def cruce_uniforme(padre1, padre2, prob=0.5):
    hijo1 = []
    hijo2 = []
    for gen1, gen2 in zip(padre1, padre2):
        if random.random() < prob:
            hijo1.append(gen1)
            hijo2.append(gen2)
        else:
            hijo1.append(gen2)
            hijo2.append(gen1)
    return hijo1, hijo2
def cruce_aritmetico(padre1, padre2, alfa=0.5):
    hijo1 = [(alfa * g1 + (1 - alfa) * g2) for g1, g2 in zip(padre1, padre2)]
    hijo2 = [(alfa * g2 + (1 - alfa) * g1) for g1, g2 in zip(padre1, padre2)]
    return hijo1, hijo2
# MUTACIÓN
def mutacion_binaria(individuo, prob_mut=0.01):
    return [1 - gen if random.random() < prob_mut else gen for gen in individuo]
def mutacion_swap(individuo):
    a, b = random.sample(range(len(individuo)), 2)
    individuo[a], individuo[b] = individuo[b], individuo[a]
    return individuo
def mutacion_gaussiana(individuo, mu=0, sigma=1, prob_mut=0.1):
    return [
        gen + random.gauss(mu, sigma) if random.random() < prob_mut else gen
        for gen in individuo
    ]