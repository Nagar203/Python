s1 = "THIs is STRing."
s2 = "This \nis string."
s3 = "This\t is \r string"

# retrn false special char
print(s1.isprintable())
print(s2.isprintable())
print(s3.isprintable())