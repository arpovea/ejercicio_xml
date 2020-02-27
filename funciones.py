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
	numero = (doc.xpath('/list/item/LOCALIZACION[LOCALIDAD="%s"])'%localidad)
	listabibliotecas=[]
	for elem in localidad:
		nombrebiblioteca = doc.xpath('/list/item/LOCALIZACION[LOCALIDAD="%s"]/../NOMBRE/text()'%localidad)
		añofundacion = doc.xpath('/list//item/LOCALIZACION[LOCALIDAD="%s"]/../AÑO_FUNDACION/text()'%localidad)
	return (numero,nombrebiblioteca,añofundacion)
