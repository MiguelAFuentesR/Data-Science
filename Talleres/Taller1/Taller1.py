#Solución Taller 1 Miguel Angel Fuentes Ramirez - 20182005007

#Primero se genera el numero aleatorio , para ello se importa el modulo random
import random as rn

#Generacion de un numero aleatorio entre 0 y 99
numero_random = rn.randint(0, 99)

#Se definen las Variables del Programa:

Puntaje = 100
numero_usuario = 0
Intentos = 0


#Se utiliza un bucle While que permita controlar el numero de intentos del usuario

while Intentos < 10 and numero_usuario != numero_random:
    
    numero_usuario = int(input("Intenta a Adivinar que número eligió tu PC: \n"))
    Intentos = Intentos+1 
    #Se controla el numero de intentos para la impresión de pistas
    if Intentos !=10:
        #Se compara si el número ingresado es igual al random
        if numero_usuario == numero_random :  
            print("\n ¡¡¡¡¡ Felicidades Adivinaste !!!!! ")      
            break #Se rompe el bucle si se adivina el número
        #Se compara si el número ingresado es menor al random
        elif (numero_usuario < numero_random):
            print("\n Oh no .. Casi lo logras ! , El numero random es mayor a ",numero_usuario)
            print('\n Te quedan ',10-Intentos," Intentos")
        #Se compara si el número ingresado es mayor al random
        elif (numero_usuario > numero_random):
            print("\n Oh no .. Casi lo logras ! , El numero random es menor a ",numero_usuario)
            print('\n Te quedan ',10-Intentos," Intentos")              
    #Se resta 10 puntos por cada intento perdido
    Puntaje = Puntaje-10
 #Se determina que el usuario perdio ya que utilizo todos los intentos posibles
else:
    
    print("¡¡¡¡¡ Perdiste !!!!! :( ")
    
print("Lograste un Puntaje de :", Puntaje ,"Puntos de 100,  El número random era : ",numero_random)   
