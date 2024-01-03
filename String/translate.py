s = "THIs is STRInG"

# 71  G        103  g
# 72  H        104  h
# 73  I        105  i
# 82  R        114  r
# 83  S        115  s
# 84  T        116  t
d = {71: 103, 72: 104, 73: 105, 84:116, 82:114, 83:115}

print(s.translate(d))