C=1
X=0
i=0
Z=0


m=int(input("ingrese su numero entero ="))
while i<m:
    Z=C+i
    print(i,'+',C,'=',Z)
    X=i*(i+1)/2
    print('SUMA',i,'(',i,'+ 1 )','/','2 =',int(X))


    i += 1
        