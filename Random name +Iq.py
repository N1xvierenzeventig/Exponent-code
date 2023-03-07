try:
    A = int(input("The base number"))
    B = int(input("The power number"))

    def exponent(base, power):
        result = 1
        for i in range(power):
            result = result * base
        return result

    print(exponent(A, B))
except ValueError:
    print("There's a value error, my advise will be to use numbers instead of whatever.")




