# Напишите функцию, которая находит
# наибольший общий делитель двух натуральных чисел
# На входе два числа, на выходе их НОД.
def z(a, b):
    while b != 0:
        a, b = b, a % b
    return a
n1=int(input())
n2=int(input())
print(f"НОД чисел {n1} и {n2} равен {z(n1, n2)}")
