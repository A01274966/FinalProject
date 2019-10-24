#Proyecto "Hangman"
#Autor: Julio César Gómez González
#Matricula: A00882900

#Comentarios generales del programa

# -*- coding: utf-8 -*- 
import random
#Programas con listas======================================================================================

hangman = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']
#=============================================================================================================================

nombre_usuario = input("Ingresa tu nombre:").upper()
print(" HOLA!", nombre_usuario)
print("")
print("  BIENVENID@")
print("      A")
print(" H A N G M A N")

#Programas con listas anidadas================================================================================================
#Correccion de Programas que involucran calculos==============================================================================

lista_categorias_facil = [["sarten", "olla", "estufa", "horno","plato", "taza", "vaso", "jarra"],
                          ["pera", "sandia", "coco", "limon","cereza","piña","uva","kiwi"],
                          ["taco", "pozole", "mole", "tamal", "jaiba", "sope", "birria", "torta"]]



lista_categorias_dificil=[["cuchillo","cuchara", "tenedor", "refrigerador", "cacerola","espatula", "parrilla", "rallador"],
                          ["manzana","guayaba",  "naranja", "platano", "durazno", "aguacate", "maracuya","ciruela"],
                          ["enchiladas", "mixiote", "quesadilla","barbacoa","garnacha", "chalupa", "pambazo", "gordita"]]

#=============================================================================================================================
#=============================================================================================================================


#Programas con funciones y pruebas===========================================================================================

def palabra_random(listapalabras):
    palabra_escojida = random.randint(0, len(listapalabras))
    return listapalabras[palabra_escojida]
def pantalla(hangman):
    print(hangman[len(letras_incorrectas)])
'''Funcion que invertira las palabras de la lista si asi lo quiere el usuario'''

#Programas con cadenas de texto==============================================================================================
def reverse(lista):
    return (list(map(lambda x: x[::-1], lista)))
#============================================================================================================================

#=============================================================================================================================
 
#Programas con listas=========================================================================================================
intentos = ''
letras_incorrectas=[]
#=============================================================================================================================

vidas = 6
fin = True
opcion = "0"

#Correccion de programas con estructura de repeticion========================================================================

while opcion != "1" and opcion != "2":
    print("")
    print("      +---+")
    print("      |   |")
    print("      O   |")
    print("     /|\  |")
    print("     / \  |")
    print("          |")
    print("    =========")
    print("")
    print("Instrucciones(1)")
    print("Nuevo juego(2)")
    opcion = input()
    if opcion == "1":
        op = "0"
        while op != "1":
            print("La computradora automaticamente generara una palabra secreta, tu trabajo es adivinarlo, letra por letra, tienes 5 vidas, si se te acaban, pierdes el juego")
            print("List@? Si(1) o No(2)")
            op = input()
            if op == "1":
                fin = False

    elif opcion == "2":
        fin = False
    else:
        print("Opcion no valida")
        
#============================================================================================================================


#Programas con funciones y pruebas===========================================================================================
        
def nuevo_juego():
    print ('Quieres jugar de nuevo? (Y/N)')
    return input().lower().startswith('y')

#============================================================================================================================

#Correccion de programas con estructura de repeticion========================================================================

print("Modos de Juego")
print("")
print("Facil (Palabras de menos de 6 letras)(1)")
print("Dificil (Palabras de mas de 6 letras)(2)")
print("Invertido (Palabras dificiles invertidas)(3)")
modo_escojido= input()

while modo_escojido != "1" and modo_escojido != "2" and modo_escojido != "3":
    print("Por favor, escoja una opcion valida")
    print("Modos de Juego")
    print("")
    print("Facil (Palabras de menos de 6 letras)(1)")
    print("Dificil (Palabras de mas de 6 letras)(2)")
    print("Invertido (Palabras dificiles invertidas)(3)")
    modo_escojido= input()
    
print("Categorias")
print("")
print("Concina(1)")
print("Frutas(2)")
print("Comida Mexicana(3)")
categoria= input()

while categoria != "1" and categoria != "2" and categoria != "3":
    print("Por favor, escoja una opcion valida")
    print("")
    print("Categorias")
    print("")
    print("Concina(1)")
    print("Frutas(2)")
    print("Comida Mexicana(3)")
    categoria= input()
    
#===========================================================================================================================

#Programas que involucran estructuras de decision===========================================================================
    
if modo_escojido == "1" and categoria == "1":
    palabra = palabra_random(lista_categorias_facil[0])
elif modo_escojido == "1" and categoria == "2":
    palabra = palabra_random(lista_categorias_facil[1])
elif modo_escojido == "1" and categoria == "3":
    palabra = palabra_random(lista_categorias_facil[2])
elif modo_escojido == "2" and categoria == "1":
    palabra = palabra_random(lista_categorias_dificil[0])
elif modo_escojido == "2" and categoria == "2":
    palabra = palabra_random(lista_categorias_dificil[1])
elif modo_escojido == "2" and categoria == "3":
    palabra = palabra_random(lista_categorias_dificil[2])
elif modo_escojido == "3" and categoria == "1":
    palabra = palabra_random(reverse(lista_categorias_dificil[0]))
elif modo_escojido == "3" and categoria == "2":
    palabra = palabra_random(reverse(lista_categorias_dificil[1]))
elif modo_escojido == "3" and categoria == "3":
    palabra = palabra_random(reverse(lista_categorias_dificil[2]))
    
#============================================================================================================================

#Programas con estructura de repeticion======================================================================================
    
while fin == False:
    perdido = 0
    for char in palabra:
        if char in intentos:    
            print(char,"", end="")
        else:    
            print ("_","",end="")
            perdido += 1    

    if perdido == 0:
        fin = True
        print("  Ganaste!!")
        if modo_escojido == "3":
            print("Tu palabra era:", palabra[::-1])
        else:
             print("Tu palabra era:", palabra) 
  
    if perdido != 0:
        intento = input("  Intenta advinar una letra de la palabra:").lower()
        intentos += intento

    if intento not in palabra:  
        letras_incorrectas.append(intento)
        pantalla(hangman)
        vidas -= 1        
        print("NO!")
        print( "Tienes", + vidas, " vidas ")
        
#Programas con cadenas de texto==========================================================================================
        
        '''Se reconoce si el usuario ingresa mas de una sola letra'''
        if len(intento) != 1:
            print("Tip: Ingresa una sola letra")
        
        '''Se reconoce si el usuario ingresa un numero'''
        if(intento.isdigit()):
            print("Tip: Ingresa una letra")
            
#=======================================================================================================================            

        if vidas == 0:
            fin = True
            print("Perdiste")
            print("Tu palabra era:", palabra)

#==========================================================================================================================
        

#Programas que involucran estructuras de decision===========================================================================
    if fin == True:
        if nuevo_juego():
            vidas = 6
            fin= False
            letras_incorrectas=[]
            intentos = ''
#Programas con estructura de repeticion======================================================================================
            print("Modos de Juego")
            print("")
            print("Facil (Palabras de menos de 6 letras)(1)")
            print("Dificil (Palabras de mas de 6 letras)(2)")
            print("Invertido (Palabras dificiles invertidas)(3)")
            modo_escojido= input()
            while modo_escojido != "1" and modo_escojido != "2" and modo_escojido != "3":
                print("Por favor, escoja una opcion valida")
                print("Modos de Juego")
                print("")
                print("Facil (Palabras de menos de 6 letras)(1)")
                print("Dificil (Palabras de mas de 6 letras)(2)")
                print("Invertido (Palabras dificiles invertidas)(3)")
                modo_escojido= input()
                
            print("Categorias")
            print("")
            print("Concina(1)")
            print("Frutas(2)")
            print("Comida Mexicana(3)")
            categoria= input()

            while categoria != "1" and categoria != "2" and categoria != "3":
                print("Por favor, escoja una opcion valida")
                print("")
                print("Categorias")
                print("")
                print("Concina(1)")
                print("Frutas(2)")
                print("Comida Mexicana(3)")
                categoria= input()
#==========================================================================================================================                

#Programas que involucran estructuras de decision===========================================================================
            if modo_escojido == "1" and categoria == "1":
                palabra = palabra_random(lista_categorias_facil[0])
            elif modo_escojido == "1" and categoria == "2":
                palabra = palabra_random(lista_categorias_facil[1])
            elif modo_escojido == "1" and categoria == "3":
                palabra = palabra_random(lista_categorias_facil[2])
            elif modo_escojido == "2" and categoria == "1":
                palabra = palabra_random(lista_categorias_dificil[0])
            elif modo_escojido == "2" and categoria == "2":
                palabra = palabra_random(lista_categorias_dificil[1])
            elif modo_escojido == "2" and categoria == "3":
                palabra = palabra_random(lista_categorias_dificil[2])
            elif modo_escojido == "3" and categoria == "1":
                palabra = palabra_random(reverse(lista_categorias_dificil[0]))
            elif modo_escojido == "3" and categoria == "2":
                palabra = palabra_random(reverse(lista_categorias_dificil[1]))
            elif modo_escojido == "3" and categoria == "3":
                palabra = palabra_random(reverse(lista_categorias_dificil[2]))
        else:
            break
        
#=========================================================================================================================
#=========================================================================================================================
   

#Elemento extra===========================================================================================================
        
#PROGRAMA SUBIDO A GITHUB, SE PUEDE ACCEDER UTILIZANDO EL SIGUIENTE LINK https://github.com/A01274966/FinalProject/blob/master/HangmanProyecto.py

#=========================================================================================================================
            