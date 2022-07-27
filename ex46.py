print("ex46 is running")
print(__name__)

if __name__ == "__main__":
    print("hello world")

d = {'name': "refun", 'age': 10}

s = "i am {name} and my age is age is {age}".format(*d)
print(s)


