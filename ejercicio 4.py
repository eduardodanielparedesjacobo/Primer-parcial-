
C=1
X=6
i=0

while i<X:
    A = int(input("ingrese el primer numero ="))
    B = int(input("ingrese el segundo numero ="))
    if A==1 and B==0 or A==0 and B==1 or A==1 and B==1:
        print(A , '+', B, '=' , C) 
    elif A==0 and B==0 :
        print(A, '+', B, '=' , 0)
        i += 1
        
