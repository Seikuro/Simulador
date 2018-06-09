import Equipo
import time
import threading
import random
import re
import sys

balon=""
semaforo=threading.Lock()

lista=["alemania","brasil"]

formaciones={
    "1":"4-4-2",
    "2":"4-3-3",
    "3":"4-3-1-2",
    "4":"4-2-3-1"
}

etapas={
    "1":"Fase De Grupos",
    "2":"8vos De Final",
    "3":"4tos De Final",
    "4":"Semifinal",
    "5":"final"   
}




#metodo que ejecutaran los hilos
def jugar(equipo,rival,duracion):

    inicio=time.time()
    tiempo=0

    equipo.cargar_probabilidades()
    rival.cargar_probabilidades()

    while tiempo<duracion:

        time.sleep(1)

        semaforo.acquire()

        global balon
        balon=equipo.nombre

        if equipo.hacer_pases():
            equipo.chutar(rival.prob_encajar)
        tiempo=time.time()-inicio

        semaforo.release()

def sorteo(equipo1, equipo2):

	lista = [equipo1, equipo2]
	ganador = random.choice(lista)

	if ganador.nombre == equipo1.nombre:
		equipos = {'atacante': equipo1, 'defensor': equipo2}
	else:
		equipos = {'atacante': equipo2, 'defensor': equipo1}

	return equipos



#metodo principal a ejecutar
def principal():

    #codigo para escoger la etapa del partido
    etapa=0
    print("Indique una etapa(1-"+str(len(etapas))+"):")
    for keys,values in etapas.items():
        print(keys+")"+values)

    while (etapa<1 or etapa>len(etapas)):

        try:
            etapa=float(input("indique la etapa del partido(1-"+str(len(etapas))+"):"))
        except:
            print("debe ingresar un numero")
            etapa=0
        else:
            if (etapa<1 or etapa>len(etapas)):
                print("debe ingresar una etapa valida(1-"+str(len(etapas))+"):")

    #carga de informacion de los equipos
    print("Indique informacion del Equipo A:")
    e1=cargar_equipo()
    print("Indique informacion del Equipo B:")
    e2=cargar_equipo()




    #sorteo de que equipo jugara primero
    resultado=sorteo(e1,e2)

    ataca_primero=resultado["atacante"]
    defiende_primero=resultado["defensor"]

    print("Se lanza la moneda y "+ataca_primero.nombre+" gana la primera posesión del balon")
    input()

    #definicion de hilos para el 1er tiempo
    hilo1=threading.Thread(name='hilo1',target=jugar,args=(ataca_primero,defiende_primero,10))
    hilo2=threading.Thread(name='hilo2',target=jugar,args=(defiende_primero,ataca_primero,10))

    print("Empieza el partido")

    hilo1.start()
    hilo2.start()

    hilo1.join()
    hilo2.join()

    print("El arbitro pita el final del primer tiempo")
    input()

    #definicion de hilos para el 2do tiempo
    hilo1=threading.Thread(name='hilo1',target=jugar,args=(defiende_primero,ataca_primero,10))
    hilo2=threading.Thread(name='hilo2',target=jugar,args=(ataca_primero,defiende_primero,10))

    print("Empieza el segundo tiempo")

    hilo1.start()
    hilo2.start()

    hilo1.join()
    hilo2.join()

    print("El arbitro pita el final del segundo tiempo")
    input()

    e1=ataca_primero
    e2=defiende_primero

    if(e1.goles==e2.goles and etapa!=1):

        print("El partido se ira a tiempo extra")
        input()
        resultado=sorteo(e1,e2)

        ataca_primero=resultado["atacante"]
        defiende_primero=resultado["defensor"]

        print("Se lanza la moneda y "+ataca_primero.nombre+" gana la primera posesión del balon en el tiempo extra")
        input()

        #definicion de hilos para el 1er tiempo extra
        hilo1=threading.Thread(name='hilo1',target=jugar,args=(ataca_primero,defiende_primero,5))
        hilo2=threading.Thread(name='hilo2',target=jugar,args=(defiende_primero,ataca_primero,5))

        print("Empieza el tiempo extra")

        hilo1.start()
        hilo2.start()

        hilo1.join()
        hilo2.join()

        print("El arbitro pita el final del primer tiempo extra")
        input()          

        #definicion de hilos para el 2do tiempo extra
        hilo1=threading.Thread(name='hilo1',target=jugar,args=(defiende_primero,ataca_primero,10))
        hilo2=threading.Thread(name='hilo2',target=jugar,args=(ataca_primero,defiende_primero,10))

        print("Empieza el segundo tiempo extra")

        hilo1.start()
        hilo2.start()

        hilo1.join()
        hilo2.join()

        print("El arbitro pita el final del segundo tiempo extra")
        input()            

        e1=ataca_primero
        e2=defiende_primero

    print("Finaliza el partido")
    input()
    resultados(e1,e2,etapa)



#metodo para imprimir los resultados del juego
def resultados(equipo1,equipo2,etapa):

    print("Resultados del partido:")

    print(equipo1.nombre+":")
    print("Pases exitosos:"+str(equipo1.pases))
    print("Tiros al arco fallidos:"+str(equipo1.fallos))
    print("Goles:"+str(equipo1.goles))
    print("Formacion utilizada:"+formaciones[str(equipo1.formacion)])

    print(equipo2.nombre+":")
    print("Pases exitosos:"+str(equipo2.pases))
    print("Tiros al arco fallidos:"+str(equipo2.fallos))
    print("Goles:"+str(equipo2.goles))
    print("Formacion utilizada:"+formaciones[str(equipo2.formacion)])

    print("El ultimo equipo en realizar una jugada con el balon fue:"+balon)




def cargar_equipo():

    #codigo para seleccionar nombre del equipo
    nombre=""
    while nombre not in lista :

        nombre = input("Indique el nombre del equipo:")
        
        if nombre.lower() not in lista:
            print ("ingrese un equipo valido")

    #codigo para escoger ranking
    rank=0
    while (rank<1 or rank>100):

        try:
            rank=float(input("indique el ranking del equipo(1-100):"))
        except:
            print("debe ingresar un numero")
            rank=0
        else:
            if (rank<1 or rank>100):
                print("debe ingresar un rango valido(1-100)")

    #codigo para escoger la formacion
    print("Indique una formacion(1-"+str(len(formaciones))+"):")
    for keys,values in formaciones.items():
        print(keys+")"+values)

    formacion=0
    while (formacion<1 or formacion>len(formaciones)):

        try:
            formacion=int(input("indique la formacion del equipo(1-"+str(len(formaciones))+"):"))
        except:
            print("debe ingresar un numero")
            formacion=0
        else:
            if (formacion<1 or formacion>len(formaciones)):
                print("debe ingresar una formacion valida(1-"+str(len(formaciones))+"):")

    return Equipo.Equipo(nombre,rank,formacion)


principal()















