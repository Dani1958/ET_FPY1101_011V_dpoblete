
import random
import os
import statistics
import csv
os.system('cls')

trabajadores = ['Juan Perez', 'Maria Garcia', 'Carlos Lopez', 'Ana Martinez', 'Pedro Rodriguez', 'Laura Hernandez', 'Miguel Sanchez', 'Isabel Gomez', 'Francisco Diaz', 'Elena Fernandez']
#menu
def menu(titulo, lista):
     print(titulo.upper())
     while True:
        i=1
        for elem in lista:
            print(i,'.-',elem)
            i+=1
        opc=input('Ingrese Opción: ')
        if opc.isdigit():
            opc_int=int(opc)
            if opc_int>=1 and opc_int<=i:
                return opc_int
            else:
                print('Debe Ingresar un Número entre 1 y ',i)
        else:
            print('Ingrese Sólo Números')

#asignar sueldos
def sueldo_azar(trabajadores):
    salario = {worker: random.randint(300000, 2500000) for worker in trabajadores}
    print('Sueldos Aleatorios: ')
    for worker, salario in salario.items():
        print(f'{worker}: {salario}')
    return salario

def reporte(salario):   
    with open('salarios.csv', 'w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv, delimiter=';')
        escritor_csv.writerow(['Nombre Empleado', 'Sueldo Base', 'Descuento Salud', 'Descuento AFP', 'Sueldo Liquido'])

    dcto_salud = round(salario * 0.07)
    dcto_afp = round(salario *0.12)
    sueldo_liq = round(salario - dcto_salud - dcto_afp)
    print(f'Descuento salud: {dcto_salud}\n Descuento AFP: {dcto_afp}\n Sueldo Liquido: {sueldo_liq}')

#menu principal
while True:
    opc = menu('menu principal',['Asignar sueldos aleatorios', 'Reporte de sueldos', 'Salir del programa'])
    if opc == 1:
        salario = sueldo_azar(trabajadores)
    if opc == 2:
        reporte(salario)
    elif opc == 3:
        print('Finalizando programa...')
        print('Desarrollado por Carlos Vergara')
        print('RUT: 12.345.678-9 ')
        break
