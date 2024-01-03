A=input('Enter A : ')
B=input('Enter B : ')
C=input('Enter C : ')
if(A>=B)and(A>=C):
    largest=A
elif(B>=A)and(B>=C):
    largest=B
else:
    largest=C
print("Largest Number Between {0} ,{1} and {2} is {3}".format(A,B,C,largest))
