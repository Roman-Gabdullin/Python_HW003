# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
# Негафибоначчи


k = int(input('Введите k: '))
length = k*2+1
list = []
def NegaFibonacci(number):
    if number == -2: return -1
    elif number == -1: return 1
    else:
        return NegaFibonacci(number+2)-NegaFibonacci(number+1)

def Fibonacci (number):
    if number == 0: return 0
    elif number in [1,2]: return 1
    else:
        return Fibonacci(number-1)+Fibonacci(number-2)
    
for i in range(-k,k+1):
    if i < 0:
        list.append(NegaFibonacci(i))
    else:
        list.append(Fibonacci(i))
print(*list, sep = ' ')