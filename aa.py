n=int(input('enter the a nuber:'))
m=int(input('enter the a nuber:'))

class ex (object):
    def add (a,b):
        print(a+b)
    def diff (a,b):
        print(a-b)
    def mul (a,b):
        print(a*b)

if __name__ == "__main__":
    ad=ex.add(n,m)
    di=ex.diff(n,m)
    mu=ex.mul(n,m)