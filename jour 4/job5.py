def calcule(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    if operator == "-":
        return num1 - num2
    if operator == "*":
        return num1 * num2
    if operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Impossible"
    if operator == "%":
        return num1 % num2
    else:
        return "Impossible"

print(calcule(5, "+", 7))
print(calcule(5, "-", 7))
print(calcule(5, "*", 7))
print(calcule(5, "/", 7))

