def calcule(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    elif operator == "%":
        return num1 % num2
    else:
        return "l'operation n'est pas valide"
print(calcule(3, "+", 5))
print(calcule(3, "-", 5))
print(calcule(3, "*", 5))
print(calcule(3, "/", 5))
print(calcule(3, "%", 5))
print(calcule(3, "l", 5))