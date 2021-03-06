i=1
s=0

while i<=7:
    print('dia',i)
    h=int(input("tiempo promedio usado por dia  = "))
    i+=1
    s+=h
T=s/(i-1)   
print('total de horas estudiadas por semana = ',s)
print('tiempo promedio horas a la semana que estudia cada dia = ',T)

