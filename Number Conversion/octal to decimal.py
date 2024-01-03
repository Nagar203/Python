def octalToDecimal(octal):
    decimal, i, n = 0, 0, octal
    while(n != 0):
        dec = n % 8
        decimal = decimal + dec * pow(8, i)
        n //= 8
        i += 1

    print(decimal)

octal = 0o24
octalToDecimal(octal)