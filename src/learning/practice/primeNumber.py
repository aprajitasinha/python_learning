class primeNumber:
    def __init__(self, n):
        self.n = n

    def isPrime(self):
        # code here
        if self.n <= 1:
            return False
        for i in range(2, int(self.n ** 0.5) + 1):
            if self.n % i == 0:
                return False
        return True

    

if __name__ == "__main__":
    n = 20
    prime_obj = primeNumber(n)
    print(prime_obj.isPrime())
