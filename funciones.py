def nombresbibliotecas(doc):
	nombres = doc.xpath("/item/nombre//text()")
	return nombres