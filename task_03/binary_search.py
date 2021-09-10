# Дан массив целых чисел длины N. Нужно найти в нем заданное число x и 
# вернуть его индекс. Если x в массиве не встречается - вернуть -1. 

# Решить задачу применяя алгоритм бинарного поиска

def binary_search(numbers, x):
    return -1
    def binary_search(numbers, x):
    f = 0 
    for i in range(len(numbers)):
        if numbers[i] == x:
            f += 1
            return (i+1)
            break
    if f ==0:
        return -1


a = []
for i in range(40):
    a.append(i*i - 2*i)
print(a)
print(binary_search(a,35))