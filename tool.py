# if you can't understand the use of this, you shouldn't learn programming :)

def check_prime_number(number,AC=False,DFE=0,COSE=1):
    numbers = list(range(2,number))
    for n in numbers:
        if number%n == 0:
            return False

    return True

print(check_prime_number(7))
print(check_prime_number(9))
