#!/usr/bin/env python3
import time 
import statistics
# Variable globales
existe_pob = False
existe_var = False
existe_muestra = False 
existe_varianza = False
existe_name_var = False
existe_tabla = False

def calcular_repeticiones(poblacion):
    unico = set(poblacion)
    repeticiones_dict = {}
    acum_rep = 0 
    for elemento in unico:
        repeticiones = poblacion.count(elemento)
        print(f"El número {elemento} se repite {repeticiones} veces en la población.")
        repeticiones_dict[elemento] = repeticiones
        acum_rep += repeticiones
        time.sleep(0.5)
    return repeticiones_dict, acum_rep

def imprimir_tabla(repeticiones_dict, acum_rep):
        print("\n\t---------------------------------------------------------------------------------------------------------------")
        print("\t|  Categoria  |  Frecuencia absoluta  |  Frecuencia acumulada  |  Frecuencia relativa  |  Relativa acumulada  |")
        print("\t---------------------------------------------------------------------------------------------------------------")
        acum = 0
        rela_acum = 0
        for elemento, repe in repeticiones_dict.items():
            acum += repe
            rela_acum += (repe/acum_rep)
        # Imprimir fila de la tabla con formato ajustado
            print(f"\t|     {elemento:<6}  |          {repe:<12} |          {acum:<13} |  {(repe/acum_rep):<20} |  {rela_acum:<19} |")
            print("\t---------------------------------------------------------------------------------------------------------------")
        print("\n")
        time.sleep(8)

def calcular_y_mostrar_tabla(poblacion):
    repeticiones_dict, acum_rep = calcular_repeticiones(poblacion)
    imprimir_tabla(repeticiones_dict, acum_rep)

def calcular_varianza_ponderada(poblacion, frecuencias):
    media = sum(x * f for x, f in zip(poblacion, frecuencias)) / sum(frecuencias)
    suma_cuadrados_ponderados = sum((x - media) ** 2 * f for x, f in zip(poblacion, frecuencias))
    varianza_ponderada = suma_cuadrados_ponderados / (sum(frecuencias) - 1)
    return varianza_ponderada

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
    print("[+] 10. Nombre de la variable")
    print("[+] 11. Resumen (necesario pasar por todos los modulos)")
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
            print("\n[+] Opción 5: Muestre el tipo de variable")
            print("---------------------------------------------------\n")

            if existe_var:
                print(f"[*] La variable es: {var}, {espe}")
                time.slee(4)
            else:
                print("[!] No existe aún el tipo de variable...")
                time.sleep(3)

        elif opcion == '6':
            if existe_pob:            
                print("\n[+] Opción 6: Mostrando la tabla de frecuencia")
                print("---------------------------------------------------\n")
                calcular_y_mostrar_tabla(poblacion)
                existe_tabla = True
            else:
                print("[!] No existe el valor de poblacion para tabular.")

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
                        #poblacion_var = set(poblacion)

                        if existe_pob and existe_muestra:
                            pass
                            #repeticiones_poblacion, frecuencias_poblacion = calcular_repeticiones(poblacion)
                            #varianza_poblacion = calcular_varianza_ponderada(poblacion, frecuencias_poblacion)
                           # if existe_muestra:
                           #     repeticiones_muestra, frecuencias_muestra = calcular_repeticiones(muestra)
                           #     varianza_muestra = calcular_varianza_ponderada(muestra, frecuencias_muestra)
                           #     print(f"[*] La varianza de la muestra es: {varianza_muestra}")
                           # else:
                          #      print("[!] La muestra no está definida.")

                          #  print(f"[*] La varianza de la poblacion es: {varianza_poblacion}")
                          #  existe_varianza = True
                           # time.sleep(5)
                        else:
                            if existe_pob: 
                                #repeticiones_poblacion, frecuencias_poblacion = calcular_repeticiones(poblacion)
                                #varianza_poblacion = calcular_varianza_ponderada(poblacion, frecuencias_poblacion)
                                Desviacion_estandar = statistics.stdev(poblacion)
                                varianza_poblacion = Desviacion_estandar ** 2
                                print(f"[*] La varianza de la poblacion es: {varianza_poblacion}")
                                #print(f"[!] No existe un valor para muestra. Agregalo en el menú principal.")
                                existe_varianza = True
                                time.sleep(5)
                            else:
                                print("[!] No existe ningún valor a la que se le pueda calcular la varianza")
                        
                    elif submenu2 == '2':
                        print("\n[+] Opción 2: Desviación estandar")
                        print("--------------------------------------------------------\n")
                        if existe_varianza:
                            Desviacion_estandar = varianza_poblacion ** 0.5
                            print(f"[*] La desviación estandar es: {Desviacion_estandar}")
                            time.sleep(4)
                        else:
                            print("[!] No existe un valor al cual calcular la desviación estandar")
                            time.sleep(3)

                    else:
                        print(f"[!] No hay una opción determinada para {submenu2}")
                        time.sleep(4)
                else:
                    if submenu2 == '0':
                        print("[!] Saliendo al menú...")
                        time.sleep(2)
                        break
                    print(f"[!] No hay una opción determinada para {submenu2}")
        elif opcion == '10':
            print("\n[+] Opción 10: Ingresar el nombre de la variable")
            print("---------------------------------------------------\n")

            nombre_var = input("[*] Ingresa el nombre de la variable: ")
            existe_name_var = True
        elif opcion == '11':
            print("\n[+] Opción 11: Resumen")
            print("---------------------------------------------------\n")

            if existe_pob and existe_var and existe_varianza and existe_tabla or existe_muestra:

                print("[*] Resumen...\n")
                print(f"[+] Nombre de la variable: {nombre_var}\n")
                print(f"[+] El tipo de variable es: {var}: {espe}\n")
                print(f"[+] Los valores de la poblacion: {poblacion}")
                if existe_muestra:
                    print(f"[+] Los valores que se utilizan como muestra: {muestra}")
                time.sleep(2)
                print(f"[+] Mostrando la tabla de frecuencia...\n")
                calcular_y_mostrar_tabla(poblacion)                
                print("\n")
                time.sleep(5)
                print(f"[+] La media es: {media}")
                print(f"[+] La mediana es: {mediana}")
                print(f"[+] La moda es: {moda}")
                print(f"[+] La varianza es: {varianza_poblacion}")
                print(f"[]")
                print(f"[+] La desviación estandar es: {Desviacion_estandar}")
                time.sleep(2)
            else: 
                print("[!] Debes pasar por todos los modulos para obtener el resumen")
                time.sleep(1)

        else:
            print(f"[!] No hay una opción determinada para {opcion}")
            time.sleep(4)

    else:
        if opcion == '0':
            print("[!] Saliendo...")
            time.sleep(2)
            break
        print(f"[!] No hay una opcion determinada para {opcion}")


