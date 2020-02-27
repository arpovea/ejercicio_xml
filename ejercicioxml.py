from funciones import nombresbibliotecas
from funciones import numerobibliotecas
from funciones import bibliolocalidad
from funciones import tipodeacceso
from funciones import nombreañofundacion

from lxml import etree
doc= etree.parse('bibliotecas.xml')

while True:
	print ('''
	Elige una opcion:
	1-Muestra el nombre de las localidades de las que tenemos información sobre Bibliotecas.
	2-Muestra la cantidad de Bibliotecas de los que tenemos información.
	3-Pide por teclado una localidad, muestra el nombre de la Biblioteca que tiene y su horario.
	4-Pide por teclado un tipo de acceso, muestra el nombre de las Bibliotecas y su horario.
	5-Pide por teclado una localidad, cuenta las Bibliotecas que tiene, muestra su nombre y año de fundación.
	0-Para salir.
	''')
	opcion=int(input("Opcion: "))

	if opcion==1:
		print ("Las Bibliotecas de las que tenemos información son: ")
		for nombre in nombresbibliotecas(doc):
			print(nombre)
	elif opcion==2:
		print ("La cantidad de Bibliotecas en nuesta base de datos es: ", numerobibliotecas(doc))
	elif opcion==3:
		localidad=str(input("Dime la localidad, te mostraré las bibliotecas y sus horarios: "))
		for biblioteca in bibliolocalidad(localidad,doc):
			print (biblioteca)
	elif opcion==4:
		acceso=str(input("Dime un tipo de acceso y te mostraré las Bibliotecas que lo cumplen: "))
		for biblioteca in tipodeacceso(acceso,doc):
			print (biblioteca)
	elif opcion==5:
		localidad=str(input("Dime una localidad, te mostrare el numero de bibliotecas totales, su nombre y año de fundación respectivamente: ")) 
		for biblioteca in nombreañofundacion(localidad,doc):
			#for elem in biblioteca:
			#	print (elem)
	elif opcion==0:
		print("Hasta la proxima.")
		break;
