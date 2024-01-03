def gcd(m,n):
    if(n>m):
        (m,n)=(n,m)
    if(m%n==0):
        return(n)
    else:
        return(gcd(n,m%n))
    
print(gcd(10, 15))
