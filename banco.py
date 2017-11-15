import time

obtenerDatos = open("datos.txt","r")
contador = 0
datos1 =obtenerDatos.read()
for i in datos1:
    if (i == "\n"):
        contador = contador + 1
obtenerDatos.close()
obtenerDatos = open("datos.txt","r")

preguntar = "si"
suich = "no"
min2 = 0
while (suich=="no"):
    print("Por favor ingrese el numero de cuenta")
    noCuenta = str(input())
    for i in range(contador):
        datos2 = obtenerDatos.readline()
        n1,n2,n3,n4,n5,n6 = datos2.split()
        if (noCuenta == n4):
            suich = "si"
    if (suich=="no"):
        print("numero de cuenta incorrecto")
        break
while (preguntar=="si" and suich!="no"):
    obtenerDatos.close()
    obtenerDatos = open("datos.txt","r")
    print("1. Mostrar informacion del cliente")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Hacer transferencia bancaria")
    print("")
    print("Por favor ingrese el numero de operacion")
    operacion = str(input())
    if (operacion == "1"):
        for e in range(contador):
            datos2 = obtenerDatos.readline()
            n1,n2,n3,n4,n5,n6 = datos2.split()
            if (noCuenta == n4):
                print("Nombre:",n1,n2)
                print("Numero de dni:",n3)
                print("Usted tiene ",n5,n6)
    elif (operacion == "2"):
        datos20 = obtenerDatos.readlines()
        for e in range(contador):
            datos2 = datos20[e]
            n1,n2,n3,n4,n5,n6 = datos2.split()
            if (noCuenta == n4):
                monto = int(n6)
                if(monto<=100):
                    print("usted no tiene saldo que pueda retirar")
                else:
                    print("ingrese la cantidad que desea retirar")
                    saldo = int(input())
                    nuevoSaldo = monto - saldo
                    if (nuevoSaldo <=100):
                        print("usted no puede retirar esta cantidad")
                    else:
                        fecha = time.localtime()
                        min1 = fecha[4]
                        if (min1<min2):
                            print("aun no puede retirar dinero")
                        else:
                            obtenerDatos.close()
                            obtenerDatos = open("datos.txt","w")
                            obtenerDatos.write("")
                            obtenerDatos.close()
                            for x in range(contador):
                                datos4 = datos20[x]
                                m1,m2,m3,m4,m5,m6 = datos4.split()
                                if (n3!=m3):
                                    obtenerDatos.close()
                                    obtenerDatos = open("datos.txt","a")
                                    obtenerDatos.write(m1+' '+m2+' '+m3+' '+m4+' '+m5+' '+m6+"\n")
                            obtenerDatos.close()
                            obtenerDatos = open("datos.txt","a")
                            obtenerDatos.write(n1+' '+n2+' '+n3+' '+n4+' '+n5+' '+str(nuevoSaldo)+"\n")
                            obtenerDatos.close()
                            fecha = time.localtime()
                            min2 = fecha[4] + 2
    elif (operacion == "3"):
        datos5 = obtenerDatos.readlines()
        for e in range(contador):
            datos6 = datos5[e]
            n1,n2,n3,n4,n5,n6 = datos6.split()
            if (noCuenta == n4):
                monto = int(n6)
                print("ingrese la cantidad a depositar")
                deposito = int(input())
                nuevoSaldo = monto + deposito
                print("usted tiene",n5,str(nuevoSaldo))
                obtenerDatos.close()
                obtenerDatos = open("datos.txt","w")
                obtenerDatos.write("")
                obtenerDatos.close()
                obtenerDatos = open("datos2.txt","r")
                for x in range(contador):
                    datos7 = datos5[x]
                    m1,m2,m3,m4,m5,m6 = datos7.split()
                    if (n3!=m3):
                        obtenerDatos.close()
                        obtenerDatos = open("datos.txt","a")
                        obtenerDatos.write(m1+' '+m2+' '+m3+' '+m4+' '+m5+' '+m6+"\n")
                obtenerDatos.close()
                obtenerDatos = open("datos.txt","a")
                obtenerDatos.write(n1+' '+n2+' '+n3+' '+n4+' '+n5+' '+str(nuevoSaldo)+"\n")
                obtenerDatos.close()
    elif (operacion == "4"):
        datos8 = obtenerDatos.readlines()
        for e in range(contador):
            datos9 = datos8[e]
            n1,n2,n3,n4,n5,n6 = datos9.split()
            if (noCuenta == n4):
                monto = int(n6)
                print("ingrese la cantidad que desea tranferir")
                tranferencia = int(input())
                nuevoSaldo1 = monto - tranferencia
                if (nuevoSaldo1 <= 100):
                    print("usted no puede tranferir esta cantidad")
                else:
                    print("ingrese el numero de cuenta al que desea transferir")
                    noCuenta2 = str(input())
                    com1 = 0
                    for i in range(contador):
                        datos34 = datos8[i]
                        p1,p2,p3,p4,p5,p6 = datos34.split()
                        if (noCuenta2 == p4):
                            if (p5 == n5):
                                monto2 = int(p6)
                                nuevoSaldo2 = monto2 + tranferencia
                                obtenerDatos.close()
                                obtenerDatos = open("datos.txt","w")
                                obtenerDatos.write("")
                                obtenerDatos.close()
                                for x in range(contador):
                                    datos33 = datos8[x]
                                    m1,m2,m3,m4,m5,m6 = datos33.split()
                                    if (n3==m3):
                                        obtenerDatos.close()
                                        obtenerDatos = open("datos.txt","a")
                                        obtenerDatos.write(n1+' '+n2+' '+n3+' '+n4+' '+n5+' '+str(nuevoSaldo1)+"\n")
                                    elif (p3 == m3):
                                        obtenerDatos.close()
                                        obtenerDatos = open("datos.txt","a")
                                        obtenerDatos.write(p1+' '+p2+' '+p3+' '+p4+' '+p5+' '+str(nuevoSaldo2)+"\n")
                                    else:
                                        obtenerDatos.close()
                                        obtenerDatos = open("datos.txt","a")
                                        obtenerDatos.write(m1+' '+m2+' '+m3+' '+m4+' '+m5+' '+m6+"\n")
                                obtenerDatos.close()
                            else:
                                print("transferencia de tipo de moneda no valido")
                        else:
                            com1 = com1 + 1
                    if (com1 == contador):
                        print("el numero de cuenta ingresado no existe")

    print("")
    print("Desea realizar otra operacion?")
    preguntar = input()
