from woocommerce import API
import sqlite3
import os

wcapi = API(
    url="http://irenic.nolimits4u.com",
    consumer_key="ck_ef3e0827be1490d3c846afd0ad3da4e8c704440d",
    consumer_secret="cs_3db60cc6e72d0b353c2b4421694701bfe307e9e3",
    version="wc/v3",
    timeout=10,
)

def creo_datos(accion, datos):
    data = {
        accion:[
            datos
        ]
    }
    return data

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

conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

cur.execute("SELECT id, name FROM Categoria")
categorias_base = cur.fetchall()

cur.execute("SELECT nombre, precio, categoria_id FROM ProductosShiri")
productos = cur.fetchall()

######### MUESTRO LAS CATEGORIAS ACTUALES QUE ESTAN EN WOOCOMMERCE#############

categorias_woo = wcapi.get("products/categories", params={"per_page": 100}).json()

nombres_woo = [x["name"] for x in categorias_woo]
nombres_base = [categoria_base[1] for categoria_base in categorias_base]


######## ACTUALIZO WOOCOMMERCE CON LA BASE DE DATOS ###############
for categoria_base in categorias_base:
    datos = {}
    if categoria_base[1] not in nombres_woo:
        print("Actualizando categorias desde base...",categoria_base[1])
        quehago = "create"
        datos = categoria_base[1]

        data = creo_datos(quehago, datos)

        actualizo_woo(data)

    else:
        print(f"{categoria_base[1]} ya existe en Woocommerce!")

######### BORRO DE WOOCOMMERCE LO QUE NO ESTE EN LA BASE ######################
for categoria_woo in categorias_woo:
    datos = ""

    if categoria_woo["name"] not in nombres_base:
        print("Depurando Woocommerce desde la base....",categoria_woo["name"])
        quehago = "delete"
        datos = categoria_woo["id"]

        data = creo_datos(quehago, datos)

        actualizo_woo(data)



######### MUESTRO LAS CATEGORIAS ACTUALES QUE ESTAN EN WOOCOMMERCE#############

r = wcapi.get("products/categories", params={"per_page": 100}).json()
for i in r:
    print(i["id"], i["name"])

# else:
# print("No hay archivos de fotos para seguir")
# r = wcapi.get("products", params={"per_page": 100}).json()
# for i in r:
#     print(i["id"],i["name"], i["price"])
