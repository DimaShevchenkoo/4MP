import math
x = [0, 1.5, 3, 4.5, 6, 7.5]
y = [2.075, 1.711, 0.942, -0.314, -2.155, -4.665]
h = x[1] - x[0]
def func(y, j):
    masiv = []
    for i in range(len(y)):
        masiv.append(y[i] - y[i - 1])
    masiv.pop(0)
    if j == 1:
        return masiv
    else:
        j -= 1
        return func(masiv, j)
yx1 = 1 / h * func(y, 1)[1] - func(y, 2)[1] / 2 + func(y, 3)[1] / 3 - func(y, 4)[1] / 4
yx2 = 1 / h ** 2 * func(y, 2)[1] - func(y, 3)[1] + 11 / 12 * func(y, 4)[1]
print(yx1)
print(yx2)