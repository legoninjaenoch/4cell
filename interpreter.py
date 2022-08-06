from random import randint
x = input()
a,b,c,d = 0,0,0,0
def interpret(str,a,b,c,d):
    i = 0
    while i < len(str):
        if str[i] == 'a':
            a+=1
            i+=1
        elif str[i] == 'b':
            b+=1
            i+=1
        elif str[i] == 'c':
            c+=1
            i+=1
        elif str[i] == 'd':
            d+=1
            i+=1
        elif str[i] == 'A':
            a-=1
            i+=1
        elif str[i] == 'B':
            b-=1
            i+=1
        elif str[i] == 'C':
            c-=1
            i+=1
        elif str[i] == 'D':
            d-=1
            i+=1
        elif str[i] == '>':
            temp = eval(str[i+1])
            if str[i+2] == 'a':
                a = temp
            if str[i+2] == 'b':
                b = temp
            if str[i+2] == 'c':
                c = temp
            if str[i+2] == 'd':
                d = temp
            i+=3
        elif str[i] == '+':
            temp = eval("eval(str[i+1]) + eval(str[i+2])")
            if str[i+3] == 'a':
                a = temp
            if str[i+3] == 'b':
                b = temp
            if str[i+3] == 'c':
                c = temp
            if str[i+3] == 'd':
                d = temp
            i+=4
        elif str[i] == '-':
            temp = eval("eval(str[i+1]) - eval(str[i+2])")
            if str[i+3] == 'a':
                a = temp
            if str[i+3] == 'b':
                b = temp
            if str[i+3] == 'c':
                c = temp
            if str[i+3] == 'd':
                d = temp
            i+=4
        elif str[i] == '.':
            print(eval(str[i+1]))
            i+=2
        elif str[i] == ',':
            print(chr(eval(str[i+1])))
            i+=2
        elif str[i] == '?':
            if str[i+1] == 'a':
                a = randint(0,144)
            if str[i+1] == 'b':
                b = randint(0,144)
            if str[i+1] == 'c':
                c = randint(0,144)
            if str[i+1] == 'd':
                d = randint(0,144)
            i+=2
        elif str[i] == '!':
            if str[i+1] == 'a':
                a = 0
            if str[i+1] == 'b':
                b = 0
            if str[i+1] == 'c':
                c = 0
            if str[i+1] == 'd':
                d = 0
            i+=2
        elif str[i] == '(':
            sc = i+3
            com = ""
            while str[sc] != '}':
                com += str[sc]
                sc+=1
            for j in range(eval(str[i+1])):
                a,b,c,d = interpret(com,a,b,c,d)
            i += len(com)+4
        else:
            i+=1
    return a,b,c,d
a,b,c,d = interpret(x,a,b,c,d)
#print("final values")  these can be commented back in if you want to see the final state of all the cells
#print("a:",a,"b:",b,"c:",c,"d:",d)
input(); #stops the program from closing right after on windows
