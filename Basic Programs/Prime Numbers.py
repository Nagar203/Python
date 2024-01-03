A=int(input('Enter A : '))
array=[]
if(A>1):
    for i in range(2,A):
        if(A%i==0):
            print('Not Prime Number')
            break
    else:
        print('prime number')
if(A==1 or A<1):
    print('not prime number')
