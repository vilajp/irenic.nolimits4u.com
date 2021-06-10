from woocommerce import API
import sqlite3
import os
import shutil

def actualizo_woo(data, salir=False):
	while not salir:

		try:
			print(wcapi.post("products/categories/batch", data).json())
			break
		except KeyboardInterrupt:
			print("Programa interrumpido por Operador")
			salir = True
			break
		else:
			print("No pude conectarme, reintentando...")


def actualizo(accion, datos):
	data = {
		accion: [
			datos
		]
	}
	return data


wcapi = API(
	url="http://irenic.nolimits4u.com",
	consumer_key="ck_ef3e0827be1490d3c846afd0ad3da4e8c704440d",
	consumer_secret="cs_3db60cc6e72d0b353c2b4421694701bfe307e9e3",
	version="wc/v3",
	timeout=10,
	)


conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

cur.execute("SELECT id, name FROM Categoria")
categorias_base = cur.fetchall()

cur.execute("SELECT nombre, precio, categoria_id FROM ProductosShiri")
productos_base = cur.fetchall()

#          MUESTRO LAS CATEGORIAS ACTUALES QUE ESTAN EN WOOCOMMERCE

categorias_woo = wcapi.get("products/categories", params={"per_page": 100}).json()
productos_woo = wcapi.get("products", params={"per_page": 100}).json()

nombres_cat_woo = [(x["name"], x["id"]) for x in categorias_woo]
nombres_cat_base = [categoria_base[1] for categoria_base in categorias_base]

nombres_prod_base = [cada_producto_base[1] for cada_producto_base in productos_base]
nombres_prod_woo = [y["name"] for y in productos_woo]

for cada_producto_base in productos_base:
	datos = {}
	if cada_producto_base[0] not in nombres_prod_woo:
		print("Actualizando productos desde base...",cada_producto_base[0])
		quehago = "create"
		datos["name"] = cada_producto_base[0]
		datos["price"] = cada_producto_base[1]
		datos["categories"] = [{"id":cada_producto_base[2]}]


		data = actualizo(quehago, datos)

		actualizo_woo(data)

	else:
		print(f"{producto_base[0]} ya existe en Woocommerce!")





data = {
    # "create": [
    #     {
    #         "name": "Brand"
    #     },
    #     {
    #         "name": "Publisher"
    #     }
    # ],
    # "update": [
    #     {
    #         "id": 389,
    #         "name": "Cepillos Meraki",
    #         'regular_price':"255.99",
    #         "images": [
    #             {
    #                 "src": "http://irenic.nolimits4u.com/wp-content/uploads/2021/01/irenic-cepillos-meraki.jpg"
    #             }
    #         ],
    #     }
    # ],
    # "delete": [
    #     392,
    #     393,
    #     394,
    #     395,
    #     396,
    #     397,
    #     398,
    # ]
}

#print(wcapi.post("products/attributes/batch", data).json())

'''data = {
    "order_by": "name"
}

print(wcapi.put("products/attributes/1", data).json())'''

#           CARGO LOS ARTICULOS DESDE LOS ARCHIVOS DE FOTOS

for archivo in os.listdir("./fotos/articulos"):
	if archivo[-3:]=="jpg":

		print("Actualizando...",archivo)
		datos = {}
		nombre_producto = "".join(archivo.split("irenic - "))[0:-4]

		datos["name"] = nombre_producto.title()
		nombre_archivo = "-".join(nombre_producto.split())

		datos["images"] = [
					{
						"src": f"http://irenic.nolimits4u.com/wp-content/uploads/2021/01/irenic-{nombre_archivo}.jpg"
					}
					]

		data = actualizo("create", datos)


		while True:
			salir = False
			try:
				print(wcapi.post("products/batch", data).json())
				shutil.move(archivo, "./fotos/articulos/copiados")			
				break
			except KeyboardInterrupt:
				print("Programa interrumpido por Operador")
				salir = True
				break
			else:
				print("No pude conectarme, reintentando...")
		if salir:
			break
	else:
		print("No hay archivos de fotos para seguir")
r = wcapi.get("products", params={"per_page": 100}).json()
for i in r:
	print(i["id"],i["name"], i["price"])
	

