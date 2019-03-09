def nombresbibliotecas(doc):
	nombres = doc.xpath('/list/item//NOMBRE/text()')
	return nombres