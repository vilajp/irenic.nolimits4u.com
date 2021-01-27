import openpyxl
import sys
import os

def main():
	try:
		wb_obj = openpyxl.load_workbook("sentida\\LISTA DE PRECIOS ENERO 2021.xlsx")

	except:
		print("No se pudo abrir el archivo", sys.exc_info()[0])
		return
	
	sheet = wb_obj.active
	print(sheet)
	lista = {}
	may = "Mayorista"
	mino = "Minorista"
	nro = 0

	for row in sheet.iter_rows():
		
		for cell in row:

			if (nro%3)==0:
				
					articulo = cell.value
					lista[articulo] = {}

				
			elif (nro%3)==1 and cell.value != None and type(cell.value)!=str:
				lista[articulo][mino] = cell.value
				
			elif (nro%3)==2 and cell.value != None and type(cell.value)!=str:
				lista[articulo][may] = cell.value
			if nro < 9:	
				nro +=1
			else:
				nro = 0 
	for k,v in lista.items():
		if v != {}:
			try:
				print(k,v, end="\n") 
			except:
				print(k,"no tiene precio minorista", end="\n")



if __name__ == '__main__':
	main()