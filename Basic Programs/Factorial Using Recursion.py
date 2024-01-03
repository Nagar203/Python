def factorial(A):
    if(A>0):        
        if(A==1):
            return A
        else:
            return A*factorial(A-1)
    elif(A==0):
        print('Factorial Is One')
    else:
        print('Enter A Valid Number.')
        
        
