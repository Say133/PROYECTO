consumo_energia = {
 'Coca Codo Sinclair': {
 'Quito': { 'consumos':(400, 432, 400, 432, 420, 432, 460, 432, 400, 432, 300 , 213),'tarifa': 65},
 'Guayaquil': { 'consumos': (120, 55, 32, 120, 75, 32, 150, 55, 32, 120, 97, 32),'tarifa': 84},
 },
 'Sopladora': {
 'Guayaquil':{ 'consumos': (310, 220, 321, 310, 220, 321, 310, 220, 321, 310, 220, 321),'tarifa':55},
 'Quito': { 'consumos': (400, 432, 587, 400, 432, 587, 400, 432, 587, 400, 432, 587),'tarifa': 79},
 'Loja': { 'consumos': (50, 32, 32, 50, 32, 32, 50, 32, 32, 50, 32, 32),'tarifa': 32},
 },
}
informacion = {
 'costa': ('Guayaquil', 'Manta'),
 'sierra': ('Quito', 'Ambato', 'Loja'),
 'oriente': ('Tena', 'Nueva Loja')
}


#Consumo de Sopladora
consumototal_SopladoraGuayaquil=consumo_energia['Sopladora']["Guayaquil"]["consumos"]
consumototal_SopladoraQuito=consumo_energia['Sopladora']["Quito"]["consumos"]
consumototal_SopladoraLoja=consumo_energia['Sopladora']["Loja"]["consumos"]
tarifa_SopladoraGuayaquil=consumo_energia["Sopladora"]["Guayaquil"]["tarifa"]
tarifa_SopladoraQuito=consumo_energia["Sopladora"]["Quito"]["tarifa"]
tarifa_SopladoraLoja=consumo_energia["Sopladora"]["Loja"]["tarifa"]
#Consumo de Coca Codo Sinclair
consumototal_CocaCodoQuito=consumo_energia["Coca Codo Sinclair"]["Quito"]["consumos"]
consumototal_CocaCodoGuayaquil=consumo_energia["Coca Codo Sinclair"]["Guayaquil"]["consumos"]
tarifa_CocaCodoQuito=consumo_energia["Coca Codo Sinclair"]["Quito"]["tarifa"]
tarifa_CocaCodoGuayaquil=consumo_energia["Coca Codo Sinclair"]["Guayaquil"]["tarifa"]

opcion=-1


def menu_principal():
    print("<1> Consultar el total de MWh consumidos en planta eléctrica")
    print("<2> Consultar información de plantas en una ciudad")
    print("<3> Consultar información de dinero recaudado en una región")
    print("<4> Salir")

def menu_opcion1():
    print("Las plantas de energía registradas son:")
    print("-Sopladora")
    print("-Coca Codo Sinclair")
    plantaenergia_opcion1=str(input("Ingrese planta de energía:"))
    print("---------------------------------------------------------------------------------")
    if plantaenergia_opcion1=="Sopladora":
        print("Las ciudades en la que se encuentra esta planta electrica son:")
        print("-Guayaquil")
        print("-Quito")
        print("-Loja")
        ciudadesSopladora=str(input("Ingrese el nombre de la ciudad:"))
        if ciudadesSopladora=="Guayaquil":
            print("El total de consumo es:",sum(consumototal_SopladoraGuayaquil))
        
        elif ciudadesSopladora=="Quito":
            print("El total de consumo es:",sum(consumototal_SopladoraQuito))

        elif ciudadesSopladora=="Loja":
            print("El total de consumo es:",sum(consumototal_SopladoraLoja))
        
        else:
            print("Datos erróneos, intente nuevamente con datos correctos")
    
    elif plantaenergia_opcion1=="Coca Codo Sinclair":
        print("Las ciudades en la que se encuentra esta planta electrica son:")
        print("-Guayaquil")
        print("-Quito")
        ciudadesCocacodo=str(input("Ingrese el nombre de la ciudad:"))
        if ciudadesCocacodo=="Guayaquil":
            print("El total de consumo es:",sum(consumototal_CocaCodoGuayaquil))
        elif ciudadesCocacodo=="Quito":
            print("El total de consumo es:",sum(consumototal_CocaCodoQuito))
        else:
            print("Datos erróneos, intente nuevamente con datos correctos")
    
    else:
        print("Datos erróneos, intente nuevamente con datos correctos")


#Solicite al usuario el nombre de una ciudad y presente un nuevo diccionario cuyas claves
#son los nombres de las plantas generadoras y el valor es el total megavatios que cada
#planta le ha dado a ciudad. Si la planta no entrega energía a la ciudad entonces esa planta
#no debería aparecer en el nuevo diccionario
def menu_opcion2():
    plantas_energy={
        "Guayaquil":("Coca Codo Sinclair","Sopladora"),
        "Quito":("Coca Codo Sinclair","Sopladora"),
        "Loja":("Sopladora")
    }

    plantas_guayaquil=plantas_energy["Guayaquil"]
    plantas_quito=plantas_energy["Quito"]
    plantas_loja=plantas_energy["Loja"]

    print("Las ciudades disponibles son:\n-Guayaquil\n-Quito\n-Loja")
    ciudades2=str(input("Escoja y escriba el nombre de una ciudad:"))
    if ciudades2=="Guayaquil":
        print("Las plantas de energía existentes en esta ciudad son:",plantas_guayaquil)
        print("Coca Codo Sinclair entregó",sum(consumototal_CocaCodoGuayaquil),"MWh y Sopladora entregó",sum(consumototal_SopladoraGuayaquil),"MWh de energía")

    elif ciudades2=="Quito":
        print("Las plantas de energía existentes en esta ciudad son:",plantas_quito)
        print("Coca Codo Sinclair entregó",sum(consumototal_CocaCodoQuito),"MWh y Sopladora entregó",sum(consumototal_SopladoraQuito),"MWh de energía")

    elif ciudades2=="Loja":
        print("Las plantas de energía existentes en esta ciudad son:",plantas_loja)
        print("Sopladora entregó",sum(consumototal_SopladoraLoja),"MWh de energía")
    
    else:
        print("Datos erróneos, intente nuevamente con datos correctos")


# Solicite el nombre de una región al usuario y presente cuento dinero ha recaudado la
# región Sierra
def menu_opcion3():
    print("Las regiones son:")
    print("-Costa\n-Sierra\n-Oriente")
    region1=str(input("Ingrese el nombre de la Región a evalúar:"))
    if region1=="Costa":
        dinero_CostaCocaG=sum(consumototal_CocaCodoGuayaquil)*tarifa_CocaCodoGuayaquil
        dinero_CostaSoplaG=sum(consumototal_SopladoraGuayaquil)*tarifa_SopladoraGuayaquil
        print("En esta región se ha recaudado $",(dinero_CostaCocaG+dinero_CostaSoplaG))
    elif region1=="Sierra":
        dinero_SierraCocaQ=sum(consumototal_CocaCodoQuito)*tarifa_CocaCodoQuito
        dinero_SierraSoplaQ=sum(consumototal_SopladoraQuito)*tarifa_SopladoraQuito
        dinero_SierraSoplaL=sum(consumototal_SopladoraLoja)*tarifa_SopladoraLoja
        print("En esta región se ha recaudado $",dinero_SierraCocaQ+dinero_SierraSoplaQ+dinero_SierraSoplaL)
    elif region1=="Oriente":
        print("No existen plantas de energía en esta región aún")
    else:
        print("Datos erróneos, intente nuevamente con datos correctos")
        



          


while opcion!=0:
    menu_principal()
    opcion=int(input("Eliga una opción:"))
    print("---------------------------------------------------------------------------------")
    if opcion==1:
        menu_opcion1()
        print("---------------------------------------------------------------------------------")
    elif opcion==2:
        menu_opcion2()
        print("---------------------------------------------------------------------------------")
    elif opcion==3:
        menu_opcion3()
        print("---------------------------------------------------------------------------------")
    elif opcion==4:
        print("El programa finalizó")
        print("---------------------------------------------------------------------------------")
        exit()
