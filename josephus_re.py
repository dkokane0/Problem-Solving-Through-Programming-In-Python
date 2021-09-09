
n1=int(input("Enter a number of soldiers : "))
k1=int(input("want to skipped from : "))
n=n1
k=k1

def JosephusProblem(n , k):
    if n==1:
        return 1
    else:
        return (JosephusProblem(n-1 , k) + k-1) % n +1

print 'Safe Position : ',JosephusProblem(n,k)

