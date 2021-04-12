def gcd(a, b):
    if a == b == 0:
        return 0
        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a

    return int(a + b)

def lcm(a, b):
    if gcd(a, b) == 0:
        return 0
    else:
        return int(a * b / gcd(a,b)) 

if __name__ == '__main__':
    print("Введите два целых числа через пробел")
    a, b = input().split()

    print(f'НОД = {gcd(a, b)}, НОК = {lcm(a, b)}')
