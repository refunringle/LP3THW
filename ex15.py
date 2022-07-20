from sys import argv
script, first = argv

text=open(first)
print(f"this is your file {first} ")
print(text.read())

text1=input('Enter text name:')
a=open(text1)
print(a.read())
