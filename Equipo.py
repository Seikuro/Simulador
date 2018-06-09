import time
import random

class Equipo(object):
    
    def __init__(self,nom,rank,formacion):
        
        self.nombre=nom
        self.rank=int(rank)
        self.formacion=formacion
        self.pases=0
        self.goles=0
        self.fallos=0

    def porcentajes(self):
        if 1 <= self.rank <= 10:
            return {'ganar': 0.80, 'anotar': 0.70, 'encajar': 0.10, 'pase':0.70}
        elif 11 <=self.rank <= 20:
            return {'ganar': 0.70, 'anotar': 0.60, 'encajar': 0.15, 'pase':0.60}
        elif 21 <= self.rank <= 30:
            return {'ganar': 0.60, 'anotar': 0.50, 'encajar': 0.20, 'pase':0.50}
        elif 31<= self.rank <= 40:
            return {'ganar': 0.55, 'anotar': 0.40, 'encajar': 0.30, 'pase':0.40}
        elif 41 <= self.rank <=50:
            return {'ganar': 0.50, 'anotar': 0.30, 'encajar': 0.40, 'pase':0.35}
        elif 51 <= self.rank <= 60:
            return {'ganar': 0.45, 'anotar': 0.25, 'encajar': 0.50, 'pase':0.30}
        elif 61 <= self.rank <= 70:
            return {'ganar': 0.40, 'anotar': 0.20, 'encajar': 0.55, 'pase':0.25}
        elif 71 <=self.rank <=80:
            return {'ganar': 0.35, 'anotar': 0.15, 'encajar': 0.60, 'pase':0.20}
        elif 81 <= self.rank<=90:
            return{'ganar': 0.30, 'anotar': 0.10, 'encajar': 0.70, 'pase':0.15}
        elif 91 <= self.rank <=100:
            return {'ganar': 0.20, 'anotar': 0.05, 'encajar': 0.80, 'pase':0.10}

    def cargar_probabilidades(self):

        probabilidades = self.porcentajes()

        self.prob_ganar = probabilidades['ganar']
        self.prob_anotar = probabilidades['anotar']
        self.prob_encajar = probabilidades['encajar']
        self.prob_pase = probabilidades['pase']   

    def cal_pase(self):
        return (random.randint(0,100) + (self.prob_pase * 100))

    def hacer_pases(self):

        print(self.nombre+" tiene el balon")

        cont_pase = 0

        while self.cal_pase()>100 and  cont_pase < 4:

            self.suma_pase()
            cont_pase = cont_pase+1
            print(str(cont_pase)+" pase de:"+self.nombre)
            time.sleep(0.5)
           
        if cont_pase<4:

            print("falla el pase y pierde el balon")
            cont_pase=0
            return False

        if cont_pase == 4:
            return True    

    def chutar(self, encajar_rival):
        time.sleep(0.1)
        shoot =  random.randint(0,100) + (self.prob_anotar*100) + (encajar_rival*100)

        if shoot >= 150:
            self.sumar_gol()
            print("gol")
        else:
            self.sumar_fallos()
            print("dispara pero el portero atrapa la pelota")

    def suma_pase(self):
        self.pases += 1
    
    def sumar_gol(self):
        self.goles += 1
    
    def sumar_fallos(self):
        self.fallos += 1
    
    def imprimir(self):
        print("soy:"+self.nombre)
