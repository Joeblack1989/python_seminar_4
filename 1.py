# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from decimal import Decimal

def client_input(a):
    while True:
        string = input(a)
        try:
            result = int(string)
            return result
        except:
            print("Введено не число")
            result = -1
    

number = Decimal(client_input('Введите любое число и нажмите клавишу Enter: '))
print(number.quantize(Decimal((input ('Введите необходимую точность (например: 0.00001): ')))))

# либо еще короче
# print(Decimal(client_input('Введите любое число и нажмите клавишу Enter: ')).quantize(Decimal((input ('Введите необходимую точность (например: 0.00001): ')))))
