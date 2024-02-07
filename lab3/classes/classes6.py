class PNF:
    def __init__(self, numbers):
        self.numbers = numbers

    def is_prime(self, num):
        #check if a number is prime
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def filter_primes(self):
        # Here, the lambda calls the method is_prime for each element.
        return list(filter(lambda num: self.is_prime(num), self.numbers))
    
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primeFilter = PNF(numbers)

print("Prime numbers:", primeFilter.filter_primes())
