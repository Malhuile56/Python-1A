"""
Un pokedex est modélisé par un dictionnaire dont les clefs sont les noms des pokemons 
et les valeurs associée des informations sur des pokemons.
Ces informations sont données sous la forme d'un tuple (familles, attaque, défense, poids).
"""

def mon_pokedex():
    """ renvoie mon pokedex avec la structure de données
        donnée dans la documentaion du module """
    return {'Bulbizarre': ({'Plante', 'Poison'}, 4, 3, 7),
            'Jungko': ({'Plante'}, 7, 1, 52),
            'Herbizarre': ({'Plante', 'Poison'}, 5, 5, 13),            
            'Abo': ({'Poison'}, 4, 2, 6)}

def plus_forte_attaque(pokedex):
    def critere(nom):
        return pokedex[nom][1]
    le_plus_fort = max(pokedex, key=critere)
    (familles, attaque, defense, poids) = pokedex[le_plus_fort]
    return (le_plus_fort, familles, attaque, defense, poids)


def tri_selon_defense(pokedex):
    def defense(nom):
        return pokedex[nom][2]
    return sorted(pokedex, key=defense)


def plus_petite_force(pokedex):
    def force(pokemon):
        return pokedex[pokemon][1] + pokedex[pokemon][2]
    return min(pokedex, key=force)


def tri_selon_diversite(pokedex):
    def atq(pokemon):
        return pokedex[pokemon][1]
    def types(pokemon):
        return len(pokedex[pokemon][0])
    noms = sorted(sorted(pokedex, key=atq), key=types)
    res = []
    for poke in noms:
        (familles, attaque, defense, poids) = pokedex[poke]
        res.append((poke, familles, attaque, defense, poids))
    return res

