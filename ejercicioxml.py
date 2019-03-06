from lxml import etree
doc= etree.parse('bibliotecas.xml')

while True
print ('''
Elige una opcion:
1-Muestra el nombre de las localidades de las que tenemos información sobre Bibliotecas.
2-Muestra la cantidad de Bibliotecas de los que tenemos información.
3-Pide por teclado una localidad, muestra el nombre de la Biblioteca que tiene y su horario.
4-Pide por teclado un tipo de acceso, muestra el nombre de las Bibliotecas y su horario.
5-Pide por teclado una localidad, cuenta las Bibliotecas que tiene, muestra su nombre y año de fundación.
''')
opcion=int(input("Opcion:"))