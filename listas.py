import openpyxl
import sys

def main():
	try:
		wb_obj = openpyxl.load_workbook("sentida\\LISTA DE PRECIOS OCTUBRE 2020 excel.xlsx")

	except:
		print("No se pudo abrir el archivo", sys.exc_info()[0])
		return
	
	sheet = wb_obj.active
	print(sheet)
	lista = {}
	nro = 0

	for row in sheet.iter_rows():
		for cell in row:
			if (nro%3)==0:
				articulo = cell.value
				lista[articulo] = []
				nro +=1  
				continue
			lista[articulo].append(cell.value)
			nro += 1
	for k,v in lista.items():	
		print(k,v, end="\n") 


if __name__ == '__main__':
	main()