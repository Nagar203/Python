def gcd(m,n):
        if(n>m):
                (m,n)=(n,m)
        if(m%n)==0:
                return(n)
        else:
                diff=m-n
        return(gcd(max(n,diff),min(n,diff)))

print(gcd(10, 15))
