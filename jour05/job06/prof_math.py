def prof_math(notes):
    arrondie = []
    for i in notes:
        if i >= 40:
            multi5 = ((i // 5)+ 1) *5
            if multi5 - i < 3:
                resulta = multi5
            else:
                resulta = i
        else:
            resulta = i
        arrondie.append(resulta)
    return arrondie
notes = [15, 83, 82, 46, 80, 76, 53]
print(prof_math(notes))
