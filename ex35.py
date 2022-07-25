print('There is 2 rooms infront of u which on would u choose #a or #b ?:')
a=input('>')

def room_a ():
    print("""There is two lader is there #1 and #2 what u can take?:""")
    opp=input('>')
    if opp=="1":
        print('00ps u choose wrong ladder!... Go and sleep')
    elif opp=='2':
        print('WOOW u got $1000... Great job')
        exit(0)
    else:
        err(opp)
    exit(0)

def err (a):
    print(f"{a} its not a our option !")
    exit(1)

def game ():
    if a=="a":
        room_a()
    elif a=="b":
        room_b()
    else:
        err(a)
    exit(0)

    
def room_b ():
    print("""There is two boul is there #1 and #2 which one u can open?:""")
    opp=input('>')
    if opp=="1":
        print(':) its empty boul !... HA ha ha..')
    elif opp=='2':
        print('U are so lucky it have a choco CAKE... Go and ')
        exit(0)
    else:
        err(opp)
    exit(0)    


game()




