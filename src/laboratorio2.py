   
print"\n"    
print "***********************************************************"
print "EJERCICIO 2) Que muestre un menu que contemple las opciones" 
print "Archivo, Buscar y Salir, en caso de que no se introduzca una" 
print "opcion correcta se notificara por pantalla."
print "***********************************************************"
print"\n"   


print  "*********************************"
print  "************ MENU ***************"
print  "********  1. Archivo ************"
print  "********  2. Buscar  ************"
print  "********  3. Salir   ************"
print  "*********************************"    


opcion = int(input("ingrese opcion: "))

if opcion == 1:
    print ("la opcion es Archivo")

if opcion == 2:
    print ("la opcion es Buscar")

if opcion == 3:
    print ("la opcion es Salir")
else :
    print("no es ingreso ninguna opcion valida")
    
