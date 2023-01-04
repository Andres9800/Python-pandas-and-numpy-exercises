# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 10:48:30 2022

@author: adsc9
"""

import math as mt
import numpy as np
import pandas as pd
print("--------------- Ejercicio 1 ---------------")

class Triangulo:
    def __init__(self, lado,base,altura):
        self.__lado = lado
        self.__base = base
        self.__altura = altura
        
    @property
    def lado(self):
        return self.__lado
    @lado.setter
    def lado(self, e):
        self.__lado = e
        
    @property
    def base(self):
        return self.__base
    
    @base.setter
    def base(self, e):
        self.__base = e
        
    @property
    def altura(self):
        return self.__altura
    
    @altura.setter
    def altura(self, e):
        self.__altura = e
        
    def __str__(self):
        return "Triangulo: lado : %i, Base: %i, Altura: %i)" % (self.lado,self.base,self.altura)
    
    def calcular_area(self):
        area = int (self.__base) * int (self.__altura) / 2.0
        return (area)
    
    def calcular_perimetro(self):
        perimetro = int (self.__lado) * 3.0
        return (perimetro)

class Rectangulo:
    def __init__(self, base,altura):
        self.__base = base
        self.__altura = altura
                
    @property
    def base(self):
        return self.__base
    
    @base.setter
    def base(self, e):
        self.__base = e
        
    @property
    def altura(self):
        return self.__altura
    
    @altura.setter
    def altura(self, e):
        self.__altura = e
        
    def __str__(self):
        return "Rectangulo: Base: %i, Altura: %i)" % (self.base,self.altura)
    
    def calcular_perimetro(self):
        perimetro = (int (self.__base) + int (self.__altura)) * 2.0
        return (perimetro)
    
    def calcular_area(self):
        area = int (self.__base) * int (self.__altura)
        return (area)
    
"""

g = Triangulo(5, 16, 20)
h = Rectangulo(5, 20)

print(g.__str__())
print("Area:")
print(g.calcular_area())
print("Perimetro:")
print(g.calcular_perimetro())

print(h.__str__())
print("Area:")
print(h.calcular_area())
print("Perimetro:")
print(h.calcular_perimetro())"""


print("\n")
print("--------------- Ejercicio 2 ---------------")

class Operacion:
    def __init__(self, U,V):
        self.__U = U
        self.__V = V

        
    @property
    def U(self):
        return self.__U
    @U.setter
    def U(self, e):
        self.__U = e
        
    @property
    def V(self):
        return self.__V
    
    @V.setter
    def V(self, e):
        self.__V = e
                
    def __str__(self):
        return "Vector U :" + str(self.U) + " Vector V:" + str(self.V)
    
    def sumar(self):
        suma = np.array (self.__U) + np.array (self.__V)
        return (suma)
    def restar(self):
        suma = np.array (self.__U) - np.array (self.__V)
        return (suma)
    def multiplicar(self):
        multi = np.dot(self.__U, self.__V)
        return (multi)
    def correlacion(self):
        multi = np.corrcoef(self.__U, self.__V)[0][1]
        return (multi)
    def covarianza(self):
        multi = np.cov(self.__U, self.__V)[0][1]
        return (multi)
"""
u = [1,1/2,3]

v = [4,-4,1]


ope = Operacion(u, v)
print(ope.__str__())
print("Sumar: ")
print(ope.sumar())
print("Restar: ")
print(ope.restar())
print("Producto punto: ")
print(ope.multiplicar())
print("Correlacion: ")
print(ope.correlacion())
print("Covarianza: ")
print(ope.covarianza())
"""

print("\n")

print("--------------- Ejercicio 3 ---------------")

class Jugadores:
    def __init__(self, DF = pd.DataFrame()):
        self.__num_filas = DF.shape[0]
        self.__num_columnas = DF.shape[1]
        self.__DF = DF

    @property
    def num_filas(self):
        return self.__num_filas
    @property
    def num_columnas(self):
        return self.__num_columnas
    @property
    def DF(self):
        return self.__DF
    
    def cantidad_equipos(self, name_team):
         
        return self.__DF.groupby('team')['team'].count()[name_team]
                
    def resumen_columna(self, name_colum):
        if (self.__DF[name_colum].dtype == object):
            return self.__DF[name_colum].mode()
        else:
            return self.__DF[name_colum].mean()
        
    def agregar_jugador(self, name, team, position, minutes, shots, passes, tackles, saves):
        
        self.__DF.loc[len(self.__DF.index)] = [name, team, position, minutes, shots, passes , tackles, saves ]
        return "EL Jugador se agrego Corrrectamente"
            
    def eliminar_jugador(self, name):
        num = 0
        num = self.__DF.index[(self.__DF["surname"] == name)]
        
        if(num.array.size > 0):
            self.__DF.drop(self.__DF.index[(self.__DF["surname"] == name)],axis=0,inplace=True)
            return "EL Jugador se Elimino Corrrectamente"
        else:
            return "El jugador No existe"
        
    def resumen_jugador(self, name):
        num = 0
        num = self.__DF.index[(self.__DF["surname"] == name)]
        
        
        if(num.array.size > 0):
            return self.__DF.loc[[num[0]]]
            return 
        else:
            return "El jugador No existe"
    def actualizar_position(self, name , posicion):
        num = 0
        num = self.__DF.index[(self.__DF["surname"] == name)]
        if(num.array.size > 0):
            self.__DF.at[num[0],'position']=posicion
            return self.__DF.loc[[num[0]]]
            return 
        else:
            return "El jugador No existe"



df = Jugadores(pd.read_csv('Players1.csv'))

print("Cantidad equipos : Jugadores del eequipo Algeria:")
print(df.cantidad_equipos('Algeria'))
print("Resumen columna : shots")
print(df.resumen_columna('shots'))
print("Resumen columna : team")
print(df.resumen_columna('team'))
print("----------------------------Agregar Jugador------------------------")
print(df.DF)
print(df.agregar_jugador("Wendy","H","forward",10,10,5,6,0))
print("----------------------------SE AGREGO A WENDY------------------------")
print(df.DF)
print("----------------------------ELIMINEMOS A  Torres 2 3 ------------------------")
print(df.eliminar_jugador('Torres 2 3'))
print(df.DF)
print("----------------------------resumen_jugador  ------------------------")
print(df.resumen_jugador('Onyewu'))
print("----------------------------actualizar_position  ------------------------")
print(df.actualizar_position('Onyewu', "ninguno"))
print(df.DF)



print("\n")

print("--------------- Ejercicio 4 ---------------")



class Analisis():
    def __init__(self,matrix):
        self.__matriz = matrix
    
    @property
    def matriz(self):
        return self.__matriz
    
    @matriz.setter
    def matriz(self, e):
        self.__matriz = e

    def as_data_frame(self):
        return  pd.DataFrame(self.__matriz)
    
    def  desviacion_estandar(self):
         data = pd.DataFrame(self.__matriz)
         return np.std(data)
     
    def  varianza(self):
         data = pd.DataFrame(self.__matriz)
         return np.var(data) 
     
    def  moda(self):
         data = pd.DataFrame(self.__matriz)
         return (data.mode()[0])
     
    def maximo(self):
        data = pd.DataFrame(self.__matriz)
        return data.max().max()
    
    def buscar(self,valor):
        data = pd.DataFrame(self.__matriz)
        k, h = data.shape
        for i in range(k):
            for j in range(h):
                if (data.iloc[i,j] == valor):
                   return [i,j]
        return None 
        
     
"""
paraM = np.matrix([ [1,2,3,4,5], [1,7,8,9,10], [2,1,12,13,14] ])


print("Matriz convertida en DataFrame de Pandas")
ana = Analisis(paraM)
print(ana.as_data_frame())
print("Imprimo la desviacion_estandar")
print(ana.desviacion_estandar())
print("Varianza")
print(ana.varianza())
print("Moda")
print(ana.moda())
print("Maximo")
print(ana.maximo())
print("Buscar")
print(ana.buscar(8))
"""




print("\n")
print("--------------- Ejercicio 5 ---------------")

class Vuelo:
    def __init__(self, numero, horaSalida, horaLlegada):
        self. __numero = numero
        self. __horaSalida = horaSalida
        self. __horaLlegada = horaLlegada
    
    @property
    def numero(self):
        return self.__numero
    @property
    def horaLlegada(self):
        return self.__horaLlegada
    @property
    def horaSalida(self):
        return self.__horaSalida
    
    @numero.setter
    def numero(self, e):
        self.__numero = e
        
    @horaLlegada.setter
    def horaLlegada(self, e):
        self.__horaLlegada = e
        
    @horaSalida.setter
    def horaSalida(self, e):
        self.__horaSalida = e
        
    def __str__(self):
        st = "**********Vuelo*************\n"
        st = st + 'Numero: ' + str(self.numero) + '\n'
        st = st +'Hora de salida: ' +str(self.__horaSalida) + '\n'
        st = st +'Hora de llegada: ' +str(self.__horaLlegada) 
        return st
        
class VueloComercial(Vuelo):
    def __init__(self,numero, horaSalida, horaLlegada, listaPasa):
        super().__init__(numero, horaSalida, horaLlegada)
        self.__listaPasa = listaPasa
    
    @property
    def listaPasa(self):
        return self.__listaPasa
    
    @listaPasa.setter
    def listaPasa(self, e):
        self.__listaPasa = e

    def __str__(self):
        st = super().__str__() + '\n' + 'Lista de los pasajeros del vuelo : ' + str(self.__listaPasa)
        return st
    
    def agregar(self, pasajero):
        self.__listaPasa.append(pasajero)
        
    def eliminar(self):
        self.__listaPasa.pop()
        
        
#------------------------------------------------------------------------------
class VueloCarga(Vuelo):
    def __init__(self, numero, horaSalida, horaLlegada ,peso_maximo):
        super().__init__(numero, horaSalida, horaLlegada)
        self.__peso_maximo = peso_maximo
    
    @property
    def peso_maximo(self):
        return self.__peso_maximo
    
    @peso_maximo.setter
    def peso_maximo(self, nuevo_valor):
        self.__peso_maximo = nuevo_valor

    def __str__(self):
        st = super().__str__() + '\n' + 'Peso Maximo: ' + str(self.peso_maximo)
        return st
    
    

class VueloInternacional(VueloComercial):
    def __init__(self, numero, horaSalida, horaLlegada,listaPasa, pais_destino):
        super().__init__(numero, horaSalida, horaLlegada,listaPasa)
        self.__pais_destino = pais_destino

    @property
    def pais_destino(self):
        return self.__pais_destino
    
    @pais_destino.setter
    def pais_destino(self, e):
        self.__pais_destino= e

    def __str__(self):
        st = super().__str__() + "\n" + "Destino del Vuelo: " + self.pais_destino
        return st


class VueloLocal(VueloComercial):
    def __init__(self, numero, horaSalida, horaLlegada,listaPasa, minimo_pasajeros):
        super().__init__(numero, horaSalida, horaLlegada,listaPasa)
        self.__minimo_pasajeros = minimo_pasajeros

    @property
    def minimo_pasajeros(self):
        return self.__minimo_pasajeros
    
    @minimo_pasajeros.setter
    def pais_destino(self, e):
        self.__minimo_pasajeros= e

    def __str__(self):
        st = super().__str__() + "\n" + "Cantidad minima de pasajeros: " + str(self.minimo_pasajeros)
        return st

#------------------------------------------------------------------------------

class Pasajero:
    def __init__(self, precioBoleto, codigo, nombre, porcentaje_impuesto, descuento):
        self.__precioBoleto = precioBoleto
        self.__codigo = codigo
        self.__nombre = nombre
        self.__porcentaje_impuesto = porcentaje_impuesto
        self.__descuento = descuento
    
    @property
    def precioBoleto(self):
        return self.__precioBoleto
    
    @precioBoleto.setter
    def precioBoleto(self, e):
        self.__precioBoleto = e

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, e):
        self.__codigo = e
        
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_valor):
        self.__nombre = nuevo_valor

    @property
    def porcentaje_impuesto(self):
        return self.__porcentaje_impuesto

    @porcentaje_impuesto.setter
    def porcentaje_impuesto(self, e):
        self._porcentaje_impuesto = e

    @property
    def descuento(self):
        return self.__descuento
    
    @descuento.setter
    def descuento(self, nuevo_valor):
        self.__descuento= nuevo_valor
        
    def total_pagar(self):
        return(self.precioBoleto + self.porcentaje_impuesto * self.precioBoleto -self.precioBoleto * self.descuento)
    
    def __repr__(self):
        st = "\n****************Pasajero****************\n"
        st = st +'Precio: ' + str(self.precioBoleto) + '\n'
        st = st +'Código: ' +str(self.codigo) + '\n'
        st = st +'Nombre: ' +str(self.nombre) +'\n'
        st = st +'Porcentaje de impuesto: ' +str(self.porcentaje_impuesto) + '\n'
        st = st +'Descuento: ' +str(self.descuento) + '\n'
        st = st +'Precio a pagar: '+ str(self.total_pagar())
        return st



class Pasajero_frecuente(Pasajero):
    def __init__(self, precioTiquete, codigo, nombre, porcentaje_impuesto, descuento, can_puntos):
        super().__init__(precioTiquete, codigo, nombre, porcentaje_impuesto, descuento)
        self.__can_puntos = can_puntos

    @property
    def can_puntos(self):
        return self.__can_puntos
    
    @can_puntos.setter
    def can_puntos(self, nuevo_valor):
        self.__descuentocan_puntos= nuevo_valor
        
    def __repr__(self):
        st = super().__repr__() + "\n" + "Cantidad de puntos del Pasajero: " + str(self.can_puntos) + '\n'
        return st



class Pasajero_No_frecuente(Pasajero):
    def __init__(self, precio_tiquete, codigo, nombre, porcentaje_impuesto, descuento, primer_vuelo):
        super().__init__(precio_tiquete, codigo, nombre, porcentaje_impuesto, descuento)
        self.__primer_vuelo = primer_vuelo

    @property
    def primer_vuelo(self):
        return self.__primer_vuelo
    
    @primer_vuelo.setter
    def can_puntos(self, nuevo_valor):
        self.__primer_vuelo= nuevo_valor
        
    def __repr__(self):
        st = super().__repr__() + "\n" + "Primer vuelo del Pasajero?: " + str(self.primer_vuelo)+ '\n'
        return st



lista = [ 
     Pasajero_frecuente(500, "54E10", "Andres Cordero Gutierrez ", 0.1, 0.25, 632),
     Pasajero_frecuente(500, "54E10", "Marco Tulio Salas", 0.1, 0.25, 55),
     Pasajero_No_frecuente(500, "54E10", "Penelope Cruz", 0.1, 0.10, True),
     Pasajero_No_frecuente(500, "54E10", "Tomate Rojo Pequeno", 0.1, 0.10, False),
     ]

pasa1 = Pasajero_frecuente(500,"54E10", "Nacho Varga", 0.1, 0.25, 22)
pasa2 = Pasajero_No_frecuente(500, "54E10", "Wendy Largaespada", 0.1, 0.10, True)


"""
print("\n---------------------------------Vuelo Carga -------------------------------------")
vCarga = VueloCarga(1, 7, 13, 540000)
print(vCarga)

print("\n---------------------------------Vuelo Internacional -------------------------------------")
vInter = VueloInternacional(2, 22,4,lista,'Italia')
print(vInter)
print("\n---------------------------------Vuelo Internacional AGREGO-------------------------------------")
vInter.agregar(pasa1)
print(vInter)
print("\n---------------------------------Vuelo Internacional ELIMINO-------------------------------------")
vInter.eliminar()
print(vInter)


print("\n---------------------------------------Vuelo Local --------------------------------------")
vLocal = VueloLocal(3, 5,10,lista,33)
print(vLocal)

print("\n---------------------------------------Vuelo Local AGREGO --------------------------------------")
vLocal.agregar(pasa2)
print(vLocal)
print("\n---------------------------------------Vuelo Local ELIMINO--------------------------------------")

vLocal.eliminar()
print(vLocal)
"""

print("\n")
print("--------------- Ejercicio 6 ---------------")




class mi_DF(pd.DataFrame):
    def __init__(self, *para1, **para2):
        super(mi_DF, self).__init__(*para1, **para2)
        self.__num_filas = self.shape[0]
        self.__num_columnas = self.shape[1]
        
    @property
    def num_filas(self):
        return self.__num_filas
    
    @property
    def num_columnas(self):
        return self.__num_columnas

    def maximo(self):
        max = self.iloc[0,0]
        for i in range(self.num_filas):
            for j in range(self.num_columnas):
                if self.iloc[i,j] > max:
                    max = self.iloc[i,j]
        return max
    
    def valores(self):
        min = self.iloc[0,0]
        max = self.iloc[0,0]
        total_ceros = 0
        total_pares = 0
        for i in range(self.num_filas):
            for j in range(self.num_columnas):
                if self.iloc[i,j] > max:
                    max = self.iloc[i,j]
                if self.iloc[i,j] < min:
                    min = self.iloc[i,j]
                if self.iloc[i,j] == 0:
                    total_ceros = total_ceros+1
                if self.iloc[i,j] % 2 == 0:
                    total_pares = total_pares+1
        return {'Maximo' : max, 'Minimo' : min, 'Total_Ceros' : total_ceros, 'Pares' : total_pares}
    
    def estadisticas(self,nc):
        media = np.mean(self.iloc[:,nc])
        mediana = np.median(self.iloc[:,nc])
        deviacion = np.std(self.iloc[:,nc])
        varianza = np.var(self.iloc[:,nc])
        maximo = np.max(self.iloc[:,nc])
        minimo = np.min(self.iloc[:,nc])
        return {'Variable' : self.columns.values[nc],
                'Media' : media,
                'Mediana' : mediana,
                'DesEst' : deviacion,
                'Varianza' : varianza,
                'Maximo' : maximo,
                'Minimo' : minimo}
    
    def candivisibles5(self):
        can = 0
        for i in range(self.num_filas):
            for j in range(self.num_columnas):
                if self.iloc[i,j] % 5 == 0:
                    can += 1
        return can
    
    def coVaCorre2(self, c1, c2):
        co = np.corrcoef(self.iloc[:,c1], self.iloc[:,c2])[0,1]
        cov = np.cov(self.iloc[:, c1], self.iloc[:,c2])[0,1]
        f = ["Covarianza: " + str(cov), "Correlacion: " + str(co)]
        return f

"""
dat = pd.read_csv('ejemplo_estudiantes.csv',delimiter=';',decimal=",",index_col=0)
datos = mi_DF(dat)

print("Mostramos los Valores")
print(datos.valores())
print("Mostramos los Estadisticas")
print(datos.estadisticas)
print("Cantidad de valores de este DataFrame que son divisibles entre 5 ")
print(datos.candivisibles5())
print("La covarianza y la correlacion entre las  columnas 1 y 2 ")
print(datos.coVaCorre2(1,2))

"""