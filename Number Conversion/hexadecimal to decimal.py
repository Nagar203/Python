def octalToDecimal(hexadecimal):
    decimal, i, n = 0, 0, hexadecimal

    while(n != 0):
        dec = n % 16
        decimal = decimal + dec * pow(16, i)
        n //= 16
        i += 1

    print(decimal)

hexadecimal = 0x14
octalToDecimal(hexadecimal)