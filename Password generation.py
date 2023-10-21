import random
import array
digits=['0','1','2','3','4','5','6','7','8','9']
Lcase=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Ucase=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
Symbols=['@','#','$','%','=',':','?','.','/','|','~','>','*','(',')','<','-','_',',']
Clist=digits+Lcase+Ucase+Symbols
w=0
rdigit=random.choice(digits)
rUcase=random.choice(Ucase)
rLcase=random.choice(Lcase)
rsymbol=random.choice(Symbols)
tpass=rdigit+rUcase+rLcase+rsymbol
res=input('Do you want to generate a password?')
if res=='yes':
    n=int(input('Enter the number of password required'))
    len=int(input('Enter the length of the password required'))
    while w <= n-1:
        for x in range(len-4):
            tpass=tpass+random.choice(Clist)
            tpasslist=array.array('u',tpass)
            random.shuffle(tpasslist)
            password=" "
        for x in tpasslist:
            password=password+x
        print(password)
        password=" "
        x=0
        w=w+1
        tpass=rdigit+rUcase+rLcase+rsymbol
else:
    print('Thank You')



