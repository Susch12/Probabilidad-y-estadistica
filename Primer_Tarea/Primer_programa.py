#!/usr/bin/env python3

# Variable globales
existe_pob = False

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
    print("[+] 8. Medidas de tendencia central.")
    print("[+] 9. Medidas de dispersión.")
    print("[+] 0. Salir.")

    opcion = int(input("\nIngresa opción: "))

    if opcion != 0:
        if opcion == 1:
            if existe_pob:
                print("[!] Existe una población")
                print("[!] ¿Quieres sobreescribir la población?")
                input("Y/N: ")
            else: 
                print("\n[+] Opción 1: Ingrese la población")
                print("---------------------------------------------------\n")
                poblacion = list(input("Ingrese la lista: "))
                existe_pob = True

        elif opcion == 2:

            if existe_pob:
                print("\n[+] Opción 2: Muestre la población")
                print("---------------------------------------------------\n")
                print(poblacion)
            else:
                print("[!] No existe una población que se muestre...")

        elif opcion == 3:
            if existe_pob:
                poblacion = list(poblacion)
                print("\n[+] Opción 3: Indique el rango de la muestra")
                print("---------------------------------------------------\n")
                print(f"[+] La cantidad de numeros en la lista es: {len(poblacion)}")
                Inicio = int(input("[+] Ingresa el número de inicio para el rango: "))-1
                print(Inicio)
                Final = int(input("[+] Ingresa el número de final para el rango: "))-1
                print(Final)
                muestra = []
                for i in range(Inicio, Final):
                    muestra.append(poblacion[i])
                print(muestra)
            else:
                print("[!] No existe una población...")
        elif opcion == 4:

            print("\n[+] Opción 4: Ingresar el tipo de variable")
            print("---------------------------------------------------\n")

            var = input("[+] Ingresa el tipo de variable (Cuantitativa/Cualitativa): ")

            if var == "Cuantitativa" or var == "cuantitativa":
                print("[!] Escogiste Cuantitativa")
                espesc = input("[!] Es Discreta o continua: ")

            else:
                if var == "Cualitativa" or var == "cualitativa":
                    print("[!] Escogiste Cualitativa")
                    espesc = input("[!] ¿Es Ordinal o Nominal? ")

        elif opcion == 5:

            




    else:
        if opcion == 0:
            break


