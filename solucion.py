import matplotlib.pyplot as plt

calculoViejo=0
calculoActual=0
g=9.8
m=68.1
c=12.5
x=[2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54]
y=[]
z=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
for i in z:
    calculoActual=calculoViejo + (g-(c/m)*calculoViejo)*((i+1)-i)
    error=((calculoActual-calculoViejo)/calculoActual)*100
    print("Error: "+str(error)+"%")
    y.append(calculoActual)
    calculoViejo=calculoActual
    print(calculoActual)

plt.plot(z, y)
plt.xlabel('Tiempo')
plt.ylabel("Velocidad")
plt.title('Gráfico de paracaidas')
plt.show()

errorsito=0
n=0
intervalos=[]
while(errorsito==0.05):
    errorsito=((calculoActual-calculoViejo)/calculoActual)*100
    n=n+1
