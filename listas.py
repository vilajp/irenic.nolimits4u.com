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
	may = "Mayorista"
	min = "Minorista"
	nro = 0

	for row in sheet.iter_rows():
		
		for cell in row:
			if (nro%3)==0:
				articulo = cell.value
				lista[articulo] = {}
				 
				
			elif (nro%3)==1 and cell.value != None:
				lista[articulo][min] = cell.value
				
			elif (nro%3)==2 and cell.value != None:
				lista[articulo][may] = cell.value
				
			nro +=1 
	for k,v in lista.items():	
		print(k,v, end="\n") 



if __name__ == '__main__':
	main()