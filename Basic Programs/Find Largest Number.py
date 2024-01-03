A=float(input('Enter A : '))
B=float(input('Enter B : '))
C=float(input('Enter C : '))
if(A>=B)and(A>=C):
    largest=A
elif(B>=A)and(B>=C):
    largest=B
else:
    largest=C
print("Largest Number Between {0} ,{1} and {2} is {3}".format(A,B,C,largest))
