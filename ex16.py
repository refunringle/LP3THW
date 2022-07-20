
a=input('enter the file you want to creat:')
b=open(a,'w')
print('its truncated for the file xxx!')
b.truncate()

x=input('enter the text :')
y=input('enter the text :')

b.write(x)
b.write("\n")
b.write(y)

