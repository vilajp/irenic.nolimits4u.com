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
				lista[grupo][articulo]["min"] = cell.value
				
			elif (nro%3)==2 and cell.value != None and type(cell.value)!=str:
				lista[grupo][articulo]["may"] = cell.value
			try:
				lista[grupo][articulo]["margen"] = round(100 * (lista[grupo][articulo]["min"] - \
				lista[grupo][articulo]["may"]) / lista[grupo][articulo]["may"],2)
			except:
				next

			if nro < 9:	
				nro +=1
			else:
				nro = 0 
	for k in lista.keys():
		for q, v in lista[k].items():
			if v=={}:
				tipo = q
				continue
			v["tipo"] = tipo 
			print(q,v)

if __name__ == '__main__':
	main()