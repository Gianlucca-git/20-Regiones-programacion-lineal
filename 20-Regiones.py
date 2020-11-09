from minizinc import Instance, Model, Solver
## comunicar con minizync
modelo = Model("pruebame2.mzn")
##seleccionar el compilador 
coin_bc= Solver.lookup("coinbc")
##instanciar el proyecto
instance = Instance(coin_bc, modelo)

instance["n"] = 20


##result = instance.solve()
# Output the array q
##print(result)

## Definicion de constantes
Ventiladores = 1000
Equipos = 2000
Costo = 3500
puntos = 1000
## -----------------------------
print ('')
print ('')
print (' -----   ----- BIENVENIDO AL MEJOR SOLUCIONADOR LINEAL DE N ----   ------ ')
print ('')
n=int ( input(" INGRESE EL NUMERO DE REGIONES ->") )
print ('')
##---------------------------------------Poblacion------------------------------------------- input
i = 1
poblacion=[ ]
i_regiones = n
print ('-------------------------------------- POBLACION -------------------------------------')
while (i_regiones > 0):
        poblacion.append ( int ( input("REGION  " +str(i) +
                                         "->") ))
        i += 1 
        i_regiones -=1

##--------------------------------------ESTACIONES-----------------------------------------input
print ('')
print ('-------------------------------------- ESTACIONES -------------------------------------')
i = 1
estaciones = [ ]
i_regiones = n    
while (i_regiones > 0):
        estaciones.append ( int ( input("REGION  " +str(i) +"->") ))
        i += 1 
        i_regiones -=1
##--------------------------------------personal---------------------------------------------input
print ('')
print ('-------------------------------------- PERSONAL -------------------------------------')

i = 1
personal = [ ]
i_regiones = n        
while (i_regiones > 0):
        personal.append ( int ( input("REGION  " +str(i) +
                                         "->") ))
        i += 1 
        i_regiones -=1

##--------------------------------------costo----------------------------------------------input
print ('')
print ('-------------------------------------- COSTO -------------------------------------')


i = 1
costo = [ ]
i_regiones = n        
while (i_regiones > 0):
        costo.append(  (1000) * (  int ( input("REGION  " +str(i) +
                                         "->") )))
        i += 1 
        i_regiones  -=1

##--------------------------------------Muertes ------------------------------------------input

print ('')
print ('-------------------------------------- MUERTES -------------------------------------')


i = 1
muertes = [ ]
i_regiones= n        
while (i_regiones> 0):
        muertes.append ( int ( input("REGION  " +str(i) +
                                         "->") ))
        i += 1 
        i_regiones  -=1

 ##--------------------------------------PROPORCION-----------------------------------------       
## formula_proporcion = e / p
i=0
proporcion = [ ]
i_regiones= n  
while ( i_regiones > 0 ):
    proporcion.append(  estaciones[i] / ( 100000 * poblacion[i]) )
    i += 1 
    i_regiones -= 1 

#print ( 'Proporcion -> ' , proporcion ) 

##-----------------------ASIGNAR BENEFICIO MAYOR AMENOR ----------------------------
    
copia=proporcion.copy()
mayor = len(proporcion)
aux = [0]*mayor
beneficio = [0]*mayor #----sale

while  (mayor  != 0 ):
        i,j= 0,0
        while ( j< len(proporcion)):
            
                if (copia [i]<copia [j] ):
                    i = j
                    j +=1
                else:
                    j+=1
          
        aux [i] = proporcion[i]    
        beneficio [i] = mayor * (-1)
        copia [i] = -1
        mayor -=1

beneficio.insert(0,1)

#print ('beneficio ->', beneficio )   ## funcion  Z
#print('proporcion ->' proporcion) 

##-----------------------2 Ventiladores por Mas MUERTES ----------------------------

#tasa de mortalidad por miles de habitantes

i=0
tasa_mortalidad= [ ]
i_regiones= n  
while ( i_regiones > 0 ):
    tasa_mortalidad.append(  (  (  muertes[i] / ( 100000 * poblacion[i]) ) * 1000000 ))
    i += 1 
    i_regiones -= 1 

copia_mortalidad = tasa_mortalidad.copy ()
mayor_mortalidad = max (copia_mortalidad)
##eliminamos el mayor
copia_mortalidad.remove(mayor_mortalidad )
mayor_2_mortalidad = max (copia_mortalidad)

dos_ventiladores = [1 ]* n
dos_ventiladores [tasa_mortalidad.index (mayor_mortalidad)] = 2
dos_ventiladores [tasa_mortalidad.index (mayor_2_mortalidad)] = 2

## print (tasa_mortalidad ) 


## -------------------------------------  CUALIFICACION --------------------------------------  

print ('')
print ('-------------------------------------- CUALIFICACION -------------------------------------')


print (" A continuacion ingrese la cualificacion que desea asiganarle a cada region" )
print (" ( En caso de no querer asignar, escriba 0 en la region)" )
i = 1
cualificacion =[ ]
i_regiones = n
while (i_regiones > 0):
        cualificacion.append(  (-1)  * ( int ( input("REGION " +str(i) +
                                         "->") ))  ) 
        i += 1 
        i_regiones -=1


      
i_regiones= 20 - n ;
lista_ceros = [0 ]*i_regiones



## ------------------------------------- Print  --------------------------------------
print('')
print ('Funcion Ventiladores ->' , dos_ventiladores  )  ### funcion Ventiladores
print ('Funcion Personal ->', personal   )
print ('Funcion Costo -> ' , costo  )
print ('Funcion Cualificacion ->', cualificacion )
print (' Z beneficio ->', beneficio )   ## funcion  Z
print('')

instance["X_INTRODUCED_1_"] =dos_ventiladores + lista_ceros ;
instance["X_INTRODUCED_3_"] = personal  + lista_ceros;
instance["X_INTRODUCED_5_"] = costo + lista_ceros ;
instance[ "X_INTRODUCED_9_"] =  cualificacion+ lista_ceros ;
instance["X_INTRODUCED_12_"] = beneficio + lista_ceros;

result =  instance.solve().solution
solucion = str ( result )
hasta = "X" + str ( n +1 )
# Output the array q
print('')
print ('-------------------------------------- SOLUCION -------------------------------------')
print( solucion [9:  solucion.find(hasta) ] )




