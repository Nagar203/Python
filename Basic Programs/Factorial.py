A=int(input('Enter A positive : '))
factorial=1
if(A<0):
    print('Enter A Valid Number.')
elif(A==0):
    print('Factorial Is One')
else:
    for i in range(1,A+1):
        factorial=factorial*i
print(factorial)
