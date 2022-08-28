import random as rand
def zarb(s,b):
    n,b=0,0
    for i in range (1,11):
        x=rand.randint(0,10)
        y=rand.randint(0,10)
        print(x,'*',y,':')
        s=eval(input())
        if x*y==s:
            b=b+1
        else:
            n=n+1
    print('true:',b)
    print('false:',n)
def taghsim(s,b):
    n,b=0,0
    for i in range (1,11):
        x=rand.randint(0,10)
        y=rand.randint(0,10)
        print(x,'/',y,':')
        s=eval(input())
        if x*y==s:
            b=b+1
        else:
            n=n+1
    print('true:',b)
    print('false:',n)
def Sum(s,b):
    n,b=0,0
    for i in range (1,11):
        x=rand.randint(0,10)
        y=rand.randint(0,10)
        print(x,'+',y,':')
        s=eval(input())
        if x*y==s:
            b=b+1
        else:
            n=n+1
    print('true:',b)
    print('false:',n)
def tafrigh(s,b):
    n,b=0,0
    for i in range (1,11):
        x=rand.randint(0,10)
        y=rand.randint(0,10)
        print(x,'-',y,':')
        s=eval(input())
        if x*y==s:
            b=b+1
        else:
            n=n+1
    print('true:',b)
    print('false:',n)
def tavan(s,b):
    n,b=0,0
    for i in range (1,11):
        x=rand.randint(0,10)
        y=rand.randint(0,10)
        print(x,'^',y,':')
        s=eval(input())
        s=1
        for j in range(1,y+1):
            s=x*s
        if x==s:
            b=b+1
        else:
            n=n+1
    print('true:',b)
    print('false:',n)

#main
x,b=0,1
i=input('+ or - or * or / or t(tavan) or (qiut -1)?')
while(i!='-1'):
    if i=='+':
        x=Sum(x,b)
        y=input('aya edame midahid yas(y) or on (n)')
        if y=='n':
            b=1
        elif y=='y':
            b=0
    elif i=='/':
        x=taghsim(x,b)
        y=input('aya edame midahid yas(y) or on (n)')
        if y=='n':
            b=1
        elif y=='y':
            b=0
    elif i=='-':
        x=tafrigh(x,b)
        y=input('aya edame midahid yas(y) or on (n)')
        if y=='n':
            b=1
        elif y=='y':
            b=0
    elif i=='*':
        x=zarb(x,b)
        y=input('aya edame midahid yas(y) or on (n)')
        if y=='n':
            b=1
        elif y=='y':
            b=0
    elif i=='t':
        x=tavan(x,b)
        y=input('aya edame midahid yas(y) or on (n)')
        if y=='n':
            b=1
        elif y=='y':
            b=0
    else:
        print('adad eshtebah')
    i=input('+ or - or * or / or t(tavan) or (qiut -1)?')
else:
     print('tamam')
