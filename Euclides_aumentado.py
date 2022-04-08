#Integrantes:
#-Marcelo Torres Acuña
#-Jhon Berly Taype Alccaccahua
#-Brian Bermudez Navarro
def e_euclides(a,b): 
    if (b == 0):
      return a,1,0
    d,x1,y1 = e_euclides(b, a % b)
    x = y1
    y = x1 - y1 * int(a / b)
    return d,x,y

a=int(input("ingrse el valor de 'a': "))
b=int(input("ingrse el valor de 'b': "))
print("\n")
mcd,x,y=e_euclides(a,b)

print("Maximo Comun Divisor de ",a," y ",b," es: ",mcd,"\n")
print("El valor de x es: ",x,"\n")
print("El valor de y es: ",y,"\n")
print("a(x)+b(y)=mcd\n")
print(a,"(",x,") + ",b,"(",y,") = ",(a*x)+(b*y))