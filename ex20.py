a= input('enter the file name:')
def pall (f):
    print(f.read())

def rw (f) :
    f.seek(0)
def prall (lc, f) :
    print(lc ,f.readline())

file= open(a)
pall(file)
rw(file)

cl=1
prall(cl,file)

cl=cl+1
prall(cl,file)

cl=cl+1
prall(cl,file)
