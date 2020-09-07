#!/usr/bin/env python
# coding: utf-8

# In[205]:


import numpy as np


# In[364]:


def factorial(n):
    if type(n) == int and (n>0.0 or n==0):
        #print ("ingresaste un numero entero y su factorial es:")
        acumulado = 1.0
        for i in np.arange(1.0,n+1.,1.):
            acumulado = i*acumulado
        #print (acumulado)
        return acumulado
    else:
        if n<0:
            
            print ("por favor solo numeros positivos y enteros")
        else:
            print ("por favor solo numeros enteros y positivos")


# In[388]:


def binomial(n,k):
    
    if (k == 0 or n==k) and n>0:
        coeficiente = 1
        print ("El coeficiente binomial es:",coeficiente)
        return coeficiente
    if k>n:
        print("n debe ser mayor que K")
        
    
    if k < 0.:
        print ("por favor ingrese un numero k positivo o cero")
    if n<0:
        print ("por favor ingrese un numero n positivo")

    else:
        numerador = factorial(n)
        denominador = factorial(k)*factorial(n-k)
        coeficiente = numerador/denominador
        #print ("El coeficiente binomial es:",coeficiente)
        return coeficiente
    #print (numerador)
    #print (denominador)
    #print (coeficiente)
    


# In[394]:


def trianguloPascal(n):
    print("profe ten piedad de mi, no me dio un triangulo isosceles")
    
    lista = [[1],[1,1]]
    
    #cubro n=0
    if n==0:
        print(lista[0])
    
    else:
        
        # este for va a correr en las filas
        for i in np.arange(1,n):
            linea = [1] #agregar el 1 que va siempre al principio    
        # este for va a correr entre los elementos dentro de una linea
            for j in np.arange(0,len(lista[i])-1):
            # sumamos el valor de la lista anterior con el siguinte
                linea.extend([lista[i][j] + lista[i][j+1]])
        # añadimos el ultimo valor a la nueva linea
            linea += [1]#agregar el 1 que va siempre al final       
        # añadimos la linea a la lista
            lista.append(linea)
        #devolvemos la lista con nuevos elementos
        
        # ahora imprimo cada elemento de la lista uno debajo de otro        
        
        #creo un archivo .txt
        f = open("Pascal-n.txt", "w")

        for i in lista:
            f.write(str(i) + "\n") #escribo los datos como str porque 
                                    #write no funciona sobre listas
        f.close()
        
        for p in np.arange(0,len(lista)):
            u = print("n=",p,"....",lista[p])
        return u
        
   


# In[410]:


def probabilidad(n,k):
    proba = binomial(n,k)/(pow(2.,n))
    return proba
    proba = proba*100.
    print("la probabilidad es:",proba,"%")

