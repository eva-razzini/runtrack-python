def veg(type, saison):
    if type == "fruits" and saison == "hiver":
        return"orange, mandarine, kiwi"
    elif type == "fruits" and saison == "ete":
        return"Poire, fraise, cassis"
    elif type == "legume" and saison == "hiver":
        return"carotte, topinambour, endive"
    elif type == "legume" and saison == "ete":
        return "artichaut, aubergine,navet"
    else:
        return "valeur incorrecte"
print(veg("fruits", "ete"))