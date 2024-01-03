A=int(input('Enter A : '))
x=A
s=0
if(A>0):
    while(A>=1):
        y=A%10
        s=s+(y)**3
        A=A/10
    if(x==s):
        print('sum = ',s)
elif(A==0):
    print('A is zero Armstrong')
else:
    print(A,' is -ve')
