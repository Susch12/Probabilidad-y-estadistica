#!/usr/bin/env python3
import time 
import statistics
# Variable globales
existe_pob = False
existe_var = False
existe_muestra = False 
existe_varianza = False
while True:
    
    print("\n--------------------------------------------------------")
    print("-------------------- MENU ------------------------------")
    print("--------------------------------------------------------\n")

    print("[+] 1. Ingrese población.")
    print("[+] 2. Muestre la población.")
    print("[+] 3. Indique el rango de la muestra")
    print("[+] 4. Ingresar el tipo de variable.")
    print("[+] 5. Muestre el tipo de variable.")
    print("[+] 6. Tabla de frecuencias.")
    print("[+] 7. Graficos")
    print("[+] 8. Medidas de tendencia central.(Media/Mediana/Moda)")
    print("[+] 9. Medidas de dispersión.(Varianza/Desviación_estandar)")
    print("[+] 0. Salir.")

    opcion = input("\nIngresa una opción: ")

    if opcion != '0':
        if opcion == '1':
            if existe_pob:
                print("[!] Existe una población")
                print("[!] ¿Quieres resetear la población?")
                aux = input("S/N: ")
                if aux == "S" or aux == "s":
                    poblacion.clear()
                    print("[*] Lista resetada...")
                    existe_pob = False
                    time.sleep(3)
                elif aux == "N" or aux == "n":
                    print("[+] Se mantiene la lista...")
                    time.sleep(3)

                else:
                    print("[!] No existe opcion para ese parametro")
                    time.sleep(3)
            else: 
                print("\n[+] Opción 1: Ingrese la población")
                print("---------------------------------------------------\n")
                entrada = input("[*] Ingrese la lista: ")
                poblacion_tuple = eval(entrada)
                poblacion = list(poblacion_tuple)
                existe_pob = True
                time.sleep(3)
        elif opcion == '2':

            if existe_pob:
                print("\n[+] Opción 2: Muestre la población")
                print("---------------------------------------------------\n")
                print(f"[*] La poblacion es: {poblacion}")
                time.sleep(4)
            else:
                print("[!] No existe una población que se muestre...")
                time.sleep(1)

        elif opcion == '3':
            if existe_pob:
                poblacion = list(poblacion)
                print("\n[+] Opción 3: Indique el rango de la muestra")
                print("---------------------------------------------------\n")
                print(f"[+] La cantidad de numeros en la lista es: {len(poblacion)}")
                Inicio = int(input("[+] Ingresa el número de inicio para el rango: "))-1
                Final = int(input("[+] Ingresa el número de final para el rango: "))
                muestra = []
                for i in range(Inicio, Final):
                    muestra.append(poblacion[i])
                print(f"[!] La muestra es: {muestra}")
                existe_muestra = True
                time.sleep(4)
            else:
                print("[!] No existe una población...")
                time.sleep(2)

        elif opcion == '4':

            print("\n[+] Opción 4: Ingresar el tipo de variable")
            print("---------------------------------------------------\n")

            var = input("[+] Ingresa el tipo de variable (Cuantitativa/Cualitativa): ")

            if var == "Cuantitativa" or var == "cuantitativa":
                print("[!] Escogiste Cuantitativa")
                espe = input("[*] Es Discreta o continua: ")
                if espe == "Discreta" or espe == "discreta" or espe == "Continua" or espe == "continua":
                    print("[+] Se guardo exitosamente el tipo de variable.")
                    existe_var = True
                    time.sleep(4)
                else:
                    print("[!] No existe esa opcion...\n [!] Intenta de nuevo.")
                    time.sleep(4)
            else:
                if var == "Cualitativa" or var == "cualitativa":
                    print("[!] Escogiste Cualitativa")
                    espe = input("[*] ¿Es Ordinal o Nominal? ")
                    if espe == "Ordinal" or espe == "ordinal" or espe == "Nominal" or espe == "nominal":
                        print("[+] Se guardo exitosamente el tipo de variable.")
                        existe_var = True
                        time.sleep(4)
                    else:
                        print("[!] No existe esa opcion...\n [!] Intenta de nuevo.")
                        time.sleep(4)
                else:
                    print("[!] No existe una opción disponible para la entrada que ingresaste\n [!] Vuelve a intentarlo.")
                    time.sleep(3)
        
        elif opcion == '5':
            if existe_var:
                print(f"[*] La variable es: {var}, {espe}")
                time.slee(4)
            else:
                print("[!] No existe aún el tipo de variable...")
                time.sleep(3)

        elif opcion == '6':
            if existe_pob:
                unico = set(poblacion)
                for elemento in unico:
                    repeticiones = poblacion.count(elemento)
                    print(f"El número {elemento} se repite {repeticiones} veces en la población.")
                    time.sleep(6)
                    #for elemento, cantidad in frecuencia.items():
                    #print(f"{elemento}: {cantidad} veces."
        elif opcion == '7':
            pass
        elif opcion == '8':
            while True:

                print("\n--------------------------------------------------------")
                print("------------- Medidas de tendencia central -------------")
                print("--------------------------------------------------------\n")

                print("[+] 1. Mostrar la Media.")
                print("[+] 2. Mostrar la Mediana.")
                print("[+] 3. Mostrar la Moda.")
                print("[+] 0. Salir al menú.")
                submenu = input("Ingresa una opcion: ")

                if submenu != '0':
                    if submenu == '1':
                        print("\n[+] Opción 1: Media aritmetica")
                        print("--------------------------------------------------------\n")
                        media = sum(poblacion)/len(poblacion)
                        print(f"[*] La media aritmetica es de: {media}") 
                        time.sleep(4)
                    
                    elif submenu == '2':
                        print("\n[+] Opción 2: Mediana")
                        print("--------------------------------------------------------\n")
                        a = len(poblacion)      
                        if a % 2 == 0:
                             mediana = (poblacion[a//2-1]+poblacion[a//2])/2
                        else:
                            mediana = poblacion[a//2]
                        
                        print(f"La mediana es: {mediana}")

                    elif submenu == '3':
                        print("\n[+] Opción 3: Moda")
                        print("--------------------------------------------------------\n")
                        moda = statistics.mode(poblacion)
                        print(f"La moda es: {moda}")

                    else:
                        print(f"[!] No hay una opción determinada para {submenu}")
                else:
                    if submenu == '0':
                        print("[!] Saliendo al menú...")
                        break
                        print(f"[!] No hay una opcion determinada para {submenu}")
        elif opcion == '9':

            while True:
                print("\n--------------------------------------------------------")
                print("------------- Medidas de dispersión ----------------------")
                print("--------------------------------------------------------\n")
                print("[+] 1. Varianza.")
                print("[+] 2. Desviación estandar.")
                print("[+] 0. Salir al menú.")

                submenu2 = input("Ingresa una opcion: ")

                if submenu2 != '0':
                    if submenu2 == '1':  
                        print("\n[+] Opción 1: Varianza")
                        print("--------------------------------------------------------\n")
                        if existe_pob and existe_muestra:
                            suma_cuadrados = sum((x - media) ** 2 for x in muestra)
                            varianza = suma_cuadrados/len(muestra)
                            print(f"[*] La varianza de la muestra es: {varianza}")
                            suma_cuadrados = sum((x - media) ** 2 for x in poblacion)
                            varianza = suma_cuadrados/len(poblacion)
                            print(f"[*] La varianza de la poblacion es: {varianza}")
                            existe_varianza = True
                            time.sleep(5)
                        else:
                            if existe_pob:
                                suma_cuadrados = sum((x - media) ** 2 for x in poblacion)
                                varianza = suma_cuadrados/len(poblacion)

                                print(f"[*] La varianza de la poblacion es: {varianza}")
                                print(f"[!] No existe un valor para muestra. Agregalo en el menú principal.")
                                existe_varianza = True
                                time.sleep(5)
                            else:
                                print("[!] No existe ningún valor a la que se le pueda calcular la varianza")
                        
                    elif submenu2 == '2':
                        print("\n[+] Opción 2: Desviación estandar")
                        print("--------------------------------------------------------\n")
                        if existe_varianza:
                            print(varianza)
                            Desviacion_estandar = varianza ** 0.5
                            print(f"[*] La desviación estandar es: {Desviacion_estandar}")
                        else:
                            print("[!] No existe un valor al cual calcular la desviación estandar")

                    else:
                        print(f"[!] No hay una opción determinada para {submenu2}")
                else:
                    if submenu2 == '0':
                        print("[!] Saliendo al menú...")
                        time.sleep(2)
                        break
                    print(f"[!] No hay una opción determinada para {submenu2}")
        else:
            print(f"[!] No hay una opción determinada para {opcion}")
            time.sleep(4)

    else:
        if opcion == '0':
            print("[!] Saliendo...")
            time.sleep(2)
            break
        print(f"[!] No hay una opcion determinada para {opcion}")


