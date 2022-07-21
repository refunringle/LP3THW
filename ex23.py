encoding=input('enter the copying file name:')
error=input('enter the file coping to :')

def main (a,encoding,errors):
    line =a.readline()
    if line:
        pl(line,encoding,errors)
        return main(a,encoding,errors)

def pl (line,encoding,errors):
    nl = line.strip()
    raw_bytes = nl.encode(encoding,errors=errors)
    cs= raw_bytes.decode(encoding,errors=errors)

    print(raw_bytes,"$$$$===>>>>",cs)

lang=open("file.txt", encoding="utf-8")
main(lang,encoding,error)



