def nombresbibliotecas(doc):
	nombres = doc.xpath('/list/item//NOMBRE/text()')
	return nombres

def numerobibliotecas(doc):
	numero = doc.xpath('count(/list/item)')
	return int(numero)

def bibliolocalidad(localidad,doc):
	nombrebiblioteca= doc.xpath('/list/item/LOCALIZACION[LOCALIDAD="%s"]/../NOMBRE/text()'%localidad)
	horariobiblioteca= doc.xpath('/list//item/LOCALIZACION[LOCALIDAD="%s"]/../HORARIO/text()'%localidad)
	resultado = zip(nombrebiblioteca, horariobiblioteca)
	return resultado

def tipodeacceso(acceso,doc):
	nombrebiblioteca=doc.xpath('/list/item[TIPO_ACCESO="%s"]/NOMBRE/text()'%acceso)
	return nombrebiblioteca

def nombreañofundacion(localidad,doc):
	nombrebiblioteca= doc.xpath('/list/item/LOCALIZACION[LOCALIDAD="%s"]/../NOMBRE/text()'%localidad)
	añofundacion=doc.xpath('/list/item/LOCALIZACION[LOCALIDAD="%s"]/../AÑO_FUNDACION/text()'%localidad)
	listabibliotecas=[]
	for elem in nombrebiblioteca:
		dicbiblioteca={}
		dicbiblioteca["nombre"]=elem
		dicbiblioteca["añofundacion"]=doc.xpath('/list/item[NOMBRE="%s"]/AÑO_FUNDACION/text()'%elem)
		listabibliotecas.append(dicbiblioteca)
	return listabibliotecas