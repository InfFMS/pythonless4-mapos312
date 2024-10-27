# Напишите рекурсивную функцию, которая
# раскладывает натуральное число на простые сомножители.
#
# Пример:
# Ввод:
# 378
# Вывод:
# 2*3*3*3*7
def f(n, d=2):
    if n == 1:
        return []
    if n % d == 0:
        return [d] + f(n // d, d)
    return f(n, d + 1)
x = int(input())
q = f(x)
result = '*'.join(map(str, q))
print(result)


