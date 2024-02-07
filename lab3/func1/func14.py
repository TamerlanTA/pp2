def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return list(filter(lambda x: is_prime(x), numbers))

numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
prime_numbers = filter_prime(numbers)
print("Prime numbers:", prime_numbers)

#Для полученной строки вызывается .split(). Поскольку аргументов у split() нет, она разбивает строку на каждый пробел (или последовательность пробелов), создавая список подстрок.
#[int(x) for x in ...] - это компиляция списка, которая итерирует каждую подстроку, полученную функцией split(), преобразует ее в целое число с помощью int(x) и собирает эти целые числа в новый список.