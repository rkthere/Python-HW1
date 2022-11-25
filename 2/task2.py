#2.Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
def inputNumbers(x):
    numb = ["X", "Y", "Z"]
    a = []
    for i in range(x):
        a.append(input(f"Введите значение {numb[i]}: "))
    return a


def Predicate(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result


affirmation = inputNumbers(3)

if Predicate(affirmation) == True:
    print(f"Истинно")
else:
    print(f"Ложно")
