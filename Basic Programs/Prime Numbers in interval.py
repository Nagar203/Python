A=int(input('Enter A : '))
array=[]
if(A>1):
    for j in range(2,A+1):    
        for i in range(2,j):
            if(j%i==0):
                break
        else:
            print(j,'prime number')
if(A==1 or A<1):
    print('not prime number')
