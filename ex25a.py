def a (stuff):
    words = stuff.split(' ')
    return words

def b (words):
    return sorted(words)

def c (words):
    word=words.pop(3)
    print(word)
    return words


def d (words):
    word =words.pop(-1)
    print(word)
    return word


def e (sent):
    words=a(sent)
    return b(words)

def f (sent):
    words = a(sent)
    c(words)
    d(words)

def g (sent):
    words=e(sent)
    c(words)
    d(words)
    
