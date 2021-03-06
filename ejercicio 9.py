i=float(input("cual es su monto a invertir = "))
a=float(input("cual es el interes anual (%)= "))
n=int(input("A cuantos años de invercion = "))
p=a/100

c=i*((1+p)**n)
print('El capital obtenido por la inversion es de = ',round(c,3))
