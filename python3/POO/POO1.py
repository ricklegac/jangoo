class Coche: 
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo 
        self.largoChassis=250 #propiedad comun de class Coche
        self.largoAncho = 120
        self.__ruedas = 4
        self.enmarcha = False

    def arrancar(self,arrancamos ): # al estar dentro de la clase Coche esto es un metodo no una funcion 
        self.enmarcha = arrancamos

        check= self.__chequeo()
        if (self.enmarcha and check):
            print("el auto esta en marcha")
        elif(self.enmarcha and not check):
            print ("falta chequear el vehiculo")
        else: 
            print("el vehiculo esta quieto ") 
    #    Caracteristicas de un metodo 
    #    palabra reservada def 
    #    parametro por defecto es self, self hace refencia al propio objeto perteneciente a la clase 
    
    def estado(self):
        print ("Cantidad de ruedas = " , self.__ruedas , "\n")
        print ("marca: " , self.marca , "\nmodelo: ",self.modelo ," \n")
    
    def __chequeo(self): #metodo encapsulado  
        print("chequeando el auto")
        self.freno = True
        self.agua = True
        self.gasolina = True
        if (self.gasolina and self.agua and self.freno ):
            return True
        else:
            return False

micoche = Coche("toyota","corolla")
micoche.arrancar(True)
micoche.ruedas = 5
micoche.estado()
print (micoche.largoChassis);

c1= Coche("Nissan", "Frontier")
c2 = Coche("Dodge" ,"Ram")

coches= [micoche,c1,c2]
import pickle
fichero = open("loscoches","wb")
pickle.dump(coches,fichero)
fichero.close()
del fichero

apertura_fichero = open("loscoches","rb")
miscoches= pickle.load(apertura_fichero)
for c in miscoches:
    print (c.estado())