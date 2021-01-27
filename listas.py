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
	grupo = str(nro)
	lista[grupo] = {}

	for row in sheet.iter_rows():
		
		for cell in row:

			if (nro%3)==0:
					grupo = str(nro)
					articulo = cell.value
					try:	
						lista[grupo][articulo] = {}
					except:
						lista[grupo] = {}
						lista[grupo][articulo] = {}

				
			elif (nro%3)==1 and cell.value != None and type(cell.value)!=str:
				lista[grupo][articulo][mino] = cell.value
				
			elif (nro%3)==2 and cell.value != None and type(cell.value)!=str:
				lista[grupo][articulo][may] = cell.value
			if nro < 9:	
				nro +=1
			else:
				nro = 0 
	for k,v in lista.items():
		
		try:
			print(k,v) 
		except:
			print(k[grupo],"no tiene precio minorista", end="\n")



if __name__ == '__main__':
	main()