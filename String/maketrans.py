s = "THIs is STRing"
data = s.maketrans("H","h")

print(s.translate(data))