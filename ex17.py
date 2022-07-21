from os.path import exists

a=input('enter the copying file name:')
b=input('enter the file coping to :')

c=open(a)
d=c.read()
print(f"i have a {len(d)} files")

print(f"it file is {exists(b)}")
e=open(b,'w')
e.write(d)
print('done')
