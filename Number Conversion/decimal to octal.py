

decimal = 20 

# Method 01
# octal = oct(decimal)
# print(octal)



# Method 02 

def decimalToOctal(decimal):
    octal = 0
    i = 0

    while decimal > 0:
        remainder = decimal % 8
        octal += remainder * pow(10, i)
        decimal //= 8
        i += 1

    print(octal)

decimal = 20
decimalToOctal(decimal)