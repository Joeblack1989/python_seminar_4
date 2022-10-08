# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N


def client_input(a):
    while True:
        string = input(a)
        try:
            result = int(string)
            return result
        except:
            print("Введено не число")
            result = -1
    

number = client_input("Введите число, которое необходимо разложить на простые множители: ")
array_factors = []
d = 2
m = number 
while d * d <= number:
        if number % d == 0:
            array_factors.append(d)
            number//=d
        else:
            d += 1
array_factors.append(number)
print(array_factors)
