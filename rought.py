n=int(input('Enter the digits:'))
s=0
while n!=0:
    d=n%10
    s=d+s
    n=n//10
    print(s)    
    if s>9:
        n=s
    print(s)