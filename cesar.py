
# Cifrado del cesar
# El cifrador del cesar lo obtuvimos de https://inventwithpython.com/es/14.html
# LA mejora que se le hizo fue calcular la clave por analisis por frecuencia
# Ingresando las letras y la cantidad de repeticiones y asi calculando mediante formula
# la clave para desencriptar el mensaje


def obtenerMensaje():
 # Esta Función captura el mensaje a descifrar   
    print('\n\nAnalisis por frecuencia  El mensaje debe estar cifrado en alfabeto 26\n')
    print('Debemos tener previamente las repeticiones de las letras con su respectiva cantidad\n')
    print('Ingresa tu mensaje:')
    return input()


def obtenerClave():
# Esta función calcula la clave de cifrado a partir de ingresar las
# repeticiones de las letras y su cantidad.
# Se van solicitando de 2 en 2 hasta que los modulos sean iguales y encuentre
# la clave 
    while True:
            print('\n Vamos a hallar la clave del criptograma\n')
            l1 = input("\ningresa la primera letra que mas se repite: ")
            n1 = int(input("numero de repeticiones de la letra "))
            l2 = input("\ningresa la segunda letra que mas se repite: ")
            n2 = int(input("numero de repeticiones de la letra "))
            if l1!=l2 and n1>=n2: 
                
                    r1=(ord(l1)-ord('e'))%26
                    print(r1)
                    r2=(ord(l2)-ord('a'))%26
                    print(r2)
                    
                    if r1==r2:
                        print("\nLa clave para descifrar el mensaje es ", r1)
                        clave = r1
                        return clave
                    else:
                        r1=(ord(l1)-ord('a'))%26
                        print(r1)
                        r2=(ord(l2)-ord('e'))%26
                        print(r2)
                    
                        if r1==r2:
                            print("\nLa clave para descifrar el mensaje es ", r1)
                            clave = r1
                            return clave    
                        else:
                            while r1!=r2:
                                l1 = input("\ningresa la siguiente letra que mas se repite: ")
                                n1 = int(input("numero de repeticiones de la letra "))
                                l2 = input("\ningresa la siguiente letra que mas se repite: ")
                                n2 = int(input("numero de repeticiones de la letra " ))
                                if l1!=l2 and n1>=n2:
                                    r1=(ord(l1)-ord('e'))%26
                                    print(r1)
                                    r2=(ord(l2)-ord('a'))%26
                                    print(r2)
                    
                                    if r1==r2:
                                        print("\nLa clave para descifrar el mensaje es ", r1)
                                        clave = r1
                                        return clave
                                    else:
                                        r1=(ord(l1)-ord('a'))%26
                                        print(r1)
                                        r2=(ord(l2)-ord('e'))%26
                                        print(r2)
                    
                                        if r1==r2:
                                            print("\nLa clave para descifrar el mensaje es ", r1)
                                            clave = r1
                                            return clave
            else:
                print("los valores ingresados no concuerdan con las reglas  por favor ingresar nuevamente los valores solicitados")
            break




def obtenerMensajeTraducido(modo, mensaje, clave):
# este modulo descifra de forma automatizada el mensaje en base a la clave
# hallada en el modulo anterior
    
    clave= -clave
    traduccion = ''

    for simbolo in mensaje:
        if simbolo.isalpha():     
            num = ord(simbolo)
            num += clave

            if simbolo.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif simbolo.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            traduccion += chr(num)

        else:
            traduccion += simbolo
    return traduccion

modo = ""
mensaje = obtenerMensaje()
clave = obtenerClave()
print('\n El texto traducido es:\n\n')
print(obtenerMensajeTraducido(modo, mensaje, clave))