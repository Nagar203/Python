def gcd(m,n):
        fm=[]
        for i in range(1,1+m):
                if((m%i)==0):
                        fm.append(i)

        fn=[]
        for i in range(1,n+1):
                if((n%i)==0):
                        fn.append(i)
        cf=[]
        for f in fm:
                if f in fn:
                        cf.append(f)
        return(cf[-1])

print(gcd(10, 15))